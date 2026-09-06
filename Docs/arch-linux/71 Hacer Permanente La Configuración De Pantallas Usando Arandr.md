<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Para hacer permanente la configuración de pantallas usando arandr, sigue estos pasos:**

1. **Guardar la configuración en arandr:**
   - *Después de ajustar la disposición de tus pantallas en arandr, haz clic en el botón "Guardar".*
   - *Se te pedirá que ingreses un nombre para el fichero de configuración. Por ejemplo, puedes nombrarlo como `monitor.sh`.*

2. **Verificar el contenido del fichero guardado:**
   - *Si revisamos el contenido del fichero `monitor.sh` en el directorio `~/.screenlayout/`, verás algo similar a esto:*

   ```bash
   #!/bin/sh
   
   # Autor: Daniel Benjamin Perez Morales
   # GitHub: https://github.com/D4nitrix13
   # Gitlab: https://gitlab.com/D4nitrix13
   # Correo electrónico: danielperezdev@proton.me 

   xrandr --output DVI-D-1 --off --output HDMI-1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --off --output HDMI-2 --off
   ```

   *Este script ejecuta los comandos `xrandr` necesarios para configurar tus pantallas según lo establecido en arandr.*

3. **Hacer la configuración permanente:**
   - *Para hacer esta configuración permanente, puedes añadir el script al fichero `~/.xsession`. Este fichero se ejecuta cada vez que inicias tu sesión X.*

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
    
    # Screens
    xrandr --output DVI-D-1 --off --output HDMI-1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --off --output HDMI-2 --off
    
    # Automount Devices
    udiskie -t &
    
    # Background image
    feh --bg-scale "/home/d4nitrix13/Wallpapers/JPEG/09 Wallpaper.jpeg"
    
    # Audio
    pulseaudio --start
    ```

   - *En el script anterior, asegúrate de reemplazar `~/.screenlayout/monitor.sh` con la ruta correcta hacia tu script de configuración guardado por arandr.*

*Este enfoque asegurará que la configuración de tus pantallas se aplique automáticamente cada vez que inicias tu sesión X en Arch Linux, proporcionando una experiencia consistente con tu configuración preferida de múltiples monitores en Qtile.*
