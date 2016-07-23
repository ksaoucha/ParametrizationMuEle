import os, sys
#from MCdata import *
import ROOT
from operator import truediv

EstiList = []
RealYieldList = []
Mass = 1100
# ----------Tab later------------#
#1, 10, 100
#for Mass in [200, 500, 800, 1100]:
for Ctau in [1, 10, 100]:
	Estimated_yield = 0
	pathToRootFile="Downloads/"
	inputEfficiency = ROOT.TFile("/home/ksaoucha/Documents/ResultingEff_m"+ str(Mass)+"_Ctau" + str(Ctau) + "_MuEl.root","read") # Closure test for sample i
	#inputEfficiency = ROOT.TFile("/home/ksaoucha/Documents/ResultingEff_All_BeamSpot.root","read") # Closure test with mean parametrization
	inputNtuples = ROOT.TChain("preCutTree","preCutTree")	
	inputNtuples.Add(pathToRootFile+"Samples_d0BeamSpot/DisplacedTop_Run2_TopTree_Study_stopTobl_m" + str(Mass) + "_Ctau" + str(Ctau) + "_MuEl_NoBlinding_1(1).root") 
	rootkeys = inputEfficiency.GetListOfKeys()
	#rootkeys = inputNtuples.GetListOfKeys()
	histnames = []
	for key in rootkeys:
		histnames.append(key.GetName())
	print histnames


#---Loop over event ---#
	j=0
	jj=0
	ii=0
	nevents=inputNtuples.GetEntries()
	for iev in inputNtuples:
		ii+=1
		#if ii>20:
		#	continue
		W_mud0=0
		W_mupt=0
		W_eled0=0
		W_elept=0
		k_loop = 0
		for i_gen in range(0,iev.nMcParticles_pc) :
			if abs(iev.motherType_mcParticle_pc[i_gen]) ==  1000006 and abs(iev.d0BeamSpot_mcParticle_pc[i_gen])<10 and iev.pt_mcParticle_pc[i_gen]>10 and iev.v0_mcParticle_pc[i_gen]<4 and iev.vz_mcParticle_pc[i_gen]<30:
				if abs(iev.type_mcParticle_pc[i_gen]) == 13 and iev.pt_mcParticle_pc[i_gen] != 0 and abs(iev.d0BeamSpot_mcParticle_pc[i_gen]) != 0:
					hg_mud0_eff=inputEfficiency.Get(histnames[0])
					h_mupt_eff=inputEfficiency.Get(histnames[2])
					mud0_value = abs(iev.d0BeamSpot_mcParticle_pc[i_gen])
					mupt_value = iev.pt_mcParticle_pc[i_gen]
					Bin_mud0_value = hg_mud0_eff.GetTotalHistogram().FindBin(mud0_value)
					Bin_mupt_value = h_mupt_eff.GetTotalHistogram().FindBin(mupt_value)
					W_mud0 = hg_mud0_eff.GetEfficiency(Bin_mud0_value)
					W_mupt = h_mupt_eff.GetEfficiency(Bin_mupt_value)
					#continue
				#	print "++++++++++++++++++++++++++++"
					#print "mud0_value = ",mud0_value
					#print "mupt_value = ",mupt_value
				#else :
				#	print "++++++++++++++++++++++++++++"
				#	print "NO MUON IN THIS MCnumber"
				#print " ------ "
			#for iele_gen in range(0,iev.nMcParticles_pc):
				if abs(iev.type_mcParticle_pc[i_gen]) == 11 and iev.pt_mcParticle_pc[i_gen] != 0 and not abs(iev.d0BeamSpot_mcParticle_pc[i_gen]) != 0:
					hg_eled0_eff=inputEfficiency.Get(histnames[1])
					h_elept_eff=inputEfficiency.Get(histnames[3])
					eled0_value = abs(iev.d0BeamSpot_mcParticle_pc[i_gen])
					elept_value = iev.pt_mcParticle_pc[i_gen]
					Bin_eled0_value = hg_eled0_eff.GetTotalHistogram().FindBin(eled0_value)
					Bin_elept_value = h_elept_eff.GetTotalHistogram().FindBin(elept_value)
					W_eled0 = hg_eled0_eff.GetEfficiency(Bin_eled0_value)
					W_elept = h_elept_eff.GetEfficiency(Bin_elept_value)
					#continue
					#print "eled0_value = ",eled0_value
					#print "elept_value = ",elept_value
				#else :
				#	print "NO ELECTRON IN THIS MCnumber"
				W_event = W_mud0*W_mupt*W_eled0*W_elept
			Estimated_yield = Estimated_yield + W_event
				
			"""print "Estimated_yield =",Estimated_yield
			print "W_mud0 = ", W_mud0 
			print "W_mupt = ", W_mupt
			print "W_eled0 = ", W_eled0
			print "W_elept = ", W_elept
			k_loop+=1
			print "MCnumber = ", k_loop
			print " event number ii : ", ii"""

				#jj+=1 #Total passed number of events
			#	if W_eled0==0:
			#		print "W_eled0 = ", W_eled0
			#		j+=1
			#		print " #Event = ", j
	#--------END OF LOOP OVER THE EVENT-----------------------------------------------#


	print "Estimated_yield_"+str(Mass)+"_"+str(Ctau)+"=", Estimated_yield
	EstiList.append(Estimated_yield)
	print "EstiList =", EstiList
	print "#Event = ", jj
	print "ii =", ii

