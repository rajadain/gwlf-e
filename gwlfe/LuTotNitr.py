import numpy as np
# from Timer import time_function
from Memoization import memoize
from nRunoff import nRunoff
from nRunoff import nRunoff_2
from SedDelivRatio import SedDelivRatio
from ErosWashoff import ErosWashoff_2
from ErosWashoff import ErosWashoff
from LuLoad import LuLoad
from LuLoad import LuLoad_2
from NLU import NLU


def LuTotNitr(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0,
              Area, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth,
              FirstManureMonth2, LastManureMonth2, SedDelivRatio_0, KF, LS, C, P, SedNitr, CNP_0, Imper, ISRR, ISRA,
              Qretention, PctAreaInfil, LoadRateImp, LoadRatePerv, Storm, UrbBMPRed, FilterWidth, PctStrmBuf, Acoef,
              CNI_0, Nqual):
    result = np.zeros((NYrs, 16))
    n_runoff = nRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0,
                       Area, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth,
                       FirstManureMonth2, LastManureMonth2)
    sed_deliv_ratio = SedDelivRatio(SedDelivRatio_0)
    eros_washoff = ErosWashoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Acoef,
                               KF, LS,
                               C, P, Area)
    lu_load = LuLoad(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                     AntMoist_0,
                     Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual,
                     LoadRateImp,
                     LoadRatePerv, Storm, UrbBMPRed,
                     FilterWidth, PctStrmBuf)
    nlu = NLU(NRur, NUrb)
    for Y in range(NYrs):
        for i in range(12):
            # Add in the urban calucation for sediment
            for l in range(NRur):
                result[Y][l] += n_runoff[Y][i][l]
                result[Y][l] += 0.001 * sed_deliv_ratio * eros_washoff[Y][l][i] * SedNitr

            for l in range(NRur, nlu):
                result[Y][l] += lu_load[Y][l][0] / NYrs / 2
    return result


@memoize
def LuTotNitr_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0,
              Area, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth,
              FirstManureMonth2, LastManureMonth2, SedDelivRatio_0, KF, LS, C, P, SedNitr, CNP_0, Imper, ISRR, ISRA,
              Qretention, PctAreaInfil, LoadRateImp, LoadRatePerv, Storm, UrbBMPRed, FilterWidth, PctStrmBuf, Acoef,
              CNI_0, Nqual):
    # n_runoff = np.reshape(
    #     np.repeat(np.sum(nRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0,
    #                                Area, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth,
    #                                FirstManureMonth2, LastManureMonth2), axis=1), repeats=10), (NYrs, 10))
    n_runoff = np.sum(nRunoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0,
                       Area, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth,
                       FirstManureMonth2, LastManureMonth2), axis =1)
    sed_deliv_ratio = SedDelivRatio(SedDelivRatio_0)
    eros_washoff = np.sum(ErosWashoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, Acoef,
                                        KF, LS,
                                        C, P, Area), axis=1)
    lu_load = LuLoad_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                     AntMoist_0,
                     Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual,
                     LoadRateImp,
                     LoadRatePerv, Storm, UrbBMPRed,
                     FilterWidth, PctStrmBuf)[:,:,0]
    # luLoad is not needed because it is only defined for NUrb land use, and the others are only defined for NRur
    return np.hstack((n_runoff + 0.001 * sed_deliv_ratio * eros_washoff * SedNitr , 12. * lu_load / NYrs / 2))
