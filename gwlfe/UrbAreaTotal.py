# from Timer import time_function
from Memoization import memoize
from NLU import NLU


# @time_function
@memoize
def UrbAreaTotal(NRur,NUrb,Area):
    result = 0
    nlu = NLU(NRur,NUrb)
    for l in range(NRur, nlu):
        result += Area[l]
    return result


# Tried, it was slower. UrbAreaTotal is faster
# @time_function
#@memoize
def UrbAreaTotal_2(NRur,NUrb,Area):
    return sum(Area[NRur:])