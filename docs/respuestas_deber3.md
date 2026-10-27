# Respuestas — Deber 3

## 1. Rojo antes de verde

La prueba esperaba «La propina no puede superar el 100%», pero recibió `null`.
Verla fallar primero era importante para comprobar que detectaba la regla que faltaba.

## 2. Linter vs. IA

El linter avisó de una variable de ejemplo sin usar (`unused_local_variable`).
La IA señaló el `100` sin nombre que fija el límite de propina. El linter no lo
marcó porque usar ese número es válido, aunque un nombre ayudaría a entenderlo.

## 3. Mi refactorización

Elegí el número mágico del límite de propina. Se reemplazó el `100` de la comparación
por la constante `_propinaMaximaPermitida`, conservando el mismo valor y mensaje.
Las doce pruebas siguieron pasando sin cambiar los resultados esperados.

## 4. Coverage

El archivo con menor cobertura fue `lib/main.dart`, con **35,71 %** (5 de 14 líneas).
Eso no significa que tenga errores: las pruebas no recorren gran parte del arranque.
La cobertura muestra qué líneas se ejecutaron, no si todo el código está correcto.
