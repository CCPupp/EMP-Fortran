#!/usr/bin/python

'''
25 COMMON variables: TAU, TPEAK, R[250], CONJ, CONQ, RHOH[250][16], DRRHOH[250][16], FC[50], FF[50], RERG[50], EERG[50], EG[50], BB[50], AA[50], SN[10], NGROUP, FJH[250][16], QH[250][16], RHO[250][15], DRRHO[250][15], RGI[50], Q[250][16], NTM1, NDR, NT

Subroutine reads from all parameters but only writes to FJH[250][16], QH[250][16], and Q[250][16].

NDR indicates when the top loop layer (common to both nests) should end.
NT indicates when the middle layer loop of the first nest should end.
NTM1 indicates when the middle layer loop of the second nest should end.
NGROUP indicates when the bottom layers of both nested loops should end.

The square root of TAU – TPEAK is required to run this subroutine. If TAU – TPEAK is negative, the subroutine is skipped entirely.

Parameters read in the top loop: R[250], CONJ, CONQ

Parameters read in the first middle loop: RHOH[250][16], DRRHOH[250][16]
Parameters read in the second middle loop: RHO[250][15], DRRHO[250][15]

Parameters read in both bottom loops: RGI[50], FC[50], FF[50], EERG[50], EG[50], AA[50], SN[10]
Parameters additionally read in the first bottom loop: DRRHOH[250][16], RERG[50], BB[50]
Parameter additionally read in the second bottom loop: DRRHO[250][15]
'''

import math


def NGAMMA(TAU, TPEAK, R, CONJ, CONQ, RHOH, DRRHOH, FC, FF, RERG, EERG, EG, BB, AA, SN, NGROUP, FJH, QH, RHO, DRRHO, RGI, Q, NTM1, NDR, NT):
    if (TAU > TPEAK):  # TAU and TPEAK are COMMON; if TAU <= TPEAK, NGAMMA is skipped entirely
        TROOT = math.sqrt(TAU – TPEAK)  # TAU and TPEAK are COMMON
        i = 0
        while (i < NDR):  # NDR is COMMON; top layer of nested loops, common to both nests
            RI = 1.0 / R[i]  # R[250] is COMMON
            CJ = CONJ * RI**2  # CONJ is COMMON
            CQ = CONQ * RI**2  # CONQ is COMMON
            j = 0
            while (j < NT):  # NT is COMMON; middle layer of first nest
                CUR = 0.0
                QRH = 0.0
                CQH = CQ * RHOH[i][j]  # RHOH[250][16] is COMMON
                AVRAD = DRRHOH[i][j] * RI  # DRRHOH[250][16] is COMMON
                k = 0
                while (k < NGROUP):  # NGROUP is COMMON; bottom layer of first nest
                    # DRRHOH[250][16] and RGI[50] are COMMON
                    GMFP = DRRHOH[i][j] * RGI[k]
                    EMFP = math.exp(-GMFP)
                    # FC[50] and FF[50] are COMMON
                    FACTO = FC[k] + FF[k] * GMFP
                    CONSJ = CJ * RERG[k] * EMFP  # RERG[50] is COMMON
                    CONSQ = CQH * EERG[k] * EMFP  # EERG[50] is COMMON
                    AJ = AVRAD * 2.055e7 * math.sqrt(GMFP)
                    AH = (1.186 – 0.062 * EG[k]) * AJ  # EG[50] is COMMON
                    FKJ = FACTO * 1.0e4 / \
                        (1.0 + BB[k] * GMFP)  # BB[50] is COMMON
                    FKQ = FACTO * 1.0e4 / \
                        (1.1 + AA[k] * GMFP)  # AA[50] is COMMON
                    FBJ = 1.0 – math.exp(–TROOT * FKJ) * (TROOT * FKJ + 1.0)
                    FBQ = 1.0 – math.exp(–TROOT * FKQ) * (TROOT * FKQ + 1.0)
                    BUFJ = 1.0 + 2.0 * AJ * FBJ / (FKJ**2)
                    BUFQ = 1.0 + 2.0 * AH * FBQ / (FKQ**2)
                    CUR = CONSJ * SN[k] * BUFJ + CUR  # SN[10] is COMMON
                    QRH = CONSQ * SN[k] * BUFQ + QRH  # SN[10] is COMMON
                    k += 1
                FJH[i][j] = CUR + FJH[i][j]  # FJH[250][16] is COMMON
                QH[i][j] = QRH + QH[i][j]  # QH[250][16] is COMMON
                j += 1
            j = 0
            while (j < NTM1):  # NTM1 is COMMON; middle layer of second nest
                QRG = 0.0
                CQG = CQ * RHO[i][j]  # RHO[250][15] is COMMON
                AVRAD = DRRHO[i][j] * RI  # DRRHO[250][15] is COMMON
                k = 0
                while (k < NGROUP):  # NGROUP is COMMON; bottom layer of second nest
                    # DRRHO[250][15] and RGI[50] are COMMON
                    GMFP = DRRHO[i][j] * RGI[k]
                    # FC[50] and FF[50] are COMMON
                    FACTO = FC[k] + FF[k] + GMFP
                    # EERG[50] is COMMON
                    CONSG = CQG * EERG[k] * math.exp(–GMFP)
                    # EG[50] is COMMON
                    AG = AVRAD * (1.186 – 0.062 * EG[k]) * 2.055e7 * math.sqrt(GMFP)
                    FKG = FACTO * 1.0e4 / \
                        (1.1 + AA[k] * GMFP)  # AA[50] is COMMON
                    FBG = 1.0 – math.exp(–TROOT * FKG) * (TROOT * FKG + 1.0)
                    BUFG = 1.0 + 2.0 * AG * FBG / (FKG**2)
                    QRG = CONSG * SN[k] * BUFG + QRG  # SN[10] is COMMON
                    k += 1
                Q[i][j] = QRG + Q[i][j]  # Q[250][16] is COMMON
                j += 1
            i += 1
    return
