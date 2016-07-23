import os, sys
#from MCdata import *
import ROOT

###############################
# pyroot file where I will make some histograms with/without cuts and efficiency
# 13 march 2016 by Kamal Saoucha, kamalsaou@hotmail.fr
#

#for ch in range(0,12)
#	"chain"+str(ch) = ROOT.TChain("preCutTree","preCutTree")

#ch  = ROOT.TChain("preCutTree","preCutTree")
pathToRootFile="Downloads/"
#ch.Add(pathToRootFile+"DisplacedTop_Run2_TopTree_Study_NP_overlay_stopTobl_m500_Ctau1_MuEl_2.root")
#200, 500, 800, 1100
#1, 10, 100

for Mass in [500]: #Looping over samples with different masses
	for Ctau in [1, 10, 100]: #Looping over samples with different lifetimes for a certain mass
		ch  = ROOT.TChain("preCutTree","preCutTree")		
		ch.Add(pathToRootFile+"Samples_d0BeamSpot/DisplacedTop_Run2_TopTree_Study_stopTobl_m" + str(Mass) + "_Ctau" + str(Ctau) + "_MuEl_NoBlinding_1(1).root") #Files of the samples

		outfile = ROOT.TFile("/home/ksaoucha/Documents/ResultingEff_m"+ str(Mass)+"_Ctau" + str(Ctau) + "_MuEl.root","recreate") # Creating a Rootfile where I stock the resulting efficiency curves
		outfile_FinalSelDistri = ROOT.TFile("/home/ksaoucha/Documents/ResultingFinalSelDistri_m"+ str(Mass)+"_Ctau" + str(Ctau) + "_MuEl.root","recreate")
# Booking some histograms, I clone the histograms of muons to make the ones of electrons because I want them to have the same scale so I can compare them later.

		# Histograms filled with pre-selected generated events for electrons and muons

		hg_mupt = ROOT.TH1F("hg_mupt","muon p_{T}",100,0,800)
		hg_mueta = ROOT.TH1F("hg_mueta","muon #eta",100,-4,4)
		hg_mud0 = ROOT.TH1F("hg_mud0","muon |d_{0}Beamspot|",100,0,10);
		hg_elept = hg_mupt.Clone("hg_elept")
		hg_eleeta = hg_mueta.Clone("hg_eleeta")
		hg_eled0 = hg_mud0.Clone("hg_eled0")

		# Histograms filled with reconstructed generated events for electrons and muons

		hg_mupt_cut = hg_mupt.Clone("hg_mupt_cut")
		hg_mueta_cut = hg_mueta.Clone("hg_mueta_cut")
		hg_mud0_cut = hg_mud0.Clone("hg_mud0_cut")
		hg_elept_cut = hg_mupt.Clone("hg_elept_cut")
		hg_eleeta_cut = hg_mueta.Clone("hg_eleeta_cut")
		hg_eled0_cut = hg_mud0.Clone("hg_eled0_cut")

		# Histograms filled with final-selected generated events for electrons and muons

		hg_mupt_cutIso = hg_mupt.Clone("hg_mupt_cutIso")
		hg_mueta_cutIso = hg_mueta.Clone("hg_mueta_cutIso")
		hg_mud0_cutIso = hg_mud0.Clone("hg_mud0_cutIso")
		hg_elept_cutIso = hg_mupt.Clone("hg_elept_cutIso")
		hg_eleeta_cutIso = hg_mueta.Clone("hg_eleeta_cutIso")
		hg_eled0_cutIso = hg_mud0.Clone("hg_eled0_cutIso")
		
		

		#hg_muN = ROOT.TH1F("hg_muN","muon #N",15,-0.5,14.5)
		#hg_eleN =  ROOT.TH1F("hg_eleN","electron #N",100,0,800)

		#h_muN = ROOT.TH1F("h_muN","muon #N",100,0,800)
		#h_eleN =  ROOT.TH1F("h_eleN","electron #N",100,0,800)

		hg_mudr = ROOT.TH1F("hg_mudr_genreco","muon #dr gen/reco",63,0,6.3)
		hg_eledr = ROOT.TH1F("hg_eledr_genreco","electron #dr gen/reco",63,0,6.3)
		# For bookkeeping


		ING=1


		# Lorentz vectors definition


		lvmu=ROOT.TLorentzVector()
		lvele=ROOT.TLorentzVector()

		lvmu_reco=ROOT.TLorentzVector()
		lvele_reco=ROOT.TLorentzVector()

		ii=0
		nevents=ch.GetEntries()

		# Start of the loop over the events

		for iev in ch:
			ii+=1
			#if ii>500:
			#	continue

