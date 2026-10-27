# Deber 4 — De TDD a CI/CD: automatizar la verificación

**Programación Asistida de Aplicaciones · USFQ**
Prof. Jose David Vega Sánchez

---

## De qué se trata

En la Semana 7 escribiste la spec, en la 8 los escenarios y las pruebas (TDD). En este deber haces que
**esas pruebas se ejecuten solas** en cada cambio, y que un pull request **no se pueda unir si
fallan**.

```text
push / pull request → analyze → test → build → ✓ / ✗  →  (solo si ✓) se puede unir a main
```

### Sobre qué trabajas

**No empiezas una app nueva.** Trabajas sobre el **divisor de cuenta que ya construiste** en las
Semanas 7 y 8 (con sus pruebas). Lo que agregas hoy es la automatización alrededor de ese proyecto:
el workflow de CI, la protección de `main` y la entrega del APK.

- Si ya tienes el proyecto en tu computador, úsalo tal cual (abre su carpeta en VS Code).
- Si no lo tienes a mano, **clónalo** desde tu repositorio de GitHub:

```bash
git clone <url-de-tu-repositorio>
cd <carpeta-del-proyecto>
flutter pub get
flutter test        # debe terminar en verde antes de seguir
```

- El proyecto con sus pruebas debe estar en `main` (si lo tenías en la rama `sdd` o en la del
  Deber 3, únelo a `main` por pull request antes de empezar).
- Si el proyecto nunca se subió a GitHub, crea un repositorio y sube el proyecto a `main` primero.

Tiempo estimado: **1 a 2 horas**.

---

## Antes de empezar

- Repositorio del divisor de cuenta en GitHub, **público** (para que el profesor pueda revisarlo con solo el enlace), con el proyecto y sus pruebas en `main`, y `flutter test` en verde en local.
- Tu agente de código instalado y andando.
- Rama `main` protegible (repositorio tuyo, público o con Actions habilitado).
- Carpeta `evidencias/` en la raíz del proyecto: ahí van todas las capturas del deber.

---

## Parte 1 — El workflow de CI

Primero la rama, **después** el archivo: el agente debe escribir sobre una rama nueva, no sobre `main`.

```bash
git switch main
git pull
git switch -c ci/primer-pipeline
```

### ▶ Pídeselo al agente

```text
Crea .github/workflows/ci.yml para esta app Flutter. Debe ejecutarse en push a main
y en cada pull request, en una máquina limpia (ubuntu-latest), y correr en este orden:
flutter pub get, flutter analyze, flutter test, flutter build apk --debug.
Usa la versión estable de Flutter y no agregues nada más. No escribas secretos en el archivo.
```

**Verifica:** el archivo existe y **lo lees completo**. Anota qué hace cada paso.

```bash
git add . && git commit -m "ci: analyze, test y build en cada pull request"
git push -u origin ci/primer-pipeline
```

Abre el pull request y mira la pestaña **Actions**. Debe aparecer un ✓ verde. **Fusiona este
pull request a `main`** antes de continuar: así el check de CI ya existe y podrás exigirlo en la Parte 2.

📸 `evidencias/parte1_ci_verde.png`

---

## Parte 2 — Proteger `main`

En GitHub: **Settings → Branches → Add branch protection rule** sobre `main`:

- Require a pull request before merging.
- Require status checks to pass before merging → selecciona el job de CI (aparece porque ya corrió en la Parte 1).

**Verifica:** la regla queda guardada y `main` ya no acepta push directo.

📸 `evidencias/parte2_proteccion.png` (**obligatoria**: la configuración de la protección no se ve desde el enlace del repositorio; esta captura es la prueba de que la hiciste)

---

## Parte 3 — Hacerlo fallar a propósito

Un pipeline que nunca falla no demuestra nada.

```bash
git switch main
git pull
git switch -c ci/rojo-a-proposito
```

1. Cambia el resultado esperado de un escenario en tu archivo de pruebas (por ejemplo, 27.50 → 27.00
   en `test/casos_de_prueba.dart`). Ese nombre y ese valor son ejemplos: usa la prueba equivalente
   de tu propio proyecto.
2. Haz commit y push, y abre un pull request.
3. Observa el ✗ rojo: lee el log y localiza la línea que falló.
4. **Captura el ✗, el fragmento del log y el botón de *merge* bloqueado.** No corrijas nada todavía.

```bash
# edita tu archivo de pruebas
git commit -am "test: fallo intencional para ver el pipeline en rojo"
git push -u origin ci/rojo-a-proposito
```

📸 `evidencias/parte3_rojo.png` (✗ y log) · `evidencias/parte3_merge_bloqueado.png`

5. Ahora corrige **el mismo PR**: restaura la prueba, haz commit y push en la misma rama, y confirma que
   el pipeline vuelve a ✓ y que el *merge* se habilita.

📸 `evidencias/parte3_verde_otra_vez.png`

**Verifica:** el PR muestra el historial de un ✗ y luego un ✓. Fusiónalo cuando esté en verde.

---

## Parte 4 — CD: entregar solo lo que pasó

