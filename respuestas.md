# Respuestas del Deber 5

## 1. ¿Qué hizo cada parte?

El modelo eligió qué herramientas usar e interpretó lo que devolvieron. Codex fue el host: abrió la sesión y arrancó el proceso local. Su cliente MCP envió las llamadas por `stdio`. El servidor ejecutó las funciones de Python y devolvió los resultados.

## 2. ¿Por qué revisar INC-003?

Hubo cuatro intentos fallidos de `admin` desde la misma IP y luego un acceso exitoso a las 03:04. Como era una cuenta administrativa, el agente registró una alerta alta. Los eventos muestran que alguien entró, pero no dicen si tenía permiso.

## 3. ¿Quién valida lo que pide el modelo?

El servidor rechaza `INC-999`, un nivel inválido, un motivo en blanco o una alerta repetida. El modelo se puede equivocar al pasar esos datos. La validación en Python hace que las reglas se cumplan en cada llamada.

## Cómo lo probé

Usé **Codex CLI** en una sesión nueva. Comprobé la conexión cuando aparecieron las tres herramientas y devolvieron resultados del servidor, incluido el error de `INC-999`. La [captura de las llamadas](evidencias/agente_tools.png) muestra los argumentos y resultados reales. La [traza JSONL](evidencias/deber5/codex-cli.jsonl) conserva la salida del CLI.

Desde la raíz del repositorio, con Python 3.11 o superior y Node.js con `npx`:

```bash
python3 -m venv mcp-detective/.venv
source mcp-detective/.venv/bin/activate
python -m pip install -r mcp-detective/requirements.txt
mcp version
python -m pytest mcp-detective -q
```

Para abrir el Inspector, ejecuta `mcp dev mcp-detective/server.py`. Si el lanzador no logra conectarse, esta es la variante que usé con el mismo SDK y el Python del entorno. El enlace temporal evita que el Inspector divida la ruta por los espacios.

```bash
ruta_inspector=$(mktemp -d)
ln -s "$PWD/mcp-detective/server.py" "$ruta_inspector/server.py"
npx -y @modelcontextprotocol/inspector@0.22.0 "$(command -v python)" "$ruta_inspector/server.py"
```

Para conectar Codex, agrega el servidor y abre una sesión nueva:

```bash
codex mcp add centinela -- "$(command -v python)" "$PWD/mcp-detective/server.py"
codex mcp list
codex
```

Pídele que liste los casos y consulte cada uno usando solo las tools de Centinela. Luego pide la alerta de `INC-003` y la consulta de `INC-999`. Consulta el [índice de capturas y pruebas](evidencias/deber5/README.md).