# ------------------------------------------------------------------ MUONS -------------------------------------------------------------------------------------------

# Loop over muons - fill in lorentz vector and fill some histograms

			for imu_gen in range(0,iev.nMcParticles_pc) : # generated particles
				if abs(iev.type_mcParticle_pc[imu_gen]) == 13 and abs(iev.motherType_mcParticle_pc[imu_gen]) ==  1000006: # Condition that checks if the lepton is a muon AND if it's coming from a sTop
					lvmu.SetPtEtaPhiE(iev.pt_mcParticle_pc[imu_gen],iev.eta_mcParticle_pc[imu_gen],iev.phi_mcParticle_pc[imu_gen],iev.E_mcParticle_pc[imu_gen])
					passedCut_muon = False
					if iev.pt_mcParticle_pc[imu_gen]>10 and iev.v0_mcParticle_pc[imu_gen]<4 and abs(iev.vz_mcParticle_pc[imu_gen])<30 and abs(iev.d0BeamSpot_mcParticle_pc[imu_gen])>0.02: # Condition that checks if the generated particle has a pt>10 and is inside the detection region
						passedCut_muon = True
					if passedCut_muon == False:
						continue
					hg_mupt.Fill(iev.pt_mcParticle_pc[imu_gen])
					hg_mueta.Fill(iev.eta_mcParticle_pc[imu_gen])
					hg_mud0.Fill(abs(iev.d0BeamSpot_mcParticle_pc[imu_gen])) # Filling the histograms with events that passed the pre-selection

						#passedCut_muon = True
					if passedCut_muon==True:
						for imu_reco in range(0,iev.nMuons_pc):
							lvmu_reco.SetPtEtaPhiE(iev.pt_muon_pc[imu_reco],iev.eta_muon_pc[imu_reco],iev.phi_muon_pc[imu_reco],iev.E_muon_pc[imu_reco])
							hg_mudr.Fill(lvmu.DeltaR(lvmu_reco)) # Delta_R distribution						
							if (lvmu.DeltaR(lvmu_reco)>0.05): # Condition: the reco and the gen particle must be close to each others
								continue
							hg_mupt_cut.Fill(iev.pt_mcParticle_pc[imu_gen])
							hg_mueta_cut.Fill(iev.eta_mcParticle_pc[imu_gen])
							hg_mud0_cut.Fill(abs(iev.d0BeamSpot_mcParticle_pc[imu_gen])) # Filling close reconstructed events in histograms 
										
							passedCut_id_iso_muon = False
							if not iev.isId_muon_pc[imu_reco] == 0 and iev.pt_muon_pc[imu_reco]>40 and not iev.isIso_muon_pc[imu_reco] == 0 and abs(iev.eta_muon_pc[imu_reco])<2.4: # Condition: reconstructed muon must have a pt>25 and must be identified and isolated 
							
								passedCut_id_iso_muon = True

							if passedCut_id_iso_muon==True:

								hg_mupt_cutIso.Fill(iev.pt_mcParticle_pc[imu_gen])	
								hg_mueta_cutIso.Fill(iev.eta_mcParticle_pc[imu_gen])	
								hg_mud0_cutIso.Fill(abs(iev.d0BeamSpot_mcParticle_pc[imu_gen]))
							break		

# ----------------------------------------------------------------- ELECTRONS ---------------------------------------------------------------------------------------

