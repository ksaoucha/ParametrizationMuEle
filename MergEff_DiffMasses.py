import os, sys
#from MCdata import *
import ROOT

###############################
# pyroot file where I will make some histograms with/without cuts and efficiency
# 13 march 2016 by Kamal Saoucha, kamalsaou@hotmail.fr
#

ch  = ROOT.TChain("preCutTree","preCutTree")
pathToRootFile="Downloads/"
ch.Add(pathToRootFile+"DisplacedTop_Run2_TopTree_Study_stopTobl_m200_Ctau1_MuEl_NoBlinding_1.root")
#for Mass in [1,10,100]:
#	for Ctau in [200, 500, 800, 1100]:
#		ch.Add(pathToRootFile+"DisplacedTop_Run2_TopTree_Study_stopTobl_m" + str(Mass) + "_Ctau" + str(Ctau) + "_MuEl_NoBlinding_1.root"
# Booking some histograms, I clone the histograms of muons to make the ones of electrons because I want them to have the same scale so I can compare them later.

hTg_200_mupt = ROOT.TH1F("hTg_200_mupt","muon p_{T}",100,0,800)
hTg_200_mueta = ROOT.TH1F("hTg_200_mueta","muon #eta",100,-4,4)
hTg_200_mud0 = ROOT.TH1F("hTg_200_mud0","muon |d_{0}|",100,0,2);
#Tg_200_elept = ROOT.TH1F("Tg_200_elept","ele p_{T}",100,0,500)
hTg_200_elept = hTg_200_mupt.Clone("hTg_200_elept")
#Tg_200_eleeta = ROOT.TH1F("Tg_200_eleeta","ele #eta",100,-4,4)
hTg_200_eleeta = hTg_200_mueta.Clone("hTg_200_eleeta")
#Tg_200_eled0 = ROOT.TH1F("Tg_200_eled0","ele |d_{0}|",200,0,2);
hTg_200_eled0 = hTg_200_mud0.Clone("hTg_200_eled0")

# Booking soms histograms after cuts, I clone the histograms of muons to make the ones of electrons because I want them to have the same scale so I can compare them later.

#Tg_200_mupt_cut = ROOT.TH1F("Tg_200_mupt_cut","muon p_{T}",100,0,2000)
hTg_200_mupt_cut = hTg_200_mupt.Clone("hTg_200_mupt_cut")
#Tg_200_mueta_cut = ROOT.TH1F("Tg_200_mueta_cut","muon #eta",100,-4,4)
hTg_200_mueta_cut = hTg_200_mueta.Clone("hTg_200_mueta_cut")
#Tg_200_mud0_cut = ROOT.TH1F("Tg_200_mud0_cut","muon |d_{0}|",200,0,2);
hTg_200_mud0_cut = hTg_200_mud0.Clone("hTg_200_mud0_cut")
#Tg_200_elept_cut = ROOT.TH1F("Tg_200_elept_cut","ele p_{T}",100,0,500)
hTg_200_elept_cut = hTg_200_mupt.Clone("hTg_200_elept_cut")
#Tg_200_eleeta_cut = ROOT.TH1F("Tg_200_eleeta_cut","ele #eta",100,-4,4)
hTg_200_eleeta_cut = hTg_200_mueta.Clone("hTg_200_eleeta_cut")
#Tg_200_eled0_cut = ROOT.TH1F("Tg_200_eled0_cut","ele |d_{0}|",200,0,2);
hTg_200_eled0_cut = hTg_200_mud0.Clone("hTg_200_eled0_cut")

# Histograms with the Iso_cut

hTg_200_mupt_cutIso = hTg_200_mupt.Clone("hTg_200_mupt_cutIso")
hTg_200_mueta_cutIso = hTg_200_mueta.Clone("hTg_200_mueta_cutIso")
hTg_200_mud0_cutIso = hTg_200_mud0.Clone("hTg_200_mud0_cutIso")
hTg_200_elept_cutIso = hTg_200_mupt.Clone("hTg_200_elept_cutIso")
hTg_200_eleeta_cutIso = hTg_200_mueta.Clone("hTg_200_eleeta_cutIso")
hTg_200_eled0_cutIso = hTg_200_mud0.Clone("hTg_200_eled0_cutIso")

#hTg_200_muN = ROOT.TH1F("hTg_200_muN","muon #N",15,-0.5,14.5)
#hTg_200_eleN =  ROOT.TH1F("hTg_200_eleN","electron #N",100,0,800)

#Tg_200_muN = ROOT.TH1F("Tg_200_muN","muon #N",100,0,800)
#Tg_200_eleN =  ROOT.TH1F("Tg_200_eleN","electron #N",100,0,800)

hTg_200_mudr = ROOT.TH1F("hTg_200_mudr_genreco","muon #dr gen/reco",63,0,6.3)
hTg_200_eledr = ROOT.TH1F("hTg_200_eledr_genreco","electron #dr gen/reco",63,0,6.3)
# For bookkeeping

#------------------------------------------------------Histograms definition reco part ---------------------------#

Tg_200_mupt = ROOT.TH1F("Tg_200_mupt","muon p_{T}",100,0,800)
Tg_200_mueta = ROOT.TH1F("Tg_200_mueta","muon #eta",100,-4,4)
Tg_200_mud0 = ROOT.TH1F("Tg_200_mud0","muon |d_{0}|",100,0,2);
#Tg_200_elept = ROOT.TH1F("Tg_200_elept","ele p_{T}",100,0,500)
Tg_200_elept = Tg_200_mupt.Clone("Tg_200_elept")
#Tg_200_eleeta = ROOT.TH1F("Tg_200_eleeta","ele #eta",100,-4,4)
Tg_200_eleeta = Tg_200_mueta.Clone("Tg_200_eleeta")
#Tg_200_eled0 = ROOT.TH1F("Tg_200_eled0","ele |d_{0}|",200,0,2);
Tg_200_eled0 = Tg_200_mud0.Clone("Tg_200_eled0")

# Booking soms histograms after cuts, I clone the histograms of muons to make the ones of electrons because I want them to have the same scale so I can compare them later.

#Tg_200_mupt_cut = ROOT.TH1F("Tg_200_mupt_cut","muon p_{T}",100,0,2000)
Tg_200_mupt_cut = Tg_200_mupt.Clone("Tg_200_mupt_cut")
#Tg_200_mueta_cut = ROOT.TH1F("Tg_200_mueta_cut","muon #eta",100,-4,4)
Tg_200_mueta_cut = Tg_200_mueta.Clone("Tg_200_mueta_cut")
#Tg_200_mud0_cut = ROOT.TH1F("Tg_200_mud0_cut","muon |d_{0}|",200,0,2);
Tg_200_mud0_cut = Tg_200_mud0.Clone("Tg_200_mud0_cut")
#Tg_200_elept_cut = ROOT.TH1F("Tg_200_elept_cut","ele p_{T}",100,0,500)
Tg_200_elept_cut = Tg_200_mupt.Clone("Tg_200_elept_cut")
#Tg_200_eleeta_cut = ROOT.TH1F("Tg_200_eleeta_cut","ele #eta",100,-4,4)
Tg_200_eleeta_cut = Tg_200_mueta.Clone("Tg_200_eleeta_cut")
#Tg_200_eled0_cut = ROOT.TH1F("Tg_200_eled0_cut","ele |d_{0}|",200,0,2);
Tg_200_eled0_cut = Tg_200_mud0.Clone("Tg_200_eled0_cut")

# Histograms with the Iso_cut

Tg_200_mupt_cutIso = Tg_200_mupt.Clone("Tg_200_mupt_cutIso")
Tg_200_mueta_cutIso = Tg_200_mueta.Clone("Tg_200_mueta_cutIso")
Tg_200_mud0_cutIso = Tg_200_mud0.Clone("Tg_200_mud0_cutIso")
Tg_200_elept_cutIso = Tg_200_mupt.Clone("Tg_200_elept_cutIso")
Tg_200_eleeta_cutIso = Tg_200_mueta.Clone("Tg_200_eleeta_cutIso")
Tg_200_eled0_cutIso = Tg_200_mud0.Clone("Tg_200_eled0_cutIso")

ING=5


# Lorentz vectors definition


lvmu=ROOT.TLorentzVector()
lvele=ROOT.TLorentzVector()

lvmu_reco=ROOT.TLorentzVector()
lvele_reco=ROOT.TLorentzVector()

ii=0
nevents=ch.GetEntries()

# Start of the loop over the events in my data

for iev in ch:
	ii+=1
	if ii>5000:
		continue
