from numpy import hstack
from numpy import sum
from numpy import zeros

from LU import LU
from Memoization import memoize
# from Timer import time_function
from NLU import NLU
from QrunI import QrunI, QrunI_2
from QrunP import QrunP, QrunP_2
from UrbAreaTotal import UrbAreaTotal
from Water import Water


# @time_function
@memoize
def UrbanQTotal(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR,
                ISRA):
    nlu = NLU(NRur, NUrb)
    result = zeros((NYrs, 12, 31))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urb_area_total = UrbAreaTotal(NRur, NUrb, Area)
    qrun_i = QrunI(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNI_0, AntMoist_0, Grow_0)
    qrun_p = QrunP(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNP_0, AntMoist_0, Grow_0)
    lu = LU(NRur, NUrb)

    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        for l in range(NRur, nlu):
                            if urb_area_total > 0:
                                result[Y][i][j] += (
                                            (qrun_i[Y][i][j][l] * (Imper[l] * (1 - ISRR[lu[l]]) * (1 - ISRA[lu[l]]))
                                             + qrun_p[Y][i][j][l] *
                                             (1 - (Imper[l] * (1 - ISRR[lu[l]]) * (1 - ISRA[lu[l]]))))
                                            * Area[l] / urb_area_total)
    return result

# @time_function
@memoize
def UrbanQTotal_2(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR,
                ISRA):
    result = zeros((NYrs, 12, 31))
    urb_area_total = UrbAreaTotal(NRur, NUrb, Area)
    qrun_i = QrunI_2(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNI_0, AntMoist_0, Grow_0)
    qrun_p = QrunP_2(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNP_0, AntMoist_0, Grow_0)
    z= zeros((10,))
    ISRR = hstack((z,ISRR))
    ISRA = hstack((z,ISRA))
    x = (Imper * (1 - ISRR) * (1 - ISRA))
    temp = (qrun_i * x + qrun_p * (1- x)) * Area
    if urb_area_total>0:
        result = sum(temp, axis=3)/urb_area_total
    return result