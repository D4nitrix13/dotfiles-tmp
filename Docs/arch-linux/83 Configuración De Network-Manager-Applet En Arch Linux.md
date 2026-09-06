<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Configuración de `network-manager-applet` en Arch Linux***

---

## ***Paso 1: Instalación de `network-manager-applet`***

1. **Actualizar el sistema e instalar `network-manager-applet`:**

    ```bash
    sudo pacman -Syu --noconfirm network-manager-applet
    ```

    - *Esto actualizará tu sistema e instalará `network-manager-applet`, una herramienta que proporciona una interfaz gráfica para gestionar conexiones de red.*

---

### ***Paso 2: Ejecutar `nm-applet`***

1. **Ejecutar `nm-applet` en segundo plano:**

    ```bash
    nm-applet &
    ```

    - *El comando `nm-applet &` ejecuta el applet de Network Manager en segundo plano, permitiéndote gestionar tus conexiones de red desde la bandeja del sistema.*

2. **Solución al error de notificaciones:**

    **Si ves un error como el siguiente:**

    ```bash
    (nm-applet:10214): GLib-GIO-WARNING **: unable to send notifications through org.freedesktop.Notifications: GDBus.Error:org.freedesktop.DBus.Error.ServiceUnknown: The name is not activatable
    ```

    - *Esto significa que `nm-applet` no puede enviar notificaciones a través de D-Bus porque el servicio de notificaciones no está activado. Para solucionar esto, asegúrate de tener instalado y configurado un servicio de notificaciones, como `dunst` **(Opcional)**:*

    ```bash
    sudo pacman -Syu --noconfirm dunst
    ```

    **Luego, inicia `dunst`:**

    ```bash
    dunst &
    ```

---

### ***Paso 3: Hacer que los cambios sean permanentes***

- *Para asegurarte de que `nm-applet` se ejecute automáticamente cada vez que inicias sesión, debes agregarlo a tu fichero de inicio de sesión, como `.xsession` o `.xinitrc`.*

1. **Agregar `nm-applet` al fichero `.xsession` o `.xinitrc`:**

    ```bash
    nano ~/.xsession
    ```

    O si usas `.xinitrc`:

    ```bash
    nano ~/.xinitrc
    ```

2. **Agregar la siguiente línea al fichero:**

    ```bash
    # Network
    nm-applet &
    ```

    - *Guarda y cierra el fichero. Esto asegura que `nm-applet` se ejecute automáticamente cuando inicias sesión en tu entorno gráfico.*

---

### ***Paso 4: Reiniciar el entorno gráfico***

**Para aplicar los cambios, reinicia tu entorno gráfico o simplemente cierra la sesión y vuelve a iniciarla.**

```bash
mod4 + ctrl + q  # Para reiniciar la sesión en Qtile
```

---

### ***Resumen***

1. *Instalaste `network-manager-applet` para gestionar tus conexiones de red.*
2. *Ejecutaste `nm-applet` y solucionaste el problema de notificaciones instalando y ejecutando `dunst`.*
3. *Hiciste que `nm-applet` se ejecute automáticamente al inicio de sesión agregándolo a tu fichero `.xsession` o `.xinitrc`.*

- *Esto debería proporcionarte una forma gráfica y conveniente de gestionar tus conexiones de red en Arch Linux. ¿Hay algo más en lo que pueda asistirte?*

**El Fichero .xsession quedaria:**

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

# Network
nm-applet &

# Notify
dunst &

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

---

### ***Información solicitada para los paquetes `network-manager-applet` y `dunst`:***

---

### ***Paquete `network-manager-applet`***

- **Página de Instalación de Arch Linux:** *[Arch Linux - network-manager-applet](https://archlinux.org/packages/extra/x86_64/network-manager-applet/ "https://archlinux.org/packages/extra/x86_64/network-manager-applet/")*
- **Repositorio de GitHub:** *[network-manager-applet](https://github.com/pavlix/nm-applet "https://github.com/pavlix/nm-applet")*
- **Página Oficial del Paquete:** *No disponible*

```bash
sudo pacman -Syu --noconfirm network-manager-applet
```

---

### ***Paquete `dunst`***

- **Página de Instalación de Arch Linux:** *[Arch Linux - dunst](https://archlinux.org/packages/extra/x86_64/dunst/ "https://archlinux.org/packages/extra/x86_64/dunst/")*
- **Repositorio de GitHub:** *[dunst](https://github.com/dunst-project/dunst "https://github.com/dunst-project/dunst")*
- **Página Oficial del Paquete:** *No disponible*

```bash
sudo pacman -Syu --noconfirm dunst
```
