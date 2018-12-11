import sys
import ROOT as r
import json
from array import array
from math import sin
from os import listdir
import os
import glob
import optparse
procDict_FCC='/afs/cern.ch/work/h/helsens/public/FCCDicts/FCC_procDict_fcc_v02.json'
procDict_HELHC='/afs/cern.ch/work/h/helsens/public/FCCDicts/HELHC_procDict_helhc_v01.json'


#__________________________________________________________
def getMasses(limit_files):
    masses=[i.split('/')[-1].replace('.root','') for i in limit_files]
    print '======================= 1 ',masses
    masses=[int(i.split('_')[-1].replace('TeV','')) for i in masses]
    print '======================= 2 ',masses
    return masses

#__________________________________________________________
def getXS(masses, template, name):
    mydict=None
    procDict=None
    if name.find("fcc")>=0: procDict=procDict_FCC
    elif name.find("helhc")>=0: procDict=procDict_HELHC

    with open(procDict) as f:
        mydict = json.load(f)
    XS=array('d')
    for m in masses:
        sig=template.replace('VALUE',str(m))
        try: 
            mydict[sig]
            XS.append(mydict[sig]['crossSection'])
        except KeyError, err:
            print err
    return XS


#__________________________________________________________
def getBRZjj(template, decay):
    # mass depandancy is tyny fo rthe masses considered at HE-LHC
    BRZjj=1.
    #
    if "PSI" in template and decay=="qq" : BRZjj=0.403+0.134
    if "PSI" in template and decay=="bb" : BRZjj=0.134
    if "PSI" in template and decay=="tt" : BRZjj=0.131
    #
    if "I"   in template and decay=="qq" : BRZjj=0.402+0.
    if "I"   in template and decay=="bb" : BRZjj=0.201
    if "I"   in template and decay=="tt" : BRZjj=0.
    #
    if "CHI" in template and decay=="qq" : BRZjj=0.402+0.037
    if "CHI" in template and decay=="bb" : BRZjj=0.184
    if "CHI" in template and decay=="tt" : BRZjj=0.035
    #
    if "LRM" in template and decay=="qq" : BRZjj=0.498+0.111
    if "LRM" in template and decay=="bb" : BRZjj=0.194
    if "LRM" in template and decay=="tt" : BRZjj=0.106
    #
    if "SSM" in template and decay=="qq" : BRZjj=0.381+0.108
    if "SSM" in template and decay=="bb" : BRZjj=0.138
    if "SSM" in template and decay=="tt" : BRZjj=0.104
    #
    if "ETA" in template and decay=="qq" : BRZjj=0.402+0.179
    if "ETA" in template and decay=="bb" : BRZjj=0.111
    if "ETA" in template and decay=="tt" : BRZjj=0.173
    #
    #print "getBRZjj->",template,decay,BRZjj
    return BRZjj

#______________________________________________________________________________
def split_comma_args(args):
    new_args = []
    for arg in args:
        new_args.extend( arg.split(',') )
    return new_args

