#!/bin/sh

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# systray battery icon
if [ -d /sys/class/power_supply/BAT0 ]; then
  cbatticon -u 5 &
fi

# Keyborad Latam
if [[ "$(setxkbmap -query | tail -n 1 | xargs | awk '{print $2}')" != "latam" ]]; then
  setxkbmap latam
fi

# systray volume
volumeicon &
