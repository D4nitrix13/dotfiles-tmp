<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Ejecuta estos comandos si tienes problema con el audio***

```bash
rm ~/.config/pulse/*
```

```bash
exec ~/.xsession
```

- *Si `pulseaudio --start` no está funcionando y PulseAudio no se inicia automáticamente al reiniciar, hay algunas cosas que puedes verificar y probar para resolver este problema:*

1. **Verificar si PulseAudio está instalado:** *Asegúrate de que PulseAudio esté instalado correctamente en tu sistema. Puedes hacerlo ejecutando:*

   ```bash
   pacman -Qs pulseaudio
   ```

   *Esto debería mostrarte los paquetes relacionados con PulseAudio que están instalados.*

2. **Verificar el estado del servicio PulseAudio:** *Asegúrate de que el servicio PulseAudio esté habilitado y funcionando. Puedes verificarlo ejecutando:*

   ```bash
   systemctl --user status pulseaudio.service
   ```

   **Esto debería mostrarte el estado del servicio PulseAudio. Si no está activo, puedes habilitarlo y arrancarlo con los siguientes comandos:**

   ```bash
   systemctl --user enable pulseaudio.service
   systemctl --user start pulseaudio.service
   ```

3. **Iniciar PulseAudio manualmente:** *Intenta iniciar PulseAudio manualmente con más verbosidad para ver si hay algún mensaje de error específico. Ejecuta el siguiente comando en la terminal:*

   ```bash
   pulseaudio --start --log-target=stderr -vvv
   ```

   *Esto debería proporcionarte más información sobre por qué PulseAudio no se está iniciando.*

4. **Eliminar ficheros de socket y reiniciar PulseAudio:** *A veces, los ficheros de socket de PulseAudio pueden causar problemas. Puedes eliminarlos y luego intentar reiniciar PulseAudio. Ejecuta:*

   ```bash
   rm -rf ~/.config/pulse
   pulseaudio --start
   ```

5. **Configurar PulseAudio para que se inicie al inicio de sesión:** *Asegúrate de que PulseAudio esté configurado para iniciarse automáticamente al iniciar sesión. Puedes agregar la línea `pulseaudio --start` a tu fichero `~/.xinitrc` o `~/.xsession` si usas `startx` para iniciar tu entorno gráfico. Si usas un gestor de ventanas, asegúrate de que esté configurado para iniciar PulseAudio.*

- *Prueba estos pasos y verifica si alguno de ellos soluciona el problema. Si sigues teniendo dificultades, por favor proporciona cualquier mensaje de error adicional que recibas para poder ofrecerte más ayuda.*

**Si sigue dando problema el audio:**

1. **Revisar los registros del servicio:** *Ejecuta el siguiente comando para ver los detalles de por qué el servicio falla al iniciar:*

   ```bash
   journalctl --user -xeu pulseaudio.service
   ```

   *Esto proporcionará más información sobre el error específico que está causando que PulseAudio no se inicie.*

2. **Forzar el inicio sin daemonizar:** *Intenta iniciar PulseAudio en el modo de depuración sin que se convierta en un demonio para ver los errores detallados:*

   ```bash
   pulseaudio --daemonize=no --log-target=stderr -vvv
   ```

3. **Revisar el fichero de servicio de PulseAudio:** *Verifica el contenido del fichero `/usr/lib/systemd/user/pulseaudio.service` y asegúrate de que esté configurado correctamente. Aquí tienes cómo debería verse típicamente:*

   ```bash
   [Unit]
    Description=Sound Service

    # We require pulseaudio.socket to be active before starting the daemon, because
    # while it is possible to use the service without the socket, it is not clear
    # why it would be desirable.
    #
    # A user installing pulseaudio and doing `systemctl --user start pulseaudio`
    # will not get the socket started, which might be confusing and problematic if
    # the server is to be restarted later on, as the client autospawn feature
    # might kick in. Also, a start of the socket unit will fail, adding to the
    # confusion.
    #
    # After=pulseaudio.socket is not needed, as it is already implicit in the
    # socket-service relationship, see systemd.socket(5).
    Requires=pulseaudio.socket
    ConditionUser=!root

    [Service]
    ExecStart=/usr/bin/pulseaudio --daemonize=no --log-target=journal
    LockPersonality=yes
    MemoryDenyWriteExecute=yes
    NoNewPrivileges=yes
    Restart=on-failure
    RestrictNamespaces=yes
    SystemCallArchitectures=native
    SystemCallFilter=@system-service
    # Note that notify will only work if --daemonize=no
    Type=notify
    UMask=0077
    Slice=session.slice

    [Install]
    Also=pulseaudio.socket
    WantedBy=default.target
   ```

- *Prueba estos pasos y proporciona los detalles del comando `journalctl --user -xeu pulseaudio.service` para obtener más información sobre el error si el problema persiste*
