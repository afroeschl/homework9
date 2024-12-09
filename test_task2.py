""" Test for Task2: Checking the functionality in 'task2.py' using assertions """

import unittest
import cmath
from task2 import Device, Circuit

class Test(unittest.TestCase):
    def test1_Device(self):
        R1 = Device("R", 1e3)
        C1 = Device("C", 1e-6)
        L1 = Device("L", 1e-3)
        self.assertEqual(R1.type, "R")
        self.assertAlmostEqual(R1.value, 1000)
        self.assertEqual(C1.type, "C")
        self.assertAlmostEqual(C1.value, 1e-6)
        self.assertEqual(L1.type, "L")
        self.assertAlmostEqual(L1.value, 1e-3)

    def test2_Device_impedance(self):
        f = 1e3/(2*cmath.pi)

        R1 = Device("R", 1e3)
        self.assertAlmostEqual(R1.impedance(f), 1000+0j)

        C1 = Device("C", 1e-6)
        self.assertAlmostEqual(C1.impedance(f), 0-1000j)
        
        L1 = Device("L", 1e-3)
        self.assertAlmostEqual(L1.impedance(f), 0+1j)

    def test3_Device_equality_op(self):
        R1 = Device("R", 1e3)
        R2 = Device("R", 1000.)
        C1 = Device("C", 1e-6)
        self.assertTrue( R1 == R2)
        self.assertFalse( R1 == C1)

    def test4_Circuit(self):
        R1 = Device("R", 1e3)
        C1 = Device("C", 2e-6)
        L1 = Device("L", 2e-4)
        devs = [R1, C1, L1]

        rlc = Circuit("Series", devs)
        self.assertEqual(rlc.type, "Series")
        self.assertEqual(len(rlc.devices), len(devs) )

        rlc = Circuit("Parallel", devs)
        self.assertEqual(rlc.type, "Parallel")
        self.assertEqual(len(rlc.devices), len(devs) )

    def test5_Circuit_impedance(self):
        R1 = Device("R", 1e3)
        C1 = Device("C", 2e-6)
        L1 = Device("L", 2e-4)
        devs = [R1, C1, L1]
        f = 5e4/(2*cmath.pi)

        rlc = Circuit("Series", devs)
        self.assertAlmostEqual(rlc.impedance(f), 1000+0j)

        rlc = Circuit("Parallel", devs)
        self.assertAlmostEqual(rlc.impedance(f), 1000+0j)


if __name__ == "__main__":
    unittest.main()
