#!/bin/bash
#to run ./script/Dijet/run_limits.sh fcc_v02
myversion=$1

for ene in 15 20 25 30 35 40 45 50;
do
    ./myFit.exe h config_FCC/Dijet_Res/"$myversion"/dijet_"$ene"TeV.config
    ./myFit.exe w config_FCC/Dijet_Res/"$myversion"/dijet_"$ene"TeV.config
    ./myFit.exe f config_FCC/Dijet_Res/"$myversion"/dijet_"$ene"TeV.config
    ./myFit.exe d config_FCC/Dijet_Res/"$myversion"/dijet_"$ene"TeV.config
    ./myFit.exe p config_FCC/Dijet_Res/"$myversion"/dijet_"$ene"TeV.config
    ./myFit.exe l config_FCC/Dijet_Res/"$myversion"/dijet_"$ene"TeV.config

done