#	for imu_reco in range(0,iev.nMuons_pc):
#		lvmu_reco.SetPtEtaPhiE(iev.pt_muon_pc[imu_reco],iev.eta_muon_pc[imu_reco],iev.phi_muon_pc[imu_reco],iev.E_muon_pc[imu_reco])
		# Loop over muons - fill in lorentz vector and fill some histograms

	for imu_gen in range(0,iev.nMcParticles_pc) :
		if abs(iev.type_mcParticle_pc[imu_gen]) == 13 and abs(iev.motherType_mcParticle_pc[imu_gen]) ==  1000006:
			lvmu.SetPtEtaPhiE(iev.pt_mcParticle_pc[imu_gen],iev.eta_mcParticle_pc[imu_gen],iev.phi_mcParticle_pc[imu_gen],iev.E_mcParticle_pc[imu_gen])
			passedCut_muon = False
			if iev.pt_mcParticle_pc[imu_gen]>10 and iev.v0_mcParticle_pc[imu_gen]<4 and iev.vz_mcParticle_pc[imu_gen]<30: #Var_cut
				passedCut_muon = True
			if passedCut_muon == False:
				continue
			hTg_200_mupt.Fill(iev.pt_mcParticle_pc[imu_gen])
			hTg_200_mueta.Fill(iev.eta_mcParticle_pc[imu_gen])
        		hTg_200_mud0.Fill(abs(iev.d0_mcParticle_pc[imu_gen]))
			#passedCut_muon = False
			#if iev.pt_mcParticle_pc[imu_gen]>10 and iev.v0_mcParticle_pc[imu_gen]<4 and iev.vz_mcParticle_pc[imu_gen]<30: #Var_cut
			#if iev.v0_mcParticle_pc[imu_gen]<4:
			#if iev.vz_mcParticle_pc[imu_gen]<30:

				#passedCut_muon = True
			if passedCut_muon==True:
				for imu_reco in range(0,iev.nMuons_pc):
					lvmu_reco.SetPtEtaPhiE(iev.pt_muon_pc[imu_reco],iev.eta_muon_pc[imu_reco],iev.phi_muon_pc[imu_reco],iev.E_muon_pc[imu_reco])
					hTg_200_mudr.Fill(lvmu.DeltaR(lvmu_reco))						
					if (lvmu.DeltaR(lvmu_reco)>0.05):
						continue
					hTg_200_mupt_cut.Fill(iev.pt_mcParticle_pc[imu_gen])
					hTg_200_mueta_cut.Fill(iev.eta_mcParticle_pc[imu_gen])
	        			hTg_200_mud0_cut.Fill(abs(iev.d0_mcParticle_pc[imu_gen]))
										
					passedCut_id_iso_muon = False
					if not iev.isId_muon_pc[imu_reco] == 0 and iev.pt_muon_pc[imu_reco]>25 and not iev.isIso_muon_pc[imu_reco] == 0: #Id_cut
							
						passedCut_id_iso_muon = True

					if passedCut_id_iso_muon==True:
								#Tg_200_mupt.Fill(iev.pt_mcParticle_pc[imu_nmu])	
								#Tg_200_mueta.Fill(iev.eta_mcParticle_pc[imu_nmu])	
	        						#Tg_200_mud0.Fill(abs(iev.d0_mcParticle_pc[imu_nmu]))	
						#		if iev.isIso_muon_pc[imu_nmu] == 1:
						hTg_200_mupt_cutIso.Fill(iev.pt_mcParticle_pc[imu_gen])	
						hTg_200_mueta_cutIso.Fill(iev.eta_mcParticle_pc[imu_gen])	
						hTg_200_mud0_cutIso.Fill(abs(iev.d0_mcParticle_pc[imu_gen]))
					break
				#if iev.type_mcParticle_pc[imu_gen] == 1:
				#	hTg_200_mupt_cutIso.Fill(iev.pt_mcParticle_pc[imu_gen])
				#	hTg_200_mueta_cutIso.Fill(iev.eta_mcParticle_pc[imu_gen])
				#	hTg_200_mud0_cutIso.Fill(iev.d0_mcParticle_pc[imu_gen])
		
# Loop over muons - fill in lorentz vector and fill some histograms

	#for iele_reco in range(0,iev.nElectrons_pc):
	#	lvele_reco.SetPtEtaPhiE(iev.pt_electron_pc[iele_reco],iev.eta_electron_pc[iele_reco],iev.phi_electron_pc[iele_reco],iev.E_electron_pc[iele_reco])
	
	for iele_gen in range(0,iev.nMcParticles_pc):
		if abs(iev.type_mcParticle_pc[iele_gen]) == 11 and abs(iev.motherType_mcParticle_pc[iele_gen]) ==  1000006:
			lvele.SetPtEtaPhiE(iev.pt_mcParticle_pc[iele_gen],iev.eta_mcParticle_pc[iele_gen],iev.phi_mcParticle_pc[iele_gen],iev.E_mcParticle_pc[iele_gen])
		#if abs(iev.motherType_mcParticle_pc[iele_gen]) ==  1000006:
			passedCut_electron = False
			if iev.pt_mcParticle_pc[iele_gen]>10 and iev.v0_mcParticle_pc[iele_gen]<4 and iev.vz_mcParticle_pc[iele_gen]<30: #Var_cut
				passedCut_electron = True
			if passedCut_electron == False:
				continue
			hTg_200_eleeta.Fill(iev.eta_mcParticle_pc[iele_gen])
			hTg_200_elept.Fill(iev.pt_mcParticle_pc[iele_gen])
			hTg_200_eled0.Fill(abs(iev.d0_mcParticle_pc[iele_gen]))
			
			if passedCut_electron == True:
				for iele_reco in range(0,iev.nElectrons_pc):
					lvele_reco.SetPtEtaPhiE(iev.pt_electron_pc[iele_reco],iev.eta_electron_pc[iele_reco],iev.phi_electron_pc[iele_reco],iev.E_electron_pc[iele_reco])
					hTg_200_eledr.Fill(lvele.DeltaR(lvele_reco))
					if (lvele.DeltaR(lvele_reco)>0.05):
						continue
					hTg_200_eleeta_cut.Fill(iev.eta_mcParticle_pc[iele_gen])
					hTg_200_elept_cut.Fill(iev.pt_mcParticle_pc[iele_gen])
					hTg_200_eled0_cut.Fill(abs(iev.d0_mcParticle_pc[iele_gen]))
						
					passedCut_id_iso_electron = False
					if not iev.isId_electron_pc[iele_reco] == 0 and iev.pt_electron_pc[iele_reco]>25 and not iev.isIso_electron_pc[iele_reco] == 0: #Id_cut
						passedCut_id_iso_electron = True

					if passedCut_id_iso_electron==True:
								#Tg_200_elept.Fill(iev.pt_mcParticle_pc[iele_nele])	
								#Tg_200_eleeta.Fill(iev.eta_mcParticle_pc[iele_nele])	
	        						#Tg_200_eled0.Fill(abs(iev.d0_mcParticle_pc[iele_nele]))	
						#		if iev.isIso_electron_pc[iele_nele] == 1:
						hTg_200_elept_cutIso.Fill(iev.pt_mcParticle_pc[iele_gen])	
						hTg_200_eleeta_cutIso.Fill(iev.eta_mcParticle_pc[iele_gen])	
						hTg_200_eled0_cutIso.Fill(abs(iev.d0_mcParticle_pc[iele_gen]))
					break



				#if iev.type_mcParticle_pc[iele_gen] == 1:
				#	hTg_200_elept_cutIso.Fill(iev.pt_mcParticle_pc[iele_gen])
				#	hTg_200_eleeta_cutIso.Fill(iev.eta_mcParticle_pc[iele_gen])
				#	hTg_200_eled0_cutIso.Fill(iev.d0_mcParticle_pc[iele_gen])

# END OF THE LOOPO !



ch  = ROOT.TChain("preCutTree","preCutTree")
pathToRootFile="Downloads/"
ch.Add(pathToRootFile+"DisplacedTop_Run2_TopTree_Study_stopTobl_m500_Ctau1_MuEl_NoBlinding_1.root")
#for Mass in [1,10,100]:
#	for Ctau in [200, 500, 800, 1100]:
#		ch.Add(pathToRootFile+"DisplacedTop_Run2_TopTree_Study_stopTobl_m" + str(Mass) + "_Ctau" + str(Ctau) + "_MuEl_NoBlinding_1.root"
# Booking some histograms, I clone the histograms of muons to make the ones of electrons because I want them to have the same scale so I can compare them later.

hTg_500_mupt = ROOT.TH1F("hTg_500_mupt","muon p_{T}",100,0,800)
hTg_500_mueta = ROOT.TH1F("hTg_500_mueta","muon #eta",100,-4,4)
hTg_500_mud0 = ROOT.TH1F("hTg_500_mud0","muon |d_{0}|",100,0,2);
#Tg_500_elept = ROOT.TH1F("Tg_500_elept","ele p_{T}",100,0,500)
hTg_500_elept = hTg_500_mupt.Clone("hTg_500_elept")
#Tg_500_eleeta = ROOT.TH1F("Tg_500_eleeta","ele #eta",100,-4,4)
hTg_500_eleeta = hTg_500_mueta.Clone("hTg_500_eleeta")
#Tg_500_eled0 = ROOT.TH1F("Tg_500_eled0","ele |d_{0}|",200,0,2);
hTg_500_eled0 = hTg_500_mud0.Clone("hTg_500_eled0")

