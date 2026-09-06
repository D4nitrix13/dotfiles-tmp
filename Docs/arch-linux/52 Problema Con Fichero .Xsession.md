<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Si tienes problema con fichero `.xsession` hay algunas cosas que podrías verificar:***

1. **Permisos de ejecución:** *Asegúrate de que el fichero `.xsession` tenga permisos de ejecución para que el sistema pueda ejecutarlo al iniciar sesión. Puedes establecer estos permisos con el siguiente comando:*

   ```bash
   chmod u+x ~/.xsession
   ```

2. **Configuración del entorno de inicio de sesión:** *Dependiendo de tu entorno de inicio de sesión (como `startx`, `lightdm`, `gdm`, etc.), es posible que necesites configurar explícitamente que se ejecute el script `.xsession`. Por ejemplo, si usas `startx`, puedes agregar la siguiente línea al fichero `~/.xinitrc`:*

   ```bash
   exec ~/.xsession
   ```

3. **Reiniciar el entorno de escritorio o iniciar sesión nuevamente:** *Después de realizar cambios en el fichero `.xsession` o en la configuración del inicio de sesión, es posible que necesites reiniciar tu entorno de escritorio o cerrar sesión y volver a iniciar sesión para que los cambios surtan efecto.*

- *Verifica estos puntos y prueba reiniciar o iniciar sesión nuevamente para ver si el script `.xsession` se ejecuta correctamente. Si continúas teniendo problemas, podría ser útil revisar los registros del sistema para ver si hay algún mensaje de error relevante que pueda ayudar a diagnosticar el problema.*
