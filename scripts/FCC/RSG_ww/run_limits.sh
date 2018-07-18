#!/bin/bash
#to run ./script/RSG_ww/run_limits.sh fcc_v02 sel0
myversion=$1
sel=$2
for ene in 10 15 20 25 30;
do
    ./myFit.exe h config_FCC/RSG_ww/"$myversion"/RSG_"$sel"_"$ene"TeV.config
    ./myFit.exe w config_FCC/RSG_ww/"$myversion"/RSG_"$sel"_"$ene"TeV.config
    ./myFit.exe f config_FCC/RSG_ww/"$myversion"/RSG_"$sel"_"$ene"TeV.config
    ./myFit.exe d config_FCC/RSG_ww/"$myversion"/RSG_"$sel"_"$ene"TeV.config
    ./myFit.exe p config_FCC/RSG_ww/"$myversion"/RSG_"$sel"_"$ene"TeV.config
    ./myFit.exe l config_FCC/RSG_ww/"$myversion"/RSG_"$sel"_"$ene"TeV.config

done

