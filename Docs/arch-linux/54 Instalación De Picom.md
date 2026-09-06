# ***Instalación de `picom`***

**Para instalar `picom` en tu sistema Arch Linux, puedes utilizar el gestor de paquetes `pacman`:**

```bash
sudo pacman -Syu picom --noconfirm
```

- **`sudo`:** *Ejecuta el comando con privilegios de superusuario.*
- **`pacman`:** *Gestor de paquetes de Arch Linux.*
- **`-Syu`:** *Subcomando para instalar paquetes.*
- **`picom`:** *Es un compositor de ventanas que añade efectos de transparencia y sombras en las ventanas del gestor de ventanas.*

---

## ***Configuración en `.xsession`***

**En el fichero `.xsession`, añadimos la siguiente línea para ejecutar `picom`:**

```bash
# Composer
picom &
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

# Background image
feh --bg-scale "/home/d4nitrix13/Wallpapers/JPG/09 Wallpaper.jpg"

# Audio
pulseaudio --start
```

- *El símbolo `"&"` al final del comando indica que se debe ejecutar `picom` en segundo plano.*
