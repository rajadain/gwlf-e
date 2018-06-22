import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.nonGrazingAnimals.Loads import NGLoadN
from gwlfe.enums import YesOrNo
from VariableUnittest import VariableUnitTest

class TestNGLoadN(VariableUnitTest):
    def test_NGLoadN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGLoadN.NGLoadN_f(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            NGLoadN.NGLoadN(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN)[z.GrazingAnimal_0 == YesOrNo.NO], decimal=7)
