#!/bin/bash
#to run ./script/Zprime_tt/run_limits.sh fcc_v02 sel0
myversion=$1
sel=$2
for ene in 10 15 20 25 30;
do

    ./myFit.exe h config_FCC/Zprime_tt/"$myversion"/Zprime_"$sel"_"$ene"TeV.config
    ./myFit.exe w config_FCC/Zprime_tt/"$myversion"/Zprime_"$sel"_"$ene"TeV.config
    ./myFit.exe f config_FCC/Zprime_tt/"$myversion"/Zprime_"$sel"_"$ene"TeV.config
    ./myFit.exe d config_FCC/Zprime_tt/"$myversion"/Zprime_"$sel"_"$ene"TeV.config
    ./myFit.exe p config_FCC/Zprime_tt/"$myversion"/Zprime_"$sel"_"$ene"TeV.config
    ./myFit.exe l config_FCC/Zprime_tt/"$myversion"/Zprime_"$sel"_"$ene"TeV.config

done

