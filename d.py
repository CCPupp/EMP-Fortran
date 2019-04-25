'''
Possible problems:
--Should NGS be 10 or 9?
--RAD(1,X) becomes rad[0][X], RAD(2,X) becomes rad[1][X], RHO(1, X) becomes RHO[0][X]
--EG, RG, EE, RE, AA, BB, FF, SIGM are not defined by the time they're used as CURFIT parameters
--GLS, GUS, FRACS, DNN, GLSN, and GUSN are (10, 5) arrays, but their last entries in DONPUT have only 4 values (DNN, GLSN, and GUSN each have just the one 4-value entry).
--Some loop variables are used as both array indeces and in equations, but arrays start at 1 in FORTRAN instead of 0 in Python. I believe I've adjusted appropriately, but any errors should look here first.
--NCR changed to NDR
--Removed semicolon from this line: RGI[K] = 1.0 / RG[K];
--Changed 'I' to '0' (guessing it was originally a '1') in this line: 80	DO  90  M=I, NGRPN
'''

import math

def d(): 
	COUNT = 0.0
	E = 1.6e-19 
	EIONPR = 34.0e-6 
	IFIT = 1 
	NP = 1
	PI = 3.14159265358979 
	STDRHO = 2.689E+25
	TAU = 0.0
	I = 0
	while (I < 1025) :
		FIRST[I] = math.exp(–I)
		SECOND[I] = math.exp(-I / 1024.0)
		I += 1
	
	#DONPUT initializations
	GLS = [[0.201, 0.5132, 0.7515, 1.0, 1.266], [1.602, 2.027, 2.887, 4.110, 5.202], [0.0, 2.3, 5.2, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.3, 0.5, 1.0, 1.5]]
	GUS = [[0.5132, 0.7515, 1.0, 1.266, 1.602], [2.027, 2.887, 4.110, 5.202, 8.332], [2.3, 5.2, 9.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.5, 1.0, 1.5, 2.0]]
	FRACS = [[0.0358, 0.0641, 0.0728, 0.0934, 0.1170], [0.1343, 0.1814, 0.1288, 0.1209, 0.0515], [0.573, 0.388, 0.039, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.173, 0.362, 0.257, 0.208]]
	NS = [10, 3, 4]
	DNN = [[1.656e22, 7.694e21, 1.417e21, 1.064e22]]
	GLSN = [[4.0, 7.0, 9.0, 13.0]]
	GUSN = [[7.0, 10.0, 13.0, 14.0]]
	NSN = [4]
	
	#Test run initializations follow
	RADS = [[0.0, 2.536e25], [1.0e3, 2.302e25], [2.0e3, 2.0847e25], [3.0e3, 1.882e25], [4.0e3, 1.696e25], [5.0e3, 1.525e25], [6.0e3, 1.367e25], [7.0e3, 1.221e25], [8.0e3, 1.089e25], [9.0e3, 9.670e25], [1.0e3, 8.560e25], [1.5e4, 4.032e24], [2.0e4, 1.840e24], [2.5e4, 8.297e23], [3.0e4, 3.811e23]]
	DR = 50
	NDR = 250
	NT = 16
	HOB = 5000
	RSTART = 500
	if (RSTART + DR * NDR > HOB) :
		DR = (HOB - RSTART) / NDR
	IPROMPT = "YES"
	NGAMMA = "YES"
	ISOMER = "NO"
	
	#LOOP TO FILL THE TIME STEP ARRAYS
	I = 0
	while (I < 10) :
		DTS[I] = 1e-9
		NDTS[I] = 15
		I += 1
	
	NGS = 10
	IRAD = “STA”
	
	#60 branch
	I = 0
	while (I < 15) :
		RAD[0][I] = RADS[0][I]
		RAD[1][I] = RADS[1][I]
		I += 1
	
	#THESE STATEMENTS DETERMINE THE WEAPON PROMPT GAMMA CHARACTERISTICS
	CASEP = 2
	DT = 3e-8
	DTDR = DT / DR
	NMAX = 200
	TRIP = 5e-7
	NCAL = 1
	GCAL = 1e33
	SIZ = 10
	IFUN = 1
	ALPHA = 2e9
	BETA = 5e8
	TPEAK = 1e-7
	
	#THESE STATEMENTS DETERMINE THE PROMPT GAMMA ENERGY GROUPS
	ISPEC = "SPE"
	NSPEC = 0
	SUMS = 0.0
	NGROUP = NS[NSPEC] #330 Branch
	I = 0
	while (I < NGROUP) :
		GRPLO[I] = GLS[I][NSPEC]
		GRPHI[I] = GUS[I][NSPEC]
		FRAC[I] = FRACS[I][NSPEC]
	CURFIT(GRPLO, GRPHI, EG, RG, EE, RE, AA, BB, FF, NGROUP, PI, SIGM)
	
	#THESE STATEMENTS SET UP THE NEUTRON-GAMMA SPECTRUM 
	I2 = 1
	CASEN = 1e30
	ISPECN = "SPE"
	NSPECN = 0
	NGRPN = NSN(NSPECN)
	I = 0
	while (I < NGRPN) :
		GRPLON[I] = GLSN[I][NSPECN]
		GRPHIN[I] = GUSN[I][NSPECN]
		DN[I] = DNN[I][NSPECN]
	
	CONVERT()
	#End of test run initializations
	
	CINC = 3 * NDR * NT 
	CONJ = E / (4.0 * PI) 
	CONQ = 1.0 / (EIONPR * 4.0 * PI) 
	DNT = PI / NT
	DR2 = DR * 0.5 
	DTDR2 = DTDR * 0.5 
	NT2 = NT / 2 
	NTMI1 = NT - 1
	I = 0
	while (I < NDR) :
		R[I] = RSTART + I * DR
		R2[I] = R[I]**2
		if (NP != 2) :
			if (R[I] - 500.0 + DR2 >= 0) : #10
				NPR = I #20
				NP = 2
		I += 1 #30
	
	#PROMPT PARAMETERS
	if (I1 != 2) :
		K = 0
		while (K < NGROUP) : #40
			EERG[K] = (EE[K] * SIGM[K] + EG[K] * (1.0 – SIGM[K])) / RG[K] 
			FC[K] = 1.0 – FF[K] * 1.0e3 / RG[K]
			FREG[K] = FRAC[K] / EG[K]
			RERG[K] = RE[K] / RG[K] * SIGM[K]
			RGI[K] = 1.0 / RG[K]
			K += 1 #50
		N = 0
		while (N < NMAX) :
			TDR[N] = N * DTDR + DTDR2
			ROOT[N] = math.sqrt(TDR[N])
			N += 1 #60
		
	#N-GAMMA PARAMETERS
	if (I1 != 2) : #70
		M = 0
		while (M < NGRPN) : #80
			DN[M] =  DN[M] * CASEN
			M += 1 #90
		
	#ISOMERIC PARAMETERS - not running ISOMER per Colonel Fee
	#if (I1 != 2) : #100
	#	L = 0
	#	while (L < NISO) : #110
	#		ROOTKI[L] = math.sqrt(DI[L])
	#		DII[L] = 1.0 / DI[L]
	#		CONISO[L] = AI[L] * DI[L]
	#		L += 1 #120
		
	#DAWSON INTEGRAL VALUES - not running ISOMER (the only subroutine to use DAWSON) per Colonel Fee
	#A0 = 0.5
	#A1 = 0.241958349
	#A2 = 0.675059021
	#I = 0
	#while (I < 10) :
	#	BI = I
	#	if (I == 0) :
	#		FACTOR[I] = 1.0 #130
	#	else :
	#		FACTOR[I] = (2.0 * BI - 3.0) / ((2.0 * BI - 1.0) * (BI - 1.0)) #140
	#	I += 1 #150
	#K = 0
	#while (K < NGRPI) :
	#	EERGI[K] =  (EEISO[K] * SIGMI[K] + EGISO[K] * (1.0 - SIGMI[K])) / RGISO[K]
	#	FCISO[K] = 1.0 - FFISO[K] * 1e3 / RGISO[K]
	#	RERGI[K] = REISO[K] / RGISO[K] * SIGMI[K]
	#	FREGI[K] = FRANCIS[K] / EGISO[K]
	#	RGISCI[K] = 1.0 / RGISO[K]
	#	K += 1 #160
	
	#RELATIVE AIR DENSITY AND INTEGRAL OF RHO * DR CALCULATION
	reldens(nrad, rad, stdrho, ntm1, dnt, r, hob, dr2, rho, drrho, dr, ndr, nt, rhoh, drrhoh) #170
	NS = 0
	while (NS < NGS) :
		#RESTART check at 180 removed - subroutine not needed in Python
		ITIME = 1 #190
		DT = DTS[NS] #200
		NDT = NDTS[NS]
		DT2 = DT * 0.5
		RDT = 2.0 / (RHO[0][NT2] * DT)
		#"SENSE SWITCH" code at 871 and 872 removed - we have much better ways of aborting programs now!
		if (COUNT - 3.5e6 < 0) : #if >= 0, program terminates
			COUNT = COUNT + CINC #210
			TAU = TAU + DT
			I = 0
			while (I < NDR) :
				J = 0
				while (j < NT) :
					FJH[I][J] = 0.0
					QH1[I][J] = QH[I][J] – QH1[I][J]
					QH[I][J] = 0.0
					J += 1 #220
				J = 0
				while (J < NTM1) :
					Q1[I][J] = Q[I][J] – Q1[I][J]
					Q[I][J] = 0.0
					J += 1 #230
				I += 1 #240
			
			#CALCULATE THE CURRENT AND IONIZATION RATE
			if (I1 != 2) :
				PROMPT()
			if (I2 != 2) :
				NGAMMA()
			if (I3 != 2) :
				ISOMER()
			#CONTINUE at 300 removed, as well as the following PRINT statement
			I = 0
			while (I < NDR ) :
				J = 0
				while (J < NTM1) :
					QH[I][J] = QH[I][J] + QH1[I][J]
					Q[I][J] = Q[I][J] + Q1[I][J]
					J += 1 #310
				J = NT
				QH[I][J] = QH[I][J] + QH1[I][J]
				I += 1 #320
			
			#print to file
			fh = open("D Code Output.txt", "w")
			fh.write("TIME\tRANGE\tCURRENT\tION-RATE(H)\tIONRATE\n")
			#TODO: write data to file
			fh.close()

d()
