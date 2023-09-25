#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Uso: $0 <arquivo de texto>"
  exit 1
fi

INPUT="$1"
TEMP=$(mktemp)

if [ ! -f "$INPUT" ]; 
    then
        echo "O arquivo '$INPUT' não existe."
        exit 1
fi

while read -r ip; do
  TEMPO_MEDIO=0
  count=0
  while IFS= read -r line; 
    do
        if [[ $line == *time=* ]]; 
            then
                time=$(echo "$line" | grep -oP 'time=\K\d+\.\d+')
                TEMPO_MEDIO=$(echo "$TEMPO_MEDIO + $time" | bc)
                count=$((count + 1))
        fi
    done < <(ping -c 5 "$ip" | grep -oP 'time=\d+\.\d+ ms')

  if [ "$count" -gt 0 ]; 
    then
        TEMPO_MEDIO=$(echo "scale=2; $TEMPO_MEDIO / $count" | bc)
        echo "$ip $TEMPO_MEDIO""ms"
  fi
done < "$INPUT" | sort -n -k 2 > "$TEMP"

echo "Lista de IPs ordenada:"
cat "$TEMP"

rm "$TEMP"
