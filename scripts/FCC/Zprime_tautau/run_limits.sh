#!/bin/bash
#to run ./scripts/FCC/Zprime_tautau/run_limits.sh fcc_v02 _sel0mzp
#to run ./scripts/FCC/Zprime_tautau/run_limits.sh fcc_v02 _sel0mr
#to run ./scripts/FCC/Zprime_tautau/run_limits.sh fcc_v02 _sel1mzp
#to run ./scripts/FCC/Zprime_tautau/run_limits.sh fcc_v02 _mt
myversion=$1
sel=$2
for ene in 4 6 8 10 12 14 16 18 20 25 30;
do

    ./myFit.exe h config_FCC/Zprime_tautau/"$myversion"/Zprime_"$ene"TeV"$sel".config
    ./myFit.exe w config_FCC/Zprime_tautau/"$myversion"/Zprime_"$ene"TeV"$sel".config
    ./myFit.exe f config_FCC/Zprime_tautau/"$myversion"/Zprime_"$ene"TeV"$sel".config
    ./myFit.exe d config_FCC/Zprime_tautau/"$myversion"/Zprime_"$ene"TeV"$sel".config
    ./myFit.exe p config_FCC/Zprime_tautau/"$myversion"/Zprime_"$ene"TeV"$sel".config
    ./myFit.exe l config_FCC/Zprime_tautau/"$myversion"/Zprime_"$ene"TeV"$sel".config

done