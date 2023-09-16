#!/bin/bash

param='^[+-]?[0-9]+([.][0-9]+)?$'

if [ "$#" -ne 3 ]; 
    then
        echo "Insira: $0 <parâmetro1> <parâmetro2> <parâmetro3>"
        exit 1
fi

if ! [[ "$1" =~ $param ]]; 
    then
        echo "Erro: $1 não é número."
        exit 1

elif ! [[ "$2" =~ $param ]]; 
    then
        echo "Erro: $2 não é número."
        exit 1

elif ! [[ "$3" =~ $param ]]; 
    then
        echo "Erro: $3 não é número."
        exit 1
fi

if [ "$1" -gt "$2" ] && [ "$1" -gt "$3" ]; 
    then
        echo "O maior número é: $1"

elif [ "$2" -gt "$1" ] && [ "$2" -gt "$3" ]; 
    then
        echo "O maior número é: $2"

else
  echo "O maior número é: $3"
fi