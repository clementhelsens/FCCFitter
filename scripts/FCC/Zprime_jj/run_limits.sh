#!/bin/bash
#to run ./scripts/FCC/Zprime_jj/run_limits.sh fcc_v02 _sel1/_sel1_5p/_sel1_10p/_sel1_15p/_sel1_20p/_sel1_2t/_sel1_3t/_sel1_4t/_sel1_5t

myversion=$1
sel=$2

for ene in 15 20 25 30 35 40 45 50;
do
    ./myFit.exe h config_FCC/Zprime_jj/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe w config_FCC/Zprime_jj/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe f config_FCC/Zprime_jj/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe d config_FCC/Zprime_jj/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe p config_FCC/Zprime_jj/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe l config_FCC/Zprime_jj/"$myversion"/dijet"$sel"_"$ene"TeV.config

done
