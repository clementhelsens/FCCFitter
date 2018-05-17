python python/significance_plot.py -f "Data/Zprime_ee_helhc_v01.json" -n "ee" -p ee --helhc
python python/significance_plot.py -f "Data/Zprime_mumu_helhc_v01.json" -n "mumu" -p mumu --helhc
python python/significance_plot.py -f "Data/Zprime_ll_helhc_v01.json" -n "ll" -p ll --helhc
python python/significance_plot.py -f "Data/Zprime_ee_helhc_v01.json Data/Zprime_mumu_helhc_v01.json Data/Zprime_ll_helhc_v01.json" -n "ee mumu ll" -p ll_comb --helhc
#python python/significance_plot.py -f "Data/bkup/Zprime_mumu_flav_ano_fcc_v02.json" -n "mumu_flav_ano" -p mumu
