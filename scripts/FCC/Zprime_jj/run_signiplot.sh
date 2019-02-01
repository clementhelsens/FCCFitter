python python/significance_plot.py -f "Data/Zprime_jj_fcc_v02.json" -n "zpjj" -p Zp_jj
python python/significance_plot.py -f "Data/Zprime_jj_fcc_v02.json Data/Zprime_jj_fcc_v02_5p.json Data/Zprime_jj_fcc_v02_10p.json Data/Zprime_jj_fcc_v02_15p.json Data/Zprime_jj_fcc_v02_20p.json" -n "nominal 5p 10p 15p 20p" -p Zp_jj_comb

python python/significance_plot.py -f "Data/Zprime_jj_fcc_v02.json Data/Zprime_jj_fcc_v02_2t.json Data/Zprime_jj_fcc_v02_3t.json Data/Zprime_jj_fcc_v02_4t.json Data/Zprime_jj_fcc_v02_5t.json" -n "nominal 6% 9% 12% 6%" -p Zp_jj_comb_smeared --mmin 15 --mmax 20
