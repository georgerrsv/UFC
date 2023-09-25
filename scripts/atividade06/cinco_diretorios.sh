#!/bin/bash

mkdir -p cinco

for ((i=1; i<=5; i++)); 
    do
        mkdir -p cinco/dir$i

        for ((j=1; j<=4; j++)); 
            do
                conteudo=""

        for ((k=1; k<=j; k++)); 
            do
                conteudo="$conteudo$j"

                if [ "$k" -lt "$j" ]; 
                    then
                    
                        conteudo="$conteudo"$'\n'
                fi
            done

            echo -e "$conteudo" > cinco/dir$i/arq$j.txt
        done
    done
