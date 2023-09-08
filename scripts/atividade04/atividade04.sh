#!/bin/bash

touch compras.txt saudacao.log
touch saudacao.sh soma.sh

chmod 0700 soma.sh saudacao.sh

echo -e "Playstation5 4999\nMacBook 9799\nGalaxyS20Ultra 5499\niPad 3499\nSmartTV554k 2799" > compras.txt

echo 'cat compras.txt | cut -d " " -f2 | tr '\n' '+' | sed 's/+$/\n/' | bc' > soma.sh

echo '#!/bin/bash
export TZ=America/Sao_Paulo
echo -e "Olá $(whoami), \nHoje é dia $(date +"%d"), do mês $(date +"%m") do ano de $(date +"%Y")." >> saudacao.log' > saudacao.sh