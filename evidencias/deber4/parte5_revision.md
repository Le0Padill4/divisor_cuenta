# Revisión crítica de ci.yml

## Lo revisado

Se leyó el workflow completo de main y se comprobaron las acciones en sus
repositorios de origen. Los registros de versión y SHA acompañan esta evidencia.
El archivo tiene dos jobs, verificar y entrega, ambos en ubuntu-latest, con Java 17
y Flutter estable 3.47.8.

## Riesgos y decisiones

- **Entorno cambiante.** Usar stable sin versión hacía que una actualización futura
  pudiera cambiar el resultado sin cambiar el proyecto. Se recomendó fijar 3.47.8.
  Leonardo eligió esa opción en el chat y descartó seguir automáticamente la estable
  más reciente. Se aplicó a los dos jobs.
- **Acciones externas.** Se comprobaron checkout, setup-java, flutter-action y
  upload-artifact y se fijaron sus commits. Las tres de actions son del proyecto
  GitHub Actions; flutter-action es una acción comunitaria de subosito. Fijar un SHA
  no elimina todos los riesgos y exige revisar futuras actualizaciones.
- **Permisos.** El token solo tiene contents: read y checkout no deja credenciales
  guardadas. No se escribieron secretos ni se usa pull_request_target para ejecutar
  código de un PR con permisos elevados.
- **Entrega condicionada.** entrega depende de verificar y solo se habilita para
  push a refs/heads/main. No usa always ni continue-on-error. Prepara su entorno y
  recompila el mismo commit, porque los jobs no comparten sus archivos.
- **Archivo ausente.** upload-artifact usa if-no-files-found: error; no puede quedar
  verde fingiendo que subió un APK que no encontró.
- **Procesos colgados.** Cada job tiene un límite de veinte minutos.
- **Límites que permanecen.** ubuntu-latest y las descargas de dependencias son
  externos y pueden cambiar o fallar. Las doce pruebas cubren casos concretos,
  no todos los dispositivos o errores posibles. El CI tampoco reemplaza una
  revisión de los cambios del workflow y de las pruebas.
- **Alcance de CD.** Se publica un APK de depuración como artifact. No se añadieron
  despliegue de producción, servicios externos ni claves de firma de release.
  El artifact expira: se guarda la captura y una descarga local del APK.

No se añadieron paquetes Flutter ni acciones de terceros sin comprobar su existencia.
La comparación con deber3 de lib/, test/, dependencias y spec quedó vacía tras
restaurar la prueba intencionalmente incorrecta.

## Fuentes primarias consultadas

- https://docs.github.com/en/rest/branches/branch-protection
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches
- https://github.com/subosito/flutter-action
- https://github.com/actions/checkout
- https://github.com/actions/setup-java
- https://github.com/actions/upload-artifact
- https://storage.googleapis.com/flutter_infra_release/releases/releases_linux.json
