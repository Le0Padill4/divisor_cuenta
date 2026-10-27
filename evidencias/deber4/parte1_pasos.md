# Lectura del primer workflow

- Obtener el proyecto: descarga el código del commit del PR; no deja credenciales de escritura en Git.
- Preparar Java: instala Java 17, compatible con la configuración Android del proyecto.
- Preparar Flutter estable: prepara el SDK del canal estable.
- flutter pub get: obtiene las dependencias declaradas.
- flutter analyze: revisa el código sin ejecutarlo y falla si encuentra problemas.
- flutter test: ejecuta las pruebas del proyecto.
- flutter build apk --debug: comprueba que la app se pueda compilar como APK de depuración.

El runner es ubuntu-latest. Se ejecuta en cada PR y en push a main. Los pasos se
procesan en orden; si uno falla, los siguientes no se ejecutan. El token tiene
contents: read. Las acciones se fijaron a SHA comprobados en sus repositorios.
