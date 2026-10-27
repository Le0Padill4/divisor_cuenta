import pathlib, sys

fuente = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'coverage/lcov.info')
registros = {}
actual = None
for linea in fuente.read_text().splitlines():
    if linea.startswith('SF:'):
        ruta = pathlib.Path(linea[3:])
        if ruta.is_absolute():
            ruta = ruta.relative_to(pathlib.Path.cwd())
        actual = registros.setdefault(ruta.as_posix(), {})
    elif linea.startswith('DA:') and actual is not None:
        numero, visitas, *_ = linea[3:].split(',')
        actual[int(numero)] = actual.get(int(numero), 0) + int(visitas)
    elif linea == 'end_of_record':
        actual = None

print('| Archivo | Cubiertas | Medidas | Porcentaje |')
print('|---|---:|---:|---:|')
cubiertas_total = medidas_total = 0
for archivo in sorted(pathlib.Path('lib').rglob('*.dart')):
    datos = registros.get(archivo.as_posix())
    if not datos:
        print(f'| {archivo.as_posix()} | — | — | N/D |')
        continue
    medidas = len(datos)
    cubiertas = sum(visitas > 0 for visitas in datos.values())
    medidas_total += medidas
    cubiertas_total += cubiertas
    print(f'| {archivo.as_posix()} | {cubiertas} | {medidas} | {100*cubiertas/medidas:.2f}% |')
if medidas_total:
    print(f'| Total medido | {cubiertas_total} | {medidas_total} | {100*cubiertas_total/medidas_total:.2f}% |')
print('')
print('N/D: archivo sin líneas registradas en LCOV; no se le asigna un porcentaje ficticio.')
print('estrategia_redondeo.dart solo declara una interfaz, sin un cuerpo que ejecutar.')
print('El porcentaje cuenta líneas ejecutadas, no garantiza que el código sea correcto.')
