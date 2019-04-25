#Code written by C. Lawson Woodward
'''
13 COMMON variables in SOURCE: IFUN, CAY, ALPHA, BETA, TPEAK, PEAK2, DT2, TC1, ALPHA1, BETA1, TC2, SOF, NSOF
Variable 'T' is a parameter passed to the function
Note that variables in all-caps are COMMON, while the rest are local
TABLIN (in line 59) is a function defined elsewhere in the program

Possible problems:
--This is a literal translation of the code, which has problems as pointed out in the meeting on 4/11.
Specifically, local variables 'a' and 'b' are calculated in lines 51 and 52, respectively, but are never used.
They would be used in lines 55 or 57, but as written, the code would generate an error if it reached those lines
	since the variables would be undefined.
The contact suggested that values that would transfer control to the problematic lines
	(specifically, in which (IFUN == 3) AND (T + DT2 - TC1 > 0))
	were never run through the system to generate an error.
In the meeting on 4/23, contact instructed us to comment out all branches where IFUN != 1

Original FORTRAN code (block of COMMON variables omitted):
GO  TO  (10, 20, 30, 100),  IFUN
10	SOURCE=CAY * EXP(ALPHA * T) / (1.0 + EXP( ( ALPHA + BETA) * (T - TPEAK) ) )
	RETURN
20	SO=EXP(ALPHA * T) / (1.0 + EXP( ( ALPHA + BETA) * (T - TPEAK) ) )
	SOURCE=CAY * SO * (2.0 - SO / PEAK2)
	RETURN
30	IF  (T+DT2-TC1)  40, 40 , 70
40	IF  (T-DT2-DT)  50, 50 , 60
50	A=EXP( ( ALPHA1 - ALPHA) * TC1) * (1.0 + EXP( (ALPHA + BETA) * (TC1 - TPEAK) ) )
	B=A * EXP( (ALPHA + BETA1) * TC2) / (1.0 + EXP( (ALPHA + BETA) * (TC2 - TPEAK) ) )
60	SOURCE=CAY * EXP(ALPHA1 * T)
	RETURN
70	IF  (T+DT2-TC2)  80, 80, 90
80	SOURCE=CAY * A * EXP(ALPHA * T) / (1.0 + EXP( ( ALPHA + BETA) * (T - TPEAK) ) )
	RETURN
90	SOURCE=CAY * B * EXP(-BETA1 * T)
	RETURN
100	SOURCE=CAY * EXP(TABLIN(SOF, 2, NSOF, T, 2) )
	RETURN
	END
'''

import math

def source(T, IFUN, CAY, ALPHA, BETA, TPEAK, PEAK2, DT2, TC1, ALPHA1, BETA1, TC2, SOF, NSOF) :
	result = 0
	if (IFUN <= 1 or IFUN > 4) : #10
		result = CAY * math.exp(ALPHA * T) / (1.0 + math.exp((ALPHA + BETA) * (T - TPEAK)))
	
	#All branches where IFUN != 1 ignored for now
	#elif (IFUN == 2) : #20
	#	SO = math.exp(ALPHA * T) / (1.0 + math.exp((ALPHA + BETA) * (T - TPEAK)))
	#	result = CAY * SO * (2.0 - SO / PEAK2)
	#elif (IFUN == 3) : #30
	#	if (T + DT2 - TC1 <= 0) : #directs to 40, 40 , 70
	#		if  (T - DT2 - DT <= 0) : #40; directs to 50, 50 , 60
	#			a = math.exp((ALPHA1 - ALPHA) * TC1) * (1.0 + math.exp((ALPHA + BETA) * (TC1 - TPEAK))) #50
	#			b = a * math.exp((ALPHA + BETA1) * TC2) / (1.0 + math.exp((ALPHA + BETA) * (TC2 - TPEAK)))
	#		result = CAY * math.exp(ALPHA1 * T) #60
	#	elif (T + DT2 - TC2 <= 0) : #70; directs to 80, 80, 90
	#		result = CAY * a * math.exp(ALPHA * T) / (1.0 + math.exp(( ALPHA + BETA) * (T - TPEAK))) #80
	#	else :
	#		result = CAY * b * math.exp(-BETA1 * T) #90
	#else : #100; only reaches here if IFUN == 4
	#	result = CAY * math.exp(tablin(SOF, 2, NSOF, T, 2))
	
	return result
