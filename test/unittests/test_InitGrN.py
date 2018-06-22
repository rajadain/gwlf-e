import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Loads import InitGrN
from VariableUnittest import VariableUnitTest

class TestInitGrN(VariableUnitTest):
    def test_InitGrN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            InitGrN.InitGrN_f(z.GrazingAnimal_0,z.NumAnimals,z.AvgAnimalWt,z.AnimalDailyN),
            InitGrN.InitGrN(z.GrazingAnimal_0,z.NumAnimals,z.AvgAnimalWt,z.AnimalDailyN), decimal=7)