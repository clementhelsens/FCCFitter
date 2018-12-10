python python/significance_plot.py -f "Data/Zprime_ee_helhc_v01.json" -n "ee" -p ee --helhc
python python/significance_plot.py -f "Data/Zprime_mumu_helhc_v01.json" -n "mumu" -p mumu --helhc
python python/significance_plot.py -f "Data/Zprime_ll_helhc_v01.json" -n "ll" -p ll --helhc
python python/significance_plot.py -f "Data/Zprime_ee_helhc_v01.json Data/Zprime_mumu_helhc_v01.json Data/Zprime_ll_helhc_v01.json" -n "ee mumu ll" -p ll_comb --helhc
python python/significance_plot.py -f "Data/Zprime_mumu_flav_ano_helhc_v01.json" -n "mumu_flav_ano" -p mumu --helhc
#
python python/significance_plot.py -f "Data/Zprime_tt_helhc_v01.json" -n "tt" -p tt --helhc
python python/significance_plot.py -f "Data/Zprime_bb_helhc_v01.json" -n "bb" -p bb --helhc
python python/significance_plot.py -f "Data/Zprime_qq_helhc_v01.json" -n "qq" -p qq --helhc

