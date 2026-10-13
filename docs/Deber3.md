# Deber 3 — TDD, linter y refactorización en el divisor de cuenta

**Programación Asistida de Aplicaciones · USFQ**
Prof. Jose David Vega Sánchez

---

## De qué se trata

En clase vimos cuatro ideas:

| Idea | En una frase |
|---|---|
| **TDD** | primero la prueba, verla fallar (rojo), después el código mínimo (verde), y al final limpiar (refactor) |
| **Linter** | un programa que lee tu código sin ejecutarlo y avisa lo que rompe una regla |
| **Code smell** | código que funciona, pero que va a costar entender o cambiar |
| **Refactorizar** | mejorar la forma del código **sin cambiar lo que hace** |

En este deber vas a aplicar las cuatro, **una sola vez y en pequeño**, sobre una app que ya
tienes: el **divisor de cuenta** que construiste en la **Participación de la Semana 7**
(*Vibe coding vs. SDD con GitHub Spec Kit*), en la rama `sdd`.

La regla nueva que vas a agregar con TDD es:

> **La propina no puede superar el 100 %.**
> Si supera 100, la app muestra *"La propina no puede superar el 100%"* y no calcula nada.
> Una propina de exactamente 100 % sí está permitida.

Tiempo estimado: **1 a 2 horas**.

---

## Antes de empezar: ¿qué es `flutter test`?

`flutter test` es un comando que **viene incluido con Flutter**: no hay que instalar nada.
Busca todos los archivos de la carpeta `test/` que terminan en `_test.dart`, ejecuta las
pruebas que hay dentro y al final te dice si pasaron todas o cuáles fallaron.

En la Participación de la Semana 7 ya lo usaste: en la **Parte 9** de esa participación, en la
rama `sdd`, creaste estos archivos y los corriste con `flutter test`:

| Archivo | Qué tenía |
|---|---|
| `test/casos_de_prueba.dart` | los seis casos de la spec (entradas y resultados esperados) |
| `test/division_test.dart` | recorre esos casos y los verifica, más la prueba de LSP |
| `test/pantalla_test.dart` | tres pruebas de la pantalla |

En este deber vas a **agregar pruebas nuevas** a `test/division_test.dart`.

---

## Parte 1 — El punto de partida: todo en verde

### 1.1 Vuelve al proyecto de la participación

Abre en VS Code la carpeta `divisor_cuenta` de la Semana 7 y, en la terminal:

```bash
git checkout sdd
flutter test
```

Al final debe decir **`All tests passed!`**. Eso quiere decir que todas las pruebas que
creaste en la participación siguen pasando. TDD siempre empieza desde un punto en verde.

📸 `evidencias/parte1_verde.png` (crea la carpeta `evidencias/` en la raíz del proyecto;
ahí van todas las capturas del deber)

| Si te pasa esto… | Qué haces |
|---|---|
| Alguna prueba falla | Arréglala antes de seguir: no se agrega nada nuevo sobre algo roto. |
| No existe la carpeta `test/` con esos archivos (no llegaste a la Parte 9 de la participación) | Haz primero la **Parte 9** de la Participación de la Semana 7 y después vuelve aquí. |
| `flutter test` solo corre `widget_test.dart` y falla | Es la prueba de ejemplo que Flutter crea por defecto (la del contador). Bórrala: tu app ya no es el contador. |

### 1.2 Crea una rama para este deber

```bash
git checkout -b deber3
```

Así todo lo que hagas queda separado y, si algo sale mal, la rama `sdd` sigue intacta.

---

## Parte 2 — ROJO: primero la prueba

Todavía **no** se toca el código de la app. Primero se escribe lo que debe pasar.

### ▶ Pídeselo al agente

```text
Lee lib/domain/ y test/.
Escribe SOLO dos pruebas nuevas en test/division_test.dart para esta regla:
"La propina no puede superar el 100 %".

1. Con monto 100, 4 personas y propina 150, la validación devuelve
   exactamente "La propina no puede superar el 100%".
2. Con monto 100, 4 personas y propina 100, la validación NO devuelve error
   (el límite exacto sí se permite).

NO toques lib/. No implementes nada. Solo las pruebas.
```

**Revisa lo que escribió** antes de seguir: abre `test/division_test.dart` y comprueba que
las dos pruebas dicen exactamente lo de arriba (números y mensaje). Si el agente tocó algo
en `lib/`, deshazlo con `git restore lib/`.

Ahora corre:

```bash
flutter test
```

Debe salir **en rojo**: la prueba 1 falla porque la regla todavía no existe. La prueba 2
probablemente pasa (hoy no hay ninguna regla que la rechace), y eso está bien: protege el
límite para cuando escribas el código.

📸 `evidencias/parte2_rojo.png`

Guarda este momento en git:

```bash
git add test/
git commit -m "rojo: pruebas de propina maxima 100"
```

> **¿Por qué ver el rojo?** Si una prueba nunca falló, no sabes si realmente prueba algo.
> El rojo demuestra que la prueba detecta el problema.

---

## Parte 3 — VERDE: el código mínimo

### ▶ Pídeselo al agente

```text
Escribe el código mínimo en lib/ para que las pruebas nuevas pasen.
No modifiques nada en test/. No agregues funcionalidades extra.
Al terminar, corre flutter test.
```

Corre tú también:

```bash
flutter test
```

Todo debe estar **en verde**: las pruebas viejas y las dos nuevas.

📸 `evidencias/parte3_verde.png`

### Comprueba que el agente no hizo trampa

```bash
git diff --stat
```

En la lista **solo** deben aparecer archivos de `lib/`. Si aparece algo de `test/`, el
agente cambió la prueba para que pase: eso no vale. Revierte ese archivo con
`git restore test/` y vuelve a pedirle el código.

