import source
import sourcen
import math
import sys
from scipy import special

def gamma(ai, ciso, di, dn, dt, edep, edei, eden, engi, engp, engn, frac, fracis, gdoti, gdotn, grphi, grphii,
          grphin, grplo, grploi, grplon, gdot, gtime, gcal, hz, i1, ifun, ndei, nden, ngroup, ngrpi, ngrpn,
          ntrani, rdt, siz, sn, sor, totali, totaln, trani, peak):

    cay = 1.0
    dt = .000000001
    dt2= dt * 0.5
    gcal = gcal/siz
    total = 0.0

    if ((i1 <= 1)  or (i1 > 2)):  #GO TO(10, 160), I1 - STOPS AT 160

        if ((ifun == 2)): #GO TO (30, 20, 30, 30), IFUN            #10 #Colonel Fee mentioned IFUN will always be 1
            ifun2 = ifun                                        
            ifun = 1                                               #20
            ###GO TO 40
                                           
        #if (ncal == 1):                                           #30 #Colonel Fee mentioned IFUN will always be 1 so we need to jump to 40
        i = 2                                                      #40
        while (i < 250): #ENDS AT 50                           
            t1 = i * dt                #Original Fortran had T * DT... I think it was supposed to be I * DT???
            t2 = (i-1) * dt    
            s1 = source.source(t1)
            s2 = source.source(t2)
            i += 1
        #end while loop                                            
            
            if ((s1 - s2) >= 0): #go to 50 if 0 or positive. Go to 60 if negative.
                #CONTINUE                                          #50
                sys.exit("Error occured. ifun is: {0}.".format(ifun)) #Print an error, then "STOP"
                
        peak = s2                                                  #60
        cay = gcal/peak

        if ((ifun2 - 2) == 0):
            peak2 = peak                                           #70
            ifun = ifun2
            if (ncal == 2):
                cay = 1.0                                          #75                    
            i = 1
            while (i < 250):                                       #80
                t = (i - 0.5) * dt
                total = total + source.source(t) * dt
                i += 1
            #end while loop                                        #90
            cay = gcal/total
        #end last two if statements                                #100
            
        ig = 1
        i = 1
        t = 1 * dt2
        t1 = i * dt
        gtime[i-1] = t1           #Original Fortran code had gtime(i). Fortran arrays start at 1.
        gdot[i-1] = source.source(t1)   #Original Fortran code had gdot(i). Fortran arrays start at 1.
        total = source.source(t) * dt

        i = 2
        while (i < 250):
            inn = i
            t = (i - 0.5) * dt
            t1 = i * dt
            gtime[i-1] = t1         #Original Fortran code had gtime(i). Fortran arrays start at 1.
            gdot[i-1] = source.source(t1)  #Original Fortran code had gdot(i). Fortran arrays start at 1.
            total = total + source.source(t) * dt
            if ((ig == 1) or (ig < 1) or (ig > 2)):
                if ((gdot[i-1] - gdot[i-2]) < 0):                    #110  #Original Fortran code had gdot(i) - dgot(i-1). Fortray arrays start at 1.
                    peak = gdot[i-2]                                 #120  #Original Fortran code had gdot(i-1). Fortran arrays start at 1.
                    ig = 2
            i += 1
        #end while loop & if statements                              #130
        ndot = inn

        #PRINT 420, peak, total
        print ("Peak: ", peak, "Total: ", total)

        i = 1
        while (i < 50):
            n1 = i
            n2 = i + 50
            n3 = i + 100
            n4 = 1 + 150
            n5 = i + 200
            print(i, gdot[n1-1], gdot[n2-1], gdot[n3-1], gdot[n4-1], gdot[n5-1]) #Original Fortran code had gdot(n1), gdot(n2), etc. Fortran arrays start at 1.
            i += 1
            #CONTINUE/end while loop                                 #140

        k=1
        while (k < ngroup): 
            n1 = 2 * k
            n2 = 2 * k + 1
            engp[n1-1]= grplo[k-1]   #Changed the arrays in this line and next 3 lines to be (x-1) because Fortran arrays start at 1.
            engp[n2-1] = grphi[k-1]
            edep[n1-1] = frac[k-1]/(grphi[k-1]-grplo[k-1])
            edep[n2-1] = edep[n1-1]
            k += 1
        #CONTINUE                                                     #150

        engp[0] = grplo[0]          #Original Fortran code: engp(1) = grplo(1). Fortran arrays start at 1.
        edep[0] = 0.0               #Changed edep(1) to edep(0)
        ndep = 2 * ngroup + 2
        engp[ndep-1] = grphi[ngroup-1] #Changed arrays from x to x-1 because Fortran arrays start at 1.
        edep[ndep-1] = 0.0             #Changed array from x to x-1 because Fortran arrays start at 1.

    #GO TO (170, 310), I2
    if(i2 == 1):                                                  #160
        rdt = math.exp(tablin.tablin(rad, 2, nrad, hob, 1)/stdrho)       #170
        rdt = 2.0/ (rdt * dt)

        m = 1
        while (m < ngrpn):         
            sor[m-1] = dn[m-1]                                    #180      #Changed sor(m) = dn(m) because Fortran arrays start at 1.
            m += 1

        i = 1
        while (i < 250):
            taut = i * dt
            #if neg go to 210, if 0 or pos go to 190
            if ((taut - tspeak) >= 0):
                #CALL SOURCEN                                     #190
                sourcen.sourcen()
                    
                k = 1
                while (k < ngroup):  
                    gdotn[i-1] = sn[k-1] + gdotn[i-1]             #200  #Changed (x) to (x-1) because Fortran arrays start at 1
                    k += 1
                #end while loop/CONTINUE                          #210
                        
            i += 1
        #end while loop and if statement
                
        rdt = 0.02 * rdt
        summ = 0.0

        m = 1
        while (m < ngrpn-1):  
            dn[m-1] = sor[m-1]                                        #220   #Changed dn(m) = sor(m) because Fortran arrays start at 1
            m += 1

        #CALL SOURCEN
        sourcen.sourcen()
                
        m= 1
        while (m < ngrpn-1):
            dn[m-1] = (sor[m-1] + dn[m-1]) * 0.5 #Changed dn(m) = (sor(m) + dn(m)) because Fortran arrays start at 1

            k= 1
            while ((k-1) < (ngroup-1)): #Changed ngrpn to ngrpn-1  and (k) to (k-1)because Fortran arrays start at 1
                summ = summ + hz[k-1][m-1] * dn[m-1] * 0.00000005       #230   #(x-1) instead of (x) to all arrays because Fortran arrays start at 1
                k += 1
                    
            m += 1 
        #CONTINUE                                                 #240

        i = 1
        while (i < 1000):
            #CALL SOURCEN
            sourcen.sourcen()
            k=1
            while ((k-1) < (ngroup-1)):  #Changed k and ngroup to (k-1) and (ngroup-1) because Fortran arrays start at 1
                summ = summ + sn[k-1] * 0.00000005                #250   #Changed sn(k) because Fortran arrays start at 1
                k += 1
            i += 1
        #CONTINUE                                                 #260

        totalg = summ

        m = 1
        while (m < ngrpn):
            dn[m-1] = sor[m-1]                                         #changed m to m-1 because Fortran arrays start at 1.
            sor[m-1] = 0.0                                        #270 #Changed m to m-1 because Fortran arrays start at 1.
            m += 1

        summ = 0.0

        m = 1
        while (m < ngrpn):
            summ = summ + (grphin[m-1] + grplon[m-1]) * 0.5 * dn[m-1]   #280 #Changed m to m-1 because Fortran arrays start at 1.
            m += 1

        totaln = summ

        #PRINT 440, TOTALN, TOTALG
        print ("totaln is: ", totaln, ". totalg is: ", totalg)

        i = 1
        while (i <  50):
            n1= i
            n2 = i + 50
            n3 = i + 100
            n4 = i + 150
            n5 = i + 200
            print (i, gdotn[n1], gdotn[n2], gdotn[n3], gdotn[n4], gdotn[n5])
            i += 1
        #CONTINUE                                                 #290

        m = 1
        while (m < ngrpn):
            n1 = 2 * m
            n2 = n1 + 1
            engn[n1-1] = grplon[m-1]   #Changed all array locations until end of while loop from x to x-1 because Fortran arrays start at 1.
            engn[n2-1] = grphin[m-1]
            eden[n1-1] = (grplon[m-1] + grphin[m-1]) * 0.5 * dn[m]/((grphin[m-1] - grplon[m-1]) + totaln)
            eden[n2-1] = eden[n1-1]
            m += 1
        #CONTINUE                                                 #300

        engn[0] = grplon[0] #original Fortran code: engn(1) = grplon(1) (Fortran arrays start at 1)
        eden[0] = 0.0       #original Fortran code: eden(1) (Fortran arrays start at 1)
        nden = 2 * ngrpn + 2
        engn[nden-1] = grphin[ngrpn-1] #original Fortran: engn(nden) = grphin(ngrpn) (Fortran arrays start at 1)
        eden[nden-1] = 0.0    #original Fortran code: eden(nden) (Fortran arrays start at 1)

    #GO TO (320, 400), I3                                         #310
    if ((i3 < 2) or (i3 > 2)): #go to end of code if none of these fit

        i = 1
        while (i < 250):                                          #320
            t = i * dt
            tiso = t - ciso
            if ((t-ciso) >= 0):
                summ = 0.0                                        #330
                l = 1
                while (l < niso):
                    summ = summ + ai[l-1] * math.exp(-tiso/di[0]) * tablin(trani, 2, ntrani, tiso, 2)  #340  #Changed di(1) to di(0) because Fortran arrays start at 1
                    gdoti[i-1] = summ            #Changed gdoti(i) to (i-1) because Fortran arrays start at 1
                    l += 1
            i += 1
        #CONTINUE/ends while & if & while                         #350

        dt = 0.00000001
        summ = 0.0

        i = 1
        while (i < 1000):
            t = (i - 0.5) * dt

            l = 1
            while (l < niso):
                summ = summ + ai[l-1] * dt * math.exp(-t/di[l-1]) * TABLIN(trani, 2, ntrani, t, 2) #360  #Changed ai(l) and di(l) because Fortran arrays start at 1.
                l += 1
            i += 1
        #CONTINUE - ends previous two while loops                 #370

        totali = summ
        #PRINT 450, TOTALI
        print("totali is: ", totali)

        i = 1
        while (i < 50):
            n1 = i
            n2 = i + 50
            n3 = i + 100
            n4 = i + 150
            n5 = i + 200
            print(i, gdoti[n1-1], gdoti[n2-1], gdoti[n3-1], gdoti[n4-1], gdoti[n5-1]) #Changed all array locations from (x) to (x-1) because Fortran arrays start at 1
            i += 1
        #CONTINUE                                                  #380

        k = 1
        while (k < ngrphi):
            n1 = 2 * k
            n2 = n1 + 1
            engi[n1-1] = grploi[k-1] #original Fortran code: engi(n1) = grploi(k) (Fortran arrays start at 1)
            engi[n2-1] = grphii[k-1] #same as above for next few lines until end of while loop
            edei[n1-1] = fracis[k-1]/(graphii[k-1] - grploi[k-1])
            edei[n2-1] = edei[n1-1]
            k += 1
        #CONTINUE                                                  #390

        engi[0] - grploi[0]          #original Fortran code: engi(1) - grploi(1) (Fortran arrays start at 1)
        edei[0] = 0.0                #original Fortran code: edei(1) (Fortran arrays start at 1)
        ndei = 2 * ngrpi + 2
        engi[ndei-1] = grphii[ngrphi-1] # (x-1) in the array index because Fortran arrays start at 1
        edei[ndei-1] = 0.0
#RETURN                                                                 #400

                    

                            

                    
            
        
        
    
            
            
        
            

            
