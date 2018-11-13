import ROOT as r

only_100=True
#only_100=False

rsgww      = ["RSG #rightarrow W^{+}W^{-}",
              [5.,7.,11.],  #  27 TeV ->   1, 15, 100 ab-1
              [15.,22.,34.]] # 100 TeV -> 2.5, 30, 100 ab-1
qstar      = ["Q* #rightarrow jj",
              [10.,12.,16.],
              [36.,40.,50.]]
zpttTC2    = ["Z\'_{TC2} #rightarrow t#bar{t}",
              [6.,8.,18.],
              [16.,23.,33.]]
zpttSSM    = ["Z\'_{SSM} #rightarrow t#bar{t}",
              [4.,6.,18.],
              [10.,18.,29.]]
zpll       = ["Z\'_{SSM} #rightarrow l^{+}l^{-}",
              [10.,13.,17.],
              [33.,43.,55.]]
zptautau   = ["Z\'_{SSM} #rightarrow #tau^{+}#tau^{-}",
              [3.,6.,10.],
              [12.,18.,29.]]
# f.a. = 1710.06363
zpmumuflav = ["Z\'_{f.a.} #rightarrow #mu^{+}#mu^{-}",
              [0.1,2.,8.],
              [10.,19.,34.]]

database=[
zptautau,
#zpmumuflav,
zpll,
rsgww,
zpttSSM,
zpttTC2,
qstar,
]

nAna=6
nbins = (3*nAna)
if only_100==True : nbins = (2*nAna)
h_27=[]
h_27.append( r.TH1D("h_27_1", "h_27_1", nbins,0.,nbins))
h_27.append( r.TH1D("h_27_2", "h_27_2", nbins,0.,nbins))
h_27.append( r.TH1D("h_27_3", "h_27_3", nbins,0.,nbins))
h_100=[]
h_100.append(r.TH1D("h_100_1","h_100_1",nbins,0.,nbins))
h_100.append(r.TH1D("h_100_2","h_100_2",nbins,0.,nbins))
h_100.append(r.TH1D("h_100_3","h_100_3",nbins,0.,nbins))

nMax=len(h_100)-1

color  = [[r.kYellow-7, r.kAzure-9], [r.kRed+1, r.kBlue+1], [r.kGray+3, r.kGray+2]]
legend = [["1 ab^{-1}", "2.5 ab^{-1}"], ["15 ab^{-1}", "30 ab^{-1}"], ["100 ab^{-1}", "100 ab^{-1}"]]

process = [database[0][0],database[1][0],database[2][0],database[3][0],database[4][0],database[5][0]]
val27   = [database[0][1],database[1][1],database[2][1],database[3][1],database[4][1],database[5][1]]
val100  = [database[0][2],database[1][2],database[2][2],database[3][2],database[4][2],database[5][2]]

count = 1
count_ana = 0
for i_bin in xrange( 1, nbins+1 ):
  if count==4 : count=1
  if count==1 :
    if only_100==False :
      for i in xrange( 0, nMax+1 ) : h_27[i].SetBinContent(i_bin, val27[count_ana][i])
    else :
      count+=1
  if count==2 :
    for i in xrange( 0, nMax+1 ) :
      h_100[i].SetBinContent(i_bin, val100[count_ana][i])
  #
  if only_100==False :
    str_27   = '#scale[0.75]{27 TeV}'
    str_100  = '#scale[0.75]{100 TeV}'
    if count==1 : h_100[nMax].GetXaxis().SetBinLabel(i_bin,str_27)
    if count==2 : h_100[nMax].GetXaxis().SetBinLabel(i_bin,str_100)
    if count==3 :
      str_proc = '#scale[1.02]{#font[22]{'+process[count_ana]+'}}'
      h_100[nMax].GetXaxis().SetBinLabel(i_bin,str_proc)
      count_ana+=1
  else :
    if count==2 :
      str_proc = '#scale[1.02]{#font[22]{'+process[count_ana]+'}}'
      h_100[nMax].GetXaxis().SetBinLabel(i_bin,str_proc)
      count_ana+=1
  count+=1

for i in xrange( 0, nMax+1 ) :
  alpha=0.42
  if i==0: alpha=0.8
  if i==nMax: alpha=0.15
  #
  h_27[i].SetFillColor(color[i][0])
  h_27[i].SetLineColor(color[i][0])
  h_27[i].SetFillColorAlpha(color[i][0],alpha)
  h_100[i].SetFillColor(color[i][1])
  h_100[i].SetLineColor(color[i][1])
  h_100[i].SetFillColorAlpha(color[i][1],alpha)

canvas = r.TCanvas("test", "test", 600, 600)
canvas.SetTicks(1,1)
canvas.SetLeftMargin(0.21)
canvas.SetRightMargin(0.02)
r.gStyle.SetOptStat(0)
r.gPad.SetGridx()

leg = r.TLegend(0.73,0.52,0.98,0.70)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetLineColor(0)
leg.SetShadowColor(10)
leg.SetTextSize(0.035)
leg.SetTextFont(42)

the_max=h_100[nMax].GetMaximum()
h_100[nMax].SetMaximum(the_max*1.1)
h_100[nMax].SetTitle("")
h_100[nMax].GetYaxis().SetTitleOffset(1.30)
h_100[nMax].GetYaxis().SetTitle("Mass scale [TeV]")
h_100[nMax].GetXaxis().SetLabelSize(0.05)

h_100[nMax].Draw("hbar")
for i in xrange( nMax, -1, -1 ) :
  h_100[i].Draw("hbarsame")
  if only_100==False : h_27[i].Draw("hbarsame")

for i in xrange( 0, nMax+1 ) :
  if only_100==False and i!=nMax : leg.AddEntry(h_27[i],legend[i][0])
  leg.AddEntry(h_100[i],legend[i][1])
leg.Draw("same")

Text = r.TLatex()
Text.SetNDC()
Text.SetTextAlign(31);
Text.SetTextSize(0.033)
text = '5 #sigma Discovery'
Text.DrawLatex(0.95, 0.72, text)

canvas.RedrawAxis()
canvas.GetFrame().SetBorderSize( 12 )
canvas.Modified()
canvas.Update()

extra=""
if only_100==True : extra="_onlyFCChh"
canvas.Print("summaryDisco"+extra+".pdf")

