#!/bin/sh

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# systray battery icon
for bat in /sys/class/power_supply/BAT*; do
  [ -d "$bat" ] && /bin/cbatticon -i standard -u 15 -l 20 -r 10 -n &
  break
done

# Keyborad Latam
if [[ "$(/bin/setxkbmap -query | /bin/tail -n 1 | /bin/xargs | /bin/awk '{print $2}')" != "latam" ]]; then
  /bin/setxkbmap latam
fi

# Keyboard NumLock
if /bin/xset q | /bin/grep -iq "Num Lock: *off"; then
  /bin/numlockx on
fi

# systray volume
# volumeicon &