Agrega un job que se ejecute **solo si CI pasó** y solo en `main`, y que publique el APK como
*artifact* del workflow.

> Los jobs de GitHub Actions corren en **entornos independientes**: el job `entrega` **no** encuentra
> el APK que compiló `verificar`. Hay dos formas correctas: (a) `entrega` **genera de nuevo el APK**,
> o (b) `verificar` lo sube con `upload-artifact` y `entrega` lo recupera con `download-artifact`.

```bash
git switch main
git pull
git switch -c ci/entrega
```

### ▶ Pídeselo al agente

```text
Extiende ci.yml: agrega un job "entrega" que dependa del job de CI (needs) y corra
solo en push a main. Como los jobs no comparten archivos, haz que "entrega" vuelva a
generar el APK (flutter build apk --debug) y lo suba con actions/upload-artifact
(o, alternativamente, que "verificar" lo suba y "entrega" lo descargue con
actions/download-artifact). No uses secretos y no despliegues a ningún servicio externo.
```

**Verifica:** abre el pull request, espera el ✓, fusiónalo y descarga el artifact desde **Actions**.

📸 `evidencias/parte4_artifact.png` (**obligatoria**: los artifacts de Actions expiran con el tiempo; la captura de la sección *Artifacts* del run, con el APK listado, es tu respaldo)

> Esto es una **introducción a la entrega automatizada**: el artefacto queda generado tras pasar CI.
> Un APK de depuración **no** está listo para publicarse a usuarios finales; un release de producción
> exige build de release, firma y otros controles. Desplegar a producción sin aprobación humana
> sería *continuous deployment*.

---

## Parte 5 — Revisión crítica del agente

Pídele a tu agente: *"Revisa mi ci.yml: ¿qué riesgos de seguridad o fragilidad tiene?"*
Lee la respuesta con ojo crítico: ¿alguna sugerencia agrega dependencias o acciones de
terceros que **no verificaste**? Recuerda que un agente puede proponer paquetes que no existen.

---

## Parte 6 — Entrega

`main` está protegida: **no se hace push directo**. Sube tus respuestas y capturas en una rama con pull request.

```bash
git switch main
git pull
git switch -c deber4
# agrega respuestas.md en la raíz y las capturas en evidencias/
git add respuestas.md evidencias/
git commit -m "deber4: respuestas y evidencias"
git push -u origin deber4
```

Abre el pull request de `deber4` hacia `main`. Las imágenes se guardan en `evidencias/` y se enlazan
desde `respuestas.md`.

### Formulación: qué entregas

- **Entrega:** un único **enlace** al pull request de `deber4`. El repositorio debe ser **público**: el
  profesor revisa todo desde ese enlace (workflow, PR rojo y verde, Actions, `respuestas.md` y `evidencias/`).
- **Evidencia:** las capturas de `evidencias/` (partes 1 a 4). Dos son indispensables porque el enlace no las
  muestra: la **protección de `main`** y el **artifact** del APK.
- **Pregunta:** ¿qué detectó el pipeline que tú no habías visto? (pregunta 7).
- **Cierre:** ¿qué garantiza realmente un CI verde y qué errores pueden quedar sin detectar? (pregunta 6).

---

## Preguntas

Responde en `respuestas.md`, en la raíz del proyecto. Respuestas cortas, con tus palabras.

1. Pega tu `ci.yml` y explica, en una línea cada uno, qué hace `analyze`, `test` y `build`.
2. Adjunta la captura del ✗ de la Parte 3. ¿Qué línea del log te dijo exactamente qué falló?
3. ¿Qué diferencia hay entre *continuous integration*, *continuous delivery* y *continuous
   deployment*? ¿Cuál implementaste y por qué?
4. Adjunta la captura del *merge* bloqueado (Parte 3). ¿Qué problema evita que `main` quede roto?
5. ¿Qué sugirió el agente en la Parte 5? ¿Cuál aceptaste y cuál rechazaste, y por qué?
6. ¿Qué garantiza realmente un CI verde y qué errores pueden quedar sin detectar? Da un ejemplo de un error que pasaría en verde.
7. ¿Qué detectó el pipeline que tú no habías visto?

---

## Antes de entregar

- [ ] `.github/workflows/ci.yml` está en `main` (fusionado por pull request).
- [ ] El pipeline corre `analyze`, `test` y `build` en cada pull request.
- [ ] Hay un pull request que falló (✗) y luego pasó (✓), con la captura del *merge* bloqueado.
- [ ] El repositorio es **público**.
- [ ] `main` tiene protección de rama con el check de CI requerido (captura `parte2_proteccion.png`).
- [ ] El job de entrega genera o descarga el APK y lo sube como artifact (captura `parte4_artifact.png`).
- [ ] No hay secretos ni claves en el repositorio ni en el workflow.
- [ ] La rama `deber4` tiene `respuestas.md` y la carpeta `evidencias/` (imágenes enlazadas desde `respuestas.md`), y su pull request está abierto hacia `main`.
- [ ] Entregas **solo el enlace** a ese pull request.
