#!/bin/bash
#to run ./scripts/Zprime_ll/run_limits.sh fcc_v02 ee/mumu/ll
myversion=$1
lepton=$2
#for ene in 4 6 8 10 15 20 25 30 35 40 45 50;
for ene in 20;
do

    echo $lepton
    if [ $lepton == "ll" ]
    then 
        ./myFit.exe mwfl config_FCC/Zprime_ll/"$myversion"/Zprime_"$lepton"_"$ene"TeV.config

    else
        ./myFit.exe h config_FCC/Zprime_ll/"$myversion"/Zprime_"$lepton"_"$ene"TeV.config
        ./myFit.exe w config_FCC/Zprime_ll/"$myversion"/Zprime_"$lepton"_"$ene"TeV.config
        ./myFit.exe f config_FCC/Zprime_ll/"$myversion"/Zprime_"$lepton"_"$ene"TeV.config
        ./myFit.exe d config_FCC/Zprime_ll/"$myversion"/Zprime_"$lepton"_"$ene"TeV.config
        ./myFit.exe p config_FCC/Zprime_ll/"$myversion"/Zprime_"$lepton"_"$ene"TeV.config
        ./myFit.exe l config_FCC/Zprime_ll/"$myversion"/Zprime_"$lepton"_"$ene"TeV.config
    fi
done

