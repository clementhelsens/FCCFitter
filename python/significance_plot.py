import json
import optparse
import sys
from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import os
import ROOT as r
from ROOT import *
from array import array
plotname=''
#__________________________________________________________
def getMassDisco(signiDict):
    
    indict=None
    with open(signiDict,'r') as f:
        indict = json.load(f)
        
    mass =[]
    disco = []

    for m in indict:
        signi=[]
        lumi=[]
        print m
        for i in indict[m]:
            signi.append(i['signi'])
            lumi.append(i['lumi'])
        print signi
        print lumi

        signi,lumi = zip(*sorted(zip(signi, lumi)))

        plt.figure()
        xnew = np.linspace(min(lumi), max(lumi), 100)
        f = interp1d(lumi, signi)
        plt.plot(lumi, signi, 'o-', xnew, f(xnew), '-')
        plt.plot([min(lumi), max(lumi)], [5, 5], 'k-', lw=2)
        plt.plot([min(lumi), max(lumi)], [3, 3], 'k-', lw=2)            
        plt.xlabel('luminosity fb$^{-1}')
        plt.ylabel('significance sigma')
        plt.grid(True)
        plt.savefig('Plots/Signi_%s_%s.eps'%(m,plotname))
        plt.close()


        plt.figure()
        xnew = np.linspace(min(signi), max(signi), 1000)
        f = interp1d(signi, lumi)
        plt.plot(signi, lumi, 'o-', xnew, f(xnew), '-')
        plt.plot([5,5],[min(lumi), max(lumi)], 'k-', lw=2)
        plt.plot([3,3],[min(lumi), max(lumi)], 'k-', lw=2)            
        plt.ylabel('luminosity fb$^{-1}')
        plt.xlabel('significance sigma')
        plt.grid(True)
        discolumi = f(5) if xnew[-1]>5.0 else f(xnew[-1])
        plt.plot([0,5],[discolumi, discolumi], 'k-', lw=2)            
        plt.savefig('Plots/SigniInverse_%s_%s.eps'%(m,plotname))
        print 'lumi = %f'%discolumi
        plt.close()

        mass.append(int(m))
        disco.append(discolumi)

    Mass,Disco = zip(*sorted(zip(mass, disco)))
    print Mass
    print Disco
    return Disco,Mass

#__________________________________________________________
if __name__=="__main__":
    
    parser = optparse.OptionParser(description="analysis parser")
    parser.add_option('-f', '--files', dest='files', type=str, default='')
    parser.add_option('-n', '--names', dest='names', type=str, default='')
    parser.add_option('-p', '--plot', dest='plot', type=str, default='')

    ops, args = parser.parse_args()
    signiDict=ops.files
    names=ops.names
    
    if not os.path.isdir("Plots/"):
        os.system('mkdir Plots')

    signiList = signiDict.split(' ')
    namesList = names.split(' ')
    print signiList
    print namesList
    if len(signiList)!=len(namesList):
        print 'different length, name, signi, exit',len(signiList),'  ',len(namesList)
        sys.exit(3)
    plt.figure()

    graph_array = []
    
    for s in xrange(len(signiList)):
        plotname=namesList[s]

        print signiList[s]
        Disco,Mass=getMassDisco(signiList[s])
        Disco=[i/1000. for i in Disco]
        from scipy import interpolate
        f = interpolate.interp1d(Mass, Disco)
        xnew = np.linspace(Mass[0],Mass[-1],50)
        Disco_smooth = f(xnew)

        plt.plot(Mass, Disco, label=namesList[s])
        #plt.plot( xnew, Disco_smooth, '-')
        
        Mass_array  = array( 'd' )
        Disco_array = array( 'd' )
        for m in range( len(Mass) ) :
          Mass_array.append( Mass[m] )
          Disco_array.append( Disco[m] )
        graph_array.append( [namesList[s],Mass_array,Disco_array] )


    plt.ylabel('Int. Luminosity fb$^{-1}$')
    plt.xlabel('mass [TeV]')
    #plt.title('luminosity versus mass for a 5 $\sigma$ discovery')
    if 'tt' in namesList:
        plt.ylim(ymax = 1000000, ymin = 100)
        plt.text(10.57, 500000, r'$Z\' \rightarrow = t \bar{t}$')
        plt.text(10.57, 300000, r'Integrated luminosity versus mass for a 5 $\sigma$ discovery')

        plt.text(10.57, 2500, r'$2.5ab^{-1}$')
        plt.plot([10,30], [2500, 2500], color='black')
        plt.text(10.57, 30000, r'$30ab^{-1}$')
        plt.plot([10,30], [30000, 30000], color='black')

    if 'll' in namesList:
        plt.ylim(ymax = 1000000, ymin = 10)
        plt.text(16, 500000, r'$Z\' \rightarrow = l^{+}l^{-}$')
        plt.text(16, 300000, r'Integrated luminosity versus mass for a 5 $\sigma$ discovery')

        plt.text(16, 2500, r'$2.5ab^{-1}$')
        plt.plot([15,50], [2500, 2500], color='black')
        plt.text(16, 30000, r'$30ab^{-1}$')
        plt.plot([15,50], [30000, 30000], color='black')
        plt.legend(loc=4)


    plt.grid(True)
    #plt.legend(loc=4)
    plt.yscale('log')

    plt.savefig('Plots/DiscoveryPotential_%s.eps'%(plotname))
    plt.savefig('Plots/DiscoveryPotential_%s.png'%(plotname))

    plt.close()

    ########################
    # ROOT style
    canvas = r.TCanvas("Discovery","Discovery",0,0,600,600)
    canvas.SetLogy(1)
    canvas.SetTicks(1,1)
    canvas.SetLeftMargin(0.14)
    canvas.SetRightMargin(0.08)
    canvas.SetGridx()
    #canvas.SetGridy()

    lg = r.TLegend(0.6,0.18,0.78,0.28)
    lg.SetFillStyle(0)
    lg.SetLineColor(0)
    lg.SetBorderSize(0)
    lg.SetShadowColor(10)
    lg.SetTextSize(0.040)
    lg.SetTextFont(42)


    dicgraph={}
    max_mass_idx=-1
    mass_for_latex=int(graph_array[0][1][0])*1.12
    color = [kBlue-4,kRed,kGreen-3,kViolet,kBlack]
    for s in xrange(len(signiList)):
      ana   = graph_array[s][0]
      Mass  = graph_array[s][1]
      nmass = len(Mass)
      Disco = graph_array[s][2]
      dicgraph[str(s)]= r.TGraph(nmass, Mass, Disco)
      #gdisco_root = r.TGraph(nmass, Mass, Disco)
      if s<5 : dicgraph[str(s)].SetLineColor(color[s])
      else   : dicgraph[str(s)].SetLineColor(s+20)
      dicgraph[str(s)].SetLineWidth(3)
      if s == 0:
        dicgraph[str(s)].SetName(ana)
        dicgraph[str(s)].SetTitle( "" )
        dicgraph[str(s)].GetXaxis().SetTitle( "Mass [TeV]" )
        dicgraph[str(s)].GetYaxis().SetTitle( "Int. Luminosity [fb^{-1}]" )
        # check if need to rescale x-axis
        for d in Disco :
          if d>1E+6 and max_mass_idx==-1: max_mass_idx=Disco.index(d)
        dicgraph[str(s)].GetXaxis().SetLimits(Mass[0], Mass[max_mass_idx])
        if Disco[0]>1E+2:
            dicgraph[str(s)].SetMinimum(1E+2)
        elif Disco[0]>1E+1:
            dicgraph[str(s)].SetMinimum(1E+1)
        else :
            dicgraph[str(s)].SetMinimum(1E+0)

        dicgraph[str(s)].SetMaximum(1E+6)
        dicgraph[str(s)].GetYaxis().SetTitleOffset(1.6)