# Booking soms histograms after cuts, I clone the histograms of muons to make the ones of electrons because I want them to have the same scale so I can compare them later.

#Tg_500_mupt_cut = ROOT.TH1F("Tg_500_mupt_cut","muon p_{T}",100,0,2000)
hTg_500_mupt_cut = hTg_500_mupt.Clone("hTg_500_mupt_cut")
#Tg_500_mueta_cut = ROOT.TH1F("Tg_500_mueta_cut","muon #eta",100,-4,4)
hTg_500_mueta_cut = hTg_500_mueta.Clone("hTg_500_mueta_cut")
#Tg_500_mud0_cut = ROOT.TH1F("Tg_500_mud0_cut","muon |d_{0}|",200,0,2);
hTg_500_mud0_cut = hTg_500_mud0.Clone("hTg_500_mud0_cut")
#Tg_500_elept_cut = ROOT.TH1F("Tg_500_elept_cut","ele p_{T}",100,0,500)
hTg_500_elept_cut = hTg_500_mupt.Clone("hTg_500_elept_cut")
#Tg_500_eleeta_cut = ROOT.TH1F("Tg_500_eleeta_cut","ele #eta",100,-4,4)
hTg_500_eleeta_cut = hTg_500_mueta.Clone("hTg_500_eleeta_cut")
#Tg_500_eled0_cut = ROOT.TH1F("Tg_500_eled0_cut","ele |d_{0}|",200,0,2);
hTg_500_eled0_cut = hTg_500_mud0.Clone("hTg_500_eled0_cut")

# Histograms with the Iso_cut

hTg_500_mupt_cutIso = hTg_500_mupt.Clone("hTg_500_mupt_cutIso")
hTg_500_mueta_cutIso = hTg_500_mueta.Clone("hTg_500_mueta_cutIso")
hTg_500_mud0_cutIso = hTg_500_mud0.Clone("hTg_500_mud0_cutIso")
hTg_500_elept_cutIso = hTg_500_mupt.Clone("hTg_500_elept_cutIso")
hTg_500_eleeta_cutIso = hTg_500_mueta.Clone("hTg_500_eleeta_cutIso")
hTg_500_eled0_cutIso = hTg_500_mud0.Clone("hTg_500_eled0_cutIso")

#hTg_500_muN = ROOT.TH1F("hTg_500_muN","muon #N",15,-0.5,14.5)
#hTg_500_eleN =  ROOT.TH1F("hTg_500_eleN","electron #N",100,0,800)

#Tg_500_muN = ROOT.TH1F("Tg_500_muN","muon #N",100,0,800)
#Tg_500_eleN =  ROOT.TH1F("Tg_500_eleN","electron #N",100,0,800)

hTg_500_mudr = ROOT.TH1F("hTg_500_mudr_genreco","muon #dr gen/reco",63,0,6.3)
hTg_500_eledr = ROOT.TH1F("hTg_500_eledr_genreco","electron #dr gen/reco",63,0,6.3)
# For bookkeeping

#------------------------------------------------------Histograms definition reco part ---------------------------#

Tg_500_mupt = ROOT.TH1F("Tg_500_mupt","muon p_{T}",100,0,800)
Tg_500_mueta = ROOT.TH1F("Tg_500_mueta","muon #eta",100,-4,4)
Tg_500_mud0 = ROOT.TH1F("Tg_500_mud0","muon |d_{0}|",100,0,2);
#Tg_500_elept = ROOT.TH1F("Tg_500_elept","ele p_{T}",100,0,500)
Tg_500_elept = Tg_500_mupt.Clone("Tg_500_elept")
#Tg_500_eleeta = ROOT.TH1F("Tg_500_eleeta","ele #eta",100,-4,4)
Tg_500_eleeta = Tg_500_mueta.Clone("Tg_500_eleeta")
#Tg_500_eled0 = ROOT.TH1F("Tg_500_eled0","ele |d_{0}|",200,0,2);
Tg_500_eled0 = Tg_500_mud0.Clone("Tg_500_eled0")

# Booking soms histograms after cuts, I clone the histograms of muons to make the ones of electrons because I want them to have the same scale so I can compare them later.

#Tg_500_mupt_cut = ROOT.TH1F("Tg_500_mupt_cut","muon p_{T}",100,0,2000)
Tg_500_mupt_cut = Tg_500_mupt.Clone("Tg_500_mupt_cut")
#Tg_500_mueta_cut = ROOT.TH1F("Tg_500_mueta_cut","muon #eta",100,-4,4)
Tg_500_mueta_cut = Tg_500_mueta.Clone("Tg_500_mueta_cut")
#Tg_500_mud0_cut = ROOT.TH1F("Tg_500_mud0_cut","muon |d_{0}|",200,0,2);
Tg_500_mud0_cut = Tg_500_mud0.Clone("Tg_500_mud0_cut")
#Tg_500_elept_cut = ROOT.TH1F("Tg_500_elept_cut","ele p_{T}",100,0,500)
Tg_500_elept_cut = Tg_500_mupt.Clone("Tg_500_elept_cut")
#Tg_500_eleeta_cut = ROOT.TH1F("Tg_500_eleeta_cut","ele #eta",100,-4,4)
Tg_500_eleeta_cut = Tg_500_mueta.Clone("Tg_500_eleeta_cut")
#Tg_500_eled0_cut = ROOT.TH1F("Tg_500_eled0_cut","ele |d_{0}|",200,0,2);
Tg_500_eled0_cut = Tg_500_mud0.Clone("Tg_500_eled0_cut")

# Histograms with the Iso_cut

Tg_500_mupt_cutIso = Tg_500_mupt.Clone("Tg_500_mupt_cutIso")
Tg_500_mueta_cutIso = Tg_500_mueta.Clone("Tg_500_mueta_cutIso")
Tg_500_mud0_cutIso = Tg_500_mud0.Clone("Tg_500_mud0_cutIso")
Tg_500_elept_cutIso = Tg_500_mupt.Clone("Tg_500_elept_cutIso")
Tg_500_eleeta_cutIso = Tg_500_mueta.Clone("Tg_500_eleeta_cutIso")
Tg_500_eled0_cutIso = Tg_500_mud0.Clone("Tg_500_eled0_cutIso")

ING=5


# Lorentz vectors definition


lvmu=ROOT.TLorentzVector()
lvele=ROOT.TLorentzVector()

lvmu_reco=ROOT.TLorentzVector()
lvele_reco=ROOT.TLorentzVector()

ii=0
nevents=ch.GetEntries()

# Start of the loop over the events in my data

for iev in ch:
	ii+=1
	if ii>5000:
		continue
#	for imu_reco in range(0,iev.nMuons_pc):
#		lvmu_reco.SetPtEtaPhiE(iev.pt_muon_pc[imu_reco],iev.eta_muon_pc[imu_reco],iev.phi_muon_pc[imu_reco],iev.E_muon_pc[imu_reco])
		# Loop over muons - fill in lorentz vector and fill some histograms

	for imu_gen in range(0,iev.nMcParticles_pc) :
		if abs(iev.type_mcParticle_pc[imu_gen]) == 13 and abs(iev.motherType_mcParticle_pc[imu_gen]) ==  1000006:
			lvmu.SetPtEtaPhiE(iev.pt_mcParticle_pc[imu_gen],iev.eta_mcParticle_pc[imu_gen],iev.phi_mcParticle_pc[imu_gen],iev.E_mcParticle_pc[imu_gen])
			passedCut_muon = False
			if iev.pt_mcParticle_pc[imu_gen]>10 and iev.v0_mcParticle_pc[imu_gen]<4 and iev.vz_mcParticle_pc[imu_gen]<30: #Var_cut
				passedCut_muon = True
			if passedCut_muon == False:
				continue
			hTg_500_mupt.Fill(iev.pt_mcParticle_pc[imu_gen])
			hTg_500_mueta.Fill(iev.eta_mcParticle_pc[imu_gen])
        		hTg_500_mud0.Fill(abs(iev.d0_mcParticle_pc[imu_gen]))
			#passedCut_muon = False
			#if iev.pt_mcParticle_pc[imu_gen]>10 and iev.v0_mcParticle_pc[imu_gen]<4 and iev.vz_mcParticle_pc[imu_gen]<30: #Var_cut
			#if iev.v0_mcParticle_pc[imu_gen]<4:
			#if iev.vz_mcParticle_pc[imu_gen]<30:

				#passedCut_muon = True
			if passedCut_muon==True:
				for imu_reco in range(0,iev.nMuons_pc):
					lvmu_reco.SetPtEtaPhiE(iev.pt_muon_pc[imu_reco],iev.eta_muon_pc[imu_reco],iev.phi_muon_pc[imu_reco],iev.E_muon_pc[imu_reco])
					hTg_500_mudr.Fill(lvmu.DeltaR(lvmu_reco))						
					if (lvmu.DeltaR(lvmu_reco)>0.05):
						continue
					hTg_500_mupt_cut.Fill(iev.pt_mcParticle_pc[imu_gen])
					hTg_500_mueta_cut.Fill(iev.eta_mcParticle_pc[imu_gen])
	        			hTg_500_mud0_cut.Fill(abs(iev.d0_mcParticle_pc[imu_gen]))
										
					passedCut_id_iso_muon = False
					if not iev.isId_muon_pc[imu_reco] == 0 and iev.pt_muon_pc[imu_reco]>25 and not iev.isIso_muon_pc[imu_reco] == 0: #Id_cut
							
						passedCut_id_iso_muon = True

					if passedCut_id_iso_muon==True:
								#Tg_500_mupt.Fill(iev.pt_mcParticle_pc[imu_nmu])	
								#Tg_500_mueta.Fill(iev.eta_mcParticle_pc[imu_nmu])	
	        						#Tg_500_mud0.Fill(abs(iev.d0_mcParticle_pc[imu_nmu]))	
						#		if iev.isIso_muon_pc[imu_nmu] == 1:
						hTg_500_mupt_cutIso.Fill(iev.pt_mcParticle_pc[imu_gen])	
						hTg_500_mueta_cutIso.Fill(iev.eta_mcParticle_pc[imu_gen])	
						hTg_500_mud0_cutIso.Fill(abs(iev.d0_mcParticle_pc[imu_gen]))
					break
				#if iev.type_mcParticle_pc[imu_gen] == 1:
				#	hTg_500_mupt_cutIso.Fill(iev.pt_mcParticle_pc[imu_gen])
				#	hTg_500_mueta_cutIso.Fill(iev.eta_mcParticle_pc[imu_gen])
				#	hTg_500_mud0_cutIso.Fill(iev.d0_mcParticle_pc[imu_gen])
		
