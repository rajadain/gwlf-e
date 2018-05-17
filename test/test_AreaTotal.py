import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import AreaTotal


class TestAreaTotal(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_AreaTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AreaTotal.AreaTotal_2(z.Area),
            AreaTotal.AreaTotal(z.NRur, z.NUrb, z.Area), decimal=7)