#__________________________________________________________
if __name__=="__main__":
    print 'run python limitplot.py name files'

    
    parser = optparse.OptionParser(description="analysis parser")
    parser.add_option('-f', '--files_nom', dest='files_nom', type=str, default='')
    parser.add_option('-n', '--name', dest='name', type=str, default='')
    parser.add_option('-p', '--plotname', dest='plotname', type=str, default='')
    parser.add_option('-c', '--file_cms', dest='files_cms', type=str, default='')
    parser.add_option('--smeart2', dest='files_smeart2', type=str, default='')
    parser.add_option('--smeart3', dest='files_smeart3', type=str, default='')
    parser.add_option('--smeart4', dest='files_smeart4', type=str, default='')
    parser.add_option('--smeart5', dest='files_smeart5', type=str, default='')
    parser.add_option('-s', '--signal', dest='signal', type=str, default='')
    parser.add_option('-m', '--models', dest='models', type=str, default='')

    ops, args = parser.parse_args()
    args = split_comma_args(args)

    if not os.path.isdir("Plots/"):
        os.system('mkdir Plots')

    files_nom=[]
    masses_nom=[]
    if ops.files_nom!='':
        files_nom=glob.glob(ops.files_nom)
        masses_nom=getMasses(files_nom)

    files_cms=[]
    masses_cms=[]
    if ops.files_cms!='': 
        files_cms=glob.glob(ops.files_cms)
        masses_cms=getMasses(files_cms)

    files_smeart2=[]
    masses_smeart2=[]
    if ops.files_smeart2!='': 
        files_smeart2=glob.glob(ops.files_smeart2)
        masses_smeart2=getMasses(files_smeart2)

    files_smeart3=[]
    masses_smeart3=[]
    if ops.files_smeart3!='': 
        files_smeart3=glob.glob(ops.files_smeart3)
        masses_smeart3=getMasses(files_smeart3)

    files_smeart4=[]
    masses_smeart4=[]
    if ops.files_smeart4!='': 
        files_smeart4=glob.glob(ops.files_smeart4)
        masses_smeart4=getMasses(files_smeart4)

    files_smeart5=[]
    masses_smeart5=[]
    if ops.files_smeart5!='': 
        files_smeart5=glob.glob(ops.files_smeart5)
        masses_smeart5=getMasses(files_smeart5)


    signal = ops.signal
    print 'NOM=============================================='
    print masses_nom
    print files_nom
    print '=============================================='

    models =  ops.models
    models = models.split(" ")
    if len(masses_nom)!=len(files_nom):
        print 'different length for nominal, exit'
        sys.exit(2)

    if len(masses_cms)!=len(files_cms):
        print 'different length for cms, exit'
        sys.exit(2)

    if len(masses_smeart2)!=len(files_smeart2):
        print 'different length for smeart2, exit'
        sys.exit(2)

    if len(masses_smeart3)!=len(files_smeart3):
        print 'different length for smeart2, exit'
        sys.exit(2)

    if len(masses_smeart4)!=len(files_smeart4):
        print 'different length for smeart2, exit'
        sys.exit(2)

    if len(masses_smeart5)!=len(files_smeart5):
        print 'different length for smeart2, exit'
        sys.exit(2)

    if len(masses_nom)>0:masses_nom, files_nom = (list(t) for t in zip(*sorted(zip(masses_nom, files_nom))))
    if len(masses_cms)>0: masses_cms, files_cms = (list(t) for t in zip(*sorted(zip(masses_cms, files_cms))))
    if len(masses_smeart2)>0: masses_smeart2, files_smeart2 = (list(t) for t in zip(*sorted(zip(masses_smeart2, files_smeart2))))
    if len(masses_smeart3)>0: masses_smeart3, files_smeart3 = (list(t) for t in zip(*sorted(zip(masses_smeart3, files_smeart3))))
    if len(masses_smeart4)>0: masses_smeart4, files_smeart4 = (list(t) for t in zip(*sorted(zip(masses_smeart4, files_smeart4))))
    if len(masses_smeart5)>0: masses_smeart5, files_smeart5 = (list(t) for t in zip(*sorted(zip(masses_smeart5, files_smeart5))))


    # dav hack
    do_SSM=False
    if signal=="p8_pp_Zprime_VALUETeV_ttbar": do_SSM=True
 
    XStheo_SSM = array( 'd' )
    if ops.name.find("fcc")>=0:
      XStheo_SSM.append(6.481e-3)
      XStheo_SSM.append(8.906e-4)
      XStheo_SSM.append(1.965e-4)
      XStheo_SSM.append(5.065e-5)
      XStheo_SSM.append(1.541e-5)
      XStheo_SSM.append(5.696e-6)
    elif ops.name.find("helhc")>=0 :
      XStheo_SSM.append(0.331572)
      XStheo_SSM.append(0.0141432)
      XStheo_SSM.append(0.00142035)
      XStheo_SSM.append(0.000216873)
      XStheo_SSM.append(4.59795e-5)
      XStheo_SSM.append(1.46051e-5)
      XStheo_SSM.append(6.5528e-6)

    XS=getXS(masses_nom, signal, ops.name)
    XStheo=array('d')
    for v in XS:
        if signal=="p8_pp_ZprimeSSM_VALUETeV_ll": XStheo.append(v/3.)
        elif "p8_pp_Zprime" in signal and (ops.plotname=="tt" or ops.plotname=="bb" or ops.plotname=="qq"): XStheo.append(v*getBRZjj(signal, ops.plotname))