# Loop over muons - fill in lorentz vector and fill some histograms

	#for iele_reco in range(0,iev.nElectrons_pc):
	#	lvele_reco.SetPtEtaPhiE(iev.pt_electron_pc[iele_reco],iev.eta_electron_pc[iele_reco],iev.phi_electron_pc[iele_reco],iev.E_electron_pc[iele_reco])
	
	for iele_gen in range(0,iev.nMcParticles_pc):
		if abs(iev.type_mcParticle_pc[iele_gen]) == 11 and abs(iev.motherType_mcParticle_pc[iele_gen]) ==  1000006:
			lvele.SetPtEtaPhiE(iev.pt_mcParticle_pc[iele_gen],iev.eta_mcParticle_pc[iele_gen],iev.phi_mcParticle_pc[iele_gen],iev.E_mcParticle_pc[iele_gen])
		#if abs(iev.motherType_mcParticle_pc[iele_gen]) ==  1000006:
			passedCut_electron = False
			if iev.pt_mcParticle_pc[iele_gen]>10 and iev.v0_mcParticle_pc[iele_gen]<4 and iev.vz_mcParticle_pc[iele_gen]<30: #Var_cut
				passedCut_electron = True
			if passedCut_electron == False:
				continue
			hTg_500_eleeta.Fill(iev.eta_mcParticle_pc[iele_gen])
			hTg_500_elept.Fill(iev.pt_mcParticle_pc[iele_gen])
			hTg_500_eled0.Fill(abs(iev.d0_mcParticle_pc[iele_gen]))
			
			if passedCut_electron == True:
				for iele_reco in range(0,iev.nElectrons_pc):
					lvele_reco.SetPtEtaPhiE(iev.pt_electron_pc[iele_reco],iev.eta_electron_pc[iele_reco],iev.phi_electron_pc[iele_reco],iev.E_electron_pc[iele_reco])
					hTg_500_eledr.Fill(lvele.DeltaR(lvele_reco))
					if (lvele.DeltaR(lvele_reco)>0.05):
						continue
					hTg_500_eleeta_cut.Fill(iev.eta_mcParticle_pc[iele_gen])
					hTg_500_elept_cut.Fill(iev.pt_mcParticle_pc[iele_gen])
					hTg_500_eled0_cut.Fill(abs(iev.d0_mcParticle_pc[iele_gen]))
						
					passedCut_id_iso_electron = False
					if not iev.isId_electron_pc[iele_reco] == 0 and iev.pt_electron_pc[iele_reco]>25 and not iev.isIso_electron_pc[iele_reco] == 0: #Id_cut
						passedCut_id_iso_electron = True

					if passedCut_id_iso_electron==True:
								#Tg_500_elept.Fill(iev.pt_mcParticle_pc[iele_nele])	
								#Tg_500_eleeta.Fill(iev.eta_mcParticle_pc[iele_nele])	
	        						#Tg_500_eled0.Fill(abs(iev.d0_mcParticle_pc[iele_nele]))	
						#		if iev.isIso_electron_pc[iele_nele] == 1:
						hTg_500_elept_cutIso.Fill(iev.pt_mcParticle_pc[iele_gen])	
						hTg_500_eleeta_cutIso.Fill(iev.eta_mcParticle_pc[iele_gen])	
						hTg_500_eled0_cutIso.Fill(abs(iev.d0_mcParticle_pc[iele_gen]))
					break



				#if iev.type_mcParticle_pc[iele_gen] == 1:
				#	hTg_500_elept_cutIso.Fill(iev.pt_mcParticle_pc[iele_gen])
				#	hTg_500_eleeta_cutIso.Fill(iev.eta_mcParticle_pc[iele_gen])
				#	hTg_500_eled0_cutIso.Fill(iev.d0_mcParticle_pc[iele_gen])

# END OF THE LOOPO !

ch  = ROOT.TChain("preCutTree","preCutTree")
pathToRootFile="Downloads/"
ch.Add(pathToRootFile+"DisplacedTop_Run2_TopTree_Study_stopTobl_m800_Ctau1_MuEl_NoBlinding_1.root")
#for Mass in [1,10,100]:
#	for Ctau in [200, 500, 800, 1100]:
#		ch.Add(pathToRootFile+"DisplacedTop_Run2_TopTree_Study_stopTobl_m" + str(Mass) + "_Ctau" + str(Ctau) + "_MuEl_NoBlinding_1.root"
# Booking some histograms, I clone the histograms of muons to make the ones of electrons because I want them to have the same scale so I can compare them later.

hTg_800_mupt = ROOT.TH1F("hTg_800_mupt","muon p_{T}",100,0,800)
hTg_800_mueta = ROOT.TH1F("hTg_800_mueta","muon #eta",100,-4,4)
hTg_800_mud0 = ROOT.TH1F("hTg_800_mud0","muon |d_{0}|",100,0,2);
#Tg_800_elept = ROOT.TH1F("Tg_800_elept","ele p_{T}",100,0,500)
hTg_800_elept = hTg_800_mupt.Clone("hTg_800_elept")
#Tg_800_eleeta = ROOT.TH1F("Tg_800_eleeta","ele #eta",100,-4,4)
hTg_800_eleeta = hTg_800_mueta.Clone("hTg_800_eleeta")
#Tg_800_eled0 = ROOT.TH1F("Tg_800_eled0","ele |d_{0}|",200,0,2);
hTg_800_eled0 = hTg_800_mud0.Clone("hTg_800_eled0")

# Booking soms histograms after cuts, I clone the histograms of muons to make the ones of electrons because I want them to have the same scale so I can compare them later.

#Tg_800_mupt_cut = ROOT.TH1F("Tg_800_mupt_cut","muon p_{T}",100,0,2000)
hTg_800_mupt_cut = hTg_800_mupt.Clone("hTg_800_mupt_cut")
#Tg_800_mueta_cut = ROOT.TH1F("Tg_800_mueta_cut","muon #eta",100,-4,4)
hTg_800_mueta_cut = hTg_800_mueta.Clone("hTg_800_mueta_cut")
#Tg_800_mud0_cut = ROOT.TH1F("Tg_800_mud0_cut","muon |d_{0}|",200,0,2);
hTg_800_mud0_cut = hTg_800_mud0.Clone("hTg_800_mud0_cut")
#Tg_800_elept_cut = ROOT.TH1F("Tg_800_elept_cut","ele p_{T}",100,0,500)
hTg_800_elept_cut = hTg_800_mupt.Clone("hTg_800_elept_cut")
#Tg_800_eleeta_cut = ROOT.TH1F("Tg_800_eleeta_cut","ele #eta",100,-4,4)
hTg_800_eleeta_cut = hTg_800_mueta.Clone("hTg_800_eleeta_cut")
#Tg_800_eled0_cut = ROOT.TH1F("Tg_800_eled0_cut","ele |d_{0}|",200,0,2);
hTg_800_eled0_cut = hTg_800_mud0.Clone("hTg_800_eled0_cut")

