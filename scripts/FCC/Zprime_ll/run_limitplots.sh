python python/limitplot.py -f "Outputs/fcc_v02/Zprime/mumu/Zprime_mumu_*TeV/Limits/*" -n "Zprime_mumu_fcc_v02" -p "Z\' \rightarrow \mu\mu" -s "p8_pp_ZprimeSSM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/ee/Zprime_ee_*TeV/Limits/*" -n "Zprime_ee_fcc_v02" -p "Z\' \rightarrow ee" -s "p8_pp_ZprimeSSM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/ll/Zprime_ll*TeV/Limits/*" -n "Zprime_ll_fcc_v02" -p "Z\' \rightarrow ll\ (l=e,\mu)" -s "p8_pp_ZprimeSSM_VALUETeV_ll"

python python/limitplot.py -f "Outputs/fcc_v02/Zprime/mumu/Zprime_mumu_*TeV/Limits/*" -n "Zprime_mumu_fcc_v02_allxs" -p "Z\' \rightarrow \mu\mu" -s "p8_pp_ZprimeSSM_VALUETeV_ll" -m "p8_pp_ZprimeCHI_VALUETeV_ll p8_pp_ZprimePSI_VALUETeV_ll p8_pp_ZprimeI_VALUETeV_ll p8_pp_ZprimeETA_VALUETeV_ll p8_pp_ZprimeLRM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/ee/Zprime_ee_*TeV/Limits/*" -n "Zprime_ee_fcc_v02_allxs" -p "Z\' \rightarrow ee" -s "p8_pp_ZprimeSSM_VALUETeV_ll" -m "p8_pp_ZprimeCHI_VALUETeV_ll p8_pp_ZprimePSI_VALUETeV_ll p8_pp_ZprimeI_VALUETeV_ll p8_pp_ZprimeETA_VALUETeV_ll p8_pp_ZprimeLRM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/ll/Zprime_ll*TeV/Limits/*" -n "Zprime_ll_fcc_v02_allxs" -p "Z\' \rightarrow ll\ (l=e,\mu)" -s "p8_pp_ZprimeSSM_VALUETeV_ll" -m "p8_pp_ZprimeCHI_VALUETeV_ll p8_pp_ZprimePSI_VALUETeV_ll p8_pp_ZprimeI_VALUETeV_ll p8_pp_ZprimeETA_VALUETeV_ll p8_pp_ZprimeLRM_VALUETeV_ll"


python python/limitplot.py -f "Outputs/fcc_v02/Zprime/mumu_smeared_2t/Zprime_mumu_smeared_*TeV/Limits/*" -n "Zprime_mumu_fcc_v02_smeared_2t" -p "\mu\mu" -s "p8_pp_ZprimeSSM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/mumu_smeared_3t/Zprime_mumu_smeared_*TeV/Limits/*" -n "Zprime_mumu_fcc_v02_smeared_3t" -p "\mu\mu" -s "p8_pp_ZprimeSSM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/mumu_smeared_4t/Zprime_mumu_smeared_*TeV/Limits/*" -n "Zprime_mumu_fcc_v02_smeared_4t" -p "\mu\mu" -s "p8_pp_ZprimeSSM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/mumu_smeared_5t/Zprime_mumu_smeared_*TeV/Limits/*" -n "Zprime_mumu_fcc_v02_smeared_5t" -p "\mu\mu" -s "p8_pp_ZprimeSSM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/mumu_smeared_hl/Zprime_mumu_smeared_*TeV/Limits/*" -n "Zprime_mumu_fcc_v02_smeared_hl" -p "\mu\mu" -s "p8_pp_ZprimeSSM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/mumu_smeared_2hl/Zprime_mumu_smeared_*TeV/Limits/*" -n "Zprime_mumu_fcc_v02_smeared_2hl" -p "\mu\mu" -s "p8_pp_ZprimeSSM_VALUETeV_ll"


python python/limitplot.py -f "Outputs/fcc_v02/Zprime/mumu/Zprime_mumu_*TeV/Limits/*" -n "Zprime_mumu_fcc_v02_smeared" -p "\mu\mu" -s "p8_pp_ZprimeSSM_VALUETeV_ll" --smeart2 "Outputs/fcc_v02/Zprime/mumu_smeared_2t/Zprime_mumu_smeared_*TeV/Limits/*" --smeart3 "Outputs/fcc_v02/Zprime/mumu_smeared_3t/Zprime_mumu_smeared_*TeV/Limits/*" --smeart4 "Outputs/fcc_v02/Zprime/mumu_smeared_4t/Zprime_mumu_smeared_*TeV/Limits/*" --smeart5 "Outputs/fcc_v02/Zprime/mumu_smeared_5t/Zprime_mumu_smeared_*TeV/Limits/*" 

python python/limitplot.py -f "Outputs/fcc_v02/Zprime/mumu/Zprime_mumu_*TeV/Limits/*" -n "Zprime_mumu_fcc_v02_smeared_hl_comp" -p "\mu\mu" -s "p8_pp_ZprimeSSM_VALUETeV_ll" --smeart2 "Outputs/fcc_v02/Zprime/mumu_smeared_hl/Zprime_mumu_smeared_*TeV/Limits/*" --smeart3 "Outputs/fcc_v02/Zprime/mumu_smeared_2hl/Zprime_mumu_smeared_*TeV/Limits/*" 
