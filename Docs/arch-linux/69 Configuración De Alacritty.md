<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Configuración de Alacritty***

**En el fichero `alacritty.toml`, las configuraciones son:**

- *[Documentacion](https://alacritty.org/config-alacritty.html "https://alacritty.org/config-alacritty.html")*

```toml
# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

[window]
opacity = 0.9
padding = { x = 5, y = 5 }

[font]
normal = { family = "Cascadia Code NF", style = "Bold Italic" }
size = 22.0
offset = { x = 1, y = 2 }
glyph_offset = { x = 1, y = -1 }
builtin_box_drawing = true
```

1. **`opacity = 0.9`:**
   - **Descripción:** *Define la opacidad de la ventana de Alacritty.*
   - **Valor:** *Un valor entre 0.0 (completamente transparente) y 1.0 (totalmente opaco). En este caso, 0.9 indica que la ventana será ligeramente transparente.*

2. **`padding = { x = 5, y = 5 }`:**
   - **Descripción:** *Establece el espaciado interno de la ventana de Alacritty.*
   - **Valor:** *Un objeto que define el espaciado en píxeles tanto horizontal (`x`) como vertical (`y`). En este ejemplo, se agrega un margen interno de 5 píxeles en cada dirección.*

3. **Configuración de la fuente (`[font]`):**
   - **`normal = { family = "Cascadia Code NF", style = "Bold Italic" }`:**
     - **Descripción:** *Define la fuente y el estilo para el texto normal en Alacritty.*
     - **Valor:**
       - **`family`:** *Especifica la familia de la fuente, en este caso "Cascadia Code NF".*
       - **`style`:** *Define el estilo de la fuente, aquí se usa "Bold Italic" (negrita e itálica).*

   - **`size = 22.0`:**
     - **Descripción:** *Establece el tamaño de la fuente en puntos.*
     - **Valor:** *Un número que representa el tamaño de la fuente. En este caso, la fuente se establece en 22 puntos.*

   - **`offset = { x = 1, y = 2 }`:**
     - **Descripción:** *Define el ajuste del texto en píxeles.*
     - **Valor:** *Un objeto que especifica el desplazamiento horizontal (`x`) y vertical (`y`) del texto.*

   - **`glyph_offset = { x = 1, y = -1 }`:**
     - **Descripción:** *Ajusta la posición de los glifos en la fuente.*
     - **Valor:** *Similar a `offset`, pero específicamente ajusta la posición de los glifos (caracteres) en la pantalla.*

   - **`builtin_box_drawing = true`:**
     - **Descripción:** *Habilita los caracteres de dibujo de cajas incorporados en la fuente.*
     - **Valor:** *`true` para habilitar esta característica, lo que permite que Alacritty dibuje cuadros y bordes utilizando caracteres especiales de la fuente.*

*Estas configuraciones permiten personalizar la apariencia y el comportamiento visual de Alacritty según tus preferencias, incluyendo la transparencia de la ventana, el espaciado interno, el tipo de fuente, el tamaño, el estilo, y ajustes específicos para el texto y los caracteres de dibujo de cajas.*

---

## ***Instalación de `udisks2` y `udiskie`***

1. **Instalación de paquetes necesarios:**

   **Instala `udisks2` y `udiskie` desde los repositorios de Arch Linux:**

   ```bash
   sudo pacman -Syu udisks2 udiskie --noconfirm
   ```

2. **Verificación y configuración de `udisks2`:**

   **Asegúrate de que el servicio `udisks2` esté activo y configurado para ejecutarse automáticamente:**

   ```bash
   systemctl status udisks2
   sudo systemctl enable --now udisks2
   ```

3. **Configuración de `udiskie`:**

   - **Crear el fichero de configuración para `udiskie`:**
     **Crea el fichero `config.yml` dentro del directorio `~/.config/udiskie/` si no existe:**

     ```bash
     mkdir -p ~/.config/udiskie
     touch ~/.config/udiskie/config.yml
     ```

   - **Configuración del fichero `config.yml`:**
   - *[Documentacion](https://github.com/coldfix/udiskie/blob/master/example/config.yml "https://github.com/coldfix/udiskie/blob/master/example/config.yml")*

     ```yaml
     # Autor: Daniel Benjamin Perez Morales
     # GitHub: https://github.com/D4nitrix13
     # Gitlab: https://gitlab.com/D4nitrix13
     # Correo electrónico: danielperezdev@proton.me 

     program_options:
       tray: auto  # Controla la visibilidad automática del icono en la bandeja del sistema.
       menu: flat  # Define el estilo del menú en la bandeja del sistema.
       automount: false  # Deshabilita el montaje automático de dispositivos.
       notify: true  # Habilita las notificaciones.
       password_cache: false  # Deshabilita el almacenamiento en caché de contraseñas.

     icon_names:
       media: [drive-removable-media, media-optical]  # Iconos para medios removibles y ópticos.
       browse: [document-open, folder-open]  # Iconos para abrir documentos o carpetas.
       terminal: [terminal, terminator, xfce-terminal]  # Iconos para abrir terminal.
       mount: [udiskie-mount]  # Iconos para montar dispositivos.
       unmount: [udiskie-unmount]  # Iconos para desmontar dispositivos.
       unlock: [udiskie-unlock]  # Iconos para desbloquear dispositivos encriptados.
       lock: [udiskie-lock]  # Iconos para bloquear dispositivos encriptados.
       eject: [udiskie-eject, media-eject]  # Iconos para expulsar dispositivos.
       detach: [udiskie-detach]  # Iconos para desconectar dispositivos.
       delete: [udiskie-eject]  # Iconos para eliminar dispositivos.
       quit: [application-exit]  # Icono para salir de udiskie.

     notifications:
       timeout: 1.5  # Tiempo predeterminado para todas las notificaciones.
       device_mounted: 5  # Duración de la notificación de montaje.
       device_unmounted: false  # Deshabilitar la notificación de desmontaje.
       device_added: false  # Deshabilitar la notificación de aparición de dispositivo.
       device_removed: false  # Deshabilitar la notificación de desaparición de dispositivo.
       device_unlocked: -1  # Notificación de desbloqueo de dispositivo encriptado.
       device_locked: -1  # Notificación de bloqueo de dispositivo encriptado.
       job_failed: -1  # Notificación de falla en tarea (montaje, desbloqueo, etc.).
     ```

> [!IMPORTANT]
> **Reiniciar el sitema operativo si no funciona**

---

### ***Configuración Adicional***

1. **Configuración del punto de montaje:**

   - *El lugar de montaje para dispositivos USB normalmente se encuentra en `/run/media/user/Usb`. Asegúrate de que este directorio esté configurado correctamente para los montajes automáticos.*

2. **Añadir línea en `.xsession`:**

   **Para montar dispositivos automáticamente al inicio, añade la siguiente línea al fichero `.xsession`:**

   ```bash
   # Automount Devices
   udiskie -t &
   ```

   ```bash
   #!/bin/sh
   
   # Autor: Daniel Benjamin Perez Morales
   # GitHub: https://github.com/D4nitrix13
   # Gitlab: https://gitlab.com/D4nitrix13
   # Correo electrónico: danielperezdev@proton.me 
   
   userresources=$HOME/.Xresources
   usermodmap=$HOME/.Xmodmap
   sysresources=/etc/X11/xinit/.Xresources
   sysmodmap=/etc/X11/xinit/.Xmodmap
   
   # merge in defaults and keymaps
   
   if [ -f $sysresources ]; then
       xrdb -merge $sysresources
   fi
   
   if [ -f $sysmodmap ]; then
       xmodmap $sysmodmap
   fi
   
   if [ -f "$userresources" ]; then
       xrdb -merge "$userresources"
   fi
   
   if [ -f "$usermodmap" ]; then
       xmodmap "$usermodmap"
   fi
   
   # start some nice programs
   
   if [ -d /etc/X11/xinit/xinitrc.d ] ; then
    for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
     [ -x "$f" ] && . "$f"
    done
    unset f
   fi
   
   # Composer
   picom &
   
   # Keyboard Layout
   setxkbmap latam &
   
   # Automount Devices
   udiskie -t &
   
   # Background image
   feh --bg-scale /home/d4nitrix13/Wallpapers/Img/09.jpg
   
   # Audio
   pulseaudio --start
   ```

3. **Verificar permisos:**

   **Asegúrate de que tu usuario tenga permisos para montar dispositivos. Si es necesario, añade tu usuario al grupo `wheel`:**

   ```bash
   sudo usermod -aG wheel $USER
   ```

4. **Verificar el montaje de dispositivos:**

   **Inserta un dispositivo USB y verifica que `udiskie` esté intentando montarlo correctamente:**

   ```bash
   udiskie -tv
   ```

*Con estos pasos detallados, deberías tener configurados tanto Alacritty como `udiskie` correctamente en tu entorno Arch Linux.*
