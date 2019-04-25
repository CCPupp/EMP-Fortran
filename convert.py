import math
import sys

def convert(cn, cnn, eg, g, g1, g2, grphi, grplo, h, hz, ngrpn)

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
            if ((grphi(k) - g2(i)) > 0) #if pos
                i = 10                                                       #30
                #GO TO 230!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!FIX THIS!!!

            elif ((grphi(k) - g2(i)): < 0) # if negative
                #if neg or 0 go to 50, if pos go to 60
                if ((grphi(k) - g1(i)) <= 0 ):                               #40
                    j = i                                                    #50
                    #######then go to 160!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            elif ((grphi(k) - g2(i)) == 0): #if 0
                if ((k - 1) <= 0) #if neg or 0 go to 70, if pos go to 120    #60
                    p2 = (grphi(k) - g1(i))/(g2(i) - g1(i))                  #70
                    j1 = 1
                    while (j1 < i):
                        j = i - j1 + 1
                        if ((grplo(k) - g1(j)) < 0)#if neg go to 80, if 0 or pos go to 90
                            j = 0                                             #80
                            p1 = 0.0
                            ###############then go to 160!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        elif ((grplo(k) - g1(j)) >= 0): #if 0 or pos
                            if ((i-j) <= 0 ): #- or 0 goto 100, + goto 110     #90   
                                p1 = (grphi(k) - grplo (k))/(g2(j) - g1(j))   #100
                                #######then go to 160!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                            elif ((i-j) > 0 ): #if pos
                                p1 = (g2(j) - grplo(k))/(g2(j)-g1(j))         #110
                                #######then go to 160!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                        if ((i - n1) <= 0) #- or 0 goto 130, + goto 140       #120
                            p1 = (grphi(k) - g1(i))/(g2(i)-g1(i)) - p2        #130
                            #######then go to 150!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        #end if statement
                    p1 = 1.0 - p2                                             #140
                    j = n1                                                    #150
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

                if ((i - j - 1) == 0): ##THIS IS WRONG, CLEAN THIS UP
                    hsum = hsum + p2 * h(i,m) * g(i)                          #190

                if ((i - j - 1) > 0):#THIS IS WRONG, CLEAN THIS UP
                    hsum = hsum + p1 * h(j,m) * g(j)                          #200
                    hz(k,m) = hsum/eg(k)
            #CONTINUE end while loop                                          #210

            ni = 1
    #CONTINUE   end while loop                                                #220
    #RETURN ##################################################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    if ((grplo(k) - g2(i)) < 0): #ENDS AT 330                                 #230
        j1 = 1
        while (j1 < i):                                                       #240
            j = i - j1 + 1
            if ((grplo(k) - g1(j)) < 0):
                j = 0                                                         #250
                ###THEN GO TO 270!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            p1 = (g2(j) - grplo(k))/(g2(j) - g1(j))                           #260

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
                
                
                    
                    
