# from Timer import time_function
from Memoization import memoize
from numpy import zeros

try:
    from InitSnow_2_inner_compiled import InitSnow_2_inner
except ImportError:
    print("Unable to import compiled InitSnow_inner, using slower version")
    from InitSnow_inner import InitSnow_2_inner


# @memoize
def InitSnow(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    result = zeros((NYrs, 12, 31))
    yesterday = InitSnow_0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] <= 0:
                    result[Y][i][j] = yesterday + Prec[Y][i][j]
                else:
                    if yesterday > 0.001:
                        result[Y][i][j] = max(yesterday - 0.45 * Temp[Y][i][j], 0)
                    else:
                        result[Y][i][j] = yesterday
                yesterday = result[Y][i][j]
    return result


@memoize
def InitSnow_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    return InitSnow_2_inner(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
