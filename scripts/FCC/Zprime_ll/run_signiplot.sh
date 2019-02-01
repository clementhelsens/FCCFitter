python python/significance_plot.py -f "Data/Zprime_ee_fcc_v02.json" -n "ee" -p ee
python python/significance_plot.py -f "Data/Zprime_mumu_fcc_v02.json" -n "mumu" -p mumu
python python/significance_plot.py -f "Data/Zprime_ll_fcc_v02.json" -n "ll" -p ll
python python/significance_plot.py -f "Data/Zprime_ee_fcc_v02.json Data/Zprime_mumu_fcc_v02.json Data/Zprime_ll_fcc_v02.json" -n "ee mumu ll" -p ll_comb
python python/significance_plot.py -f "Data/May2018_highstatprod/FCChh/Zprime_mumu_flav_ano_fcc_v02.json" -n "mumu_flav_ano" -p mumu
python python/significance_plot.py -f "Data/May2018_highstatprod/FCChh/LQ_mumu_fcc_v02.json" -n "mumu_LQ" -p LQ_mumu


python python/significance_plot.py -f "Data/Zprime_mumu_fcc_v02.json Data/Zprime_mumu_fcc_v02_hl.json Data/Zprime_mumu_fcc_v02_2hl.json" -n "FCC CMS CMSx2" -p ll_smearhl --mmax 45 --mmin 25
