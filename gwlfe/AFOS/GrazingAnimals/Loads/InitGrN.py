from numpy import sum

from GRLoadN import GRLoadN
from GRLoadN import GRLoadN_2
from gwlfe.GrazingAnimal import GrazingAnimal
from gwlfe.enums import YesOrNo


def InitGrN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = 0
    gr_load_n = GRLoadN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    grazing_animal = GrazingAnimal(GrazingAnimal_0)
    for a in range(9):
        if grazing_animal[a] is YesOrNo.NO:
            pass
        elif grazing_animal[a] is YesOrNo.YES:
            result += gr_load_n[a]
    return result


def InitGrN_2(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    return sum(GRLoadN_2(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN))
