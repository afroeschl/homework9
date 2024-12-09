""" Test for Task1: Checking the functionality in 'task1.py' using assertions """

import unittest
import cmath
import task1

class Test(unittest.TestCase):
    def setUp(self) -> None:
        w = 5e4 # rad/s
        self.f = w/(2*cmath.pi) # Hz
        self.R = 10 # Ohm
        self.L = 2e-4 # H
        self.C = 2e-6 # F

    def test1_task1_impedance(self):
        expected = self.R + 0j
        self.assertAlmostEqual(task1.device_impedance("R", self.R, self.f), expected, delta=1e-5)
        
        expected = 0 + 10j
        self.assertAlmostEqual(task1.device_impedance("L", self.L, self.f), expected, delta=1e-5)

        expected = 0 - 10j
        self.assertAlmostEqual(task1.device_impedance("C", self.C, self.f), expected, delta=1e-5)

    def test2_task1_impedance_raiseException(self):
        # test exception raised
        with self.assertRaises(ValueError):
            Z = task1.device_impedance("Q", 1.0, 10)

    def test3_task1_series(self):
        devices = [("R", self.R), ("L", self.L), ("C", self.C)]
        expected = self.R + 0j
        self.assertAlmostEqual(task1.series_impedance(devices, self.f), expected)

        # 4x
        devices = devices * 4
        expected = 4*self.R + 0j
        self.assertAlmostEqual(task1.series_impedance(devices, self.f), expected)

    def test4_task1_parallel(self):
        devices = [("R", self.R), ("L", self.L), ("C", self.C)]
        expected = self.R + 0j
        self.assertAlmostEqual(task1.parallel_impedance(devices, self.f), expected)

        # 4x
        devices = devices * 4
        expected = self.R/4 + 0j
        self.assertAlmostEqual(task1.parallel_impedance(devices, self.f), expected)

if __name__ == "__main__":
    unittest.main()
