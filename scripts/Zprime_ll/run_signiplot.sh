python python/significance_plot.py -f "Data/Zprime_ee_fcc_v02.json" -n "ee" -p ee
python python/significance_plot.py -f "Data/Zprime_mumu_fcc_v2.json" -n "mumu" -p mumu
python python/significance_plot.py -f "Data/Zprime_ll_fcc_v02.json" -n "ll" -p ll
python python/significance_plot.py -f "Data/Zprime_ee_fcc_v02.json Data/Zprime_mumu_fcc_v02.json Data/Zprime_ll_fcc_v02.json" -n "ee mumu ll" -p ll_comb
python python/significance_plot.py -f "Data/bkup/Zprime_mumu_flav_ano_fcc_v02.json" -n "mumu_flav_ano" -p mumu
