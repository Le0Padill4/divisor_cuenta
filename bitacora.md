# Bitácora — Deber 2

## Autoría y medición

La ejecución técnica la realizó Codex, integración del laboratorio (Spec Kit 1.0.13).
No se ejecutó speckit-specify. Las Partes 2 y 7.2 **no se realizaron personalmente**:
analisis_spec.md y casosDePrueba.js son borradores generados por el agente para revisión
 o ejecución del estudiante. Los comandos autónomos, pruebas y las dos revisiones converge
no cuentan como mensajes de corrección del estudiante.

La tabla vacía se creó en la rama sdd Flutter, commit 61801e5, antes de planificar React.
El análisis preparado por el agente quedó en 47604f1; no equivale al análisis personal.

| Métrica | Flutter (laboratorio) | React (este deber) |
|---|---:|---:|
| Minutos hasta la primera versión que compila | no registrado | 6.3472 |
| Minutos hasta que pasan los 6 casos | no registrado | 6.4973 |
| Iteraciones con el agente | no registrado | 0 mensajes de corrección observados |
| Líneas de código escritas a mano | no registrado | 0 observadas en esta ejecución; Parte 7.2 pendiente |
| Enunciados modificados en la spec | — | 0 de 62 |
| Enunciados modificados en la Constitution | — | 14 de 39: 9 adaptados + 5 reemplazados |
| Líneas modificadas en el plan (físicas) | — | +103 / −59; 162 afectadas |
| Enunciados originales del plan adaptados | — | 27 de 51 inventariados |
| Casos de aceptación que pasan (0–6) | 6/6 verificados ahora | 6/6 |

El deber usa «líneas del plan» en su tabla y pide en 8.3 contar enunciados. Se informan
ambas unidades por separado. La atomización está en evidencias/plan-enunciados.md.
No se infieren métricas del laboratorio a partir de fechas de commits ni de recuerdos.

## Cronómetro automático (hora de Guayaquil)

- Inicio speckit-plan: 2026-10-09T21:47:48.810073-05:00.
- Primera compilación correcta: 2026-10-09T21:54:09.640093-05:00.
- Fin al concluir el primer runner de dominio con seis casos verdes: 2026-10-09T21:54:18.650910-05:00.
- Se eligió el fin del runner como momento observable en que todos los casos constan
  correctos. No se extendió la medición a pantallas, publicación ni documentación.
- Fuente: evidencias/cronometro.json y metadatos de build-primero/division-test.
- Es medición automática del agente, no un cronómetro manejado por el estudiante.
- El tiempo es contexto descriptivo; no prueba calidad ni permite comparar duración con Flutter.

## Registro por partes

1. **Origen:** ClaseApps/sdd, dd58c42efee5eec4f7f11df5df60b7d961d5f30b,
   Semana7_DivisorCuenta/divisor_cuenta. flutter test pasó 10 pruebas; exportación
   independiente por subtree conserva archivos e historial filtrado, 56c9b29.
   Feature: specs/001-divisor-cuenta; constitución: .specify/memory/constitution.md.
2. **Análisis:** borrador de 62 enunciados QUÉ (100 %), CÓMO/MIXTO 0 %;
   Constitution separada: 25 idénticas, 9 adaptadas, 5 reemplazadas. Pendiente personal.
3. **Proyecto:** create-vite 9.2.1, plantilla react JavaScript, npm install; Vite
   arrancó en 127.0.0.1:5178 y respondió HTML. Repositorios independientes;
   no se necesitó modificar un .gitignore de ClaseApps. Copia spec y diff 0 bytes
   antes del plan: commit d56ce40. La fuente adjunta se conserva en docs/Deber2.md.
4. **Constitution:** skill instalada speckit-constitution; resolve-template oficial;
   versión 2.0.0 por sustitución de reglas tecnológicas incompatibles. Cambios en
   2c049f0, informe constitution-workflow.md. Oxlint es el linter real de la plantilla;
   la previsión inicial de ESLint se corrigió antes del plan.
5. **Plan/tareas/analyze:** habilidades instaladas leídas y ejecutadas por este agente;
   setup-plan, setup-tasks y check-prerequisites oficiales. SPECIFY_FEATURE_DIRECTORY
   configurada; feature.json y scripts/feature-env.sh apuntan al directorio correcto.
   Se investigaron fuentes oficiales con un agente de investigación del flujo plan.
   Analyze: cobertura 12/12, cero contradicciones, dos observaciones LOW, no bloqueos.
   No fue un comando CLI que generase automáticamente texto: Codex ejecutó el workflow
   y redactó sus artefactos siguiendo la habilidad. Commit 228f4b2.
6. **Implement/converge:** pruebas antes del código, commit f39379c; primera ejecución
   roja: 2 suites no cargaron por módulos ausentes, no fueron seis assertions fallidas.
   Se implementó src sin cambiar test ni la spec. Converge disponible: primera revisión
   añadió T020–T022 por documentación, registro del navegador y publicación; el núcleo
   ya satisfacía FR/SC/AC. Se completan esos entregables y la segunda revisión comprueba
   su cierre. Esto son pasadas autónomas, no iteraciones del estudiante.
7. **Validación:** seis aceptación + LSP + tres pantallas = 10/10, lint correcto y build
   correcto. Controles SOLID y dependencias correctos; solo main compone concretas
   fuera de data. Pantalla real: 27.50, cero personas sin resultado, abc inválido y 4.00
   hacia arriba. No se acreditan observaciones móviles físicas ni trabajo manual.
8. **Medición:** spec final idéntica, 0 bytes; 6/6 escenarios conceptualmente idénticos;
   Constitution +15/−12 líneas físicas; plan +103/−59. Se distinguen líneas de enunciados.
   Las seis respuestas enlazan archivos, hashes y salidas reales. El umbral 30 % es
   pedagógico para este deber, no regla universal.

## Pendientes del estudiante

- Leer el adjunto, hacer/revisar personalmente el análisis inicial de Parte 2 y la
  atomización de tablas. El análisis automatizado no demuestra el ejercicio a mano.
- Escribir personalmente test/casosDePrueba.js (Parte 7.2), conservando los seis casos,
  y volver a ejecutar npm test. La copia actual está marcada como borrador del agente.
- Explicar las funciones, revisar respuestas y entregar los enlaces al profesor.

Todas las salidas relevantes se guardan en evidencias/ del proyecto React. La salida
Flutter también se conserva en evidencias/ del original independiente.

## Publicación verificada

Ambos repositorios públicos creados y enviados sin force-push; rama predeterminada sdd.
- https://github.com/Le0Padill4/divisor_cuenta
- https://github.com/Le0Padill4/divisor_cuenta_web

Comandos y salidas en github-publicacion.{txt,json}, flutter-github-publicacion.{txt,json}
y publicacion.json. ClaseApps original permanece en dd58c42, sin cambios de trabajo.
