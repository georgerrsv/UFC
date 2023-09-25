#!/bin/bash

mkdir -p cinco

for ((i=1; i<=5; i++)); do
    mkdir -p cinco/dir$i

    for ((j=1; j<=4; j++)); do

        CONTEUDO=""

        for ((k=1; k<=j; k++)); do

            CONTEUDO="$CONTEUDO$j"
            
            if [ "$k" -lt "$j" ]; 
                then
                    CONTEUDO="$CONTEUDO"$'\n'
            fi
            
        done

        echo -n -e "$CONTEUDO" > cinco/dir$i/arq$j.txt
    done
done
