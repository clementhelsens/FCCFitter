#!/bin/bash
#to run ./scripts/Zprime_ll/run_limits.sh helhc_v01 ee/mumu/ll
myversion=$1
lepton=$2
for ene in 2 4 6 8 10 12 14;
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