# Loop over electrons - fill in lorentz vector and fill some histograms

	
			for iele_gen in range(0,iev.nMcParticles_pc):
				if abs(iev.type_mcParticle_pc[iele_gen]) == 11 and abs(iev.motherType_mcParticle_pc[iele_gen]) ==  1000006:
					lvele.SetPtEtaPhiE(iev.pt_mcParticle_pc[iele_gen],iev.eta_mcParticle_pc[iele_gen],iev.phi_mcParticle_pc[iele_gen],iev.E_mcParticle_pc[iele_gen])
				
					passedCut_electron = False
					if iev.pt_mcParticle_pc[iele_gen]>10 and iev.v0_mcParticle_pc[iele_gen]<4 and abs(iev.vz_mcParticle_pc[iele_gen])<30 and abs(iev.d0BeamSpot_mcParticle_pc[imu_gen])>0.02:
						passedCut_electron = True
					if passedCut_electron == False:
						continue
					hg_eleeta.Fill(iev.eta_mcParticle_pc[iele_gen])
					hg_elept.Fill(iev.pt_mcParticle_pc[iele_gen])
					hg_eled0.Fill(abs(iev.d0BeamSpot_mcParticle_pc[iele_gen]))
			
					if passedCut_electron == True:
						for iele_reco in range(0,iev.nElectrons_pc):
							lvele_reco.SetPtEtaPhiE(iev.pt_electron_pc[iele_reco],iev.eta_electron_pc[iele_reco],iev.phi_electron_pc[iele_reco],iev.E_electron_pc[iele_reco])
							hg_eledr.Fill(lvele.DeltaR(lvele_reco))
							if (lvele.DeltaR(lvele_reco)>0.05):
								continue
							hg_eleeta_cut.Fill(iev.eta_mcParticle_pc[iele_gen])
							hg_elept_cut.Fill(iev.pt_mcParticle_pc[iele_gen])
							hg_eled0_cut.Fill(abs(iev.d0BeamSpot_mcParticle_pc[iele_gen]))
						
							passedCut_id_iso_electron = False
							if not iev.isId_electron_pc[iele_reco] == 0 and iev.pt_electron_pc[iele_reco]>42 and not iev.isIso_electron_pc[iele_reco] == 0 and abs(iev.eta_electron_pc[iele_reco])<2.4:
								passedCut_id_iso_electron = True

							if passedCut_id_iso_electron==True:
										
								hg_elept_cutIso.Fill(iev.pt_mcParticle_pc[iele_gen])	
								hg_eleeta_cutIso.Fill(iev.eta_mcParticle_pc[iele_gen])	
								hg_eled0_cutIso.Fill(abs(iev.d0BeamSpot_mcParticle_pc[iele_gen]))
							break



		# END OF THE LOOPO !


		# create canvas
		t3=ROOT.TCanvas()

		# create sub-pads and cd() to them, draw some histograms
		t3.Divide(3,2)
		t3.cd(1)
		hg_mupt.Draw()
		hg_mupt_cut.Draw("same")
		hg_mupt_cutIso.Draw("same")
		hg_mupt_cut.SetLineColor(2)
		hg_mupt_cutIso.SetLineColor(8)
		leg1 = ROOT.TLegend(0.7,0.4,0.9,0.5)
		leg1.SetFillColor(19)
		leg1.SetBorderSize(1)
		leg1.AddEntry(hg_mupt,"Preselected","l")
		leg1.AddEntry(hg_mupt_cut,"Reconstructed","l")
		leg1.AddEntry(hg_mupt_cutIso,"Final Selected","l")
		leg1.Draw()
		hg_mupt.GetYaxis().SetTitle("Entries")
		hg_mupt.GetXaxis().SetTitle("p_{T} (GeV)")
		t3.cd(2)
		hg_mueta.Draw()
		hg_mueta_cut.Draw("same")
		hg_mueta_cutIso.Draw("same")
		hg_mueta_cut.SetLineColor(2)
		hg_mueta_cutIso.SetLineColor(8)
		leg2 = ROOT.TLegend(0.7,0.4,0.9,0.5)
		leg2.SetFillColor(19)
		leg2.SetBorderSize(1)
		leg2.AddEntry(hg_mueta,"Preselected","l")
		leg2.AddEntry(hg_mueta_cut,"Reconstructed","l")
		leg2.AddEntry(hg_mueta_cutIso,"Final Selected","l")
		leg2.Draw()
		hg_mueta.GetYaxis().SetTitle("Entries")
		hg_mueta.GetXaxis().SetTitle("#eta")
		t3.cd(3)
		ROOT.gPad.SetLogy()
		hg_mud0.Draw()
		hg_mud0_cut.Draw("same")
		hg_mud0_cutIso.Draw("same")
		hg_mud0_cut.SetLineColor(2)
		hg_mud0_cutIso.SetLineColor(8)
		leg3 = ROOT.TLegend(0.7,0.4,0.9,0.5)
		leg3.SetFillColor(19)
		leg3.SetBorderSize(1)
		leg3.AddEntry(hg_mud0,"Preselected","l")
		leg3.AddEntry(hg_mud0_cut,"Reconstructed","l")
		leg3.AddEntry(hg_mud0_cutIso,"Final Selected","l")
		leg3.Draw()
		hg_mud0.GetYaxis().SetTitle("Entries")
		hg_mud0.GetXaxis().SetTitle("|d_{0}Beamspot| (cm)")
		t3.cd(4)
		hg_elept.Draw()
		hg_elept_cut.Draw("same")
		hg_elept_cutIso.Draw("same")
		hg_elept_cut.SetLineColor(2)
		hg_elept_cutIso.SetLineColor(8)
		leg4 = ROOT.TLegend(0.7,0.4,0.9,0.5)
		leg4.SetFillColor(19)
		leg4.SetBorderSize(1)
		leg4.AddEntry(hg_elept,"Preselected","l")
		leg4.AddEntry(hg_elept_cut,"Reconstructed","l")
		leg4.AddEntry(hg_elept_cutIso,"Final Selected","l")
		leg4.Draw()
		hg_elept.GetYaxis().SetTitle("Entries")
		hg_elept.GetXaxis().SetTitle("p_{T} (GeV)")
		hg_elept.SetTitle("electron p_{T}")
		t3.cd(5)
		hg_eleeta.Draw()
		hg_eleeta_cut.Draw("same")
		hg_eleeta_cutIso.Draw("same")
		hg_eleeta_cut.SetLineColor(2)
		hg_eleeta_cutIso.SetLineColor(8)
		leg5 = ROOT.TLegend(0.7,0.4,0.9,0.5)
		leg5.SetFillColor(19)
		leg5.SetBorderSize(1)
		leg5.AddEntry(hg_eleeta,"Preselected","l")
		leg5.AddEntry(hg_eleeta_cut,"Reconstructed","l")
		leg5.AddEntry(hg_eleeta_cutIso,"Final Selected","l")
		leg5.Draw()
		hg_eleeta.GetYaxis().SetTitle("Entries")
		hg_eleeta.GetXaxis().SetTitle("#eta")
		hg_eleeta.SetTitle("electron #eta")
		t3.cd(6)
		ROOT.gPad.SetLogy()
		hg_eled0.Draw()
		hg_eled0_cut.Draw("same")
		hg_eled0_cutIso.Draw("same")
		hg_eled0_cut.SetLineColor(2)
		hg_eled0_cutIso.SetLineColor(8)
		leg6 = ROOT.TLegend(0.7,0.4,0.9,0.5)
		leg6.SetFillColor(19)
		leg6.SetBorderSize(1)
		leg6.AddEntry(hg_eled0,"Preselected","l")
		leg6.AddEntry(hg_eled0_cut,"Reconstructed","l")
		leg6.AddEntry(hg_eled0_cutIso,"Final Selected","l")
		leg6.Draw()
		hg_eled0.GetYaxis().SetTitle("Entries")
		hg_eled0.GetXaxis().SetTitle("|d_{0}Beamspot| (cm)")
		hg_eled0.SetTitle("electron |d_{0}Beamspot|")
		t3.Update()
		t3.Print("TOGETHERPreVsRecoVsSelecDistr_m"+str(Mass)+"_Ctau"+ str(Ctau)+".pdf") # TCanvas::Print also can make .pdf or .root/.C plots

		t3_cut=ROOT.TCanvas()
		t3_cut.Divide(2,2)
		t3_cut.cd(1)
		ROOT.gPad.SetGridy()
		hg_mupt_cut.Rebin(ING)
		hg_mupt_cutIso.Rebin(ING)
		h_mupt_eff = ROOT.TEfficiency(hg_mupt_cutIso,hg_mupt_cut)
		h_mupt_eff.Draw("AP") # A draw axis, P draw points
		ROOT.gPad.Update()
		Eff_mupt_eff = h_mupt_eff.GetPaintedGraph()
		Eff_mupt_eff.SetMaximum(1)
		Eff_mupt_eff.SetMinimum(0)
		ROOT.gPad.Update()
		h_mupt_eff.SetTitle("Sel. Eff. Muon; p_{T} (GeV); Eff.")
		t3_cut.cd(2)
		ROOT.gPad.SetGridy()
		hg_elept_cut.Rebin(ING)
		hg_elept_cutIso.Rebin(ING)
		h_elept_eff = ROOT.TEfficiency(hg_elept_cutIso,hg_elept_cut)
		h_elept_eff.Draw("AP")
		ROOT.gPad.Update()
		Eff_elept_eff = h_elept_eff.GetPaintedGraph()
		Eff_elept_eff.SetMaximum(1)
		Eff_elept_eff.SetMinimum(0)
		ROOT.gPad.Update()
		h_elept_eff.SetTitle("Sel. Eff. Electron; p_{T} (GeV); Eff.")
		t3_cut.cd(3)
		ROOT.gPad.SetGridy()
		hg_mud0.Rebin(ING)
		hg_mud0_cut.Rebin(ING)
		hg_mud0_eff = ROOT.TEfficiency(hg_mud0_cut,hg_mud0)
		hg_mud0_eff.Draw("AP")
		ROOT.gPad.Update()
		Eff_mud0_eff = hg_mud0_eff.GetPaintedGraph()
		Eff_mud0_eff.SetMaximum(1)
		Eff_mud0_eff.SetMinimum(0)
		Eff_mud0_eff.GetXaxis().SetRangeUser(0,4)
		ROOT.gPad.Update()
		hg_mud0_eff.SetTitle("Reco. Eff. Muon; |d_{0}Beamspot| (cm); Eff.")
		t3_cut.cd(4)
		ROOT.gPad.SetGridy()
		hg_eled0.Rebin(ING)
		hg_eled0_cut.Rebin(ING)
		hg_eled0_eff = ROOT.TEfficiency(hg_eled0_cut,hg_eled0)
		hg_eled0_eff.Draw("AP")
		ROOT.gPad.Update()
		Eff_eled0_eff = hg_eled0_eff.GetPaintedGraph()
		Eff_eled0_eff.SetMaximum(1)
		Eff_eled0_eff.SetMinimum(0)
		Eff_eled0_eff.GetXaxis().SetRangeUser(0,4)
		ROOT.gPad.Update()
		hg_eled0_eff.SetTitle("Reco. Eff. Electron; |d_{0}Beamspot| (cm); Eff.")
		t3_cut.Update()
		t3_cut.Print("Parametrization_Sample_m"+str(Mass)+"_Ctau"+ str(Ctau)+".pdf")

		
		outfile.cd() # Filling the rootfile with efficiency curves
		hg_mud0_eff.Write()
		hg_eled0_eff.Write()
		h_mupt_eff.Write()
		h_elept_eff.Write()
		outfile_FinalSelDistri.cd()
		hg_mupt_cutIso.Write()
		hg_mud0_cutIso.Write()
		hg_elept_cutIso.Write()
		hg_eled0_cutIso.Write()

