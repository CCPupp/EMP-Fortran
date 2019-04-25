'''
15 COMMON variables: nrad, rad[2][30], stdrho, ntm1, dnt, r[250], hob, dr2, rho[250][15], drrho[250][15], dr, ndr, nt, rhoh[250][16], drrhoh[250][16]

7 local variables: m, j, cost, h1, h2, rhod, i

Possible problems:
--Several references to R(1) in the original code, which I changed to r[0] in Python. Similarly, RHO(1, X) becomes rho[0][X], and DRRHO(1, X) becomes drrho[0][X].
--Some loop variables are used as both array indeces and in equations, but arrays start at 1 in FORTRAN instead of 0 in Python. I believe I've adjusted appropriately, but any errors should look here first.
--Several calls to TABLIN, at this time we're unsure if we're translating the function or able to use a similar one in Python
----Update: Dylan has written a Python version of TABLIN

Original FORTRAN code (block of COMMON variables omitted):
DO  10  M = 1, NRAD
RAD(2,M) = ALOG(RAD(2,M) / STDRHO)
10	CONTINUE 
DO  30  J = 1, NTM1
COST = COSF(J * DNT)
H1 = R(1) * COST + HOB
H2 = ( R(1) – DR2) * COST + HOB 
RHO (1, J) =EXP (TABLIN(RAD, 2, NRAD, H1, 1) )
RHOD = EXP (TABLIN(RAD, 2, NRAD, H2, 1) )
DRRHO(1, J) = RHOD * DR
DO  20  I = 2, NDR
H1 = R (I) * COST + HOB
H2 = (R(I) – DR2) * COST + HOB 
RHO(I, J) =EXP (TABLIN(RAD, 2, NRAD, H1, 1) )
RHOD = EXP (TABLIN(RAD, 2, NRAD, H2, 1) )
DRRHO(I, J) = RHOD * DR + DRRHO(I-1, J)
20	CONTINUE 
30	CONTINUE 
DO  50  J = 1, NT
COST = COSF( (J – 0.5) * DNT)
H1 = R(1) * COST + HOB
H2 = ( R(1) – DR2) * COST + HOB 
RHOH(1, J) = EXP (TABLIN (RAD, 2, NRAD, H1, 1) )
RHOD = EXP (TABLIN (RAD, 2, NRAD, H2, 1) )
DRRHOH (1, J) = RHOD * DR
DO  40  I = 2, NDR
H1 = R(I) * COST + HOB
H2 = (R(I) – DR2) * COST + HOB 
RHOH (I, J) =EXP (TABLIN (RAD, 2, NRAD, H1, 1) )
RHOD = EXP (TABLIN (RAD, 2, NRAD, H1, 1) )
DRRHOH (I, J) = RHOD * DR + DRRHOH (I-1, J) 
40	CONTINUE 
50	CONTINUE 
RETURN
END
'''

import math
import tablin

def reldens(nrad, rad, stdrho, ntm1, dnt, r, hob, dr2, rho, drrho, dr, ndr, nt, rhoh, drrhoh) :
	m = 0
	while (m < nrad) :
		rad[2][m] = math.log(rad[2][m] / stdrho)
		m += 1 #10
	j = 0
	while (j < ntm1) :
		cost = math.cos((j + 1) * dnt)
		h1 = r[0] * cost + hob
		h2 = (r[0] - dr2) * cost + hob 
		rho[0][j] = math.exp(tablin.tablin(rad, 2, nrad, h1, 1))
		rhod = math.exp(tablin.tablin(rad, 2, nrad, h2, 1))
		drrho[0][j] = rhod * dr
		i = 1
		while (i < ndr) :
			h1 = r[i] * cost + hob
			h2 = (r[i] - dr2) * cost + hob 
			rho[i][j] = math.exp(tablin.tablin(rad, 2, nrad, h1, 1))
			rhod = math.exp(tablin.tablin(rad, 2, nrad, h2, 1))
			drrho[i][j] = rhod * dr + drrho[i-1][j]
			i += 1 #20
		j += 1 #30
	j = 0
	while (j < nt) :
		cost = math.cos((j + 0.5) * dnt)
		h1 = r[0] * cost + hob
		h2 = (r[0] – dr2) * cost + hob
		rhoh[0][j] = math.exp(tablin.tablin(rad, 2, nrad, h1, 1))
		rhod = math.exp(tablin.tablin(rad, 2, nrad, h2, 1))
		drrhoh[0][j] = rhod * dr
		i = 1
		while (i < ndr) :
			h1 = r[i] * cost + hob
			h2 = (r[i] – dr2) * cost + hob
			rhoh[i][j] = math.exp(tablin.tablin(rad, 2, nrad, h1, 1))
			rhod = math.exp(tablin.tablin(rad, 2, nrad, h1, 1))
			drrhoh[i][j] = rhod * dr + drrhoh[i-1][j]
			i += 1 #40
		j += 1 #50
