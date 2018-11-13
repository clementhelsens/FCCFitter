python python/limitplot.py -f "Outputs/helhc_v01/Zprime/mumu/Zprime_mumu_*TeV/Limits/*" -n "Zprime_mumu_helhc_v01" -p "\mu\mu" -s "p8_pp_ZprimeSSM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/helhc_v01/Zprime/ee/Zprime_ee_*TeV/Limits/*" -n "Zprime_ee_helhc_v01" -p "ee" -s "p8_pp_ZprimeSSM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/helhc_v01/Zprime/ll/Zprime_ll*TeV/Limits/*" -n "Zprime_ll_helhc_v01" -p "ll (l=e,\mu)" -s "p8_pp_ZprimeSSM_VALUETeV_ll"

python python/limitplot.py -f "Outputs/helhc_v01/Zprime/mumu/Zprime_mumu_*TeV/Limits/*" -n "Zprime_mumu_helhc_v01_allxs" -p "\mu\mu" -s "p8_pp_ZprimeSSM_VALUETeV_ll" -m "p8_pp_ZprimeCHI_VALUETeV_ll p8_pp_ZprimePSI_VALUETeV_ll p8_pp_ZprimeI_VALUETeV_ll p8_pp_ZprimeETA_VALUETeV_ll p8_pp_ZprimeLRM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/helhc_v01/Zprime/ee/Zprime_ee_*TeV/Limits/*" -n "Zprime_ee_helhc_v01_allxs" -p "ee" -s "p8_pp_ZprimeSSM_VALUETeV_ll" -m "p8_pp_ZprimeCHI_VALUETeV_ll p8_pp_ZprimePSI_VALUETeV_ll p8_pp_ZprimeI_VALUETeV_ll p8_pp_ZprimeETA_VALUETeV_ll p8_pp_ZprimeLRM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/helhc_v01/Zprime/ll/Zprime_ll*TeV/Limits/*" -n "Zprime_ll_helhc_v01_allxs" -p "ll (l=e,\mu)" -s "p8_pp_ZprimeSSM_VALUETeV_ll" -m "p8_pp_ZprimeCHI_VALUETeV_ll p8_pp_ZprimePSI_VALUETeV_ll p8_pp_ZprimeI_VALUETeV_ll p8_pp_ZprimeETA_VALUETeV_ll p8_pp_ZprimeLRM_VALUETeV_ll"
#
python python/limitplot.py -f "Outputs/helhc_v01/Zprime_SSM/tt/Zprime_tt*TeV/Limits/*" -n "Zprime_tt_helhc_v01_allxs" -p "tt" -s "p8_pp_ZprimeSSM_VALUETeV_jj" -m "p8_pp_ZprimeCHI_VALUETeV_jj p8_pp_ZprimePSI_VALUETeV_jj p8_pp_ZprimeI_VALUETeV_jj p8_pp_ZprimeETA_VALUETeV_jj p8_pp_ZprimeLRM_VALUETeV_jj"
python python/limitplot.py -f "Outputs/helhc_v01/Zprime_SSM/bb/Zprime_bb*TeV/Limits/*" -n "Zprime_bb_helhc_v01_allxs" -p "bb" -s "p8_pp_ZprimeSSM_VALUETeV_jj" -m "p8_pp_ZprimeCHI_VALUETeV_jj p8_pp_ZprimePSI_VALUETeV_jj p8_pp_ZprimeI_VALUETeV_jj p8_pp_ZprimeETA_VALUETeV_jj p8_pp_ZprimeLRM_VALUETeV_jj"
python python/limitplot.py -f "Outputs/helhc_v01/Zprime_SSM/qq/Zprime_qq*TeV/Limits/*" -n "Zprime_qq_helhc_v01_allxs" -p "qq" -s "p8_pp_ZprimeSSM_VALUETeV_jj" -m "p8_pp_ZprimeCHI_VALUETeV_jj p8_pp_ZprimePSI_VALUETeV_jj p8_pp_ZprimeI_VALUETeV_jj p8_pp_ZprimeETA_VALUETeV_jj p8_pp_ZprimeLRM_VALUETeV_jj"

