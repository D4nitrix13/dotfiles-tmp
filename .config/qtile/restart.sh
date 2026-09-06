#!/bin/sh

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# Keyborad Latam
if [[ "$(/bin/setxkbmap -query | /bin/tail -n 1 | /bin/xargs | /bin/awk '{print $2}')" != "latam" ]]; then
  /bin/setxkbmap latam
fi

# Delete Files
# rm -f ~/.zcompdump-asus-*
