#!/usr/bin/env bash

# Scanning Ports v1.0.0
# Autor: Daniel Benjamin Perez Morales 
# GitHub: https://github.com/DanielBenjaminPerezMoralesDev13 
# GitLab: https://gitlab.com/DanielBenjaminPerezMoralesDev13 
# Correo electrónico: danielperezdev@proton.me

trap ctrl_c INT;

function ctrl_c() {
  echo -e "\n [x] Stop Scanning.... \n";
  exit 1;
}

if [ $1 ]; then
  host=$1;
  echo Scanning host: $host;
  declare -i port;
  for port in $(seq 1 1 65535); do
    timeout 1 bash -c "echo '' > /dev/tcp/$host/$port" 2>/dev/null && echo [*] Open Port $port & disown;
  done; wait;
else
  echo -e "\n [x] Usage: $0 <host> \n";
fi

exit 0;
