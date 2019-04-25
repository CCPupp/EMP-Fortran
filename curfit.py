import math 
#GRPLOI, GRPHII, EGISO, RGISO, EEISO, REISO, AAISO, BBISO, FFISO, NGRPI, PI, SIGMI) 
def curfit(GL, GH, EG, RG, EE, RE, AA, BB, FF, N, PI, SIGM)
	A=[1.565706, -2.774190, 2.529891, -1.280640, 3.875632E-1, -7.185585E-2, 8.005050E-3, -4.921981E-4, 1.283994E-5]
	B=[2.072634E-1, 4.621258E-1, -8.721357E-1, 6.476889E-1, -2.562205E-1, 5.845509E-2, -7.705808E-3, 5.449037E-4, -1.599049E-5]
	F=[-1.955758E-2, 1.237809E-1, -1.323847E-1, 8.040323E-2, -2.774780E-2, 5.632172E-3, -6.678283E-4, 4.279942E-5, -1.144781E-6]
	E1=2.34574549
	E2=1.41259596
	E3=0.325671156
	E4=0.0200632454
	MC2=0.511
	RHOE=3.888E+22
	R2PI = PI * R0 * R0
	K=1
	while K < N
		EG[K]=(GL[K] + GH[K] ) * 0.5 
		E = EG(K) 
		ALFA = E / MC2 
		A1 = 1.0 + ALFA
		A2 = 1.0 + 2.0 * ALFA 
		A3 = 1.0 + 3.0 * ALFA 
		A4 = math.log(A2) 
		A5 = ALFA * ALFA 
		A6 = A2 * A2
		SIGC = 2.0 * R2PI * (A1 / A5 * (2.0 * A1 / A2 – A4 / ALFA) + A4 / (2.0 * ALFA) – A3 / A6) 
		SIGS = R2PI * (A4 / (ALFA * A5) + 2.0 * A1 * (2.0 * A5 – A2) / (A5 * A6) + 8.0 * A5 / (3.0 * A2 * A6) ) 
		SIGA = SIGC – SIGS
		#double if statement that has wierd control flow.
		if (E - 2.5) < 0
			if E < 1.5
				SIGT=SIGC
			else
				SIGT = SIGC / (1.0 – (E – 2.0) * 0.03)
		EE[K] = SIGA / SIGC * E 
		RG[K] = 1.0 / (SIGT * RHOE) 
		RE[K] = E1 * E * E / (E2 + E) – E3 * E + E4 
		if (E – 7.0) <= 0 
			AA[K] = A[1] 
			BB[K] = B[1] 
			FF[K] = F[1] 
			I = 2
			while I < 9 
				EI = E **(I – 1) 
				AA(K) = AA[K] + A[I] * EI 
				BB(K) = BB[K] + B[I] * EI 
				FF(K) = FF[K] + F[I] * EI
				I=I+1
		
		else
			AF7 = A(1) 
			AF6 = A(1) 
			BF7 = B(1) 
			BF6 = B(1) 
			FF7 = F(1) 
			FF6 = F(1) 
			i = 2
			while i < 9
				AF7 = AF7 + A[I] * 7.0 
				AF6 = AF6 + A[I] * 6.0 
				BF7 = BF7 + B[I] * 7.0 
				BF6 = BF6 + B[I] * 6.0 
				FF7 = FF7 + F[I] * 7.0
				FF6 = FF6 + F[I] * 6.0
				i=i+1
		AA[K] = (E – 7.0) * (AF7 – AF6) + AF7 
		BB[K] = (E – 7.0) * (BF7 – BF6) + BF7 
		FF[K] = (E – 7.0) * (FF7 – FF6) + FF7 
		K = K + 1
	