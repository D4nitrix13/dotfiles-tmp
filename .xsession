#!/bin/sh

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielBenjaminPerezMoralesDev13
# Gitlab: https://gitlab.com/DanielBenjaminPerezMoralesDev13
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

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/?*.sh; do
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
# setxkbmap latam &

# Screens
xrandr --output DVI-D-1 --off --output HDMI-1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --off --output HDMI-2 --off

# Automount Devices
udiskie -t &

# Background image
feh --bg-scale "$(bash /home/d4nitrix13/Scripts/script.sh)"

# Audio
pulseaudio --start
