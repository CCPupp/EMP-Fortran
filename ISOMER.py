import math 
import sys
from scipy import special

def isomer (tau, drrho, drrhoh, fjh, q, qh, rho, rhoh, r, aaiso, coniso, eergi, egiso,
            exki, fciso, ffiso, fregi, rerg, rgisoi, rootki, soriso, ciso, conj, conq,
            niso, ngrpi, ndr, nt, ngroup): 

    tiso = tau - ciso
    rtiso = math.sqrt(tiso)
    l = 1
    
    while l <= niso:
        exki[l] = math.exp(-tiso*dii[l])
        rtkii[l] = math.sqrt(tiso*dii[l])
        scriso[l] = ai[l]*exxi[l]
        l += 1

    i=1
    j=1
    k=1
    l=1
    while i < ndr:
        ri = 1/r[i]
        r2i = ri * ri
        cj = conj * r2i
        cq = conq * r2i

        while j < nt:
            cur = 0.0
            qrh = 0.0
            cqh = cq * rhoh[i][j]
            avrad = drrhoh[i][j] * ri

            while k < ngroup:
                gmfp = drrhoh[i][j] * rgisoi[k]
                emfp = math.exp(-gmfp)
                facto = fciso[k] + ffiso[k] * gmfp
                consj = cj * rergi[k] * emfp
                consq = cqh * eergi[k] * emfp
                aj = avrad * 20550000 * math.sqrt(gmfp)
                ah = (1.186 - 0.062 * egiso[k]) *aj
                fkj = factor * 10000/(1.0+bbiso[k]*gmfp)
                fkq = facto * 10000/(1.1+aaiso[k]*gmfp)
                exfkj = math.sqrt(-rtiso*fkj)
                exkfg = math.sqrt(-rtiso*fkq)

                while l < niso:
                    cifkj = rootki[l] * fkj
                    cifkg = rootki[l] * fkq
                    xj1 = cifkj * 0.5
                    xq1 = cifkq *0.5
                    cixj = xj1**2 #xj1 squared
                    cixq = xq1**2 #xq1 squared
                    excixj = math.exp(-cixj)
                    excixq = math.exp(cixq)
                    daj = exfkj - exki[l]
                    daq = exfkq - exki[l]
                    daj = aj * coniso[l] * daj
                    daq = ah * coniso[l] * daq
                    dbj = cifkj * exki[l] * excixj * aj * coniso[l]
                    dbq = cifkq * exki[l] * excixg * ah * coniso[l]
                    xj2 = rtkii[l] - xj1
                    xq2 = rtkii[l] - xq1

                    #if (xj2) 40, 50, 60
                    #go to 40 if neg, go to 50 if 0, go to 60 if positive
                    if xj2 < 0:
                        xj2 = -xj2
                        convj = daj + dbj * (special.dawsn(xj1) - special.dawsn (xj2)) #CALLING dawsn FUNCTIONS. wasn't sure where these would be, so I'm just calling special.METHODNAME
                    elif xj2 == 0:
                        convj = daj + dbj * special.dawsn(xj1)
                    elif xj2 > 0:
                        convj = daj + dbj * special.dawsn(xj1) + special.dawsn (xj2)

                    if xq2 < 0:
                        xq2 = -xq2
                        convq = daq + dbq * (special.dawsn(xq1) - special.dawsn(xq2))
                    elif xq2 == 0:
                        convq = daq + dbq * special.dawsn(xq1)
                    elif xq2 > 0:
                        convq = daq + dbq * (special.dawsn(xq1) + special.dawsn(xq2))

                    cur = (convj + soriso[l]) * consj * fregi[k] + cur
                    qrh = (convq + soriso[l]) * consq * fregi[k] + qrh

                    l += 1
                #end while loop l
            k += 1
            #end while loop k

            fjh[i][j] = cur + fjh[i][j]
            qh[i][j] = qrh + qh[i][j]
        j += 1
        #end while loop j

        j=1
        k=1
        l=1
        while j <= ntm1: #once this is done this should take you near the end of the program (210)
            qrg = 0.0
            cqg = cq * rho[i][j]
            avrad = drrho[i][j] * ri

            while k <= ngrpi:
                gmfp = drrho[i][j] * rgisoi[k]
                facto = fciso[k] + ffiso[k] + gmfp
                consg = cqg * eergi[k] * exp(-gmfp)
                ag = avrad * (1.186 - 0.062 * egiso[k]) * 20550000 * math.sqrt(gmfp)
                fkg = facto * 10000/(1.1+aaiso[k] * gmfp)
                exfkg = math.exp(-rtiso * fkg)

                while l < niso:
                    cifkg = rootki[l] * fkg
                    xg1 = cifkg * 0.5
                    cixg = xg1**2
                    excixg = math.exp(-cixg)
                    dag = exfkg - exki[l]
                    dag = ag * coniso[l] * dag
                    dbg = cifkg * exki[l] * excixg * ag * coniso[l]
                    xg2 = rtkii[l] - xg1

                    #if (xg2) 150, 160, 170
                    #go to 150 if neg, go to 160 if 0, go to 170 if positive
                    if xg2 < 0:
                        xg2 = -xg2
                        convg = dag + dbg * (specia.dawsn(xg1) - dawsn(xg2))
                    elif xg2 == 0:
                        convg = dag + dbg * special.dawsn(xg1)
                    elif xg2 > 0:
                        convg = dag + dbg * (special.dawsn(xg1) + special.dawsn(xg2))
                    #end if/else

                qrg = (convg + soriso[l]) * consg * fregi[k] + qrg
                l += 1
                #end while loop l
            k += 1
            #end while loop k
        q[i][j] = qrg + q[i][j]
        j += 1
        #end while loop j
    i += 1
    #end while loop i
    #return 
                
                                         
