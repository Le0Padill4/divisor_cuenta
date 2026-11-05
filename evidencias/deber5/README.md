# Evidencias del Deber 5

- [Código del servidor](../parte1_server.png) con las tres herramientas.
- [Discovery](../inspector_tools.png) mediante el Inspector 0.22.0 conectado por `stdio`.
- [Historial del Inspector](../inspector_pruebas.png) y resultados individuales abajo.
- [Nueve pruebas aprobadas](../pytest.png) con SDK 2.3.0. [Salida de pytest](pytest.txt).
- [Llamadas de Codex CLI](../agente_tools.png) y [salida JSONL original](codex-cli.jsonl).

| Prueba | Resultado observado | Captura |
| --- | --- | --- |
| D1 | Tres casos con 2, 6 y 5 eventos. | [D1](D1.png) |
| D2 | Seis fallos de `admin`, de 02:10 a 02:15. | [D2](D2.png), [detalle](D2-eventos.png) |
| D3 | `El caso INC-999 no existe.` | [D3](D3.png) |
| D4 | Alerta alta para `INC-003` con estado `registrada`. | [D4](D4.png) |
| D5 | La misma llamada en el mismo proceso devolvió un error de duplicado. | [D5](D5.png) |
| D6 | El nivel `critico` fue rechazado. | [D6](D6.png) |
| D7 | El motivo de solo espacios fue rechazado. | [D7](D7.png) |
| 2c | Tras usar **Restart**, el PID cambió de 32541 a 32610 y la misma alerta se registró otra vez. | [Reinicio](reinicio.png), [PID anterior](pid-antes.txt), [PID nuevo](pid-despues.txt) |

Las capturas del Inspector son de su interfaz en Safari. Las de código, pytest y agente muestran en Safari el archivo fuente, la salida de pytest y una vista de la traza de Codex CLI, respectivamente. La vista de Codex ordena los argumentos y resultados del JSONL para que se puedan leer juntos.

La investigación se ejecutó en una sesión nueva de Codex CLI, desde un directorio vacío y con la herramienta de terminal desactivada. Se usó el Python del entorno virtual y la ruta absoluta de `server.py`. La autorización para registrar una alerta se limitó a la tool de este servidor simulado durante esa sesión. La traza contiene las seis llamadas y sus resultados.

La implementación usa [MCP Python SDK v2](https://py.sdk.modelcontextprotocol.io/). Los errores de validación son `ValueError` en Python y también `ToolError` para que el SDK v2 comunique el mensaje al cliente. La configuración de la sesión siguió la [guía de MCP en Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli).