# Histograms with the Iso_cut

hTg_800_mupt_cutIso = hTg_800_mupt.Clone("hTg_800_mupt_cutIso")
hTg_800_mueta_cutIso = hTg_800_mueta.Clone("hTg_800_mueta_cutIso")
hTg_800_mud0_cutIso = hTg_800_mud0.Clone("hTg_800_mud0_cutIso")
hTg_800_elept_cutIso = hTg_800_mupt.Clone("hTg_800_elept_cutIso")
hTg_800_eleeta_cutIso = hTg_800_mueta.Clone("hTg_800_eleeta_cutIso")
hTg_800_eled0_cutIso = hTg_800_mud0.Clone("hTg_800_eled0_cutIso")

#hTg_800_muN = ROOT.TH1F("hTg_800_muN","muon #N",15,-0.5,14.5)
#hTg_800_eleN =  ROOT.TH1F("hTg_800_eleN","electron #N",100,0,800)

#Tg_800_muN = ROOT.TH1F("Tg_800_muN","muon #N",100,0,800)
#Tg_800_eleN =  ROOT.TH1F("Tg_800_eleN","electron #N",100,0,800)

hTg_800_mudr = ROOT.TH1F("hTg_800_mudr_genreco","muon #dr gen/reco",63,0,6.3)
hTg_800_eledr = ROOT.TH1F("hTg_800_eledr_genreco","electron #dr gen/reco",63,0,6.3)
# For bookkeeping

#------------------------------------------------------Histograms definition reco part ---------------------------#

Tg_800_mupt = ROOT.TH1F("Tg_800_mupt","muon p_{T}",100,0,800)
Tg_800_mueta = ROOT.TH1F("Tg_800_mueta","muon #eta",100,-4,4)
Tg_800_mud0 = ROOT.TH1F("Tg_800_mud0","muon |d_{0}|",100,0,2);
#Tg_800_elept = ROOT.TH1F("Tg_800_elept","ele p_{T}",100,0,500)
Tg_800_elept = Tg_800_mupt.Clone("Tg_800_elept")
#Tg_800_eleeta = ROOT.TH1F("Tg_800_eleeta","ele #eta",100,-4,4)
Tg_800_eleeta = Tg_800_mueta.Clone("Tg_800_eleeta")
#Tg_800_eled0 = ROOT.TH1F("Tg_800_eled0","ele |d_{0}|",200,0,2);
Tg_800_eled0 = Tg_800_mud0.Clone("Tg_800_eled0")

# Booking soms histograms after cuts, I clone the histograms of muons to make the ones of electrons because I want them to have the same scale so I can compare them later.

#Tg_800_mupt_cut = ROOT.TH1F("Tg_800_mupt_cut","muon p_{T}",100,0,2000)
Tg_800_mupt_cut = Tg_800_mupt.Clone("Tg_800_mupt_cut")
#Tg_800_mueta_cut = ROOT.TH1F("Tg_800_mueta_cut","muon #eta",100,-4,4)
Tg_800_mueta_cut = Tg_800_mueta.Clone("Tg_800_mueta_cut")
#Tg_800_mud0_cut = ROOT.TH1F("Tg_800_mud0_cut","muon |d_{0}|",200,0,2);
Tg_800_mud0_cut = Tg_800_mud0.Clone("Tg_800_mud0_cut")
#Tg_800_elept_cut = ROOT.TH1F("Tg_800_elept_cut","ele p_{T}",100,0,500)
Tg_800_elept_cut = Tg_800_mupt.Clone("Tg_800_elept_cut")
#Tg_800_eleeta_cut = ROOT.TH1F("Tg_800_eleeta_cut","ele #eta",100,-4,4)
Tg_800_eleeta_cut = Tg_800_mueta.Clone("Tg_800_eleeta_cut")
#Tg_800_eled0_cut = ROOT.TH1F("Tg_800_eled0_cut","ele |d_{0}|",200,0,2);
Tg_800_eled0_cut = Tg_800_mud0.Clone("Tg_800_eled0_cut")

# Histograms with the Iso_cut

Tg_800_mupt_cutIso = Tg_800_mupt.Clone("Tg_800_mupt_cutIso")
Tg_800_mueta_cutIso = Tg_800_mueta.Clone("Tg_800_mueta_cutIso")
Tg_800_mud0_cutIso = Tg_800_mud0.Clone("Tg_800_mud0_cutIso")
Tg_800_elept_cutIso = Tg_800_mupt.Clone("Tg_800_elept_cutIso")
Tg_800_eleeta_cutIso = Tg_800_mueta.Clone("Tg_800_eleeta_cutIso")
Tg_800_eled0_cutIso = Tg_800_mud0.Clone("Tg_800_eled0_cutIso")

ING=5


# Lorentz vectors definition


lvmu=ROOT.TLorentzVector()
lvele=ROOT.TLorentzVector()

lvmu_reco=ROOT.TLorentzVector()
lvele_reco=ROOT.TLorentzVector()

ii=0
nevents=ch.GetEntries()

# Start of the loop over the events in my data

for iev in ch:
	ii+=1
	if ii>5000:
		continue
#	for imu_reco in range(0,iev.nMuons_pc):
#		lvmu_reco.SetPtEtaPhiE(iev.pt_muon_pc[imu_reco],iev.eta_muon_pc[imu_reco],iev.phi_muon_pc[imu_reco],iev.E_muon_pc[imu_reco])
		# Loop over muons - fill in lorentz vector and fill some histograms

	for imu_gen in range(0,iev.nMcParticles_pc) :
		if abs(iev.type_mcParticle_pc[imu_gen]) == 13 and abs(iev.motherType_mcParticle_pc[imu_gen]) ==  1000006:
			lvmu.SetPtEtaPhiE(iev.pt_mcParticle_pc[imu_gen],iev.eta_mcParticle_pc[imu_gen],iev.phi_mcParticle_pc[imu_gen],iev.E_mcParticle_pc[imu_gen])
			passedCut_muon = False
			if iev.pt_mcParticle_pc[imu_gen]>10 and iev.v0_mcParticle_pc[imu_gen]<4 and iev.vz_mcParticle_pc[imu_gen]<30: #Var_cut
				passedCut_muon = True
			if passedCut_muon == False:
				continue
			hTg_800_mupt.Fill(iev.pt_mcParticle_pc[imu_gen])
			hTg_800_mueta.Fill(iev.eta_mcParticle_pc[imu_gen])
        		hTg_800_mud0.Fill(abs(iev.d0_mcParticle_pc[imu_gen]))
			#passedCut_muon = False
			#if iev.pt_mcParticle_pc[imu_gen]>10 and iev.v0_mcParticle_pc[imu_gen]<4 and iev.vz_mcParticle_pc[imu_gen]<30: #Var_cut
			#if iev.v0_mcParticle_pc[imu_gen]<4:
			#if iev.vz_mcParticle_pc[imu_gen]<30:

				#passedCut_muon = True
			if passedCut_muon==True:
				for imu_reco in range(0,iev.nMuons_pc):
					lvmu_reco.SetPtEtaPhiE(iev.pt_muon_pc[imu_reco],iev.eta_muon_pc[imu_reco],iev.phi_muon_pc[imu_reco],iev.E_muon_pc[imu_reco])
					hTg_800_mudr.Fill(lvmu.DeltaR(lvmu_reco))						
					if (lvmu.DeltaR(lvmu_reco)>0.05):
						continue
					hTg_800_mupt_cut.Fill(iev.pt_mcParticle_pc[imu_gen])
					hTg_800_mueta_cut.Fill(iev.eta_mcParticle_pc[imu_gen])
	        			hTg_800_mud0_cut.Fill(abs(iev.d0_mcParticle_pc[imu_gen]))
										
					passedCut_id_iso_muon = False
					if not iev.isId_muon_pc[imu_reco] == 0 and iev.pt_muon_pc[imu_reco]>25 and not iev.isIso_muon_pc[imu_reco] == 0: #Id_cut
							
						passedCut_id_iso_muon = True

					if passedCut_id_iso_muon==True:
								#Tg_800_mupt.Fill(iev.pt_mcParticle_pc[imu_nmu])	
								#Tg_800_mueta.Fill(iev.eta_mcParticle_pc[imu_nmu])	
	        						#Tg_800_mud0.Fill(abs(iev.d0_mcParticle_pc[imu_nmu]))	
						#		if iev.isIso_muon_pc[imu_nmu] == 1:
						hTg_800_mupt_cutIso.Fill(iev.pt_mcParticle_pc[imu_gen])	
						hTg_800_mueta_cutIso.Fill(iev.eta_mcParticle_pc[imu_gen])	
						hTg_800_mud0_cutIso.Fill(abs(iev.d0_mcParticle_pc[imu_gen]))
					break
				#if iev.type_mcParticle_pc[imu_gen] == 1:
				#	hTg_800_mupt_cutIso.Fill(iev.pt_mcParticle_pc[imu_gen])
				#	hTg_800_mueta_cutIso.Fill(iev.eta_mcParticle_pc[imu_gen])
				#	hTg_800_mud0_cutIso.Fill(iev.d0_mcParticle_pc[imu_gen])
		
