import math
import sys
from scipy import special

def gamma(edep, engp, grphi, grplo, gdot, gtime, gcal, i1, ifun, ngroup, ngrpn,
          rdt, siz, peak)

    cay = 1.0
    dt = .000000001
    dt2= dt * 0.5
    gcal = gcal/siz
    total = 0.0

    if ((i1 == 1) or (i1 < 1) or (i1 > 2)): 
        if ((ifun == 2) or (ifun < 1) or (ifun > 4)):
            ifun2 = ifun                                           #10
            ifun = 1                                               #20
            ###goto 40
        else:                                
            ##if ncal =1 go to 40, if ncal = 2 go to 80            #30

        i = 2
        while (i < 250):                                           #40
            t1 = t * dt
            t2 = t * dt
            t2 = (i-1) * dt
            s1 = source(t1)
            s2 = source(t2)
        #end while loop                                            #50
            #if (s1 - s2) 60, 50, 50
            #go to 60 if neg, go to 50 if 0 or positive
            if ((s1 - s2) >= 0):
                #(print 410, ifun)
                #stop
            #elif ((s1 - s2) < 0):
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
                total = total + source(t) + dt
            #end while loop                                        #90
            cay = gcal/total
        #end if statement                                          #100
            
        ig = 1
        i = 1
        t = 1 * dt2
        t1 = i * dt
        gtime(i) = t1
        gdot (i) = source(t1)
        total = source(t) * dt

        i = 2
        while (i < 250):
            inn = i
            t = (i - 0.5) * dt
            t1 = i * dt
            gtime(i) = t1
            gdot(i) = source(t1)
            total = total + source(t) + dt
            if (ig == 1):
                #if neg go to 120, if 0 or pos go to 130
                if ((gdot(i) - gdot(i-1)) < 0):                    #110
                    peak = gdot(i-1)                               #120
                    ig = 2
        #end while loop & if statements                            #130
        ndot = inn

        #print 420, peak, total

        i = 1
        while (i < 50):
            n1 = i
            n2 = i + 50
            n3 = i + 100
            n4 = 1 + 150
            n5 = i + 200
            #print 430, i, gdot(n1), gdot(n2), gdot(n3), gdot(n4), gdot(n5)
            #CONTINUE                                                 #140

        k=1
        while (k < ngroup):
            n1 = 2 * k
            n2 = 2 * k + 1
            engp(n1)= grplo(k)
            engp(n2) = grphi(k)
            edep(n1) = frac(k)/(grphi(k)-grplo(k))
            edep(n2) = edep(n1)
        #CONTINUE                                                     #150

        engp(1) = grplo(1)
        edep(1) = 0.0
        ndep = 2 * ngroup + 2
        engp(ndep) = grphi(ngroup)
        edep(ndep) = 0.0

        #GO TO (170, 310), I2
        if(i2 == 1):                                                  #160
            rdt = math.exp(tablin(rad, 2, nrad, hob, 1)/stdrho)#????? #170
            rdt = 2.0/ (rdt * dt)

            m = 1
            while (m < ngrpn):
                sor(m) = dn(m)                                        #180

            i = 1
            while (i < 250):
                taut = i * dt
                #if neg go to 210, if 0 or pos go to 190
                if ((taut - tspeak) >= 0):
                    #CALL SOURCEN                                     #190
                    k = 1
                    while (k < ngroup):
                        gdotn(i) = sn(k) + gdotn(i)                   #200
                    #end while loop/CONTINUE                          #210
            #end while loop
            rdt = 2.0*math.exp(-2)*rdt
            summ = 0.0

            m = 1
            while (m < ngrpn):
                dn(m) = sor(m)                                        #220
                #CALL SOURCEN                                     
            m= 1
            while (m < ngrpn):
                dn(m) = (sor(m) + dn(m)) * 0.5

            k= 1
            while (k < ngroup):
                summ = summ + hz(k, m) * dn(m) * 0.00000005           #230
            #CONTINUE                                                 #240

            i = 1
            while (i < 1000):
                #CALL SOURCEN
                k=1
                while (k < ngroup):
                    summ = summ + sn(k) * 0.00000005                  #250
                #CONTINUE                                             #260

            totalg = summ

            m = 1
            while (m < ngrpn):
                dn(m) = sor(m)
                sor(m) = 0.0                                          #270

            summ = 0.0

            m = 1
            while (m < ngrpn):
                summ = summ + (grphin(m) + grplon(m)) * 0.5 * dn(m)   #280

            totaln = summ

            #PRINT 440, TOTALN, TOTALG

            i = 1
            while (i <  50):
                n1= i
                n2 = i + 50
                n3 = i + 100
                n4 = i + 150
                n5 = i + 200
                #PRINT 430, I, GDOTN(N1), ETC....
            #CONTINUE                                                 #290

            m = 1
            while (m < ngrpn):
                n1 = 2 * m
                n2 = n1 + 1
                engn(n1) = grplon(m)
                engn(n2) = grphin(m)
                eden(n1) = (grplon(m) + grphin(m)) * 0.5 * dn(m)/((grphin(m) - grplon(m)) + totaln)
                eden(n2) = eden(n1)
            #CONTINUE                                                 #300

            engn(1) = grplon(1) ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            eden(1) = 0.0
            nden = 2 * ngrpn + 2
            engn(nden) = grphin(ngrpn)
            eden(nden) = 0.0

            #GO TO (320, 400), I3                                     #310
            if ((i3 < 1) or (i3 == 1) or (i3 > 4)):

                i = 1
                while (i < 250):                                      #320
                    t = i * dt
                    tiso = t - ciso
                    if ((t-ciso) >= 0):
                        summ = 0.0                                    #330
                        l = 1
                        while (l < niso):
                            summ = summ * ai(l) * math.exp(-tiso/di(l)) * Tablin(trani, 2, ntrani, tiso, 2) #!!!!!!!!TABLIN  #340
                            gdoti(i) = summ
                        #CONTINUE/ends while & if & while              #350

                dt = 0.00000001
                summ = 0.0

                i = 1
                while (i < 1000):
                    t = (i - 0.5) * dt

                    l = 1
                    while (l < niso):
                        summ = summ + ai(l) * dt * math.exp(-t/di(l)) * TABLIN(trani, 2, ntrani, t, 2) #360
                    #CONTINUE - ends previous two while loops            #370

                totali = summ
                #PRINT 450, TOTAL I

                i = 1
                while (i < 50):
                    n1 = i
                    n2 = i + 50
                    n3 = i + 100
                    n4 = i + 150
                    n5 = i + 200
                    #PRINT 430, I, GDOTI(N1), etc.....
                #CONTINUE                                                 #380

                k = 1
                while (k < ngrphi):
                    n1 = 2 * k
                    n2 = n1 + 1
                    engi(n1) = grploi(k)
                    engi(n2) = grphii(k)
                    edei(n1) = fracis(k)/(graphii(k) - grploi(k))
                    edei(n2) = edei(n1)
                #CONTINUE                                                 #390

            engi(1) - grploi(1)
            edei(1) = 0.0
            ndei = 2 * ngrpi + 2
            engi(ndei) = grphii(ngrphi)
            edei(ndei) = 0.0
            #RETURN                                                       #400

                    

                            

                    
            
        
        
    
            
            
        
            

            
