#!/bin/bash

read -p "Informe o arquivo: " ARQUIVO


if [ ! -e "$ARQUIVO" ]; then
  echo "O arquivo '$ARQUIVO' não existe."
  exit 1
fi


cat "$ARQUIVO" | sed 's/[.,]//g' | tr -s '[:space:]' '\n' | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -k 1nr,1 -k 2,2 | while read CONTADOR PALAVRA; do
  echo "$PALAVRA: $CONTADOR"
done