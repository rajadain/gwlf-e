import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import AttenN
from VariableUnittest import VariableUnitTest

class TestAttenN(VariableUnitTest):
    pass


    # @skip("not ready")
    # def test_AttenN(self):
    #     z = self.z
    #     np.testing.assert_array_almost_equal(
    #         AttenN.AttenN_2(),
    #         AttenN.AttenN(), decimal=7)