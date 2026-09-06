#!/bin/bash

# Script: getfolder.sh
# Descarga solo una carpeta específica de un repo GitHub usando sparse-checkout
# Uso:
#   ./getfolder.sh <URL>
#   ./getfolder.sh --depth <n> <URL>

###############################################
# PARSEO DE ARGUMENTOS
###############################################

DEPTH=1 # valor por defecto
URL=""

# Si el usuario pasa --depth
if [ "$1" = "--depth" ]; then
  # Validar que haya un valor siguiente
  if [ -z "$2" ]; then
    echo "Error: Debes proporcionar un valor para --depth."
    exit 1
  fi

  # Validar que sea número entero >= 0
  if ! [[ "$2" =~ ^[0-9]+$ ]]; then
    echo "Error: --depth debe ser un número entero mayor o igual a 0."
    exit 1
  fi

  DEPTH="$2"
  shift 2
fi

# El último argumento debe ser la URL
URL="$1"

if [ -z "$URL" ]; then
  echo "Uso:"
  echo "  ./getfolder.sh <URL>"
  echo "  ./getfolder.sh --depth <n> <URL>"
  exit 1
fi

###############################################
# PROCESAR LA URL DE GITHUB
###############################################

# Repo sin /tree/
REPO_URL=$(echo "$URL" | sed -E 's|(https://github.com/[^/]+/[^/]+)/tree/.*|\1|')

# Branch
BRANCH=$(echo "$URL" | sed -E 's|.*/tree/([^/]+)/.*|\1|')

# Carpeta
FOLDER=$(echo "$URL" | sed -E 's|.*/tree/[^/]+/(.*)|\1|')

# Destino
DEST=$(basename "$REPO_URL")-"$(basename "$FOLDER")"

###############################################
# EJECUCIÓN
###############################################

echo "-----------------------------------------"
echo "Clonando carpeta específica desde GitHub:"
echo "Repo:   $REPO_URL"
echo "Branch: $BRANCH"
echo "Folder: $FOLDER"
echo "Depth:  $DEPTH"
echo "Destino: $DEST"
echo "-----------------------------------------"
echo

# Clonar con profundidad definida
git clone --depth="$DEPTH" --no-checkout "$REPO_URL".git "$DEST"
cd "$DEST" || exit 1

git sparse-checkout init --cone
git sparse-checkout set "$FOLDER"
git checkout "$BRANCH"

echo
echo "Carpeta descargada en:"
echo "  $DEST/$FOLDER"
echo