# Loop over muons - fill in lorentz vector and fill some histograms

	#for iele_reco in range(0,iev.nElectrons_pc):
	#	lvele_reco.SetPtEtaPhiE(iev.pt_electron_pc[iele_reco],iev.eta_electron_pc[iele_reco],iev.phi_electron_pc[iele_reco],iev.E_electron_pc[iele_reco])
	
	for iele_gen in range(0,iev.nMcParticles_pc):
		if abs(iev.type_mcParticle_pc[iele_gen]) == 11 and abs(iev.motherType_mcParticle_pc[iele_gen]) ==  1000006:
			lvele.SetPtEtaPhiE(iev.pt_mcParticle_pc[iele_gen],iev.eta_mcParticle_pc[iele_gen],iev.phi_mcParticle_pc[iele_gen],iev.E_mcParticle_pc[iele_gen])
		#if abs(iev.motherType_mcParticle_pc[iele_gen]) ==  1000006:
			passedCut_electron = False
			if iev.pt_mcParticle_pc[iele_gen]>10 and iev.v0_mcParticle_pc[iele_gen]<4 and iev.vz_mcParticle_pc[iele_gen]<30: #Var_cut
				passedCut_electron = True
			if passedCut_electron == False:
				continue
			hTg_800_eleeta.Fill(iev.eta_mcParticle_pc[iele_gen])
			hTg_800_elept.Fill(iev.pt_mcParticle_pc[iele_gen])
			hTg_800_eled0.Fill(abs(iev.d0_mcParticle_pc[iele_gen]))
			
			if passedCut_electron == True:
				for iele_reco in range(0,iev.nElectrons_pc):
					lvele_reco.SetPtEtaPhiE(iev.pt_electron_pc[iele_reco],iev.eta_electron_pc[iele_reco],iev.phi_electron_pc[iele_reco],iev.E_electron_pc[iele_reco])
					hTg_800_eledr.Fill(lvele.DeltaR(lvele_reco))
					if (lvele.DeltaR(lvele_reco)>0.05):
						continue
					hTg_800_eleeta_cut.Fill(iev.eta_mcParticle_pc[iele_gen])
					hTg_800_elept_cut.Fill(iev.pt_mcParticle_pc[iele_gen])
					hTg_800_eled0_cut.Fill(abs(iev.d0_mcParticle_pc[iele_gen]))
						
					passedCut_id_iso_electron = False
					if not iev.isId_electron_pc[iele_reco] == 0 and iev.pt_electron_pc[iele_reco]>25 and not iev.isIso_electron_pc[iele_reco] == 0: #Id_cut
						passedCut_id_iso_electron = True

					if passedCut_id_iso_electron==True:
								#Tg_800_elept.Fill(iev.pt_mcParticle_pc[iele_nele])	
								#Tg_800_eleeta.Fill(iev.eta_mcParticle_pc[iele_nele])	
	        						#Tg_800_eled0.Fill(abs(iev.d0_mcParticle_pc[iele_nele]))	
						#		if iev.isIso_electron_pc[iele_nele] == 1:
						hTg_800_elept_cutIso.Fill(iev.pt_mcParticle_pc[iele_gen])	
						hTg_800_eleeta_cutIso.Fill(iev.eta_mcParticle_pc[iele_gen])	
						hTg_800_eled0_cutIso.Fill(abs(iev.d0_mcParticle_pc[iele_gen]))
					break



				#if iev.type_mcParticle_pc[iele_gen] == 1:
				#	hTg_800_elept_cutIso.Fill(iev.pt_mcParticle_pc[iele_gen])
				#	hTg_800_eleeta_cutIso.Fill(iev.eta_mcParticle_pc[iele_gen])
				#	hTg_800_eled0_cutIso.Fill(iev.d0_mcParticle_pc[iele_gen])

# END OF THE LOOPO !

ch  = ROOT.TChain("preCutTree","preCutTree")
pathToRootFile="Downloads/"
ch.Add(pathToRootFile+"DisplacedTop_Run2_TopTree_Study_stopTobl_m1100_Ctau1_MuEl_NoBlinding_1.root")
#for Mass in [1,10,100]:
#	for Ctau in [200, 500, 800, 1100]:
#		ch.Add(pathToRootFile+"DisplacedTop_Run2_TopTree_Study_stopTobl_m" + str(Mass) + "_Ctau" + str(Ctau) + "_MuEl_NoBlinding_1.root"
# Booking some histograms, I clone the histograms of muons to make the ones of electrons because I want them to have the same scale so I can compare them later.

hTg_1100_mupt = ROOT.TH1F("hTg_1100_mupt","muon p_{T}",100,0,800)
hTg_1100_mueta = ROOT.TH1F("hTg_1100_mueta","muon #eta",100,-4,4)
hTg_1100_mud0 = ROOT.TH1F("hTg_1100_mud0","muon |d_{0}|",100,0,2);
#Tg_1100_elept = ROOT.TH1F("Tg_1100_elept","ele p_{T}",100,0,500)
hTg_1100_elept = hTg_1100_mupt.Clone("hTg_1100_elept")
#Tg_1100_eleeta = ROOT.TH1F("Tg_1100_eleeta","ele #eta",100,-4,4)
hTg_1100_eleeta = hTg_1100_mueta.Clone("hTg_1100_eleeta")
#Tg_1100_eled0 = ROOT.TH1F("Tg_1100_eled0","ele |d_{0}|",200,0,2);
hTg_1100_eled0 = hTg_1100_mud0.Clone("hTg_1100_eled0")

# Booking soms histograms after cuts, I clone the histograms of muons to make the ones of electrons because I want them to have the same scale so I can compare them later.

#Tg_1100_mupt_cut = ROOT.TH1F("Tg_1100_mupt_cut","muon p_{T}",100,0,2000)
hTg_1100_mupt_cut = hTg_1100_mupt.Clone("hTg_1100_mupt_cut")
#Tg_1100_mueta_cut = ROOT.TH1F("Tg_1100_mueta_cut","muon #eta",100,-4,4)
hTg_1100_mueta_cut = hTg_1100_mueta.Clone("hTg_1100_mueta_cut")
#Tg_1100_mud0_cut = ROOT.TH1F("Tg_1100_mud0_cut","muon |d_{0}|",200,0,2);
hTg_1100_mud0_cut = hTg_1100_mud0.Clone("hTg_1100_mud0_cut")
#Tg_1100_elept_cut = ROOT.TH1F("Tg_1100_elept_cut","ele p_{T}",100,0,500)
hTg_1100_elept_cut = hTg_1100_mupt.Clone("hTg_1100_elept_cut")
#Tg_1100_eleeta_cut = ROOT.TH1F("Tg_1100_eleeta_cut","ele #eta",100,-4,4)
hTg_1100_eleeta_cut = hTg_1100_mueta.Clone("hTg_1100_eleeta_cut")
#Tg_1100_eled0_cut = ROOT.TH1F("Tg_1100_eled0_cut","ele |d_{0}|",200,0,2);
hTg_1100_eled0_cut = hTg_1100_mud0.Clone("hTg_1100_eled0_cut")

# Histograms with the Iso_cut

hTg_1100_mupt_cutIso = hTg_1100_mupt.Clone("hTg_1100_mupt_cutIso")
hTg_1100_mueta_cutIso = hTg_1100_mueta.Clone("hTg_1100_mueta_cutIso")
hTg_1100_mud0_cutIso = hTg_1100_mud0.Clone("hTg_1100_mud0_cutIso")
hTg_1100_elept_cutIso = hTg_1100_mupt.Clone("hTg_1100_elept_cutIso")
hTg_1100_eleeta_cutIso = hTg_1100_mueta.Clone("hTg_1100_eleeta_cutIso")
hTg_1100_eled0_cutIso = hTg_1100_mud0.Clone("hTg_1100_eled0_cutIso")

#hTg_1100_muN = ROOT.TH1F("hTg_1100_muN","muon #N",15,-0.5,14.5)
#hTg_1100_eleN =  ROOT.TH1F("hTg_1100_eleN","electron #N",100,0,800)

#Tg_1100_muN = ROOT.TH1F("Tg_1100_muN","muon #N",100,0,800)
#Tg_1100_eleN =  ROOT.TH1F("Tg_1100_eleN","electron #N",100,0,800)

hTg_1100_mudr = ROOT.TH1F("hTg_1100_mudr_genreco","muon #dr gen/reco",63,0,6.3)
hTg_1100_eledr = ROOT.TH1F("hTg_1100_eledr_genreco","electron #dr gen/reco",63,0,6.3)
# For bookkeeping

#------------------------------------------------------Histograms definition reco part ---------------------------#

