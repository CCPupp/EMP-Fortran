import math
import sys
from scipy import special


def isomer(aaiso, ciso, conj, conq, coniso, dii, drrho, drrhoh, eergi, egiso, exki,
           fciso, ffiso, fjh, fregi, niso, ngrpi, ndr, nt, ngroup, q, qh, rho,
           rhoh, r, rerg, rgisoi, rootki, soriso, tau): 

    tiso = tau - ciso

    #IF (TISO) 10, 20, 20                                                          #10
    if (tiso < 0):
        #RETURN  
        return
    
    rtiso = math.sqrt(tiso)                                                        #20
    l = 1

    while (l < niso):
        exki[l-1] = math.exp(-tiso*dii[l-1])   #Changed [l] to [l-1] because Python arrays start at 1.
        rtkii[l-1] = math.sqrt(tiso*dii[l-1])  #Changed [l] to [l-1]
        soriso[l-1] = ai[l-1]*exxi[l-1]      #Changed [l] to [l-1]
        l += 1
    #CONTINUE end while loop                                                        #30

    i = 1
    j = 1
    k = 1
    l = 1
    while (i < ndr): #ENDS AT 220
        ri = 1/r[i-1]   #Changed [i] to [i-1] 
        r2i = ri * ri
        cj = conj * r2i
        cq = conq * r2i

        while (j < nt): #ENDS AT 140
            cur = 0.0
            qrh = 0.0
            cqh = cq * rhoh[i-1][j-1]         #Changed [i] and [j] to [i-1] [j-1]
            avrad = drrhoh[i-1][j-1] * ri     #Changed [i] and [j] to [i-1] [j-1]

            while (k < ngroup): #ENDS AT 130
                gmfp = drrhoh[i-1][j-1] * rgisoi[k-1] #Changed [x] to [x-1]
                emfp = math.exp(-gmfp)
                facto = fciso[k-1] + ffiso[k-1] * gmfp    #Changed [x] to [x-1]
                consj = cj * rergi[k-1] * emfp      #Changed [x] to [x-1]
                consq = cqh * eergi[k-1] * emfp     #Changed [x] to [x-1]
                aj = avrad * 20550000 * math.sqrt(gmfp)
                ah = (1.186 - 0.062 * egiso[k-1]) * aj #Changed [x] to [x-1]
                fkj = factor * 10000/(1.0+bbiso[k-1]*gmfp) #Changed [x] to [x-1]
                fkq = facto * 10000/(1.1+aaiso[k-1]*gmfp) #Changed [x] to [x-1]
                exfkj = math.sqrt(-rtiso*fkj)
                exkfg = math.sqrt(-rtiso*fkq)

                while (l < niso): #ENDS AT 120
                    cifkj = rootki[l-1] * fkj  #Changed [x] to [x-1]
                    cifkg = rootki[l-1] * fkq  #Changed [x] to [x-1]
                    xj1 = cifkj * 0.5
                    xq1 = cifkq * 0.5
                    cixj = xj1**2  # xj1 squared
                    cixq = xq1**2  # xq1 squared
                    excixj = math.exp(-cixj)
                    excixq = math.exp(cixq)
                    daj = exfkj - exki[l-1]  #Changed [x] to [x-1]
                    daq = exfkq - exki[l-1]  #Changed [x] to [x-1]
                    daj = aj * coniso[l-1] * daj  #Changed [x] to [x-1]
                    daq = ah * coniso[l-1] * daq  #Changed [x] to [x-1]
                    dbj = cifkj * exki[l-1] * excixj * aj * coniso[l-1]  #Changed [x] to [x-1]
                    dbq = cifkq * exki[l-1] * excixg * ah * coniso[l-1]  #Changed [x] to [x-1]
                    xj2 = rtkii[l-1] - xj1  #Changed [x] to [x-1]
                    xq2 = rtkii[l-1] - xq1  #Changed [x] to [x-1]

                    # if (xj2) 40, 50, 60
                    # go to 40 if neg, go to 50 if 0, go to 60 if positive
                    if (xj2 < 0): #if neg
                        xj2 = -xj2                                                   #40
                        # CALLING dawsn FUNCTIONS. wasn't sure where these would be, so I'm just calling special.METHODNAME
                        convj = daj + dbj * (special.dawsn(xj1) - special.dawsn(xj2))
                        #GOTO 70
                    elif (xj2 == 0): 
                        convj = daj + dbj * special.dawsn(xj1)                       #50
                        #GO TO 70
                    else: #elif (xj2 > 0)
                        convj = daj + dbj * special.dawsn(xj1) + special.dawsn(xj2)  #60
                    #CONTINUE                                                        #70

                    if (xq2 < 0):
                        xq2 = -xq2                                                   #80
                        convq = daq + dbq * (special.dawsn(xq1) - special.dawsn(xq2))
                        #GO TO 110
                    elif (xq2 == 0):
                        convq = daq + dbq * special.dawsn(xq1)                       #90
                        #GO TO 110
                    else: #elif (xq2 > 0):
                        convq = daq + dbq * (special.dawsn(xq1) + special.dawsn(xq2))#100
                    #CONTINUE                                                        #110

                    cur = (convj + soriso[l-1]) * consj * fregi[k-1] + cur #Changed [x] to [x-1]
                    qrh = (convq + soriso[l-1]) * consq * fregi[k-1] + qrh #Changed [x] to [x-1]

                    l += 1
                #CONTINUE end while loop l                                           #120
            k += 1
            # CONTINUE end while loop k                                              #130

            fjh[i-1][j-1] = cur + fjh[i-1][j-1] #Changed [x] to [x-1]
            qh[i-1][j-1] = qrh + qh[i-1][j-1]   #Changed [x] to [x-1]
        j += 1
        #CONTINUE  end while loop j                                                  #140

        j = 1
        k = 1
        l = 1
        while (j < ntm1): #ENDS AT 210
            qrg = 0.0
            cqg = cq * rho[i-1][j-1]                   #Changed [x] to [x-1]
            avrad = drrho[i-1][j-1] * ri               #Changed [x] to [x-1]

            while (k < ngrpi): #ENDS AT 200
                gmfp = drrho[i-1][j-1] * rgisoi[k-1]   #Changed [x] to [x-1]
                facto = fciso[k-1] + ffiso[k-1] + gmfp #Changed [x] to [x-1]
                consg = cqg * eergi[k-1] * exp(-gmfp)  #Changed [x] to [x-1]
                ag = avrad * (1.186 - 0.062 *
                              egiso[k-1]) * 20550000 * math.sqrt(gmfp) #Changed [x] to [x-1]
                fkg = facto * 10000/(1.1+aaiso[k-1] * gmfp) #Changed [x] to [x-1]
                exfkg = math.exp(-rtiso * fkg)

                while (l < niso): #ENDS AT 190
                    cifkg = rootki[l-0] * fkg            #Changed [x] to [x-1]
                    xg1 = cifkg * 0.5
                    cixg = xg1**2
                    excixg = math.exp(-cixg)
                    dag = exfkg - exki[l-1]            #Changed [x] to [x-1]
                    dag = ag * coniso[l-1] * dag       #Changed [x] to [x-1]
                    dbg = cifkg * exki[l-1] * excixg * ag * coniso[l-1] #Changed [x] to [x-1]
                    xg2 = rtkii[l-1] - xg1             #Changed [x] to [x-1]

                    # if (xg2) 150, 160, 170
                    # go to 150 if neg, go to 160 if 0, go to 170 if positive
                    if (xg2 < 0):
                        xg2 = -xg2                                                    #150
                        convg = dag + dbg * \
                                (special.dawsn(xg1) - special.dawsn(xg2))
                        #GO TO 180
                    elif (xg2 == 0):
                        convg = dag + dbg * special.dawsn(xg1)                        #160
                        #GO TO 180
                    else: #elif (xg2 > 0)
                        convg = dag + dbg * (special.dawsn(xg1) + special.dawsn(xg2)) #170
                    # CONTINUE end if/else                                            #180

                qrg = (convg + soriso[l-1]) * consg * fregi[k-1] + qrg #Changed [x] to [x-1]
                l += 1
                #CONTINUE  end while loop l                                           #190
            k += 1
            #CONTINUE  end while loop k                                               #200
        q[i-1][j-1] = qrg + q[i-1][j-1]                 #Changed [x] to [x-1]
        j += 1
        #CONTINUE end while loop j                                                    #210
    i += 1
    #CONTINUE  end while loop i                                                       #220
# return
