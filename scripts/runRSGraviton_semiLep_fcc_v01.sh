for ene in 5 10 15 20 25 30 35 40;
do

    ./myFit.exe h config_FCC/RSGraviton_ww/fcc_v01/semiLep/RSG_semiLep_"$ene"TeV.config
    ./myFit.exe w config_FCC/RSGraviton_ww/fcc_v01/semiLep/RSG_semiLep_"$ene"TeV.config
    ./myFit.exe f config_FCC/RSGraviton_ww/fcc_v01/semiLep/RSG_semiLep_"$ene"TeV.config
    ./myFit.exe d config_FCC/RSGraviton_ww/fcc_v01/semiLep/RSG_semiLep_"$ene"TeV.config
    ./myFit.exe p config_FCC/RSGraviton_ww/fcc_v01/semiLep/RSG_semiLep_"$ene"TeV.config
    ./myFit.exe l config_FCC/RSGraviton_ww/fcc_v01/semiLep/RSG_semiLep_"$ene"TeV.config

done