Tg_1100_mupt = ROOT.TH1F("Tg_1100_mupt","muon p_{T}",100,0,800)
Tg_1100_mueta = ROOT.TH1F("Tg_1100_mueta","muon #eta",100,-4,4)
Tg_1100_mud0 = ROOT.TH1F("Tg_1100_mud0","muon |d_{0}|",100,0,2);
#Tg_1100_elept = ROOT.TH1F("Tg_1100_elept","ele p_{T}",100,0,500)
Tg_1100_elept = Tg_1100_mupt.Clone("Tg_1100_elept")
#Tg_1100_eleeta = ROOT.TH1F("Tg_1100_eleeta","ele #eta",100,-4,4)
Tg_1100_eleeta = Tg_1100_mueta.Clone("Tg_1100_eleeta")
#Tg_1100_eled0 = ROOT.TH1F("Tg_1100_eled0","ele |d_{0}|",200,0,2);
Tg_1100_eled0 = Tg_1100_mud0.Clone("Tg_1100_eled0")

# Booking soms histograms after cuts, I clone the histograms of muons to make the ones of electrons because I want them to have the same scale so I can compare them later.

#Tg_1100_mupt_cut = ROOT.TH1F("Tg_1100_mupt_cut","muon p_{T}",100,0,2000)
Tg_1100_mupt_cut = Tg_1100_mupt.Clone("Tg_1100_mupt_cut")
#Tg_1100_mueta_cut = ROOT.TH1F("Tg_1100_mueta_cut","muon #eta",100,-4,4)
Tg_1100_mueta_cut = Tg_1100_mueta.Clone("Tg_1100_mueta_cut")
#Tg_1100_mud0_cut = ROOT.TH1F("Tg_1100_mud0_cut","muon |d_{0}|",200,0,2);
Tg_1100_mud0_cut = Tg_1100_mud0.Clone("Tg_1100_mud0_cut")
#Tg_1100_elept_cut = ROOT.TH1F("Tg_1100_elept_cut","ele p_{T}",100,0,500)
Tg_1100_elept_cut = Tg_1100_mupt.Clone("Tg_1100_elept_cut")
#Tg_1100_eleeta_cut = ROOT.TH1F("Tg_1100_eleeta_cut","ele #eta",100,-4,4)
Tg_1100_eleeta_cut = Tg_1100_mueta.Clone("Tg_1100_eleeta_cut")
#Tg_1100_eled0_cut = ROOT.TH1F("Tg_1100_eled0_cut","ele |d_{0}|",200,0,2);
Tg_1100_eled0_cut = Tg_1100_mud0.Clone("Tg_1100_eled0_cut")

# Histograms with the Iso_cut

Tg_1100_mupt_cutIso = Tg_1100_mupt.Clone("Tg_1100_mupt_cutIso")
Tg_1100_mueta_cutIso = Tg_1100_mueta.Clone("Tg_1100_mueta_cutIso")
Tg_1100_mud0_cutIso = Tg_1100_mud0.Clone("Tg_1100_mud0_cutIso")
Tg_1100_elept_cutIso = Tg_1100_mupt.Clone("Tg_1100_elept_cutIso")
Tg_1100_eleeta_cutIso = Tg_1100_mueta.Clone("Tg_1100_eleeta_cutIso")
Tg_1100_eled0_cutIso = Tg_1100_mud0.Clone("Tg_1100_eled0_cutIso")

ING=5


# Lorentz vectors definition


lvmu=ROOT.TLorentzVector()
lvele=ROOT.TLorentzVector()

lvmu_reco=ROOT.TLorentzVector()
lvele_reco=ROOT.TLorentzVector()

ii=0
nevents=ch.GetEntries()

# Start of the loop over the events in my data

for iev in ch:
	ii+=1
	if ii>5000:
		continue
#	for imu_reco in range(0,iev.nMuons_pc):
#		lvmu_reco.SetPtEtaPhiE(iev.pt_muon_pc[imu_reco],iev.eta_muon_pc[imu_reco],iev.phi_muon_pc[imu_reco],iev.E_muon_pc[imu_reco])
		# Loop over muons - fill in lorentz vector and fill some histograms

	for imu_gen in range(0,iev.nMcParticles_pc) :
		if abs(iev.type_mcParticle_pc[imu_gen]) == 13 and abs(iev.motherType_mcParticle_pc[imu_gen]) ==  1000006:
			lvmu.SetPtEtaPhiE(iev.pt_mcParticle_pc[imu_gen],iev.eta_mcParticle_pc[imu_gen],iev.phi_mcParticle_pc[imu_gen],iev.E_mcParticle_pc[imu_gen])
			passedCut_muon = False
			if iev.pt_mcParticle_pc[imu_gen]>10 and iev.v0_mcParticle_pc[imu_gen]<4 and iev.vz_mcParticle_pc[imu_gen]<30: #Var_cut
				passedCut_muon = True
			if passedCut_muon == False:
				continue
			hTg_1100_mupt.Fill(iev.pt_mcParticle_pc[imu_gen])
			hTg_1100_mueta.Fill(iev.eta_mcParticle_pc[imu_gen])
        		hTg_1100_mud0.Fill(abs(iev.d0_mcParticle_pc[imu_gen]))
			#passedCut_muon = False
			#if iev.pt_mcParticle_pc[imu_gen]>10 and iev.v0_mcParticle_pc[imu_gen]<4 and iev.vz_mcParticle_pc[imu_gen]<30: #Var_cut
			#if iev.v0_mcParticle_pc[imu_gen]<4:
			#if iev.vz_mcParticle_pc[imu_gen]<30:

				#passedCut_muon = True
			if passedCut_muon==True:
				for imu_reco in range(0,iev.nMuons_pc):
					lvmu_reco.SetPtEtaPhiE(iev.pt_muon_pc[imu_reco],iev.eta_muon_pc[imu_reco],iev.phi_muon_pc[imu_reco],iev.E_muon_pc[imu_reco])
					hTg_1100_mudr.Fill(lvmu.DeltaR(lvmu_reco))						
					if (lvmu.DeltaR(lvmu_reco)>0.05):
						continue
					hTg_1100_mupt_cut.Fill(iev.pt_mcParticle_pc[imu_gen])
					hTg_1100_mueta_cut.Fill(iev.eta_mcParticle_pc[imu_gen])
	        			hTg_1100_mud0_cut.Fill(abs(iev.d0_mcParticle_pc[imu_gen]))
										
					passedCut_id_iso_muon = False
					if not iev.isId_muon_pc[imu_reco] == 0 and iev.pt_muon_pc[imu_reco]>25 and not iev.isIso_muon_pc[imu_reco] == 0: #Id_cut
							
						passedCut_id_iso_muon = True

					if passedCut_id_iso_muon==True:
								#Tg_1100_mupt.Fill(iev.pt_mcParticle_pc[imu_nmu])	
								#Tg_1100_mueta.Fill(iev.eta_mcParticle_pc[imu_nmu])	
	        						#Tg_1100_mud0.Fill(abs(iev.d0_mcParticle_pc[imu_nmu]))	
						#		if iev.isIso_muon_pc[imu_nmu] == 1:
						hTg_1100_mupt_cutIso.Fill(iev.pt_mcParticle_pc[imu_gen])	
						hTg_1100_mueta_cutIso.Fill(iev.eta_mcParticle_pc[imu_gen])	
						hTg_1100_mud0_cutIso.Fill(abs(iev.d0_mcParticle_pc[imu_gen]))
					break
				#if iev.type_mcParticle_pc[imu_gen] == 1:
				#	hTg_1100_mupt_cutIso.Fill(iev.pt_mcParticle_pc[imu_gen])
				#	hTg_1100_mueta_cutIso.Fill(iev.eta_mcParticle_pc[imu_gen])
				#	hTg_1100_mud0_cutIso.Fill(iev.d0_mcParticle_pc[imu_gen])
		
