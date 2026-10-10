# Análisis de spec y Constitution — borrador del agente

**Pendiente del estudiante (Parte 2):** el profesor exige este análisis a mano, antes del código. Esta tabla fue preparada por Codex como apoyo; no acredita que Leonardo realizó el ejercicio personal. Debes leer las dos fuentes, revisar la atomización y clasificación, y dejar tu propio análisis. La ejecución automatizada continúa por autorización del usuario.

## Método de conteo

Se cuenta cada aparición normativa en Input, historia, prueba independiente, aceptación, casos límite, requisitos, entidades, criterios y supuestos. Las repeticiones entre secciones se cuentan por aparición y se identifican por línea; no son requisitos adicionales. Se separan obligaciones independientes unidas por «y», «ni» o listas de restricciones. Un escenario conserva sus precondiciones y resultado como una regla verificable; la prohibición de mostrar resultado se separa. La definición de una entidad conserva su conjunto de atributos como una idea. No se cuentan título, fecha, branch, status, encabezados ni la explicación de prioridad. Son enunciados, no líneas Markdown.

## Spec

| Enunciado de la spec | Tipo (QUÉ/CÓMO/MIXTO) | ¿Viaja a React? | Justificación |
|---|---|---|---|
| S01 · spec.md:9 · Una app offline | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S02 · spec.md:9 · de una pantalla | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S03 · spec.md:9 · recibe monto | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S04 · spec.md:9 · recibe personas | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S05 · spec.md:9 · recibe propina | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S06 · spec.md:10 · permite elegir redondeo exacto | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S07 · spec.md:10 · permite elegir redondeo hacia arriba al entero | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S08 · spec.md:10 · muestra el valor por persona | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S09 · spec.md:16 · ingreso el monto total | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S10 · spec.md:17 · ingreso el número de personas | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S11 · spec.md:17 · ingreso el porcentaje de propina | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S12 · spec.md:17 · elijo el redondeo | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S13 · spec.md:18 · calculo cuánto paga cada persona | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S14 · spec.md:22 · Ingresar los valores de los seis escenarios y comprobar el resultado o mensaje indicado | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S15 · spec.md:23 · sin conexión de red | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S16 · spec.md:27 · 100.00, 4 personas, 10%, exacto → 27.50 | QUÉ | Intacto | Criterio observable con entradas y salida constantes |
| S17 · spec.md:28 · 90.00, 3 personas, 0%, exacto → 30.00 | QUÉ | Intacto | Criterio observable con entradas y salida constantes |
| S18 · spec.md:29 · 50.00, 0 personas → Debe haber al menos una persona | QUÉ | Intacto | Criterio observable con entradas y salida constantes |
| S19 · spec.md:29 · 50.00, 0 personas → no se muestra resultado | QUÉ | Intacto | Criterio observable con entradas y salida constantes |
| S20 · spec.md:30 · monto abc → Monto inválido | QUÉ | Intacto | Criterio observable con entradas y salida constantes |
| S21 · spec.md:31 · 10.00, 3 personas, 0%, exacto → 3.33 | QUÉ | Intacto | Criterio observable con entradas y salida constantes |
| S22 · spec.md:32 · 10.00, 3 personas, 0%, arriba → 4.00 | QUÉ | Intacto | Criterio observable con entradas y salida constantes |
| S23 · spec.md:36 · cero personas: se informa el error | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S24 · spec.md:36 · cero personas: no se muestra un resultado anterior | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S25 · spec.md:37 · monto no numérico: Monto inválido | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S26 · spec.md:37 · monto no numérico: no se muestra resultado | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S27 · spec.md:38 · el cálculo exacto presenta dos decimales | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S28 · spec.md:38 · hacia arriba lleva al entero siguiente cuando tiene fracción | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S29 · spec.md:44 · FR-001: ingresar monto total | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S30 · spec.md:44 · FR-001: ingresar número de personas | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S31 · spec.md:44 · FR-001: ingresar porcentaje de propina | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S32 · spec.md:44 · FR-001: una sola pantalla | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S33 · spec.md:45 · FR-002: seleccionar redondeo exacto | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S34 · spec.md:45 · FR-002: seleccionar redondeo hacia arriba al entero | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S35 · spec.md:46 · FR-003: sumar la propina porcentual al total antes de dividir por las personas | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S36 · spec.md:47 · FR-004: valor por persona exacto con dos decimales | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S37 · spec.md:48 · FR-005: redondeo hacia el entero siguiente | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S38 · spec.md:49 · FR-006: cero personas produce Debe haber al menos una persona | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S39 · spec.md:49 · FR-006: cero personas no produce resultado | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S40 · spec.md:50 · FR-007: monto no numérico produce Monto inválido | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S41 · spec.md:50 · FR-007: monto no numérico no produce resultado | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S42 · spec.md:51 · FR-008: cálculos locales | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S43 · spec.md:51 · FR-008: sin red | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S44 · spec.md:51 · FR-008: sin base de datos | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S45 · spec.md:55 · Cuenta: monto total, cantidad de personas y porcentaje de propina | QUÉ | Intacto | Concepto de negocio; no impone clase, carpeta ni lenguaje |
| S46 · spec.md:56 · Resultado: monto por persona luego de propina y redondeo | QUÉ | Intacto | Concepto de negocio; no impone clase, carpeta ni lenguaje |
| S47 · spec.md:57 · Estrategia de redondeo: regla seleccionada para convertir el valor por persona | QUÉ | Intacto | Concepto de negocio; no impone clase, carpeta ni lenguaje |
| S48 · spec.md:63 · SC-001: los seis escenarios producen exactamente el resultado o mensaje especificado | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S49 · spec.md:64 · SC-002: las entradas inválidas nunca muestran un resultado calculado | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S50 · spec.md:65 · SC-003: una sola pantalla | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S51 · spec.md:65 · SC-003: sin red | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S52 · spec.md:65 · SC-003: sin guardar datos | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S53 · spec.md:66 · SC-004: los seis escenarios se verifican repetiblemente con pruebas | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S54 · spec.md:70 · la propina es un porcentaje del monto total | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S55 · spec.md:70 · la propina se reparte entre las personas | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S56 · spec.md:71 · el modo exacto muestra dos decimales | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S57 · spec.md:71 · hacia arriba devuelve el entero siguiente por persona | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S58 · spec.md:72 · no se requiere persistencia | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S59 · spec.md:72 · no se requiere historial | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S60 · spec.md:72 · no se requiere autenticación | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S61 · spec.md:72 · no se requiere conexión de red | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |
| S62 · spec.md:72 · no se requieren más pantallas | QUÉ | Intacto | Comportamiento, alcance o condición verificable independiente del framework |

