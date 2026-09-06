#!/usr/bin/env bash

# Ruta donde están los fondos de pantalla
BACKGROUND_DIR="/usr/share/backgrounds"

# Obtén la lista de archivos de fondo en el directorio
BACKGROUNDS=($BACKGROUND_DIR/*.{jpeg,jpg,png,webp})

# Verifica si hay fondos disponibles
if [ ${#BACKGROUNDS[@]} -eq 0 ]; then
  # echo "No se encontraron fondos de pantalla en el directorio $BACKGROUND_DIR"
  exit 1
fi

# Selecciona un fondo aleatorio
SELECTED_BACKGROUND=${BACKGROUNDS[$RANDOM % ${#BACKGROUNDS[@]}]}

# Establece el fondo en el archivo de configuración de slick-greeter
sed -i "s|^background=.*|background=$SELECTED_BACKGROUND|" slick-greeter.conf

# Name Service: set-greeter-background.service.service
# Name Script: set-random-greeter-background.sh
# sudo chmod +x /root/set-random-greeter-background.sh
# Command 1: sudo mv set-greeter-background.service /etc/systemd/system/
# Command 2: sudo systemctl daemon-reexec
# Command 3: sudo systemctl daemon-reload
# Enable Service: sudo systemctl enable set-greeter-background.service

