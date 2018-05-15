#for ene in 10;
for ene in 10 15 20 25 30;
do
    ./myFit.exe h config_FCC/RSG_ww/fcc_v02/RSG_sel0_"$ene"TeV.config
    ./myFit.exe w config_FCC/RSG_ww/fcc_v02/RSG_sel0_"$ene"TeV.config
    ./myFit.exe f config_FCC/RSG_ww/fcc_v02/RSG_sel0_"$ene"TeV.config
    ./myFit.exe d config_FCC/RSG_ww/fcc_v02/RSG_sel0_"$ene"TeV.config
    ./myFit.exe p config_FCC/RSG_ww/fcc_v02/RSG_sel0_"$ene"TeV.config
    ./myFit.exe l config_FCC/RSG_ww/fcc_v02/RSG_sel0_"$ene"TeV.config

done

