python python/significance_plot.py -f "Data/bkup/Zprime_tt_fcc_v02_cut.json" -n "tt" -p tt_cut
python python/significance_plot.py -f "Data/bkup/Zprime_tt_fcc_v02_cut_TRFbtag.json" -n "tt" -p tt_cut_TRFbtag
python python/significance_plot.py -f "Data/bkup/Zprime_tt_TC2_fcc_v02_tagger.json" -n "TC2" -p tt_TC2_tagger
python python/significance_plot.py -f "Data/bkup/Zprime_tt_TC2_fcc_v02_tagger_TRFbtag.json" -n "TC2" -p tt_TC2_tagger_TRFbtag
python python/significance_plot.py -f "Data/bkup/Zprime_tt_SSM_fcc_v02_tagger_TRFbtag.json" -n "SSM" -p tt_SSM_tagger_TRFbtag
python python/significance_plot.py -f "Data/bkup/Zprime_tt_SSM_fcc_v02_tagger_TRFbtag.json Data/bkup/Zprime_tt_TC2_fcc_v02_tagger_TRFbtag.json" -n "SSM TC2" -p tt_SSM_TC2_tagger_TRFbtag

