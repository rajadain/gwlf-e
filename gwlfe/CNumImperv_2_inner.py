from numba.pycc import CC
import numpy as np

cc = CC('CNumImperv_2_inner_compiled')

@cc.export('CNumImperv_2_inner',
           '(int64, int64, int32[:,::1], float64[:,:,::1], int64, float64[:,::1], float64[:,:,::1], float64[:,:,::1], float64[::1], float64[:,:,::1])')
def CNumImperv_2_inner(NYrs, NRur, DaysMonth, Temp, nlu, cni, water, melt, grow_factor, amc5):
    result = np.zeros((NYrs, 12, 31, nlu))
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        for l in range(NRur, nlu):
                            if cni[1][l] > 0:
                                if melt[Y][i][j] <= 0:
                                    if grow_factor[i] > 0:
                                        # Growing season
                                        if amc5[Y][i][j] >= 5.33:
                                            result[Y][i][j][l] = cni[2][l]
                                        elif amc5[Y][i][j] < 3.56:
                                            result[Y][i][j][l] = cni[0][l] + (
                                                    cni[1][l] - cni[0][l]) * amc5[Y][i][j] / 3.56
                                        else:
                                            result[Y][i][j][l] = cni[1][l] + (cni[2][l] - cni[1][l]) * (
                                                    amc5[Y][i][j] - 3.56) / 1.77
                                    else:
                                        # Dormant season
                                        if amc5[Y][i][j] >= 2.79:
                                            result[Y][i][j][l] = cni[2][l]
                                        elif amc5[Y][i][j] < 1.27:
                                            result[Y][i][j][l] = cni[0][l] + (
                                                    cni[1][l] - cni[0][l]) * amc5[Y][i][j] / 1.27
                                        else:
                                            result[Y][i][j][l] = cni[1][l] + (cni[2][l] - cni[1][l]) * (
                                                    amc5[Y][i][j] - 1.27) / 1.52
                                else:
                                    result[Y][i][j][l] = cni[2][l]
    return result