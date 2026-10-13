# Revisión de code smells — Parte 5

Revisión del código limpio en el commit e5371b0, antes de refactorizar.
Se leyeron los once archivos Dart de lib/. No se cambió el código durante la revisión.

| Archivo y línea | Code smell | Por qué puede molestar | Adaptación propuesta |
|---|---|---|---|
| lib/domain/validar_entrada.dart:14 | Número mágico: 100 como límite de propina | El nombre de la regla solo se entiende al leer la comparación y el mensaje; una constante expresa qué límite representa. | Usar una constante propinaMaximaPermitida y conservar el valor 100 y el mensaje exacto. |
| lib/data/redondeo_exacto.dart:5 | Número mágico: factor 100 repetido | El factor define dos decimales, pero no tiene un nombre que explique su propósito. | Usar una constante factorDosDecimales, conservando la misma fórmula. |

Son oportunidades pequeñas de legibilidad, no errores funcionales. El linter actual
no exige constantes para esos números. Recomendación: el límite de propina,
porque conecta directamente con la regla nueva del deber y es fácil de explicar.
Solo se refactorizará una opción.
