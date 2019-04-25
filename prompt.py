import sys
import math
import convo


def do(DECG, FREG, DECQ, DECJ, L, EXP, NINCR, TDR, SOURCE, SOR, DTDR, TAU, TPEAK, R, CONJ, CONQ, RHOH, DRRHOH, FC, FF, RERG, EERG, EG, BB, AA, SN, NGROUP, FJH, QH, RHO, DRRHO, RGI, Q, NTM1, NDR, NT):
    DIFF = TAU - NINCR * DTDR
    N = 0
    while NINCR != N:  # Loop
        TCON = TAU - TDR(N)
        SOR[N] = SOURCE[TCON] * DTDR
        N += 1
    TDRL = 0.5 * (TAU + NINCR * DTDR)
    ROOTL = math.sqrt(TDRL)
    TCONL = (TAU - TDRL)
    SORL = SOURCE[TCONL] * DIFF
    SORT = SOURCE[TAU]
    I = 0
    while NDR != I:
        RI = 1 / R[I]
        R2I = RI * RI
        CJ = CONJ * R2I
        CQ = CONQ * R2I
        J = 0
        while NT != J:
            CUR = 0
            QRH = 0
            CQH = CQ * RHOH[I][J]
            AVRAD = DRRHOH[I][J] * RI
            SAVRAD = math.sqrt(AVRAD)
            K = 0
            while NGROUP != K:
                GMFP = DRRHOH[I][J] * RGI[K]
                EMFP = EXP[-GMFP]
                FACTO = FC[K] + FF[K] * GMFP
                CONSJ = CJ * RERG[K] * EMFP
                CONSQ = CQH * EERG[K] * EMFP
                AJ = AVRAD * 20550000 * math.sqrt(GMFP)
                AH = (1.186 - 0.062 * EG[K]) * AJ
                FKJ = FACTO * 10000 / (1.0 + BB[K] * GMFP)
                FKQ = FACTO * 10000 / (1.1 + AA[K] * GMFP)
                DCJ = -SAVRAD * FKJ
                DCQ = -SAVRAD * FKQ
                CONVJ = 0.0
                CONVQ = 0.0
                if NINCR > 0:
                    convo.convo2()  # Call convolution integral 2
                    CONVJ = AJ * CONVJ
                    CONVQ = AH * CONVQ
                else:
                    DELFRJ = AJ * EXP[DCJ * ROOTL]
                    DELFRQ = AH * EXP[DCQ + ROOTL]
                    CONVJ = CONVJ + SORL * DELFRJ + SORT
                    CONVQ = CONVQ + SORL * DELFRQ + SORT
                    CUR = CONVJ * CONSJ * FREG[K] + CUR
                    QRH = CONVQ * CONSQ * FREG[K] + QRH
            FJH[I, J] = CUR
            QH[I, J] = QRH
            if L:
                DECQ[I, J] = QRH
                DECJ[I, J] = CUR
            J += 1
        while NTM1 != J:
            QRG = 0.0
            CQG = CQ * RHO[I, J]
            AVRAD = DRRHO[I, J] * RI
            SAVRAD = math.sqrt(AVRAD)
            K = 0
            while NGROUP != K:
                GMFP = DRRHO[I, J] * RGI[K]
                FACTO = FC[K] + FF[K] + GMFP
                CONSG = CQG * EERG[K] * EXP[-GMFP]
                AG = AVRAD * (1.186 - 0.062 * EG[K]) * 20550000 * math.sqrt(GMFP)
                FKG = FACTO * 10000 / (1.1 + AA[K] * GMFP)
                DCG = -SAVRAD * FKG
                CONVG = 0.0
                if NINCR > 0:
                    convo.convo1()
                    CONVG = AG * CONVG
                else:
                    DELFRG = AG * EXP[DCG * ROOTL]
                    CONVG = CONVG + SORL * DELFRG + SORT
                    QRG = CONVG * CONSG * FREG[K] + QRG
            J += 1
        Q[I, J] = QRG
        if L:
            DECG[I, J] = QRG
        I += 1


def prompt(DECG, FREG, DECQ, DECJ, L, EXP, ifit, DT, DT2, NMAX, TRIP, TDR, SOURCE, SOR, DTDR, TAU, TPEAK, R, CONJ, CONQ, RHOH, DRRHOH, FC, FF, RERG, EERG, EG, BB, AA, SN, NGROUP, FJH, QH, RHO, DRRHO, RGI, Q, NTM1, NDR, NT):
    if ifit == 0:
        if (TAU + DT + DT2) < 0:
            # do convolution
            NINCR = TAU / DTDR
            if (NINCR - NMAX) > 0:
                print("Error in prompt")
                return
            else:
                do(DECG, FREG, DECQ, DECJ, L, EXP, NINCR, TDR, SOURCE, SOR, DTDR, TAU, TPEAK, R, CONJ, CONQ, RHOH, DRRHOH, FC, FF, RERG, EERG, EG, BB, AA, SN, NGROUP, FJH, QH, RHO, DRRHO, RGI, Q, NTM1, NDR, NT)
    elif ifit == 1:
        # GOTO 270
        return
    else:
        if (TAU + DT + DT2 - TRIP) < 0:
            if (TAU + DT2 - TRIP) < 0:
                L = 2
            # do convolution
            NINCR = TAU / DTDR
            if (NINCR - NMAX) > 0:
                print("Error in prompt")
                return
            else:
                do(DECG, FREG, DECQ, DECJ, L, EXP, NINCR, TDR, SOURCE, SOR, DTDR, TAU, TPEAK, R, CONJ, CONQ, RHOH, DRRHOH, FC, FF, RERG, EERG, EG, BB, AA, SN, NGROUP, FJH, QH, RHO, DRRHO, RGI, Q, NTM1, NDR, NT)