"""		# create canvas
		t3=ROOT.TCanvas()

		# create sub-pads and cd() to them, draw some histograms
		t3.Divide(3,2)
		t3.cd(1)
		hg_mupt_cut.Draw()
		hg_mupt_cutIso.Draw("same")
		hg_mupt_cut.SetLineColor(2)
		hg_mupt_cutIso.SetLineColor(8)
		hg_mupt_cut.GetYaxis().SetTitle("Entries")
		hg_mupt_cut.GetXaxis().SetTitle("p_{T} (GeV)")
		t3.cd(2)
		hg_mueta_cut.Draw()
		hg_mueta_cutIso.Draw("same")
		hg_mueta_cut.SetLineColor(2)
		hg_mueta_cutIso.SetLineColor(8)
		hg_mueta_cut.GetYaxis().SetTitle("Entries")
		hg_mueta_cut.GetXaxis().SetTitle("#eta")
		t3.cd(3)
		ROOT.gPad.SetLogy()
		hg_mud0_cut.Draw()
		hg_mud0_cutIso.Draw("same")
		hg_mud0_cut.SetLineColor(2)
		hg_mud0_cutIso.SetLineColor(8)
		hg_mud0_cut.GetYaxis().SetTitle("Entries")
		hg_mud0_cut.GetXaxis().SetTitle("|d_{0}Beamspot| (cm)")
		t3.cd(4)
		hg_elept_cut.Draw()
		hg_elept_cutIso.Draw("same")
		hg_elept_cut.SetLineColor(2)
		hg_elept_cutIso.SetLineColor(8)
		hg_elept_cut.GetYaxis().SetTitle("Entries")
		hg_elept_cut.GetXaxis().SetTitle("p_{T} (GeV)")
		hg_elept_cut.SetTitle("electron p_{T}")
		t3.cd(5)
		hg_eleeta_cut.Draw()
		hg_eleeta_cutIso.Draw("same")
		hg_eleeta_cut.SetLineColor(2)
		hg_eleeta_cutIso.SetLineColor(8)
		hg_eleeta_cut.GetYaxis().SetTitle("Entries")
		hg_eleeta_cut.GetXaxis().SetTitle("#eta")
		hg_eleeta_cut.SetTitle("electron #eta")
		t3.cd(6)
		ROOT.gPad.SetLogy()
		hg_eled0_cut.Draw()
		hg_eled0_cutIso.Draw("same")
		hg_eled0_cut.SetLineColor(2)
		hg_eled0_cutIso.SetLineColor(8)
		hg_eled0_cut.GetYaxis().SetTitle("Entries")
		hg_eled0_cut.GetXaxis().SetTitle("|d_{0}Beamspot| (cm)")
		hg_eled0_cut.SetTitle("electron |d_{0}Beamspot|")
		t3.Update()
		t3.Print("RecoVsSelDistr_m"+str(Mass)+"_Ctau"+ str(Ctau)+".pdf") # TCanvas::Print also can make .pdf or .root/.C plots

		t2=ROOT.TCanvas()

		# create sub-pads and cd() to them, draw some histograms
		t2.Divide(2,1)
		t2.cd(1)
		ROOT.gPad.SetLogy()
		#hg_muN.Draw()
		hg_mudr.Draw()
		hg_mupt_cut.SetLineColor(2)
		hg_mudr.GetYaxis().SetTitle("Entries")
		hg_mudr.GetXaxis().SetTitle("dr")
		t2.cd(2)
		ROOT.gPad.SetLogy()
		hg_eledr.Draw()
		hg_mueta_cut.SetLineColor(2)
		hg_eledr.GetYaxis().SetTitle("Entries")
		hg_eledr.GetXaxis().SetTitle("dr")
		t2.Update()
		t2.Print("MCplotDr_m"+str(Mass)+"_Ctau"+ str(Ctau)+".pdf")
		t3=ROOT.TCanvas()
			       
		# create sub-pads and cd() to them, draw some histograms
		t3.Divide(2,2)
		t3.cd(1)
		ROOT.gPad.SetGridy()
		hg_mupt.Rebin(ING)
		hg_mupt_cut.Rebin(ING)
		hg_mupt_eff = ROOT.TEfficiency(hg_mupt_cut,hg_mupt)
		hg_mupt_eff.Draw("AP") # A draw axis, P draw points
		hg_mupt_eff.SetTitle("Reco. Eff. Muon; p_{T} (GeV); Eff.")
		t3.cd(2)
		ROOT.gPad.SetGridy()
		hg_mueta.Rebin(ING)
		hg_mueta_cut.Rebin(ING)
		hg_mueta_eff = ROOT.TEfficiency(hg_mueta_cut,hg_mueta)
		hg_mueta_eff.Draw("AP")
		hg_mueta_eff.SetTitle("Reco. Eff. Muon; #eta; Eff.")
		t3.cd(4)
		ROOT.gPad.SetGridy()
		hg_elept.Rebin(ING)
		hg_elept_cut.Rebin(ING)
		hg_elept_eff = ROOT.TEfficiency(hg_elept_cut,hg_elept)
		hg_elept_eff.Draw("AP")
		hg_elept_eff.SetTitle("Reco. Eff. Electron; p_{T} (GeV); Eff.")
		t3.cd(5)
		ROOT.gPad.SetGridy()
		hg_eleeta.Rebin(ING)
		hg_eleeta_cut.Rebin(ING)
		hg_eleeta_eff = ROOT.TEfficiency(hg_eleeta_cut,hg_eleeta)
		hg_eleeta_eff.Draw("AP")
		hg_eleeta_eff.SetTitle("Reco. Eff. Electron; #eta; Eff.")
		t3.cd(4)
		ROOT.gPad.SetGridy()
		hg_eled0.Rebin(ING)
		hg_eled0_cut.Rebin(ING)
		hg_eled0_eff = ROOT.TEfficiency(hg_eled0_cut,hg_eled0)
		hg_eled0_eff.Draw("AP")
		ROOT.gPad.Update()
		Eff_eled0_eff = hg_eled0_eff.GetPaintedGraph()
		Eff_eled0_eff.SetMaximum(1)
		Eff_eled0_eff.SetMinimum(0)
		Eff_eled0_eff.GetXaxis().SetRangeUser(0,4)
		ROOT.gPad.Update()
		hg_eled0_eff.SetTitle("Reco. Eff. Electron; |d_{0}Beamspot| (cm); Eff.")
		t3.Update()
		t3.Print("EffReco_m"+str(Mass)+"_Ctau"+ str(Ctau)+".pdf")

		t3=ROOT.TCanvas()
			       
		t3.Divide(3,2)
		t3.cd(1)
		ROOT.gPad.SetGridy()
		hg_mupt_cutIso.Rebin(ING)
		h_mupt_eff = ROOT.TEfficiency(hg_mupt_cutIso,hg_mupt_cut)
		h_mupt_eff.Draw("AP") # A draw axis, P draw points
		ROOT.gPad.Update()
		Eff_mupt_eff = h_mupt_eff.GetPaintedGraph()
		Eff_mupt_eff.SetMaximum(1)
		Eff_mupt_eff.SetMinimum(0)
		ROOT.gPad.Update()
		h_mupt_eff.SetTitle("Sel. Eff. Muon; p_{T} (GeV); Eff.")
		t3.cd(2)
		ROOT.gPad.SetGridy()
		hg_mueta_cutIso.Rebin(ING)
		h_mueta_eff = ROOT.TEfficiency(hg_mueta_cutIso,hg_mueta_cut)
		h_mueta_eff.Draw("AP")
		h_mueta_eff.SetTitle("Sel. Eff. Muon; #eta; Eff.")
		t3.cd(3)
		ROOT.gPad.SetGridy()
		hg_mud0_cutIso.Rebin(ING)
		h_mud0_eff = ROOT.TEfficiency(hg_mud0_cutIso,hg_mud0_cut)
		h_mud0_eff.Draw("AP")
		h_mud0_eff.SetTitle("Sel. Eff. Muon; |d_{0}Beamspot| (cm); Eff.")
		t3.cd(2)
		ROOT.gPad.SetGridy()
		hg_elept_cutIso.Rebin(ING)
		h_elept_eff = ROOT.TEfficiency(hg_elept_cutIso,hg_elept_cut)
		h_elept_eff.Draw("AP")
		ROOT.gPad.Update()
		Eff_elept_eff = h_elept_eff.GetPaintedGraph()
		Eff_elept_eff.SetMaximum(1)
		Eff_elept_eff.SetMinimum(0)
		ROOT.gPad.Update()
		h_elept_eff.SetTitle("Sel. Eff. Electron; p_{T} (GeV); Eff.")
		t3.cd(5)
		ROOT.gPad.SetGridy()
		hg_eleeta_cutIso.Rebin(ING)
		h_eleeta_eff = ROOT.TEfficiency(hg_eleeta_cutIso,hg_eleeta_cut)
		h_eleeta_eff.Draw("AP")
		h_eleeta_eff.SetTitle("Sel. Eff. Electron; #eta; Eff.")
		t3.cd(6)
		ROOT.gPad.SetGridy()
		hg_eled0_cutIso.Rebin(ING)
		h_eled0_eff = ROOT.TEfficiency(hg_eled0_cutIso,hg_eled0_cut)
		h_eled0_eff.Draw("AP")
		h_eled0_eff.SetTitle("Sel. Eff. Electron; |d_{0}Beamspot| (cm); Eff.")
		t3.Update()
		t3.Print("Parametrization_Sample_m"+str(Mass)+"_Ctau"+ str(Ctau)+".pdf")
		# -------------------------------------------------------------------------------#"""