#	print "Bin_mud0_value =", Bin_mud0_value
#	print "Bin_eled0_value =", Bin_eled0_value
#	print "Bin_mupt_value =", Bin_mupt_value
#	print "Bin_elept_value =", Bin_elept_value
#	for i_mud0_bin in range(1,hg_mud0_eff.GetTotalHistogram().GetNbinsX()):
#		print "i_mud0_bin =", i_mud0_bin
#		print "value is", hg_mud0_eff.GetEfficiency(i_mud0_bin)
#	for i_eled0_bin in range(1,hg_eled0_eff.GetTotalHistogram().GetNbinsX()):
#		print "i_eled0_bin =", i_eled0_bin
#		print "value is", hg_eled0_eff.GetEfficiency(i_eled0_bin)
#	for i_mupt_bin in range(1,h_mupt_eff.GetTotalHistogram().GetNbinsX()):
#		print "i_mupt_bin =", i_mupt_bin
#		print "value is", h_mupt_eff.GetEfficiency(i_mupt_bin)
#	for i_elept_bin in range(1,h_elept_eff.GetTotalHistogram().GetNbinsX()):
#		print "i_elept_bin =", i_elept_bin
#		print "value is", h_elept_eff.GetEfficiency(i_elept_bin)

#-------Alternative Way----------#




	inputFiles = ROOT.TChain("tree","tree")
	inputFiles.Add(pathToRootFile+"Samples_d0BeamSpot/DisplacedTop_Run2_TopTree_Study_stopTobl_m" + str(Mass) + "_Ctau" + str(Ctau) + "_MuEl_NoBlinding_1(1).root")
	nevents=inputFiles.GetEntries()
	nevents = 0
	for iev in inputFiles:
		#if abs(iev.d0BeamSpot_muon[0])<10 and abs(iev.d0BeamSpot_electron[0])<10 and iev.pt_muon[0]>10 and iev.v0_muon[0]<4 and iev.vz_muon[0]<30 and iev.pt_electron[0]>10 and iev.v0_electron[0]<4 and iev.vz_electron[0]<30:			
		nevents+=1
			#print nevents
			#if ii>100:
			#	continue
	
	RealYieldList.append(nevents)
	print "RealYieldList =", RealYieldList


	ClosureTest = map(truediv, EstiList, RealYieldList)
	print "Closure test = ", ClosureTest

print "+++++++ corresp +++++++"
print "m200:[0.81, 0.86, 1.22]"
print "m500:[0.91, 0.96, 1.27]"
print "m800:[0.97, 1.01, 1.36]"
print "m1100:[1.02, 1.06, 1.42]"

print "+++++++ MEAN +++++++"
print "m200:[0.76, 0.88, 1.42]"
print "m500:[0.84, 0.94, 1.46]"
print "m800:[0.92, 1.00, 1.53]"
print "m1100:[0.98, 1.07, 1.59]"



