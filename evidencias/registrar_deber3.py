import datetime, hashlib, json, pathlib, shlex, subprocess, sys
fase, *comando = sys.argv[1:]
registro = pathlib.Path(__file__).parent
inicio = datetime.datetime.now(datetime.timezone.utc)
cwd = pathlib.Path.cwd()
def git(*args):
    return subprocess.check_output(['git', *args], text=True).strip()
def huellas():
    return {str(p.relative_to(cwd)): hashlib.sha256(p.read_bytes()).hexdigest()
            for carpeta in ('lib', 'test') for p in (cwd/carpeta).rglob('*.dart')}
meta = {'command': comando, 'cwd': str(cwd), 'startedAtUtc': inicio.isoformat(), 'branch': git('branch', '--show-current'), 'headBefore': git('rev-parse', 'HEAD'), 'filesBefore': huellas()}
with (registro / (fase + '.txt')).open('w') as archivo:
    titulo = '$ ' + shlex.join(comando) + '\n'
    print(titulo, end='', flush=True)
    archivo.write(titulo)
    proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    for linea in proceso.stdout:
        print(linea, end='', flush=True)
        archivo.write(linea)
        archivo.flush()
    codigo = proceso.wait()
fin = datetime.datetime.now(datetime.timezone.utc)
meta.update({'finishedAtUtc': fin.isoformat(), 'elapsedSeconds': (fin-inicio).total_seconds(), 'exitCode': codigo, 'filesAfter': huellas(), 'gitStatusAfter': git('status', '--short')})
(registro / (fase + '.json')).write_text(json.dumps(meta, indent=2, ensure_ascii=False) + '\n')
sys.exit(codigo)
