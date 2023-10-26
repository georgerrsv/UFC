#!/bin/bash

if [ "$#" -ne 4 ]; then
  echo "Uso: $0 <estilo> <cor> <posição> <texto>"
  exit 1
fi

ESTILO="$1"
COR="$2"
POS="$3"
TXT="$4"

case "$ESTILO" in
  "sublinhado")
    ESTILO_VAR=$(tput smul)
    ;;
  "negrito")
    ESTILO_VAR=$(tput bold)
    ;;
  "reverso")
    ESTILO_VAR=$(tput rev)
    ;;
  *)
    echo "Estilo desconhecido. Use sublinhado, negrito ou reverso."
    exit 1
    ;;
esac

COR_VAR=$(tput setaf "$COR")

IFS=',' read -ra POS_VET <<< "$POS"
x="${POS_VET[0]}"
y="${POS_VET[1]}"
POS_VAR=$(tput cup "$x" "$y")

clear
echo -e "${ESTILO_VAR}${COR_VAR}${POS_VAR} $TXT$(tput sgr0)"