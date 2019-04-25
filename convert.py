import math
import sys

def convert(cn, eg, grphi, grplo, hz, ngrpn)

    g = [0.75, 1.25, 1.75, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5]
    g1 = [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    g2 = [1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    h = [[2.42E+3, 8.32E+2, 1.36E+3, 1.01E+4, 5.32E+3, 5*0.0, 1.21E+4, 7.24E+3, 1.08E+4, 2.07E+4], 
         [3.2E+4, 1.16E+4, 1.21E+4, 1.34E+4, 7.64E+2, 0.0, 1.05E+4, 6.86E+3, 1.03E+4, 2.13E+4], 
         [3.08E+4, 1.45E+4, 2.28E+4, 5.70E+4, 9.87E+3, 2.30E+2, 7.81E+3, 5.03E+3, 8.10E+3, 2.09E+4],
         [2.45E+4, 1.35E+4, 1.57E+4, 3.90E+4, 8.66E+3, 5.56E+2]]
    cnn = [46150, 3*0.0, 30300, 96700, 2*0.0, 78300, 31800, 146700, 0.0, 13300, 42500, 40700, 210000]
    
    ni=1
    p1=0.0
    p2=0.0
    k=1
    while (k < ngrpn):
        m=1
        while (m < ngrpn):
            n = m + (k-1) * ngrpn
            m += 1
        # end while loop m
        cn(k-1,m-1) = cnn(n-1)                                               #10  #Changed cn(k,m) = cnn(n) because Fortran arrays start at 1.
        k += 1
    #end while loop k                                                        #20

    k=1
    while (k < ngroup): #ENDS AT 220
        i = ni
        while (i < 10):
            #if neg go to 40, if 0 go to 60, if pos go to 30
            if ((grphi(k) - g2(i)) > 0): #if pos go to 30
                i = 10                                                       #30
                #GO TO 230

            elif ((grphi(k) - g2(i)) < 0): # if negative go to 40
                if ((grphi(k) - g1(i)) <= 0 ): #if neg or 0 go to 50         #40
                    j = i                                                    #50
                elif ((grphi(k) - g1(i)) > 0): #if pos go to 60
                    #GO TO 160
                        #ADDING EVERYTHING FROM 160 TO END OF LOOP TO FIX THIS: 
                    m = 1
                    while (m < ngrpn):                                                #160-copy
                        hsum = 0.0
                        if ((i - j - 1) > 0):
                            l1 = j + 1                                                #170-copy
                            l2 = i - 1
                    
                            l = l1
                            while (l < l2):
                                hsum = hsum + h(l,m) * g(l)
                            #end while loop                                           #180-copy

                        if ((i - j - 1) == 0): ##THIS IS WRONG, CLEAN THIS UP
                            hsum = hsum + p2 * h(i,m) * g(i)                          #190-copy

                        if ((i - j - 1) > 0):#THIS IS WRONG, CLEAN THIS UP
                            hsum = hsum + p1 * h(j,m) * g(j)                          #200-copy
                            hz(k,m) = hsum/eg(k)
                    #CONTINUE end while loop                                          #210-copy

                    ni = 1
                    #END GO TO 160

            elif (((grphi(k) - g2(i)) == 0): #if 0, go to 60  
                if ((k - 1) <= 0): #if neg or 0 go to 70                     #60
                    p2 = (grphi(k) - g1(i))/(g2(i) - g1(i))                  #70
                    j1 = 1
                    while (j1 < i):
                        j = i - j1 + 1
                        if ((grplo(k) - g1(j)) < 0)#if neg go to 80, if 0 or pos go to 90
                            j = 0                                             #80
                            p1 = 0.0
                            #go to 160
                        elif ((grplo(k) - g1(j)) >= 0): #if 0 or pos
                            if ((i-j) <= 0 ): #- or 0 goto 100, + goto 110     #90   
                                p1 = (grphi(k) - grplo (k))/(g2(j) - g1(j))   #100
                                #then go to 160
                            elif ((i-j) > 0 ): #if pos
                                p1 = (g2(j) - grplo(k))/(g2(j)-g1(j))         #110
                                #go to 160

                elif ((k-1) > 0): #if pos go to 120
                    if ((i - n1) <= 0): #- or 0 goto 130, + goto 140         #120
                        p1 = (grphi(k) - g1(i))/(g2(i)-g1(i)) - p2           #130
                        #then go to 150!
                        j = n1                                               #150A
                        P2 = (grphi(k) - g1(i))/(g2(i)-g1(i)) #copied from below 150B to make this fit
                    else: 
                        p1 = 1.0 - p2                                         #140
                        j = n1                                                #150B
                        P2 = (grphi(k) - g1(i))/(g2(i)-g1(i))

                m = 1
                while (m < ngrpn):                                                #160
                    hsum = 0.0
                    if ((i - j - 1) > 0):
                        l1 = j + 1                                                #170
                        l2 = i - 1
                    
                        l = l1
                        while (l < l2):
                            hsum = hsum + h(l,m) * g(l)
                        #end while loop                                           #180

                    if ((i - j - 1) == 0): #Seems a little strange - check this again.
                        hsum = hsum + p2 * h(i,m) * g(i)                          #190
                        hsum = hsum + p1 * h(j,m) * g(j)                          #200-copy
                        hz(k,m) = hsum/eg(k)                                      #copied as well

                    if ((i - j - 1) > 0):#THIS IS WRONG, CLEAN THIS UP
                        hsum = hsum + p1 * h(j,m) * g(j)                          #200
                        hz(k,m) = hsum/eg(k)
                #CONTINUE end while loop                                          #210

                ni = 1
            #CONTINUE   end if                                                    #220
                return

    if ((grplo(k) - g2(i)) < 0): #ENDS AT 330                                 #230
        j1 = 1
        while (j1 < i):                                                       #240
            j = i - j1 + 1
            if ((grplo(k) - g1(j)) < 0):
                j = 0                                                         #250
            else: 
                p1 = (g2(j) - grplo(k))/(g2(j) - g1(j))                        #260

            m = 1
            while (m1 < ngrpn): #ENDS AT 310                                  #270
                hsum = 0.0
                if ((i-j) > 0): #ENDS AT 300
                    l1 = j + 1                                                #280

                    l = l1                  
                    while (l < 10):
                        hsum = hsum + h(l,m) * g(l)
                    #CONTINUE                                                 #290

                hsum= hsum + h(j,m) * g(j) * p1                               #300
                hz(k,m) = hsum/eg(k)
            #CONTINUE end while loop                                          #310

            if ((k-n) < 0): #ENDS AT 360
                k = k + 1                                                     #320

                k1 = k
                while (k1 < ngroup):                                          #330
                    m = 1
                    while (m < ngrpn):
                        hz(k1,m) = 0.0
                    #CONTINUE                                                 #340
                #CONTINUE                                                     #350
#RETURN                                                                       #360
                
                
                    
                    
