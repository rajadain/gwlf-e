import numpy as np
from Timer import time_function
from StreamFlowLE import StreamFlowLE
from TotAreaMeters import TotAreaMeters
from Memoization import memoize


@memoize
def StreamFlowVol(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                  ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef
                  , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                  GroundWithdrawal):
    result = np.zeros((NYrs, 12))
    streamflowle = StreamFlowLE(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow,
                                CNP_0, Imper,
                                ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                                SeepCoef
                                , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                                StreamWithdrawal, GroundWithdrawal)
    totareameters = TotAreaMeters(NRur, NUrb, Area)
    for Y in range(NYrs):
        for i in range(12):
            # CALCULATE THE VOLUMETRIC STREAM Flow
            result[Y][i] = ((streamflowle[Y][i] / 100) * totareameters) / (86400 * DaysMonth[Y][i])
    return result


def StreamFlowVol_2():
    pass
