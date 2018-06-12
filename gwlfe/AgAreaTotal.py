import numpy as np
# from Timer import time_function
from enums import LandUse as LandUseNames
from Memoization import memoize


# @memoize
def AgAreaTotal(NRur, Landuse, Area):
    result = 0
    for l in range(NRur):
        if Landuse[l] is LandUseNames.FOREST:
            pass
        elif Landuse[l] is LandUseNames.CROPLAND:
            result += Area[l]
        elif Landuse[l] is LandUseNames.HAY_PAST:
            result += Area[l]
        elif Landuse[l] is LandUseNames.TURFGRASS:
            result += Area[l]
    return result

# vectorization is slower
# @time_function
# def AgAreaTotal_2(Landuse, Area):
#     return Area[Landuse == LandUseNames.CROPLAND] + \
#            Area[Landuse == LandUseNames.HAY_PAST] + \
#            Area[Landuse == LandUseNames.TURFGRASS]
