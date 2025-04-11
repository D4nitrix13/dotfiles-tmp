#!/bin/sh

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# Keyborad Latam
if [[ "$(setxkbmap -query | tail -n 1 | xargs | awk '{print $2}')" != "latam" ]]; then
  setxkbmap latam
fi