#; print "DAV->",v,getBRZjj(signal, ops.plotname),v*getBRZjj(signal, ops.plotname)
        else:  XStheo.append(v)
    nmass=len(files_nom)

    ExpMed = array( 'd' )
    ExpP2 = array( 'd' )
    ExpP1 = array( 'd' )
    ExpM1 = array( 'd' )
    ExpM2 = array( 'd' )
    dummy = array( 'd' )
    masses_array = array( 'd' )
    for i in xrange(nmass):
        rfile = r.TFile.Open(files_nom[i])
        histo=rfile.Get('limit')
        ExpMed.append(histo.GetBinContent(2)*XS[i])
        ExpP2.append((histo.GetBinContent(3)-histo.GetBinContent(2))*XS[i])
        ExpP1.append((histo.GetBinContent(4)-histo.GetBinContent(2))*XS[i])
        ExpM1.append((histo.GetBinContent(2)-histo.GetBinContent(5))*XS[i])
        ExpM2.append((histo.GetBinContent(2)-histo.GetBinContent(6))*XS[i])
        dummy.append(0)
        masses_array.append(masses_nom[i])


    gmed  = r.TGraph(nmass, masses_array, ExpMed)
    print 'XStheo  ',XStheo
    gtheo = r.TGraph(nmass, masses_array, XStheo)
    gtheo_SSM = r.TGraph(nmass, masses_array, XStheo_SSM)

    proc = '#sigma(pp #rightarrow Z\')*BR [pb]'
    theoname = "Z^{\prime}_{SSM}"

    if ops.name.find("ww")>=0 : 
        proc = '#sigma(pp #rightarrow G_{RS})*BR [pb]'
        theoname = 'G_{RS} Pythia8 LO'
    if ops.name.find("jj")>=0 : 
        proc = '#sigma(pp #rightarrow Q*)*BR [pb]'
        theoname = 'Q* Pythia8 LO'
    if ops.name.find("LQ")>=0 :
        proc = '#sigma(pp #rightarrow LQ)*BR [pb]'

    # style requests for Yellow Report
    for_YR=True
    #for_YR=False
    if for_YR==True : 
      if ops.name.find("ww")>=0 :
        proc = '#sigma(pp #rightarrow G_{RS}/G*_{RS} #rightarrow WW) [pb]'
      if ops.name.find("jj")>=0 :
        proc = '#sigma(pp #rightarrow Q\'/Q\'* #rightarrow jj) [pb]'
      if ops.name.find("tt")>=0 :
        proc = '#sigma(pp #rightarrow Z\'/Z\'* #rightarrow tt) [pb]'
      if ops.name.find("ll")>=0 :
        proc = '#sigma(pp #rightarrow Z\'/Z\'* #rightarrow ll (l=e,#mu)) [pb]'
      if ops.name.find("tautau")>=0 :
        proc = '#sigma(pp #rightarrow Z\'/Z\'* #rightarrow #tau#tau) [pb]'

    gmed.SetName("exp_median")
    gmed.SetLineColor(1)
    gmed.SetLineStyle(2)
    gmed.SetLineWidth(3)
    gmed.SetTitle( '' )
    gmed.GetXaxis().SetTitle( 'Mass [TeV]' )
    gmed.GetYaxis().SetTitle( proc )
    gmed.GetXaxis().SetLimits(masses_nom[0], masses_nom[-1])
    gmed.SetMinimum(min(ExpMed[-1],ExpM1[-1],ExpP1[-1],ExpM2[-1],ExpP2[-1],XS[-1])*0.1)
    gmed.SetMaximum(max(ExpMed[0],ExpM1[0],ExpP1[0],ExpM2[0],ExpP2[0],XS[0])*10.)
    gmed.GetYaxis().SetTitleOffset(1.6)
    gtheo.SetLineColor(2)
    gtheo.SetLineWidth(3)
    gtheo_SSM.SetLineColor(4)
    gtheo_SSM.SetLineWidth(3)

    g1s = r.TGraphAsymmErrors(nmass, masses_array, ExpMed,dummy,dummy,ExpM1,ExpP1)
    g1s.SetName("exp_pm1sig")
    g1s.SetFillColor(3)
    g1s.SetLineColor(1)
    g1s.SetFillStyle(3001)

    g2s = r.TGraphAsymmErrors(nmass, masses_array, ExpMed,dummy,dummy,ExpM2,ExpP2)
    g2s.SetName("exp_pm2sig")
    g2s.SetFillColor(5)
    g2s.SetLineColor(1)


    canvas = r.TCanvas("limit","limit versus mass",0,0,600,600)
    canvas.SetLogy(1)
    canvas.SetTicks(1,1)
    canvas.SetLeftMargin(0.14)
    canvas.SetRightMargin(0.08)

    gmed.Draw("ACP")
    g2s.Draw("3")
    g1s.Draw("3")
    gtheo.Draw("L")
    if do_SSM==True: gtheo_SSM.Draw("L")
    gmed.Draw("L")