Total: **62 enunciados**. QUÉ: 62 (100.00 %); CÓMO: 0 (0 %); MIXTO: 0 (0 %).

Reutilización propuesta: 62/62 = **100 % intacto**, 0 % adaptado y 0 % no reusable. El diff deberá comprobar identidad textual inicial y final. La clasificación es del agente y requiere revisión personal.

El **30 % es el umbral pedagógico de este deber, no una regla universal de SDD**. El 0 % CÓMO no lo supera. No se detectó ningún enunciado Flutter que bloqueara el plan React; no se solicita modificar la spec.

## Constitution (separada de la spec)

Origen: `.specify/memory/constitution.md` del proyecto Flutter. La columna React describe la adaptación ejecutada, comprobada en evidencias/constitution.diff.

| ID y regla original (línea Flutter) | Clasificación | Redacción React | Justificación |
|---|---|---|---|
| C01 · L6 · Cada clase tiene una razón de cambio | adaptada en redacción | Cada función o módulo tiene una razón de cambio | Unidad de implementación en JavaScript |
| C02 · L6 · El cálculo no valida entradas | idéntica | El cálculo no valida entradas | SRP independiente de tecnología |
| C03 · L6 · El cálculo no formatea moneda | idéntica | El cálculo no formatea moneda | SRP independiente de tecnología |
| C04 · L7 · Validación, presentación y cálculo permanecen separados | idéntica | Validación, presentación y cálculo permanecen separados | SRP |
| C05 · L10 · CalcularDivision depende de EstrategiaRedondeo | adaptada en redacción | calcularDivision depende del contrato estrategiaRedondeo | Nombres JavaScript; misma abstracción |
| C06 · L11 · Agregar estrategia no modifica el cálculo | idéntica | Agregar estrategia no modifica el cálculo | OCP |
| C07 · L11 · Agregar estrategia no modifica estrategias existentes | idéntica | Agregar estrategia no modifica estrategias existentes | OCP |
| C08 · L14 · Cualquier implementación de EstrategiaRedondeo sustituye a otra | adaptada en redacción | Cualquier implementación de estrategiaRedondeo sustituye a otra | Nombre del contrato |
| C09 · L15 · El calculador no pregunta el tipo concreto | idéntica | El calculador no pregunta el tipo concreto | LSP |
| C10 · L15 · El calculador no hace casts | idéntica | El calculador no hace casts | LSP; no se agregan comprobaciones de tipo |
| C11 · L18 · EstrategiaRedondeo expone un único método | adaptada en redacción | estrategiaRedondeo expone una función aplicar(valor) | Contrato indicado en Parte 5 |
| C12 · L19 · Ningún cliente depende de operaciones no usadas | idéntica | Ningún cliente depende de operaciones no usadas | ISP |
| C13 · L22 · Presentación depende de abstracciones del domain | idéntica | Presentación depende de abstracciones del domain | DIP |
| C14 · L22 · domain no importa Flutter | adaptada en redacción | domain no importa React ni DOM | Parte 4 explicita el aislamiento equivalente |
| C15 · L23 · domain no depende de data | idéntica | domain no depende de data | DIP |
| C16 · L23 · Solo main.dart instancia implementaciones concretas | adaptada en redacción | Solo main.jsx compone implementaciones concretas | Punto de composición de React |
| C17 · L28 · Una pantalla para monto, personas, propina y resultado | idéntica | Una pantalla para monto, personas, propina y resultado | Mismo alcance |
| C18 · L29 · Capas presentation, domain y data | idéntica | Capas presentation, domain y data | Los nombres de las capas se conservan |
| C19 · L30 · presentation -> domain <- data | idéntica | presentation -> domain <- data | Misma regla de dependencia |
| C20 · L31 · domain es Dart puro | adaptada en redacción | domain es JavaScript puro | Cambio de lenguaje |
| C21 · L31 · Sin red | idéntica | Sin red | Mismo requisito offline |
| C22 · L31 · Sin base de datos | idéntica | Sin base de datos | Mismo alcance |
| C23 · L32 · No se agregan paquetes externos | reemplazada | Solo React/React DOM y herramientas Vite, Oxlint y pruebas exigidas | Las Partes 3 y 7 obligan a instalar paquetes npm |
| C24 · L32 · No se agregan secretos | idéntica | No se agregan secretos | Misma seguridad |
| C25 · L33 · Se usa null safety | reemplazada | Validación explícita de números y ausencia de resultado con null | JavaScript carece de null safety estática de Dart |
| C26 · L33 · Nombres en español | idéntica | Nombres en español | Misma convención |
| C27 · L37 · Cada criterio tiene una prueba ejecutable | idéntica | Cada criterio tiene una prueba ejecutable | Misma calidad |
| C28 · L38 · Cálculo crítico tiene pruebas sin widgets | adaptada en redacción | Cálculo crítico tiene pruebas sin React ni DOM | Vitest ejecuta el núcleo puro |
| C29 · L38 · Pantalla tiene pruebas de widgets | adaptada en redacción | Pantalla tiene pruebas del DOM con Testing Library | Cambia la herramienta de UI |
| C30 · L39 · Pasar flutter test | reemplazada | Pasar npm test | Runner requerido en Parte 7 |
| C31 · L39 · Pasar flutter analyze | reemplazada | Pasar npm run lint | Comprobación estática equivalente de plantilla Vite |
| C32 · L40 · Pasar flutter build apk --debug | reemplazada | Pasar npm run build | Producto web, no APK |
| C33 · L41 · Estudiante explica propósito, entradas, salida y errores de cada función | idéntica | Estudiante explica propósito, entradas, salida y errores de cada función | Misma obligación personal |
| C34 · L46 · La constitución prevalece sobre plan y código | idéntica | La constitución prevalece sobre plan y código | Misma gobernanza |
| C35 · L48 · Cada cambio requiere actualizar el archivo | idéntica | Cada cambio requiere actualizar el archivo | Misma gobernanza |
| C36 · L48 · Cada cambio requiere actualizar la versión | idéntica | Cada cambio requiere actualizar la versión | Misma gobernanza |
| C37 · L48 · Revisión comprueba capas | idéntica | Revisión comprueba capas | Misma gobernanza |
| C38 · L49 · Revisión comprueba los cinco SOLID | idéntica | Revisión comprueba los cinco SOLID | Misma gobernanza |
| C39 · L49 · Revisión comprueba pruebas requeridas por spec | idéntica | Revisión comprueba pruebas requeridas por spec | Misma gobernanza |

