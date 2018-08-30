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

    signal = ops.signal
    print 'NOM=============================================='
    print masses_nom
    print files_nom
    print '=============================================='


    print 'CMS=============================================='
    print masses_cms
    print files_cms
    print '=============================================='

    models =  ops.models
    models = models.split(" ")
    if len(masses_nom)!=len(files_nom):
        print 'different length for nominal, exit'
        sys.exit(2)

    if len(masses_cms)!=len(files_cms):
        print 'different length for cms, exit'
        sys.exit(2)



    if len(masses_nom)>0:masses_nom, files_nom = (list(t) for t in zip(*sorted(zip(masses_nom, files_nom))))
    if len(masses_cms)>0: masses_cms, files_cms = (list(t) for t in zip(*sorted(zip(masses_cms, files_cms))))


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
        proc = '#sigma(pp #rightarrow RSG)*BR [pb]'
        theoname = 'RSG Pythia8 LO'
    if ops.name.find("jj")>=0 : 
        proc = '#sigma(pp #rightarrow Q*)*BR [pb]'
        theoname = 'Q* Pythia8 LO'

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


    lg = None
    if len(models)>1 : lg = r.TLegend(0.58,0.5,0.90,0.88)
    else:lg = r.TLegend(0.58,0.65,0.90,0.88)
        
    lg.SetFillStyle(0)
    lg.SetLineColor(0)
    lg.SetBorderSize(0)
    lg.SetShadowColor(10)
    lg.SetTextSize(0.030)
    lg.SetTextFont(42)


    lg.AddEntry(gmed, "Median expected.", "L")
    lg.AddEntry(g1s,"95% expected","F")
    lg.AddEntry(g2s,"68% expected","F")
    #lg.AddEntry(gtheo,"Z^{\prime}_{SSM}","L")
    sig_found=True
    if signal.find("p8_pp_Zprime")>=0 and signal.find("_VALUETeV_jj")>=0: sig_found=False
    if signal=="mgp8_pp_Zprime_mumu_5f_Mzp_VALUETeV": sig_found=False
    if signal=="p8_pp_ZprimeSSM_VALUETeV_ll": sig_found=False
    if sig_found==True :
      lg.AddEntry(gtheo,theoname,"L")
    else :
      if signal=="mgp8_pp_Zprime_mumu_5f_Mzp_VALUETeV" : 
        lg.AddEntry(gtheo,"Z^{\prime} (1710.06363)","L")
      elif signal=="mgp8_pp_LQ_mumu_5f_MLQ_VALUETeV" :
        lg.AddEntry(gtheo,"LQ (1710.06363)","L")
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
      elif do_SSM==True :
        lg.AddEntry(gtheo,    "Z^{\prime}_{TC2}","L")
        lg.AddEntry(gtheo_SSM,"Z^{\prime}_{SSM}","L")
      elif len(models)>1 :
          print "-----------------------------------------"
          gtheolist={}
          gtheocolorlist={'p8_pp_ZprimeCHI_VALUETeV_ll':4, 
                          'p8_pp_ZprimePSI_VALUETeV_ll':5,
                          'p8_pp_ZprimeLRM_VALUETeV_ll':6,
                          'p8_pp_ZprimeETA_VALUETeV_ll':7,
                          'p8_pp_ZprimeI_VALUETeV_ll':8,
                          }
          gtheonamelist={'p8_pp_ZprimeCHI_VALUETeV_ll':'\\chi', 
                          'p8_pp_ZprimePSI_VALUETeV_ll':'\\psi',
                          'p8_pp_ZprimeLRM_VALUETeV_ll':'LRM',
                          'p8_pp_ZprimeETA_VALUETeV_ll':'\\eta',
                          'p8_pp_ZprimeI_VALUETeV_ll':'I',
                          }

          lg.AddEntry(gtheo,"Z^{\prime}_{SSM}","L")
          for mod in models:
              print 'model    ',mod
              if mod=="":continue
              XS=getXS(masses_nom, mod, ops.name)
              XStheo=array('d')
              for v in XS:
                  if "p8_pp_Zprime" in mod and "ll" in mod: XStheo.append(v/3.)
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
      else :
        lg.AddEntry(gtheo,"Z^{\prime}_{SSM}","L")
        
    if len(masses_cms)>0: lg.AddEntry(gmed_cms, "95% CL exp. limit CMS", "L")

    lg.Draw()


    label = r.TLatex()
    label.SetNDC()
    label.SetTextColor(1)
    label.SetTextSize(0.042)
    label.SetTextAlign(12)
    if ops.name.find("fcc")>=0 :
      label.DrawLatex(0.24,0.85, "FCC simulation")
      label.DrawLatex(0.24,0.79, "\sqrt{s}=100TeV")
      label.DrawLatex(0.24,0.73, "\int Ldt=30ab^{-1}")
    elif ops.name.find("helhc")>=0 :
      label.DrawLatex(0.24,0.85, "HELHC simulation")
      label.DrawLatex(0.24,0.79, "\sqrt{s}=27TeV")
      label.DrawLatex(0.24,0.73, "\int Ldt=15ab^{-1}")
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

   