#        dicgraph[str(s)].Draw("AC")
        dicgraph[str(s)].Draw("AC")
        #dicgraph[str(s)].SetMarkerStyle(21)
        #dicgraph[str(s)].SetMarkerSize(1.5)
        #dicgraph[str(s)].SetMarkerColor(kRed)
        #dicgraph[str(s)].Draw("*")
      else :
#        dicgraph[str(s)].Draw("C")
          dicgraph[str(s)].Draw("C")
      lg.AddEntry(dicgraph[str(s)],ana.replace('mumu','#mu#mu'),"L")
    if len(signiList)>1 : lg.Draw()

    line1 = TLine(graph_array[s][1][0],2.5E+3,graph_array[s][1][max_mass_idx],2.5E+3);
    line1.SetLineWidth(3)
    line1.SetLineStyle(2)
    line1.SetLineColor(kGreen+3);
    line1.Draw("same");

    line2 = TLine(graph_array[s][1][0],3E+4,graph_array[s][1][max_mass_idx],3E+4);
    line2.SetLineWidth(3)
    line2.SetLineStyle(2)
    line2.SetLineColor(kGreen+3);
    line2.Draw("same");

    plotname = ""
    if ana=='tt' : plotname+="Z\' #rightarrow t#bar{t}"
    if ana=='ll' : plotname+="Z\' #rightarrow l^{+}l^{-}"
    if ana=='ww' : plotname+="RSG #rightarrow W^{+}W^{-}"
    label = r.TLatex()
    label.SetNDC()
    label.SetTextColor(1)
    label.SetTextSize(0.042)
    label.SetTextAlign(12)
    label.DrawLatex(0.18,0.85, "FCC simulation")
    label.DrawLatex(0.18,0.79, "\sqrt{s}=100TeV")
    label.SetTextSize(0.03)
    label.DrawLatex(0.2,0.14, "Integrated luminosity versus mass for a 5 #sigma discovery")
    label.SetTextSize(0.036)
    label.DrawLatex(0.18,0.73, plotname)
    label.SetTextSize(0.03)
    label.SetNDC(False)
    label.DrawLatex(mass_for_latex,1.5*30E+3, "30 ab^{-1}")
    label.DrawLatex(mass_for_latex,1.5*2.5E+3, "2.5 ab^{-1}")


    canvas.RedrawAxis()
    #canvas.Update()
    canvas.GetFrame().SetBorderSize( 12 )
    canvas.Modified()
    canvas.Update()
    canvas.SaveAs('Plots/DiscoveryPotential_%s_rootStyle.eps'%(ops.plot))
    canvas.SaveAs('Plots/DiscoveryPotential_%s_rootStyle.png'%(ops.plot))



