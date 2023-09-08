#!/bin/bash 
#Um comando grep que encontre todas as linhas com mensagens que não são do sshd
grep -v 'sshd' auth.log

#Um comando grep que encontre todas as linhas com mensagens que indicam um
#login de sucesso via sshd cujo nome do usuário começa com a letra j
grep -E 'New.*j' auth.log

#Um comando grep que encontre todas as vezes que alguém tentou
#fazer login via root através do sshd
grep -E 'sshd.*D.*f.*root' auth.log

#Um comando grep que encontre todas as vezes que alguém conseguiu fazer
#login com sucesso nos dias 11 ou 12 de Outubro
grep -E -e '^Oct.11.*New' -e '^Oct.12.*New' auth.log
