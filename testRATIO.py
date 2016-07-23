import os, sys
#from MCdata import *
import ROOT
from FreyaLib_modified import *
###############################
# pyroot file where I will make some histograms with/without cuts and efficiency
# 13 march 2016 by Kamal Saoucha, kamalsaou@hotmail.fr
#
ING = 5
EstiList = []
RealYieldList = []
# ----------Tab later------------#
#200, 500, 800, 1100
#1, 10, 100
for Mass in [500]:
	for Ctau in [1, 10, 100]:
		pathToRootFile="Downloads/"
	#	inputEfficiency = ROOT.TFile("/home/ksaoucha/Documents/ResultingEff_m"+ str(Mass)+"_Ctau" + str(Ctau) + "_MuEl.root","read") # Closuretest sample i
		inputEfficiency = ROOT.TFile("/home/ksaoucha/Documents/ResultingEff_All_BeamSpot.root","read") # Closure test with mean parametrization
		inputFinalSelDistri = ROOT.TFile("/home/ksaoucha/Documents/ResultingFinalSelDistri_m"+ str(Mass)+"_Ctau" + str(Ctau) + "_MuEl.root","read") # Fi
		rootkeys_FSD = inputFinalSelDistri.GetListOfKeys()
		distrinames = []
		for Key in rootkeys_FSD:
			distrinames.append(Key.GetName())
		print distrinames
		hg_mupt_cutIso = inputFinalSelDistri.Get(distrinames[0])
		hg_mud0_cutIso = inputFinalSelDistri.Get(distrinames[1])
		hg_elept_cutIso = inputFinalSelDistri.Get(distrinames[2])
		hg_eled0_cutIso = inputFinalSelDistri.Get(distrinames[3])


		inputNtuples = ROOT.TChain("preCutTree","preCutTree")		
		inputNtuples.Add(pathToRootFile+"Samples_d0BeamSpot/DisplacedTop_Run2_TopTree_Study_stopTobl_m" + str(Mass) + "_Ctau" + str(Ctau) + "_MuEl_NoBlinding_1(1).root") 
		rootkeys = inputEfficiency.GetListOfKeys()
		#rootkeys = inputNtuples.GetListOfKeys()
		histnames = []
		for key in rootkeys:
			histnames.append(key.GetName())
		print histnames
		
		pt_generated = []
		pt_reconstructed = [] 
		
		hg_mupt = ROOT.TH1F("hg_mupt","muon p_{T}",100,0,1200)
		hg_mueta = ROOT.TH1F("hg_mueta","muon #eta",100,-4,4)
		hg_mud0 = ROOT.TH1F("hg_mud0","muon |d_{0}|",100,0,2);
		hg_elept = hg_mupt.Clone("hg_elept")
		hg_eleeta = hg_mueta.Clone("hg_eleeta")
		hg_eled0 = hg_mud0.Clone("hg_eled0")
		
	#---Loop over event ---#
		ii=0
		nevents=inputNtuples.GetEntries()
		for iev in inputNtuples:
			ii+=1
			#if ii>500:
			#	continue
			W_mud0=0
			W_mupt=0
			W_eled0=0
			W_elept=0
			n_gen_ele= 0
			n_gen_mu = 0
			for i_gen in range(0,iev.nMcParticles_pc) :
				if abs(iev.motherType_mcParticle_pc[i_gen]) ==  1000006 and abs(iev.d0BeamSpot_mcParticle_pc[i_gen])<10 and iev.pt_mcParticle_pc[i_gen]>10 and iev.v0_mcParticle_pc[i_gen]<4 and abs(iev.vz_mcParticle_pc[i_gen])<30 and abs(iev.d0BeamSpot_mcParticle_pc[i_gen])>0.02:
					if abs(iev.type_mcParticle_pc[i_gen]) == 13:
						n_gen_mu+=1
						print " n_gen_mu = ", n_gen_mu, " in nMcparticles_pc ", i_gen, " in event number ", ii
					if abs(iev.type_mcParticle_pc[i_gen]) == 11:
						n_gen_ele+=1
						print " n_gen_ele = ", n_gen_ele, " in nMcparticles_pc ", i_gen, " in event number ", ii



			if n_gen_ele != 1 and n_gen_mu !=1:
				continue
			for i_gen in range(0,iev.nMcParticles_pc) :
				if abs(iev.motherType_mcParticle_pc[i_gen]) ==  1000006 and abs(iev.d0BeamSpot_mcParticle_pc[i_gen])<10 and iev.pt_mcParticle_pc[i_gen]>10 and iev.v0_mcParticle_pc[i_gen]<4 and abs(iev.vz_mcParticle_pc[i_gen])<30 and abs(iev.d0BeamSpot_mcParticle_pc[i_gen])>0.02:
					if abs(iev.type_mcParticle_pc[i_gen]) == 13 or abs(iev.type_mcParticle_pc[i_gen]) == 11:
						hg_mud0_eff=inputEfficiency.Get(histnames[0])
						h_mupt_eff=inputEfficiency.Get(histnames[2])
						mud0_value = abs(iev.d0BeamSpot_mcParticle_pc[i_gen])
						mupt_value = iev.pt_mcParticle_pc[i_gen]
						Bin_mud0_value = hg_mud0_eff.GetTotalHistogram().FindBin(mud0_value)
						Bin_mupt_value = h_mupt_eff.GetTotalHistogram().FindBin(mupt_value)
						W_mud0 = hg_mud0_eff.GetEfficiency(Bin_mud0_value)
						W_mupt = h_mupt_eff.GetEfficiency(Bin_mupt_value)
						#print "mud0_value = ",mud0_value
						#print "mupt_value = ",mupt_value

						#if abs(iev.type_mcParticle_pc[i_gen]) == 11:
						hg_eled0_eff=inputEfficiency.Get(histnames[1])
						h_elept_eff=inputEfficiency.Get(histnames[3])
						eled0_value = abs(iev.d0BeamSpot_mcParticle_pc[i_gen])
						elept_value = iev.pt_mcParticle_pc[i_gen]
						Bin_eled0_value = hg_eled0_eff.GetTotalHistogram().FindBin(eled0_value)
						Bin_elept_value = h_elept_eff.GetTotalHistogram().FindBin(elept_value)
						W_eled0 = hg_eled0_eff.GetEfficiency(Bin_eled0_value)
						W_elept = h_elept_eff.GetEfficiency(Bin_elept_value)
						#print "eled0_value = ",eled0_value
						#print "elept_value = ",elept_value

					W_event = W_mud0*W_mupt*W_eled0*W_elept

					if abs(iev.type_mcParticle_pc[i_gen]) == 13 :
						hg_mupt.Fill(iev.pt_mcParticle_pc[i_gen], W_event)
						hg_mueta.Fill(iev.eta_mcParticle_pc[i_gen], W_event)
						hg_mud0.Fill(abs(iev.d0BeamSpot_mcParticle_pc[i_gen]), W_event)
					if abs(iev.type_mcParticle_pc[i_gen]) == 11 :
						hg_eleeta.Fill(iev.eta_mcParticle_pc[i_gen], W_event)
						hg_elept.Fill(iev.pt_mcParticle_pc[i_gen], W_event)
						hg_eled0.Fill(abs(iev.d0BeamSpot_mcParticle_pc[i_gen]), W_event)
						#continue
						#print "eled0_value = ",eled0_value
						#print "elept_value = ",elept_value
					#else :
					#	print "NO ELECTRON IN THIS MCnumber"
					
				#for i_gen in range(0,iev.nMcParticles_pc): # Give weight to each generated event
				#	if abs(iev.type_mcParticle_pc[i_gen]) == 13 and abs(iev.motherType_mcParticle_pc[i_gen]) ==  1000006:
				#		hg_mupt.Fill(iev.pt_mcParticle_pc[imu_gen], W_event)
				#		hg_mueta.Fill(iev.eta_mcParticle_pc[imu_gen], W_event)
				#		hg_mud0.Fill(abs(iev.d0BeamSpot_mcParticle_pc[imu_gen]), W_event)

				#for iele_gen in range(0,iev.nMcParticles_pc):
				#	if abs(iev.type_mcParticle_pc[iele_gen]) == 11 and abs(iev.motherType_mcParticle_pc[iele_gen]) ==  1000006:
				#		hg_eleeta.Fill(iev.eta_mcParticle_pc[iele_gen], W_event)
				#		hg_elept.Fill(iev.pt_mcParticle_pc[iele_gen], W_event)
				#		hg_eled0.Fill(abs(iev.d0BeamSpot_mcParticle_pc[iele_gen]), W_event)
		#				lvele.SetPtEtaPhiE(iev.pt_mcParticle_pc[iele_gen],iev.eta_mcParticle_pc[iele_gen],iev.phi_mcParticle_pc[iele_gen],iev.E_mcParticle_pc[iele_gen]
		#				for iele_reco in range(0,iev.nElectrons):
		#					lvele_reco.SetPtEtaPhiE(iev.pt_electron[iele_reco],iev.eta_electron[iele_reco],iev.phi_electron[iele_reco],iev.E_electron[iele_reco])
		#					if (lvele.DeltaR(lvele_reco)>0.05):
		#						pt_generated.append(iev.pt_mcParticle_pc())
		#						pt_reconstructed.append(iev.pt_electron())
		#					print pt_generated
		#					print pt_reconstructed




