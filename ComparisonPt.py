import os, sys
#from MCdata import *
import ROOT
import matplotlib.pyplot as plt

pathToRootFile="Downloads/"
for Mass in [200]: #Looping over samples with different masses
	for Ctau in [1, 10, 100]: #Looping over samples with different lifetimes for a certain mass
	
		ch  = ROOT.TChain("preCutTree","preCutTree")		
		ch.Add(pathToRootFile+"Samples_d0BeamSpot/DisplacedTop_Run2_TopTree_Study_stopTobl_m" + str(Mass) + "_Ctau" + str(Ctau) + "_MuEl_NoBlinding_1(1).root") #Files of the samples
		#chh = ROOT.TChain("tree","tree")		
		#chh.Add(pathToRootFile+"DisplacedTop_Run2_TopTree_Study_stopTobl_m" + str(Mass) + "_Ctau" + str(Ctau) + "_MuEl_NoBlinding_1.root") #Files of the samples
		#hg_elept_cut = ROOT.TH1F("hg_mupt" + str(Ctau) + str(Mass),"muon p_{T}",100,0,800)
		#hg_eleeta_cut = ROOT.TH1F("hg_mueta","muon #eta",100,-4,4)
		#hg_eled0_cut = ROOT.TH1F("hg_mud0","muon |d_{0}|",100,0,10);

		pt_generated = []
		pt_reconstructed = [] 

		lvmu=ROOT.TLorentzVector()
		lvele=ROOT.TLorentzVector()

		lvmu_reco=ROOT.TLorentzVector()
		lvele_reco=ROOT.TLorentzVector()
		
		ii=0
		#jj=0
		nevents=ch.GetEntries()	
		#NEVENTS=chh.GetEntries()

		
		for iev in ch:
			ii+=1
#			if ii>500:
#				continue
		
			for iele_gen in range(0,iev.nMcParticles_pc):
				if abs(iev.type_mcParticle_pc[iele_gen]) == 11 and abs(iev.motherType_mcParticle_pc[iele_gen]) ==  1000006:
					lvele.SetPtEtaPhiE(iev.pt_mcParticle_pc[iele_gen],iev.eta_mcParticle_pc[iele_gen],iev.phi_mcParticle_pc[iele_gen],iev.E_mcParticle_pc[iele_gen])
					for iele_reco in range(0,iev.nElectrons_pc):
						if not iev.isId_electron_pc[iele_reco] == 0  and iev.eta_electron_pc[iele_reco]<2.4 and iev.pt_electron_pc[iele_reco]>42 and not iev.isIso_electron_pc[iele_reco] == 0:
							"""hg_eleeta_cut.Fill(iev.eta_electron_pc[iele_reco])
							hg_elept_cut.Fill(iev.pt_electron_pc[iele_reco])
							hg_eled0_cut.Fill(abs(iev.d0_electron_pc[iele_reco]))"""

							lvele_reco.SetPtEtaPhiE(iev.pt_electron_pc[iele_reco],iev.eta_electron_pc[iele_reco],iev.phi_electron_pc[iele_reco],iev.E_electron_pc[iele_reco])
							if (lvele.DeltaR(lvele_reco)>0.05):								
								pt_generated.append(iev.pt_mcParticle_pc[iele_gen])
								pt_reconstructed.append(iev.pt_electron_pc[iele_reco])
							#print pt_generated
							#print pt_reconstructed


		plt.plot(pt_generated, pt_generated, 'ro')
		#plt.axis([0, 6, 0, 20])
		plt.show()

"""		h_elept = ROOT.TH1F("h_mupt","muon p_{T}",100,0,800)
		h_eleeta = ROOT.TH1F("h_mueta","muon #eta",100,-4,4)
		h_eled0 = ROOT.TH1F("h_mud0","muon |d_{0}|",100,0,10);


		for iev_tr in chh:
			jj+=1
			
			for iele in range(0,iev_tr.nElectrons):
				h_eleeta.Fill(iev_tr.eta_electron[iele])
				h_elept.Fill(iev_tr.pt_electron[iele])
				h_eled0.Fill(abs(iev_tr.d0BeamSpot_electron[iele]))


		t3=ROOT.TCanvas()

		# create sub-pads and cd() to them, draw some histograms
		t3.Divide(2,2)
		t3.cd(1)
		h_elept.Draw()
		hg_elept_cut.Draw("same")
		hg_elept_cut.SetLineColor(2)
		h_elept.GetYaxis().SetTitle("Entries")
		h_elept.GetXaxis().SetTitle("p_{T} (GeV)")
		h_elept.SetTitle("electron p_{T}")
		t3.cd(2)
		h_eleeta.Draw()
		hg_eleeta_cut.Draw("same")
		hg_eleeta_cut.SetLineColor(2)
		h_eleeta.GetYaxis().SetTitle("Entries")
		h_eleeta.GetXaxis().SetTitle("#eta")
		h_eleeta.SetTitle("electron #eta")
		t3.cd(3)
		ROOT.gPad.SetLogy()
		h_eled0.Draw()
		hg_eled0_cut.Draw("same")
		hg_eled0_cut.SetLineColor(2)
		h_eled0.GetYaxis().SetTitle("Entries")
		h_eled0.GetXaxis().SetTitle("|d_{0}| (cm)")
		h_eled0.SetTitle("electron |d_{0}|")
		t3.Update()
		t3.Print("ComparisonTREE_PRECUTTREE_"+str(Ctau)+".pdf")"""