Total Constitution: **39 reglas atómicas**; idéntica: 25; adaptada en redacción: 9; reemplazada: 5.

No se añaden principios SOLID nuevos. DOM explicita el equivalente web de no depender del framework; la lista npm está impuesta por las Partes 3 y 7, y Oxlint conserva la comprobación estática existente. El lenguaje y los runners sí requieren reemplazo. No se conserva como idéntica la prohibición absoluta de paquetes externos ni se afirma que JavaScript tenga null safety.

## Trabajo personal pendiente

- Rehacer o revisar personalmente el análisis de la Parte 2 y sus denominadores antes de presentarlo como propio.
- Escribir personalmente `test/casosDePrueba.js` (Parte 7.2), conservando entradas, mensajes y esperados. El archivo generado por Codex será un borrador funcional.
- Explicar cada función y revisar las seis respuestas antes de entregar.

## Evidencia final y procedencia Git

- Spec inicial: evidencias/spec-inicial.diff vacío (0 bytes, código 0), commit d56ce40.
- Spec final: evidencias/spec-final.diff vacío (0 bytes, código 0).
- SHA-256 original y React: 36d61f7e911a07eb5d8de81a52b88ac66ae4d1593d12c5a22827e5a46c0046de.
- Constitution: commit 2c049f0, evidencias/constitution.diff; plan: 228f4b2 y ajustes
  de versiones resueltas/empates en 5f7402e. No existe cambio separado de spec porque no se cambió.
- Escenarios: scripts/comparar-casos.mjs confirmó 6/6 idénticos incluyendo NaN.
- El inventario Constitution tiene 39 obligaciones originales: 25 idénticas, 9
  adaptadas, 5 reemplazadas; metadatos versión/fecha no son obligaciones.
- React Constitution conserva las cinco secciones SOLID. C23 sustituye paquetes
  para cumplir las Partes 3 y 7; no librerías de estado explicita Parte 5, no un
  principio inventado. C25 sustituye null safety estática por validación explícita.
- El inventario de plan tiene 51 enunciados originales; 27 requirieron adaptación
  y 24 conservaron significado. Ver evidencias/plan-enunciados.md.

Citas Constitution React: SRP L6–7, OCP L10–11, LSP L14–15, ISP L18–19,
DIP L22–24, restricciones L28–37, pruebas/aprendizaje L41–45, gobernanza L49–52.
Las reglas originales y sus líneas están en la tabla anterior y snapshot
evidencias/flutter/constitution.md.
