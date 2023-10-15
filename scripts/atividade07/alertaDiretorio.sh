#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <intervalo_segundos> <diretorio>"
    exit 1
fi

intervalo=$1
diretorio=$2

if [ ! -d "$diretorio" ]; then
    mkdir -p "$diretorio"
fi

log_file="dirSensors.log"

arquivos_anteriores=($(ls "$diretorio"))
contador_arquivos=${#arquivos_anteriores[@]}

while true; do
    
    arquivos_atuais=($(ls "$diretorio"))

    adicionados=()
    removidos=()

    for arquivo in "${arquivos_anteriores[@]}"; do
        if [[ ! " ${arquivos_atuais[@]} " =~ " $arquivo " ]]; then
            removidos+=("$arquivo")
        fi
    done

    for arquivo in "${arquivos_atuais[@]}"; do
        if [[ ! " ${arquivos_anteriores[@]} " =~ " $arquivo " ]]; then
            adicionados+=("$arquivo")
        fi
    done

    if [ ${#adicionados[@]} -gt 0 ] || [ ${#removidos[@]} -gt 0 ]; then
        data=$(date +"[%d-%m-%Y %H:%M:%S]")

        if [ ${#removidos[@]} -gt 0 ]; then
            echo "$data Alteração! $contador_arquivos->${#arquivos_atuais[@]}. Removidos: ${removidos[*]}" >> "$log_file"
        fi

        if [ ${#adicionados[@]} -gt 0 ]; then
            echo "$data Alteração! $contador_arquivos->${#arquivos_atuais[@]}. Adicionados: ${adicionados[*]}" >> "$log_file"
        fi
        
        contador_arquivos=${#arquivos_atuais[@]}
    fi

    arquivos_anteriores=("${arquivos_atuais[@]}")

    sleep "$intervalo"
done