```bash
git add lib/
git commit -m "verde: propina maxima 100"
```

---

## Parte 4 — El linter

```bash
flutter analyze
```

Pueden pasar dos cosas:

| Resultado | Qué haces |
|---|---|
| `No issues found!` | Agrega a propósito, en cualquier archivo de `lib/`, una variable que no se usa y un `print('hola');`. Corre `flutter analyze` otra vez para ver los avisos. Después bórralos. |
| Aparecen avisos | Léelos. Cada uno dice el archivo, la línea y el nombre de la regla. |

📸 `evidencias/parte4_analyze.png` (la salida **con** avisos)

Si había avisos reales en tu código, corrígelos:

### ▶ Pídeselo al agente

```text
Corrige SOLO los avisos que reporta flutter analyze.
No cambies el comportamiento de la app. No toques test/.
Al terminar, corre flutter analyze y flutter test.
```

Debe quedar `No issues found!` y las pruebas en verde.

```bash
git add .
git commit -m "linter: sin avisos"
```

Si `flutter analyze` ya estaba limpio y solo agregaste y borraste los avisos de prueba, no
habrá nada que guardar: sáltate este commit.

---

## Parte 5 — Code smells con IA

El linter ya no se queja. Ahora le pedimos a la IA que mire lo que una regla fija no ve.

### ▶ Pídeselo al agente

```text
Revisa los archivos de lib/.
Lista los code smells que encuentres: archivo, línea, cuál es y por qué molesta.
NO cambies el código todavía.
```

Lee la lista con calma. Algunos ejemplos de lo que puede aparecer:

| Code smell | Cómo se ve |
|---|---|
| Número mágico | un `100` suelto en el código |
| Nombres pobres | variables como `a`, `x`, `tmp`, `res` |
| Código duplicado | la misma validación escrita dos veces |
| Función larga | un método que valida, calcula y formatea a la vez |

**Elige UNO** (el que entiendas mejor). Anótalo, lo vas a usar en la pregunta 3.

> La IA puede equivocarse o exagerar. Si un "smell" no te convence, no lo elijas: decides tú.

---

## Parte 6 — Refactorizar sin romper nada

Antes de tocar nada, confirma que estás en verde y que todo está guardado:

```bash
flutter test
git status          # debe decir "nothing to commit"
```

### ▶ Pídeselo al agente

```text
Refactoriza SOLO este code smell: <pega aquí el que elegiste>.
No cambies el comportamiento. No modifiques test/.
Al terminar, corre flutter test.
```

Ahora corre tú:

```bash
flutter test
```

| Si sale… | Qué haces |
|---|---|
| **Verde** | Revisa el cambio con `git diff` y haz commit. |
| **Rojo** | El agente cambió más de lo que debía. Revierte con `git restore .` y pídeselo otra vez, más concreto. No le pidas que "arregle las pruebas". |

📸 `evidencias/parte6_refactor.png` (la salida de `git diff` o de `flutter test` en verde)

```bash
git add lib/
git commit -m "refactor: <nombre del smell>"
```

---

## Parte 7 — ¿Cuánto cubren tus pruebas?

```bash
flutter test --coverage
```

Esto crea el archivo `coverage/lcov.info`. No hace falta instalar nada para leerlo:

### ▶ Pídeselo al agente

```text
Lee coverage/lcov.info y muéstrame una tabla con el porcentaje de líneas
cubiertas por cada archivo de lib/. No cambies ningún archivo.
```

📸 `evidencias/parte7_coverage.png`

La carpeta `coverage/` no se sube al repositorio: abre el archivo `.gitignore` en VS Code
y agrega al final una línea que diga:

```text
coverage/
```

> Recuerda: el coverage dice **qué partes ejecutaron tus pruebas**, no si el código está bien.

---

## Parte 8 — Entrega

Mira tu historia: tiene que contar el ciclo completo, en orden.

```bash
git log --oneline
```

Debería verse algo parecido a esto (lo más nuevo arriba):

```text
a1b2c3d refactor: numero magico
d4e5f6a linter: sin avisos
0718293 verde: propina maxima 100
4a5b6c7 rojo: pruebas de propina maxima 100
...
```

📸 `evidencias/parte8_log.png`

Sube la rama:

```bash
git add .
git commit -m "deber3: evidencias y respuestas"
git push -u origin deber3
```

---

## Preguntas

Responde en `respuestas.md`, en la raíz del proyecto. Respuestas cortas, con tus palabras.

1. **Rojo antes de verde.** ¿Qué mensaje de error te mostró `flutter test` en la Parte 2?
   ¿Por qué era importante ver esa prueba fallar **antes** de escribir el código?

2. **Linter vs. IA.** Nombra un aviso que te mostró `flutter analyze` y un code smell que te
   señaló la IA. ¿Por qué el linter no encontró el code smell?

3. **Tu refactorización.** ¿Qué code smell elegiste, qué cambió en el código y cómo sabes
   que la app sigue haciendo exactamente lo mismo?

4. **Coverage.** ¿Qué archivo de `lib/` tiene el porcentaje más bajo? ¿Significa eso que
   ese archivo tiene errores? Explica.

---

## Antes de entregar

- [ ] La rama `deber3` está subida a GitHub.
- [ ] `flutter test` termina en verde, incluidas las dos pruebas nuevas de la propina.
- [ ] `flutter analyze` dice `No issues found!`.
- [ ] `git log --oneline` muestra los commits de rojo, verde y refactor, en ese orden (y el
      de linter, si tuviste que corregir avisos).
- [ ] La carpeta `evidencias/` tiene las capturas de las partes 1, 2, 3, 4, 6, 7 y 8.
- [ ] `respuestas.md` tiene las cuatro respuestas.
