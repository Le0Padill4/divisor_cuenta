# Entrega — Deber 3

Rama: **deber3**. Repositorio: [divisor_cuenta](https://github.com/Le0Padill4/divisor_cuenta/tree/deber3).
Fuente: [Deber3.md](docs/Deber3.md). Respuestas: [respuestas.md](respuestas.md).

Se reutilizó la exportación independiente del proyecto de Semana 7. Antes de empezar,
lib/ y test/ eran idénticos al original ClaseApps/sdd, commit dd58c42.
La rama sdd del repositorio independiente partía de 2e98ebe.
La procedencia está en [PROCEDENCIA.md](PROCEDENCIA.md) y [origen.json](evidencias/origen.json).

## Recorrido de las ocho partes

| Parte | Resultado y evidencia |
|---|---|
| 1. Punto de partida | 10/10 pruebas; captura parte1_verde.png. Después se creó deber3 desde sdd. |
| 2. Rojo | Se agregaron solo las dos pruebas pedidas. La de 150 falló con Expected: mensaje exacto / Actual: null; 11 pasaron y 1 falló. Solo cambió test/division_test.dart. Commit 0dd51cd. |
| 3. Verde | Se agregó únicamente la validación de propina > 100 en lib/domain/validar_entrada.dart. 12/12 pruebas y diff de una sola ruta lib/. Commit e5371b0. |
| 4. Linter | Inicialmente limpio. Se agregaron temporalmente una variable sin usar y print('hola'); apareció unused_local_variable. Se quitaron ambos y volvió No issues found! No había avisos reales que corregir, así que se omitió el commit de linter, como permite el deber. |
| 5. Code smells | Se revisaron los once archivos Dart. Se listaron dos números mágicos y Leonardo eligió el límite de propina en este chat. Ver parte5_smells.md y parte5_eleccion.md. |
| 6. Refactor | Antes: 12/12 y working tree clean. Se nombró el límite con una constante, sin cambiar la regla ni las pruebas. Después: 12/12. Commit bc4e5df. |
| 7. Cobertura | 12/12 con --coverage; 71/82 líneas medidas, 86,59 %. Menor: lib/main.dart, 5/14, 35,71 %. La interfaz no tiene líneas ejecutables registradas: N/D. /coverage/ ya estaba en .gitignore y git check-ignore lo confirmó. |
| 8. Entrega | Captura parte8_log.png con rojo → verde → refactor en el historial; cuatro respuestas y siete capturas para publicar en la rama deber3. |

## Comportamiento de la regla nueva

Una propina de 150 devuelve exactamente «La propina no puede superar el 100%».
Una propina de 100 sigue permitida. El controlador ya borra el resultado previo y
retorna cuando recibe un error de validación; por ese camino no se ejecuta el cálculo.
Las dos pruebas nuevas son de validación; las tres pruebas originales de pantalla
se conservan sin cambios.

## Evidencias

Las capturas están indexadas en [README_deber3.md](evidencias/README_deber3.md).
Los .txt contienen salidas reales; los .json registran comando, fecha UTC, estado Git,
código de salida y huellas de lib/ y test/. Las capturas son pantallas auténticas de
VS Code mostrando esos archivos de salida. La herramienta entregó JPEG y se convirtió
a PNG, sin recortar ni redibujar el contenido.

La ejecución de comandos y las capturas las realizó Codex. La elección del problema
se recibió directamente de Leonardo. No se atribuyen al estudiante ejecuciones manuales.

[tests_sin_cambios.diff](evidencias/tests_sin_cambios.diff) está vacío: test/ se mantuvo
igual desde el commit rojo durante verde y refactor. [archivos_preservados.diff](evidencias/archivos_preservados.diff)
también está vacío: se conservaron la spec, la constitución, las dependencias,
la configuración del analizador y las carpetas android/ e ios/.

Para repetir la tabla de cobertura:

```bash
flutter test --coverage
python3 scripts/tabla_coverage.py coverage/lcov.info
```

coverage/lcov.info permanece local e ignorado; solo se publican la tabla y su resumen.
Los documentos del Deber 2 conservados en esta rama son antecedentes; las respuestas
actuales del Deber 3 están en respuestas.md y este documento describe el nuevo trabajo.
