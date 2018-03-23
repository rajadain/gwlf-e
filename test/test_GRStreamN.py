import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import GRStreamN


class TestGRStreamN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_GRStreamN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRStreamN.GRStreamN_2(),
            GRStreamN.GRStreamN(), decimal=7)

    @skip("not ready")
    def test_AvGRStreamN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRStreamN.AvGRStreamN_2(),
            GRStreamN.AvGRStreamN(), decimal=7)
