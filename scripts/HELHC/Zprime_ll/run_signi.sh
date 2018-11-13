python python/significance.py -f "config_FCC/Zprime_ll/helhc_v01/Zprime_ee_*TeV.config" -n Zprime_ee_helhc_v01
python python/significance.py -f "config_FCC/Zprime_ll/helhc_v01/Zprime_mumu_*TeV.config" -n Zprime_mumu_helhc_v01
python python/significance.py -f "config_FCC/Zprime_ll/helhc_v01/Zprime_ll_*TeV.config" -n Zprime_ll_helhc_v01 -c
#python python/significance.py -f "config_FCC/Zprime_mumu_ano/helhc_v01/Zprime_mumu_*TeV.config" -n Zprime_mumu_flav_ano_fcc_v02
#
python python/significance.py -f "config_HELHC/Zprime_models/helhc_v01/tagger_SSM_TRFbtag/tt/Zprime_sel0_*TeV.config" -n Zprime_tt_helhc_v01
python python/significance.py -f "config_HELHC/Zprime_models/helhc_v01/tagger_SSM_TRFbtag/bb/Zprime_sel0_*TeV.config" -n Zprime_bb_helhc_v01
python python/significance.py -f "config_HELHC/Zprime_models/helhc_v01/tagger_SSM_TRFbtag/qq/Zprime_sel0_*TeV.config" -n Zprime_qq_helhc_v01

