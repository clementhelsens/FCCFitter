python python/significance.py -f "config_FCC/Zprime_ll/fcc_v02/Zprime_ee_*TeV.config" -n Zprime_ee_fcc_v02
python python/significance.py -f "config_FCC/Zprime_ll/fcc_v02/Zprime_mumu_*TeV.config" -n Zprime_mumu_fcc_v02
python python/significance.py -f "config_FCC/Zprime_ll/fcc_v02/Zprime_ll_*TeV.config" -n Zprime_ll_fcc_v02 -c
python python/significance.py -f "config_FCC/Zprime_mumu_ano/fcc_v02/Zprime_mumu_*TeV.config" -n Zprime_mumu_flav_ano_fcc_v02
python python/significance.py -f "config_FCC/LQ_mumu/fcc_v02/LQ_mumu_*TeV.config" -n LQ_mumu_fcc_v02


python python/significance.py -f "config_FCC/Zprime_ll/fcc_v02/Zprime_mumu_*TeV_2t.config" -n Zprime_mumu_fcc_v02_2t
python python/significance.py -f "config_FCC/Zprime_ll/fcc_v02/Zprime_mumu_*TeV_3t.config" -n Zprime_mumu_fcc_v02_3t
python python/significance.py -f "config_FCC/Zprime_ll/fcc_v02/Zprime_mumu_*TeV_4t.config" -n Zprime_mumu_fcc_v02_4t
python python/significance.py -f "config_FCC/Zprime_ll/fcc_v02/Zprime_mumu_*TeV_5t.config" -n Zprime_mumu_fcc_v02_5t

python python/significance.py -f "config_FCC/Zprime_ll/fcc_v02/Zprime_mumu_*TeV_hl.config" -n Zprime_mumu_fcc_v02_hl
python python/significance.py -f "config_FCC/Zprime_ll/fcc_v02/Zprime_mumu_*TeV_2hl.config" -n Zprime_mumu_fcc_v02_2hl
