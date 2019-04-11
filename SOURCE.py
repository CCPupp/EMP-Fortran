'''
GO  TO  (10, 20, 30, 100),  IFUN
10	SOURCE=CAY * EXP(ALPHA * T) / (1.0 + EXP( ( ALPHA + BETA) * (T – TPEAK) ) )
	RETURN
20	SO=EXP(ALPHA * T) / (1.0 + EXP( ( ALPHA + BETA) * (T – TPEAK) ) )
	SOURCE=CAY * SO * (2.0 – SO / PEAK2)
	RETURN
30	IF  (T+DT2–TC1)  40, 40 , 70
40	IF  (T–DT2–DT)  50, 50 , 60
50	A=EXP( ( ALPHA1 – ALPHA) * TC1) * (1.0 + EXP( (ALPHA + BETA) * (TC1 – TPEAK) ) )
	B=A * EXP( (ALPHA + BETA1) * TC2) / (1.0 + EXP( (ALPHA + BETA) * (TC2 – TPEAK) ) )
60	SOURCE=CAY * EXP(ALPHA1 * T)
	RETURN
70	IF  (T+DT2–TC2)  80, 80, 90
80	SOURCE=CAY * A * EXP(ALPHA * T) / (1.0 + EXP( ( ALPHA + BETA) * (T – TPEAK) ) )
	RETURN
90	SOURCE=CAY * B * EXP(-BETA1 * T)
	RETURN
100	SOURCE=CAY * EXP(TABLIN(SOF, 2, NSOF, T, 2) )
	RETURN
	END
'''

import math

def SOURCE(T, IFUN, CAY, ALPHA, BETA, TPEAK, PEAK2, DT2, TC1, ALPHA1, BETA1, TC2, SOF, NSOF) :
	result = 0
	if (IFUN == 10) :
		result = CAY * math.exp(ALPHA * T) / (1.0 + math.exp((ALPHA + BETA) * (T – TPEAK)))
	elif (IFUN == 20) :
		SO = math.exp(ALPHA * T) / (1.0 + math.exp((ALPHA + BETA) * (T – TPEAK)))
		result=CAY * SO * (2.0 – SO / PEAK2)
	elif (IFUN == 30) :
		if (T + DT2 – TC1 <= 0) : #40, 40 , 70
			if  (T – DT2 – DT <= 0) : #50, 50 , 60
				A = math.exp((ALPHA1 – ALPHA) * TC1) * (1.0 + math.exp((ALPHA + BETA) * (TC1 – TPEAK)))
				B = A * math.exp((ALPHA + BETA1) * TC2) / (1.0 + math.exp((ALPHA + BETA) * (TC2 – TPEAK)))
				result = CAY * math.exp(ALPHA1 * T)
			else :
				
