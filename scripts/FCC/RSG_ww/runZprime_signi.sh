#python python/significance.py -f "config_FCC/Zprime_ll/fcc_v01/Zprime_ee_*TeV.config" -n Zprime_ee_fcc_v01
#python python/significance.py -f "config_FCC/Zprime_ll/fcc_v01/Zprime_mumu_*TeV.config" -n Zprime_mumu_fcc_v01
#python python/significance.py -f "config_FCC/Zprime_ll/fcc_v01_combined/Zprime_ll_*TeV.config" -n Zprime_ll_fcc_v01 -c

python python/significance.py -f "config_FCC/Zprime_ll/fcc_v02/Zprime_ee_*TeV.config" -n Zprime_ee_fcc_v02
python python/significance.py -f "config_FCC/Zprime_ll/fcc_v02/Zprime_mumu_*TeV.config" -n Zprime_mumu_fcc_v02
python python/significance.py -f "config_FCC/Zprime_ll/fcc_v02/Zprime_ll_*TeV.config" -n Zprime_ll_fcc_v02 -c

python python/significance.py -f "config_FCC/Zprime_tt/fcc_v02/Zprime_sel0_*TeV.config" -n Zprime_tt_fcc_v02

python python/significance.py -f "config_FCC/RSG_ww/fcc_v02/RSG_sel0_*TeV.config" -n RSG_ww_fcc_v02


#python python/significance.py -f "config_FCC/Zprime_ll/cms/Zprime_ee_*TeV.config" -n Zprime_ee_cms
#python python/significance.py -f "config_FCC/Zprime_ll/cms/Zprime_mumu_*TeV.config" -n Zprime_mumu_cms
#python python/significance.py -f "config_FCC/Zprime_ll/cms_combined/Zprime_ll_*TeV.config" -n Zprime_ll_cms -c

