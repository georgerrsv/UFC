#!/bin/bash

if [ "$#" -lt 1 ]; then
  echo "Comando: $0 [adicionar <nome> <email> | remover <email> | listar]"
  exit 1
fi

case "$1" in
  "adicionar")
    if [ $# -ne 3 ]; then
      echo "Comando: $0 adicionar <nome> <email>"
      exit 1
    fi

    nome="$2" 
    email="$3"

    if [ ! -e "agenda.db" ]; then
        touch agenda.db
        echo "Arquivo criado!"
    fi

    if grep -q ":$email$" agenda.db; then
        echo "Contato com o email $email já cadastrado!"
    else
        echo "${nome}:${email}" >> agenda.db
        echo "Usuário $nome adicionado."
    fi
    ;;
  "remover")
    if [ $# -ne 2 ]; then
      echo "Comando: $0 remover <email>"
      exit 1
    fi
    email="$2"
    if [ -e "agenda.db" ]; then
        if grep -q ":$email$" agenda.db; then
            sed -i "/:$email$/d" agenda.db
            echo "Contato com o email $email removido"
        else
            echo "Contato com o email $email não encontrado"
        fi
    else
        echo "Arquivo vazio!"
    fi
    ;;
  "listar")
    if [ -e "agenda.db" ]; then
        if [ -s "agenda.db" ]; then
            cat agenda.db
        else
            echo "Arquivo vazio!"
        fi
    else
        echo "Arquivo vazio!"
    fi
    ;;
  *)
    echo "Operação inválida. Use: $0 [adicionar <nome> <email> | remover <email> | listar]"
    exit 1
    ;;
esac