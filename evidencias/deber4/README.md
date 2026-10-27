# Evidencias del Deber 4

Las capturas en la carpeta superior son imágenes reales de GitHub; `capturas.json` indica su origen y la conversión a PNG. Los archivos de esta carpeta conservan las respuestas de GitHub, registros y diferencias del trabajo.

- [Preparación de main](https://github.com/Le0Padill4/divisor_cuenta/pull/1).
- [Primer pipeline y CI verde](https://github.com/Le0Padill4/divisor_cuenta/pull/2), [ejecución](https://github.com/Le0Padill4/divisor_cuenta/actions/runs/40557792436).
- [PR con fallo intencional y corrección](https://github.com/Le0Padill4/divisor_cuenta/pull/3): [fallo](https://github.com/Le0Padill4/divisor_cuenta/actions/runs/40558941427) y [corrección](https://github.com/Le0Padill4/divisor_cuenta/actions/runs/40560008349).
- [Entrega del APK](https://github.com/Le0Padill4/divisor_cuenta/pull/4): [ejecución en main y artifact](https://github.com/Le0Padill4/divisor_cuenta/actions/runs/40562278119).

El APK descargado de esa ejecución pasó una comprobación de integridad ZIP. Su SHA-256 es `ec8854b20233883c34621465e8a29b986481dc772cf2077a38cffb4f35f39d65`; el digest del archivo comprimido de GitHub es distinto y figura en `parte4_artifacts.json`.

La prueba inicial y las acciones registradas fueron ejecutadas por Codex. Leonardo eligió fijar Flutter 3.47.8. Los archivos `codigo_y_pruebas_preservados.diff` y `parte3_pruebas_restauradas.diff` vacíos registran las comparaciones indicadas.