#################################################
######CMS
#################################################


    XS=getXS(masses_cms, signal, ops.name)
    if len(masses_cms)>0:
        nmass=len(files_cms)

        ExpMed = array( 'd' )
        masses_array = array( 'd' )
        for i in xrange(nmass):
            rfile = r.TFile.Open(files_cms[i])
            histo=rfile.Get('limit')
            ExpMed.append(histo.GetBinContent(2)*XS[i])
            masses_array.append(masses_nom[i])

        gmed_cms  = r.TGraph(nmass, masses_array, ExpMed)
        gmed_cms.SetName("exp_median")
        gmed_cms.SetLineColor(1)
        gmed_cms.SetLineStyle(3)
        gmed_cms.SetLineWidth(3)
        gmed_cms.Draw("L")


#################################################
######smeart2
#################################################
    XS=getXS(masses_smeart2, signal, ops.name)
    if len(masses_smeart2)>0:
        nmass=len(files_smeart2)

        ExpMed = array( 'd' )
        masses_array = array( 'd' )
        for i in xrange(nmass):
            rfile = r.TFile.Open(files_smeart2[i])
            histo=rfile.Get('limit')
            ExpMed.append(histo.GetBinContent(2)*XS[i])
            masses_array.append(masses_nom[i])

        gmed_smeart2  = r.TGraph(nmass, masses_array, ExpMed)
        gmed_smeart2.SetName("exp_median")
        gmed_smeart2.SetLineColor(1)
        gmed_smeart2.SetLineStyle(3)
        gmed_smeart2.SetLineWidth(3)
        gmed_smeart2.Draw("L")

#################################################
######smeart3
#################################################
    XS=getXS(masses_smeart3, signal, ops.name)
    if len(masses_smeart3)>0:
        nmass=len(files_smeart3)

        ExpMed = array( 'd' )
        masses_array = array( 'd' )
        for i in xrange(nmass):
            rfile = r.TFile.Open(files_smeart3[i])
            histo=rfile.Get('limit')
            ExpMed.append(histo.GetBinContent(2)*XS[i])
            masses_array.append(masses_nom[i])

        gmed_smeart3  = r.TGraph(nmass, masses_array, ExpMed)
        gmed_smeart3.SetName("exp_median")
        gmed_smeart3.SetLineColor(1)
        gmed_smeart3.SetLineStyle(3)
        gmed_smeart3.SetLineWidth(3)
        gmed_smeart3.Draw("L")

#################################################
######smeart4
#################################################
    XS=getXS(masses_smeart4, signal, ops.name)
    if len(masses_smeart4)>0:
        nmass=len(files_smeart4)

        ExpMed = array( 'd' )
        masses_array = array( 'd' )
        for i in xrange(nmass):
            rfile = r.TFile.Open(files_smeart4[i])
            histo=rfile.Get('limit')
            ExpMed.append(histo.GetBinContent(2)*XS[i])
            masses_array.append(masses_nom[i])

        gmed_smeart4  = r.TGraph(nmass, masses_array, ExpMed)
        gmed_smeart4.SetName("exp_median")
        gmed_smeart4.SetLineColor(1)
        gmed_smeart4.SetLineStyle(3)
        gmed_smeart4.SetLineWidth(3)
        gmed_smeart4.Draw("L")