# -------------------------------------------------------- Filling histograms with reco/selected particles with FULL CMS SIMULATION -----------------------------+


		chh = ROOT.TChain("tree","tree")		
		chh.Add(pathToRootFile+"Samples_d0BeamSpot/DisplacedTop_Run2_TopTree_Study_stopTobl_m" + str(Mass) + "_Ctau" + str(Ctau) + "_MuEl_NoBlinding_1(1).root") #Files of the samples
		nevents=chh.GetEntries()

		h_mupt = ROOT.TH1F("h_mupt","muon p_{T}",100,0,1200)
		h_mueta = ROOT.TH1F("h_mueta","muon #eta",100,-4,4)
		h_mud0 = ROOT.TH1F("h_mud0","muon |d_{0}|",100,0,2);
		h_elept = h_mupt.Clone("h_elept")
		h_eleeta = h_mueta.Clone("h_eleeta")
		h_eled0 = h_mud0.Clone("h_eled0")

		for iev in chh:
			ii+=1
			n_gen_ele= 0
			n_gen_mu = 0


#			for i_reco in range(0,iev.nMuons) :
#				h_mupt.Fill(iev.pt_muon[i_reco])
#			 	h_mueta.Fill(iev.eta_muon[i_reco])
#				h_mud0.Fill(abs(iev.d0BeamSpot_muon[i_reco]))
#
#			for i_reco in range(0,iev.nElectrons) :
#				h_eleeta.Fill(iev.eta_electron[i_reco])
#				h_elept.Fill(iev.pt_electron[i_reco])
#				h_eled0.Fill(abs(iev.d0BeamSpot_electron[i_reco]))
			for i_gen in range(0,iev.nMcParticles) :
				if abs(iev.motherType_mcParticle[i_gen]) ==  1000006 and abs(iev.d0BeamSpot_mcParticle[i_gen])>0.02:# and abs(iev.d0BeamSpot_mcParticle[i_gen])<10 and iev.pt_mcParticle[i_gen]>10:
					if abs(iev.type_mcParticle[i_gen]) == 13:
						n_gen_mu+=1
					if abs(iev.type_mcParticle[i_gen]) == 11:
						n_gen_ele+=1

			if n_gen_ele != 1 and n_gen_mu !=1:
				continue

			for i_gen in range(0,iev.nMcParticles) :
				if abs(iev.motherType_mcParticle[i_gen]) ==  1000006 and abs(iev.d0BeamSpot_mcParticle[i_gen])>0.02:# and abs(iev.d0BeamSpot_mcParticle[i_gen])<10 and iev.pt_mcParticle[i_gen]>10:
					if abs(iev.type_mcParticle[i_gen]) == 13:
						h_mupt.Fill(iev.pt_mcParticle[i_gen])
						h_mueta.Fill(iev.eta_mcParticle[i_gen])
						h_mud0.Fill(abs(iev.d0BeamSpot_mcParticle[i_gen]))

					if abs(iev.type_mcParticle[i_gen]) == 11:
						h_eleeta.Fill(iev.eta_mcParticle[i_gen])
						h_elept.Fill(iev.pt_mcParticle[i_gen])
						h_eled0.Fill(abs(iev.d0BeamSpot_mcParticle[i_gen]))


