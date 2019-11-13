"""
! ===========================================================================
! chi2fitting.py
! ===========================================================================
!
!
!     Valentina Roquemen Echeverry, valentina.roquemen@udea.edu.co

! Up to date: 7 noviembre de 2019			
"""
# Librerias
import ROOT
from ROOT import gROOT 
import numpy as np
import matplotlib.pyplot as plt

# Definicion de B
BackgroundModel = ROOT.TH1F( 'bkg', 'My background model', 20, 50, 1050 )

expde = ROOT.TF1("expde","([2]*expo)+[3]",50,1050)
expde.SetParameters(0.0,-0.005,100,0.0);

BackgroundModel.FillRandom("expde",100000)

# Definicion de S
SignalModel = ROOT.TH1F( 'sig', 'My signal model', 20, 50, 1050 )

signal = ROOT.TF1("signal", "gaus", 50, 1050)
signal.SetParameters(1.0,500.0,50.0)

SignalModel.FillRandom("signal",1000)


# Se cargan archivos a los cuales se les debe ajustar la curva
DataFile = ROOT.TFile("Data5.root","read")
DataHisto=DataFile.Get('data')

Mu = np.arange(0,3,0.005)
chi = np.zeros_like(Mu)

# Calculo de chi2
i = 0
for mu in Mu:
	BkgpSigModel = BackgroundModel.Clone("bkgpsig")
	BkgpSigModel.Sumw2()
	BkgpSigModel.Add(SignalModel,mu)

	chi2 = 0
	for j in range(1,DataHisto.GetNbinsX()):
		chi2 += (BkgpSigModel.GetBinContent(j)-DataHisto.GetBinContent(j))**2/DataHisto.GetBinContent(j)

	chi[i] = chi2
	i += 1

# Grafica de chi2 vs. mu
mini = Mu[chi==min(chi)]
plt.plot(Mu,chi)
plt.title(r'$\mu = %f$'%mini)
plt.xlabel(r'$\mu$')
plt.ylabel(r'$\chi^2$')
plt.grid()
plt.show()

# Grafica del ajuste y de los datos
BkgpSigModel = BackgroundModel.Clone("bkgpsig")
BkgpSigModel.Sumw2()
BkgpSigModel.Add(SignalModel,mini)

c1 = ROOT.TCanvas( 'c1', 'My First Data example', 200, 10, 700, 900 )
c1.SetFillColor( 18 )
DataHisto.Draw("E")
BkgpSigModel.Draw("E same")
c1.Update()
gROOT.GetListOfCanvases().Draw()
raw_input()