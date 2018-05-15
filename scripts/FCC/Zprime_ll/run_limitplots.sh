python python/limitplot.py -f "Outputs/fcc_v02/Zprime/mumu/Zprime_mumu_*TeV/Limits/*" -n "Zprime_mumu_fcc_v02" -p "\mu\mu" -s "p8_pp_ZprimeSSM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/ee/Zprime_ee_*TeV/Limits/*" -n "Zprime_ee_fcc_v02" -p "ee" -s "p8_pp_ZprimeSSM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/ll/Zprime_ll*TeV/Limits/*" -n "Zprime_ll_fcc_v02" -p "ll (l=e,\mu)" -s "p8_pp_ZprimeSSM_VALUETeV_ll"

python python/limitplot.py -f "Outputs/fcc_v02/Zprime/mumu/Zprime_mumu_*TeV/Limits/*" -n "Zprime_mumu_fcc_v02_allxs" -p "\mu\mu" -s "p8_pp_ZprimeSSM_VALUETeV_ll" -m "p8_pp_ZprimeCHI_VALUETeV_ll p8_pp_ZprimePSI_VALUETeV_ll p8_pp_ZprimeI_VALUETeV_ll p8_pp_ZprimeETA_VALUETeV_ll p8_pp_ZprimeLRM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/ee/Zprime_ee_*TeV/Limits/*" -n "Zprime_ee_fcc_v02_allxs" -p "ee" -s "p8_pp_ZprimeSSM_VALUETeV_ll" -m "p8_pp_ZprimeCHI_VALUETeV_ll p8_pp_ZprimePSI_VALUETeV_ll p8_pp_ZprimeI_VALUETeV_ll p8_pp_ZprimeETA_VALUETeV_ll p8_pp_ZprimeLRM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/ll/Zprime_ll*TeV/Limits/*" -n "Zprime_ll_fcc_v02_allxs" -p "ll (l=e,\mu)" -s "p8_pp_ZprimeSSM_VALUETeV_ll" -m "p8_pp_ZprimeCHI_VALUETeV_ll p8_pp_ZprimePSI_VALUETeV_ll p8_pp_ZprimeI_VALUETeV_ll p8_pp_ZprimeETA_VALUETeV_ll p8_pp_ZprimeLRM_VALUETeV_ll"