# Loop over muons - fill in lorentz vector and fill some histograms

	#for iele_reco in range(0,iev.nElectrons_pc):
	#	lvele_reco.SetPtEtaPhiE(iev.pt_electron_pc[iele_reco],iev.eta_electron_pc[iele_reco],iev.phi_electron_pc[iele_reco],iev.E_electron_pc[iele_reco])
	
	for iele_gen in range(0,iev.nMcParticles_pc):
		if abs(iev.type_mcParticle_pc[iele_gen]) == 11 and abs(iev.motherType_mcParticle_pc[iele_gen]) ==  1000006:
			lvele.SetPtEtaPhiE(iev.pt_mcParticle_pc[iele_gen],iev.eta_mcParticle_pc[iele_gen],iev.phi_mcParticle_pc[iele_gen],iev.E_mcParticle_pc[iele_gen])
		#if abs(iev.motherType_mcParticle_pc[iele_gen]) ==  1000006:
			passedCut_electron = False
			if iev.pt_mcParticle_pc[iele_gen]>10 and iev.v0_mcParticle_pc[iele_gen]<4 and iev.vz_mcParticle_pc[iele_gen]<30: #Var_cut
				passedCut_electron = True
			if passedCut_electron == False:
				continue
			hTg_1100_eleeta.Fill(iev.eta_mcParticle_pc[iele_gen])
			hTg_1100_elept.Fill(iev.pt_mcParticle_pc[iele_gen])
			hTg_1100_eled0.Fill(abs(iev.d0_mcParticle_pc[iele_gen]))
			
			if passedCut_electron == True:
				for iele_reco in range(0,iev.nElectrons_pc):
					lvele_reco.SetPtEtaPhiE(iev.pt_electron_pc[iele_reco],iev.eta_electron_pc[iele_reco],iev.phi_electron_pc[iele_reco],iev.E_electron_pc[iele_reco])
					hTg_1100_eledr.Fill(lvele.DeltaR(lvele_reco))
					if (lvele.DeltaR(lvele_reco)>0.05):
						continue
					hTg_1100_eleeta_cut.Fill(iev.eta_mcParticle_pc[iele_gen])
					hTg_1100_elept_cut.Fill(iev.pt_mcParticle_pc[iele_gen])
					hTg_1100_eled0_cut.Fill(abs(iev.d0_mcParticle_pc[iele_gen]))
						
					passedCut_id_iso_electron = False
					if not iev.isId_electron_pc[iele_reco] == 0 and iev.pt_electron_pc[iele_reco]>25 and not iev.isIso_electron_pc[iele_reco] == 0: #Id_cut
						passedCut_id_iso_electron = True

					if passedCut_id_iso_electron==True:
								#Tg_1100_elept.Fill(iev.pt_mcParticle_pc[iele_nele])	
								#Tg_1100_eleeta.Fill(iev.eta_mcParticle_pc[iele_nele])	
	        						#Tg_1100_eled0.Fill(abs(iev.d0_mcParticle_pc[iele_nele]))	
						#		if iev.isIso_electron_pc[iele_nele] == 1:
						hTg_1100_elept_cutIso.Fill(iev.pt_mcParticle_pc[iele_gen])	
						hTg_1100_eleeta_cutIso.Fill(iev.eta_mcParticle_pc[iele_gen])	
						hTg_1100_eled0_cutIso.Fill(abs(iev.d0_mcParticle_pc[iele_gen]))
					break



				#if iev.type_mcParticle_pc[iele_gen] == 1:
				#	hTg_1100_elept_cutIso.Fill(iev.pt_mcParticle_pc[iele_gen])
				#	hTg_1100_eleeta_cutIso.Fill(iev.eta_mcParticle_pc[iele_gen])
				#	hTg_1100_eled0_cutIso.Fill(iev.d0_mcParticle_pc[iele_gen])

# END OF THE LOOPO !

















#PLOTS
t3_cut=ROOT.TCanvas()
t3_cut.Divide(2,2)
t3_cut.cd(1)
ROOT.gPad.SetGridy()
hTg_200_mupt.Rebin(ING)
hTg_200_mupt_cut.Rebin(ING)
hTg_500_mupt.Rebin(ING)
hTg_500_mupt_cut.Rebin(ING)
hTg_800_mupt.Rebin(ING)
hTg_800_mupt_cut.Rebin(ING)
hTg_1100_mupt.Rebin(ING)
hTg_1100_mupt_cut.Rebin(ING)
Tg_200_mupt_eff = ROOT.TEfficiency(hTg_200_mupt_cut,hTg_200_mupt)
Tg_500_mupt_eff = ROOT.TEfficiency(hTg_500_mupt_cut,hTg_500_mupt)
Tg_800_mupt_eff = ROOT.TEfficiency(hTg_800_mupt_cut,hTg_800_mupt)
Tg_1100_mupt_eff = ROOT.TEfficiency(hTg_1100_mupt_cut,hTg_1100_mupt)
Tg_200_mupt_eff.Draw("AP") # A draw axis, P draw points
Tg_500_mupt_eff.Draw("same")
Tg_500_mupt_eff.SetLineColor(8)
Tg_800_mupt_eff.Draw("same")
Tg_800_mupt_eff.SetLineColor(2)
Tg_1100_mupt_eff.Draw("same")
Tg_1100_mupt_eff.SetLineColor(5)
Tg_200_mupt_eff.SetTitle("Reconst. Eff. Muon; p_{T} (GeV); Eff.")

t3_cut.cd(2)
ROOT.gPad.SetGridy()
hTg_200_mud0.Rebin(ING)
hTg_200_mud0_cut.Rebin(ING)
hTg_500_mud0.Rebin(ING)
hTg_500_mud0_cut.Rebin(ING)
hTg_800_mud0.Rebin(ING)
hTg_800_mud0_cut.Rebin(ING)
hTg_1100_mud0.Rebin(ING)
hTg_1100_mud0_cut.Rebin(ING)
Tg_200_mud0_eff = ROOT.TEfficiency(hTg_200_mud0_cut,hTg_200_mud0)
Tg_500_mud0_eff = ROOT.TEfficiency(hTg_500_mud0_cut,hTg_500_mud0)
Tg_800_mud0_eff = ROOT.TEfficiency(hTg_800_mud0_cut,hTg_800_mud0)
Tg_1100_mud0_eff = ROOT.TEfficiency(hTg_1100_mud0_cut,hTg_1100_mud0)
Tg_200_mud0_eff.Draw("AP") # A draw axis, P draw points
Tg_500_mud0_eff.Draw("same")
Tg_500_mud0_eff.SetLineColor(8)
Tg_800_mud0_eff.Draw("same")
Tg_800_mud0_eff.SetLineColor(2)
Tg_1100_mud0_eff.Draw("same")
Tg_1100_mud0_eff.SetLineColor(5)
Tg_200_mud0_eff.SetTitle("Reconst. Eff. Muon; |d_{0}| (cm); Eff.")

t3_cut.cd(3)
ROOT.gPad.SetGridy()
hTg_200_elept.Rebin(ING)
hTg_200_elept_cut.Rebin(ING)
hTg_500_elept.Rebin(ING)
hTg_500_elept_cut.Rebin(ING)
hTg_800_elept.Rebin(ING)
hTg_800_elept_cut.Rebin(ING)
hTg_1100_elept.Rebin(ING)
hTg_1100_elept_cut.Rebin(ING)
Tg_200_elept_eff = ROOT.TEfficiency(hTg_200_elept_cut,hTg_200_elept)
Tg_500_elept_eff = ROOT.TEfficiency(hTg_500_elept_cut,hTg_500_elept)
Tg_800_elept_eff = ROOT.TEfficiency(hTg_800_elept_cut,hTg_800_elept)
Tg_1100_elept_eff = ROOT.TEfficiency(hTg_1100_elept_cut,hTg_1100_elept)
Tg_200_elept_eff.Draw("AP") # A draw axis, P draw points
Tg_500_elept_eff.Draw("same")
Tg_500_elept_eff.SetLineColor(8)
Tg_800_elept_eff.Draw("same")
Tg_800_elept_eff.SetLineColor(2)
Tg_1100_elept_eff.Draw("same")
Tg_1100_elept_eff.SetLineColor(5)
Tg_200_elept_eff.SetTitle("Reconst. Eff. Electron; p_{T} (GeV); Eff.")

t3_cut.cd(4)
ROOT.gPad.SetGridy()
hTg_200_eled0.Rebin(ING)
hTg_200_eled0_cut.Rebin(ING)
hTg_500_eled0.Rebin(ING)
hTg_500_eled0_cut.Rebin(ING)
hTg_800_eled0.Rebin(ING)
hTg_800_eled0_cut.Rebin(ING)
hTg_1100_eled0.Rebin(ING)
hTg_1100_eled0_cut.Rebin(ING)
Tg_200_eled0_eff = ROOT.TEfficiency(hTg_200_eled0_cut,hTg_200_eled0)
Tg_500_eled0_eff = ROOT.TEfficiency(hTg_500_eled0_cut,hTg_500_eled0)
Tg_800_eled0_eff = ROOT.TEfficiency(hTg_800_eled0_cut,hTg_800_eled0)
Tg_1100_eled0_eff = ROOT.TEfficiency(hTg_1100_eled0_cut,hTg_1100_eled0)
Tg_200_eled0_eff.Draw("AP") # A draw axis, P draw points
Tg_500_eled0_eff.Draw("same")
Tg_500_eled0_eff.SetLineColor(8)
Tg_800_eled0_eff.Draw("same")
Tg_800_eled0_eff.SetLineColor(2)
Tg_1100_eled0_eff.Draw("same")
Tg_1100_eled0_eff.SetLineColor(5)
Tg_200_eled0_eff.SetTitle("Reconst. Eff. Electron; |d_{0}| (cm); Eff.")

t3_cut.Update()
t3_cut.Print("Merging_DiffMasses_RecoEff.pdf")
t3_cut.Print("Merging_DiffMasses_RecoEff.png")



