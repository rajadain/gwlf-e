import numpy as np
from gwlfe.Timer import time_function
from InitGrN import InitGrN


def GRAppManN(GRPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = np.zeros((12,))
    init_gr_n = InitGrN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result[i] = GRPctManApp[i] * init_gr_n
    return result


def GRAppManN_2(GRPctManApp, InitGrN):
    return GRPctManApp * InitGrN