#################################################
######smeart5
#################################################
    XS=getXS(masses_smeart5, signal, ops.name)
    if len(masses_smeart5)>0:
        nmass=len(files_smeart5)

        ExpMed = array( 'd' )
        masses_array = array( 'd' )
        for i in xrange(nmass):
            rfile = r.TFile.Open(files_smeart5[i])
            histo=rfile.Get('limit')
            ExpMed.append(histo.GetBinContent(2)*XS[i])
            masses_array.append(masses_nom[i])

        gmed_smeart5  = r.TGraph(nmass, masses_array, ExpMed)
        gmed_smeart5.SetName("exp_median")
        gmed_smeart5.SetLineColor(1)
        gmed_smeart5.SetLineStyle(3)
        gmed_smeart5.SetLineWidth(3)
        gmed_smeart5.Draw("L")

    lg = None
    if len(models)>1 : lg = r.TLegend(0.58,0.5,0.90,0.88)
    else:lg = r.TLegend(0.58,0.65,0.90,0.88)
        
    lg.SetFillStyle(0)
    lg.SetLineColor(0)
    lg.SetBorderSize(0)
    lg.SetShadowColor(10)
    lg.SetTextSize(0.030)
    lg.SetTextFont(42)


    lg.AddEntry(gmed, "Median expected", "L")
    lg.AddEntry(g1s,"95% expected","F")
    lg.AddEntry(g2s,"68% expected","F")
    #lg.AddEntry(gtheo,"Z^{\prime}_{SSM}","L")
    sig_found=True
    if signal.find("p8_pp_Zprime")>=0 and signal.find("_VALUETeV_jj")>=0: sig_found=False
    if signal=="mgp8_pp_Zprime_mumu_5f_Mzp_VALUETeV": sig_found=False
    if signal=="p8_pp_ZprimeSSM_VALUETeV_ll": sig_found=False
    if signal=="p8_pp_ZprimeSSM_VALUETeV_jj": sig_found=False
    if signal=="mgp8_pp_LQ_mumu_5f_MLQ_VALUETeV": sig_found=False
    if do_SSM==True: sig_found=False
    if sig_found==True :
      lg.AddEntry(gtheo,theoname,"L")
    else :
      if signal=="mgp8_pp_Zprime_mumu_5f_Mzp_VALUETeV" : 
        lg.AddEntry(gtheo,"Z^{\prime} (1710.06363)","L")
      elif signal=="mgp8_pp_LQ_mumu_5f_MLQ_VALUETeV" :
        lg.AddEntry(gtheo,"LQ (1710.06363)","L")
      elif do_SSM==True :
        lg.AddEntry(gtheo,    "Z^{\prime}_{TC2}","L")
        lg.AddEntry(gtheo_SSM,"Z^{\prime}_{SSM}","L")
      elif len(models)>1 :
          print "-----------------------------------------"
          gtheolist={}
          extra = 'll'
          if signal=="p8_pp_ZprimeSSM_VALUETeV_jj": extra = 'jj'
          #
          gtheocolorlist={'p8_pp_ZprimeCHI_VALUETeV_'+extra:4, 
                          'p8_pp_ZprimePSI_VALUETeV_'+extra:5,
                          'p8_pp_ZprimeLRM_VALUETeV_'+extra:6,
                          'p8_pp_ZprimeETA_VALUETeV_'+extra:7,
                          'p8_pp_ZprimeI_VALUETeV_'+extra:8,
                          }
          gtheonamelist={ 'p8_pp_ZprimeCHI_VALUETeV_'+extra:'\\chi', 
                          'p8_pp_ZprimePSI_VALUETeV_'+extra:'\\psi',
                          'p8_pp_ZprimeLRM_VALUETeV_'+extra:'LRM',
                          'p8_pp_ZprimeETA_VALUETeV_'+extra:'\\eta',
                          'p8_pp_ZprimeI_VALUETeV_'+extra:'I',
                          }

          lg.AddEntry(gtheo,"Z^{\prime}_{SSM}","L")
          for mod in models:
              print 'model    ',mod
              if mod=="":continue
              XS=getXS(masses_nom, mod, ops.name)
              XStheo=array('d')
              for v in XS:
                  if "p8_pp_Zprime" in mod and "ll" in mod: XStheo.append(v/3.)
                  elif "p8_pp_Zprime" in mod and (ops.plotname=="tt" or ops.plotname=="bb" or ops.plotname=="qq"): XStheo.append(v*getBRZjj(mod, ops.plotname))
                  else:  XStheo.append(v)
              print 'loop models nmass ',nmass
              print 'loop models mass array ',masses_array
              print 'loop models xs     ',XS
              print 'loop models xstheo ',XStheo
              
              gtheolist[mod] = r.TGraph(nmass, masses_array, XStheo)
              gtheolist[mod].SetLineColor(gtheocolorlist[mod])
              gtheolist[mod].SetLineWidth(2)

              gtheolist[mod].Draw("L")
              #lg.AddEntry(gtheo,"Z^{\prime}_{SSM}","L")
              lg.AddEntry(gtheolist[mod], "Z^{\prime}_{%s}"%gtheonamelist[mod],"L")
              #lg.AddEntry(gtheolist[mod], "Z^{'}_{%s}"%gtheonamelist[mod],"L")
      elif signal=="p8_pp_ZprimeCHI_VALUETeV_jj" :
        lg.AddEntry(gtheo,"Z^{\prime}_{\\chi}","L")
      elif signal=="p8_pp_ZprimePSI_VALUETeV_jj" :
        lg.AddEntry(gtheo,"Z^{\prime}_{\\psi}","L")
      elif signal=="p8_pp_ZprimeLRM_VALUETeV_jj" :
        lg.AddEntry(gtheo,"Z^{\prime}_{LRM}","L")
      elif signal=="p8_pp_ZprimeETA_VALUETeV_jj" :
        lg.AddEntry(gtheo,"Z^{\prime}_{\\eta}","L")
      elif signal=="p8_pp_ZprimeI_VALUETeV_jj" :
        lg.AddEntry(gtheo,"Z^{\prime}_{I}","L")
      elif signal=="p8_pp_ZprimeSSM_VALUETeV_jj" :
        lg.AddEntry(gtheo,"Z^{\prime}_{SSM}","L")
      else :
        lg.AddEntry(gtheo,"Z^{\prime}_{SSM}","L")
        
    if len(masses_cms)>0: lg.AddEntry(gmed_cms, "95% CL exp. limit CMS", "L")
    if len(masses_smeart2)>0: lg.AddEntry(gmed_smeart2, "reso x2", "L")
    if len(masses_smeart3)>0: lg.AddEntry(gmed_smeart3, "reso x3", "L")
    if len(masses_smeart4)>0: lg.AddEntry(gmed_smeart4, "reso x4", "L")
    if len(masses_smeart5)>0: lg.AddEntry(gmed_smeart5, "reso x5", "L")

    lg.Draw()


    label = r.TLatex()
    label.SetNDC()
    label.SetTextColor(1)
    label.SetTextSize(0.042)
    label.SetTextAlign(12)

    if ops.name.find("fcc")>=0 :
      label.SetNDC()
      label.SetTextAlign(31);
      label.SetTextSize(0.04)
      label.DrawLatex(0.90,0.92, "#it{FCC-hh Simulation (Delphes)}")

      label.SetTextAlign(12);
      label.SetNDC(r.kTRUE)
      label.SetTextSize(0.04)
      label.DrawLatex(0.18,0.83, "#bf{#it{#sqrt{s} = 100 TeV}}")

      label.SetTextSize(0.035)
      label.DrawLatex(0.18,0.78, "#bf{#it{   L = 30 ab^{-1}}}")

    elif ops.name.find("helhc")>=0 :
      label.SetNDC()
      label.SetTextAlign(31);
      label.SetTextSize(0.04)
      label.DrawLatex(0.90,0.92, "#it{HE-LHC Simulation (Delphes)}")

      label.SetTextAlign(12);
      label.SetNDC(r.kTRUE)
      label.SetTextSize(0.04)
      label.DrawLatex(0.18,0.83, "#bf{#it{#sqrt{s} = 27 TeV}}")

      label.SetTextSize(0.035)
      label.DrawLatex(0.18,0.78, "#bf{#it{   L = 15 ab^{-1}}}")

    else :
      print 'name does not contains fcc or helhc'
      sys.exit(3)
    label.DrawLatex(0.24,0.15, ops.plotname)


    canvas.RedrawAxis()
    canvas.Update()
    canvas.GetFrame().SetBorderSize( 12 )
    canvas.Modified()
    canvas.Update()
    canvas.SaveAs("Plots/lim_%s.eps"%(ops.name))
    canvas.SaveAs("Plots/lim_%s.png"%(ops.name))

   
