


def CONVO1:
    X3 = 0
	
    for i in NINCR:
	    X3 = SOR(i) * DCG * ROOT(i)
		CONVG = CONVG + X3
		
def CONVO2:
    X3 = 0
    for i in NINCR:
	    X3 = SOR(i) * DCQ * ROOT(i)
		CONVQ = CONVQ + X3
    X3 = 0
    for j in NINCR:
	    X3 = SOR(j) * DCJ * ROOT(j)
		CONVJ = CONVJ + X3
				