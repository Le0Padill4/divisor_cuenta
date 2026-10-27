# Evidencias — Deber 3

| Parte | Captura | Salida |
|---|---|---|
| 1: diez pruebas en verde | [parte1_verde.png](parte1_verde.png) | [parte1_verde.txt](parte1_verde.txt) |
| 2: la prueba nueva falla | [parte2_rojo.png](parte2_rojo.png) | [parte2_rojo.txt](parte2_rojo.txt) |
| 3: doce pruebas en verde y diff limitado a lib/ | [parte3_verde.png](parte3_verde.png) | [parte3_verde.txt](parte3_verde.txt), [parte3_diff.txt](parte3_diff.txt) |
| 4: aviso de variable sin usar | [parte4_analyze.png](parte4_analyze.png) | [parte4_analyze.txt](parte4_analyze.txt) |
| 6: refactor y pruebas verdes | [parte6_refactor.png](parte6_refactor.png) | [parte6_refactor.txt](parte6_refactor.txt), [parte6_diff.txt](parte6_diff.txt) |
| 7: tabla de cobertura | [parte7_coverage.png](parte7_coverage.png) | [parte7_coverage.txt](parte7_coverage.txt), [parte7_test.txt](parte7_test.txt) |
| 8: historial en orden | [parte8_log.png](parte8_log.png) | [parte8_log.txt](parte8_log.txt) |

Cada salida tiene su registro .json con el mismo nombre. [capturas_deber3.json](capturas_deber3.json)
registra las huellas de imágenes y salidas mostradas. Son capturas auténticas de VS Code,
mostrando los logs guardados de las ejecuciones del agente, convertidas a PNG.

El aviso se introdujo a propósito porque el análisis inicial estaba limpio. El código
temporal está en parte4_temporal.dart.txt; se agregaron la variable y print('hola').
La configuración actual no activó un aviso para print: el único aviso observado fue
unused_local_variable. Después se restauró exactamente el contenido anterior.
El análisis inicial, el posterior a la limpieza y el final están en parte4_inicial.txt,
parte4_final.txt y analyze_final.txt: los tres dicen No issues found!

La revisión y la elección están en [parte5_smells.md](parte5_smells.md) y
[parte5_eleccion.md](parte5_eleccion.md). La cobertura se obtiene exclusivamente del LCOV
real generado por Flutter; coverage_resumen.json conserva su hash y los conteos.