#---------------------------------------------------------------------- Comparison of pt on gen level and on reco level --------------------------------------------+

#---------------------------------------------------------------------- Histograms comparison ----------------------------------------------------------------------+

		# create canvas
		t3=ROOT.TCanvas()

		# create sub-pads and cd() to them, draw some histograms
		#t3.Divide(3,2)
		# Muons
		t3.Divide(1,2)
		t3.cd(1)
		hg_mupt.Draw()
		h_mupt.Draw("samePE")
		hg_mupt_cutIso.Draw("samePE")
		hg_mupt.SetLineColor(2)
		h_mupt.GetYaxis().SetTitle("Entries")
		h_mupt.GetXaxis().SetTitle("p_{T} (GeV)")
		leg1 = ROOT.TLegend(0.7,0.4,0.9,0.5)
		leg1.SetFillColor(19)
		leg1.SetBorderSize(1)
		leg1.AddEntry(h_mupt,"Full CMS Simu.","l")
		leg1.AddEntry(hg_mupt,"Parametrization","l")
		leg1.Draw()
		t3.cd(2)
		ROOT.gPad.SetGridy()
		Ratio_mupt = makeRatio(hg_mupt,h_mupt)
		Ratio_mupt.GetYaxis().SetTitle("Ratio")
		Ratio_mupt.GetXaxis().SetTitle("p_{T} (GeV)")
		Ratio_mupt.Draw()
		ROOT.gPad.Update()
		Ratio_mupt.SetMaximum(5)
		Ratio_mupt.SetMinimum(0)
		t3.Update()
		t3.Print("TESTRatioDistribComp_BEAMSPOT_m"+str(Mass)+"_Ctau"+ str(Ctau)+"_mupt.pdf")

		"""t3=ROOT.TCanvas()
		t3.Divide(1,2)
		t3.cd(1)
		h_mueta.Draw("PE")
		hg_mueta.Draw("same")
		hg_mueta.SetLineColor(2)
		h_mueta.GetYaxis().SetTitle("Entries")
		h_mueta.GetXaxis().SetTitle("#eta")
		leg2 = ROOT.TLegend(0.7,0.4,0.9,0.5)
		leg2.SetFillColor(19)
		leg2.SetBorderSize(1)
		leg2.AddEntry(h_mueta,"Full CMS Simu.","l")
		leg2.AddEntry(hg_mueta,"Parametrization","l")
		leg2.Draw()
		t3.cd(2)
		ROOT.gPad.SetGridy()
		Ratio_mueta = makeRatio(hg_mueta,h_mueta)
		Ratio_mueta.GetYaxis().SetTitle("Ratio")
		Ratio_mueta.GetXaxis().SetTitle("#eta")
		Ratio_mueta.Draw()
		Ratio_mueta.SetMaximum(5)
		Ratio_mueta.SetMinimum(0)
		t3.Update()
		t3.Print("RatioDistribComp_BEAMSPOT_m"+str(Mass)+"_Ctau"+ str(Ctau)+"_mueta.pdf")"""

		t3=ROOT.TCanvas()
		t3.Divide(1,2)
		t3.cd(1)
		hg_mud0.Draw()
		h_mud0.Draw("samePE")
		hg_mud0_cutIso.Draw("samePE")
		hg_mud0.SetLineColor(2)
		h_mud0.GetYaxis().SetTitle("Entries")
		h_mud0.GetXaxis().SetTitle("|d_{0}Beamspot| (cm)")
		leg3 = ROOT.TLegend(0.7,0.4,0.9,0.5)
		leg3.SetFillColor(19)
		leg3.SetBorderSize(1)
		leg3.AddEntry(h_mud0,"Full CMS Simu.","l")
		leg3.AddEntry(hg_mud0,"Parametrization","l")
		leg3.Draw()
		t3.cd(2)
		ROOT.gPad.SetGridy()
		Ratio_mud0 = makeRatio(hg_mud0,h_mud0)
		Ratio_mud0.GetYaxis().SetTitle("Ratio")
		Ratio_mud0.GetXaxis().SetTitle("d_{0} (cm)")
		Ratio_mud0.Draw()
		Ratio_mud0.SetMaximum(5)
		Ratio_mud0.SetMinimum(0)
		t3.Update()
		t3.Print("TESTRatioDistribComp_BEAMSPOT_m"+str(Mass)+"_Ctau"+ str(Ctau)+"_mud0.pdf")

		t3=ROOT.TCanvas()
		# Electrons
		t3.Divide(1,2)
		t3.cd(1)
		h_elept.Draw("PE")
		hg_elept.Draw("same")
		hg_elept_cutIso.Draw("samePE")
		hg_elept.SetLineColor(2)
		h_elept.GetYaxis().SetTitle("Entries")
		h_elept.GetXaxis().SetTitle("p_{T} (GeV)")
		h_elept.SetTitle("electron p_{T}")
		leg4 = ROOT.TLegend(0.7,0.4,0.9,0.5)
		leg4.SetFillColor(19)
		leg4.SetBorderSize(1)
		leg4.AddEntry(h_elept,"Full CMS Simu.","l")
		leg4.AddEntry(hg_elept,"Parametrization","l")
		leg4.Draw()
		t3.cd(2)
		ROOT.gPad.SetGridy()
		Ratio_elept = makeRatio(hg_elept,h_elept)
		Ratio_elept.GetYaxis().SetTitle("Ratio")
		Ratio_elept.GetXaxis().SetTitle("p_{T} (GeV)")
		Ratio_elept.Draw()
		Ratio_elept.SetMaximum(5)
		Ratio_elept.SetMinimum(0)
		t3.Update()
		t3.Print("TESTRatioDistribComp_BEAMSPOT_m"+str(Mass)+"_Ctau"+ str(Ctau)+"_elept.pdf")

		"""t3=ROOT.TCanvas()
		t3.Divide(1,2)
		t3.cd(1)
		h_eleeta.Draw("PE")
		hg_eleeta.Draw("same")
		hg_eleeta.SetLineColor(2)
		h_eleeta.GetYaxis().SetTitle("Entries")
		h_eleeta.GetXaxis().SetTitle("#eta")
		h_eleeta.SetTitle("electron #eta")
		leg5 = ROOT.TLegend(0.7,0.4,0.9,0.5)
		leg5.SetFillColor(19)
		leg5.SetBorderSize(1)
		leg5.AddEntry(h_eleeta,"Full CMS Simu.","l")
		leg5.AddEntry(hg_eleeta,"Parametrization","l")
		leg5.Draw()
		t3.cd(2)
		ROOT.gPad.SetGridy()
		Ratio_eleeta = makeRatio(hg_eleeta,h_eleeta)
		Ratio_eleeta.GetYaxis().SetTitle("Ratio")
		Ratio_eleeta.GetXaxis().SetTitle("#eta")
		Ratio_eleeta.Draw()
		Ratio_eleeta.SetMaximum(5)
		Ratio_eleeta.SetMinimum(0)
		t3.Update()
		t3.Print("RatioDistribComp_BEAMSPOT_m"+str(Mass)+"_Ctau"+ str(Ctau)+"_eleeta.pdf")"""

		t3=ROOT.TCanvas()
		t3.Divide(1,2)
		t3.cd(1)
		h_eled0.Draw("PE")
		hg_eled0.Draw("same")
		hg_eled0_cutIso.Draw("samePE")
		hg_eled0.SetLineColor(2)
		h_eled0.GetYaxis().SetTitle("Entries")
		h_eled0.GetXaxis().SetTitle("d_{0} (cm)")
		h_eled0.SetTitle("electron d_{0}")
		leg6 = ROOT.TLegend(0.7,0.4,0.9,0.5)
		leg6.SetFillColor(19)
		leg6.SetBorderSize(1)
		leg6.AddEntry(h_eled0,"Full CMS Simu.","l")
		leg6.AddEntry(hg_eled0,"Parametrization","l")
		leg6.Draw()
		t3.cd(2)
		ROOT.gPad.SetGridy()
		Ratio_eled0 = makeRatio(hg_eled0,h_eled0)
		Ratio_eled0.GetYaxis().SetTitle("Ratio")
		Ratio_eled0.GetXaxis().SetTitle("|d_{0}Beamspot| (cm)")
		Ratio_eled0.Draw()
		Ratio_eled0.SetMaximum(5)
		Ratio_eled0.SetMinimum(0)
		t3.Update()
		t3.Print("TESTRatioDistribComp_BEAMSPOT_m"+str(Mass)+"_Ctau"+ str(Ctau)+"_eled0.pdf")
		
		#t3.Update()
		#t3.Print("DistribComp_m"+str(Mass)+"_Ctau"+ str(Ctau)+".pdf") # TCanvas::Print also can make .pdf or .root/.C plots


