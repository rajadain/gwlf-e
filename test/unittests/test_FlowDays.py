import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import FlowDays
from VariableUnittest import VariableUnitTest

class TestFlowDays(VariableUnitTest):
    pass
    # @skip("not ready")
    # def test_FlowDays(self):
    #     z = self.z
    #     np.testing.assert_array_almost_equal(
    #         FlowDays.FlowDays_2(),
    #         FlowDays.FlowDays(), decimal=7)