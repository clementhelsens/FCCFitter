python python/limitplot.py -f "Outputs/fcc_v02/Zprime/jj/Zprime_jj_*TeV/Limits/*" -n "Zprime_jj_fcc_v02" -p "Z' \rightarrow jj" -s "p8_pp_ZprimeSSM_VALUETeV_jj"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/jj_5p/Zprime_jj_*TeV/Limits/*" -n "Zprime_jj_5p_fcc_v02" -p "Z' \rightarrow jj" -s "p8_pp_ZprimeSSM_VALUETeV_jj"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/jj_10p/Zprime_jj_*TeV/Limits/*" -n "Zprime_jj_10p_fcc_v02" -p "Z' \rightarrow jj" -s "p8_pp_ZprimeSSM_VALUETeV_jj"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/jj_15p/Zprime_jj_*TeV/Limits/*" -n "Zprime_jj_15p_fcc_v02" -p "Z' \rightarrow jj" -s "p8_pp_ZprimeSSM_VALUETeV_jj"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/jj_20p/Zprime_jj_*TeV/Limits/*" -n "Zprime_jj_20p_fcc_v02" -p "Z' \rightarrow jj" -s "p8_pp_ZprimeSSM_VALUETeV_jj"


python python/limitplot.py -f "Outputs/fcc_v02/Zprime/jj_2t/Zprime_jj_*TeV/Limits/*" -n "Zprime_jj_2t_fcc_v02" -p "Z' \rightarrow jj" -s "p8_pp_ZprimeSSM_VALUETeV_jj"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/jj_3t/Zprime_jj_*TeV/Limits/*" -n "Zprime_jj_3t_fcc_v02" -p "Z' \rightarrow jj" -s "p8_pp_ZprimeSSM_VALUETeV_jj"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/jj_4t/Zprime_jj_*TeV/Limits/*" -n "Zprime_jj_4t_fcc_v02" -p "Z' \rightarrow jj" -s "p8_pp_ZprimeSSM_VALUETeV_jj"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/jj_5t/Zprime_jj_*TeV/Limits/*" -n "Zprime_jj_5t_fcc_v02" -p "Z' \rightarrow jj" -s "p8_pp_ZprimeSSM_VALUETeV_jj"

python python/limitplot.py -f "Outputs/fcc_v02/Zprime/jj/Zprime_jj_*TeV/Limits/*" -n "Zprime_jj_comp_fcc_v02" -p "Z' \rightarrow jj" -s "p8_pp_ZprimeSSM_VALUETeV_jj" --smeart2 "Outputs/fcc_v02/Zprime/jj_2t/Zprime_jj_*TeV/Limits/*" --smeart3 "Outputs/fcc_v02/Zprime/jj_3t/Zprime_jj_*TeV/Limits/*" --smeart4 "Outputs/fcc_v02/Zprime/jj_4t/Zprime_jj_*TeV/Limits/*" --smeart5 "Outputs/fcc_v02/Zprime/jj_5t/Zprime_jj_*TeV/Limits/*" 
