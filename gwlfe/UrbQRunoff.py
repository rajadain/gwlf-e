import numpy as np
# from Timer import time_function
from Memoization import memoize
from NLU import NLU
from Water import Water
from Water import Water_2
from QrunI import QrunI
from QrunI import QrunI_2
from QrunP import QrunP
from QrunP import QrunP_2
from LU import LU


@memoize
def UrbQRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, CNI_0, CNP_0, AntMoist_0, Grow_0, Imper, ISRR,
               ISRA):
    result = np.zeros((NYrs, 16, 12))
    nlu = NLU(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    qruni = QrunI(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNI_0, AntMoist_0, Grow_0)
    qrunp = QrunP(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNP_0, AntMoist_0, Grow_0)
    lu = LU(NRur, NUrb)
    for Y in range(NYrs):
        for i in range(12):
            for l in range(nlu):
                result[Y, l, i] = 0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        for l in range(NRur, nlu):
                            result[Y][l][i] += (qruni[Y][i][j][l] * (
                                    Imper[l] * (1 - ISRR[lu[l]]) * (1 - ISRA[lu[l]]))
                                                + qrunp[Y][i][j][l] * (
                                                        1 - (Imper[l] * (1 - ISRR[lu[l]]) * (
                                                        1 - ISRA[lu[l]]))))

                else:
                    pass
    return result

def UrbQRunoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, CNI_0, CNP_0, AntMoist_0, Grow_0, Imper, ISRR,
                 ISRA):
    qruni = QrunI_2(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNI_0, AntMoist_0, Grow_0)[:, :, :, NRur:]
    qrunp = QrunP_2(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNP_0, AntMoist_0, Grow_0)[:, :, :, NRur:]
    temp = (Imper[NRur:] * (1 - ISRR) * (1 - ISRA))
    return np.sum(qruni * temp+ qrunp * (1 - temp),axis=2)
