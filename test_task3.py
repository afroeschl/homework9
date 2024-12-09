""" Test for Task3: Checking the functionality in 'task3.py' using assertions """

import unittest
import os
import numpy as np
import matplotlib.pyplot as plt
import task3

class Test(unittest.TestCase):
    def test1_frequency_analyzer_RC_parallel(self):
        infile = "input_RC.csv"
        outfile = "test_task3_output_RC_parallel.csv"
    
        if os.path.isfile(outfile): # if file pre-exists, remove it
            os.remove(outfile)

        f1 = 100 # Hz
        fn = 1e6 # Hz
        n = 1000
        f0 = task3.frequency_analyzer(infile, outfile, "Parallel", f1, fn, n)

        fexpected = f1
        self.assertAlmostEqual(f0, fexpected, delta=0.01*fexpected) # Expected return
        self.assertTrue(os.path.isfile(outfile)) # check outfile is created

    def test2_plot_impedance_RC_parallel(self):
        filepath = "test_task3_output_RC_parallel.csv"
        figname = "test_task3_plot_RC_parallel.png"

        if os.path.isfile(figname): # if file pre-exists, remove it
            os.remove(figname)

        # read saved file in previous test and plot
        data = np.loadtxt(filepath, delimiter=",")

        plt.close('all')
        task3.plot_impedance(data[:,0], data[:,1], data[:,2], figname)
        plt.close('all')

        self.assertTrue(os.path.isfile(figname)) # check fig is created only

    def test3_frequency_analyzer_RLC4_series(self):
        infile = "input_RLC4.csv"
        outfile = "test_task3_output_RLC4_series.csv"

        if os.path.isfile(outfile): # if file pre-exists, remove it
            os.remove(outfile)

        f1 = 100 # Hz
        fn = 1e6 # Hz
        n = 1000
        f0 = task3.frequency_analyzer(infile, outfile, "Series", f1, fn, n)

        fres = 7978 # approx.
        self.assertAlmostEqual(f0, fres, delta=0.01*fres) # Expected return
        self.assertTrue(os.path.isfile(outfile)) # check outfile is created

    def test4_plot_impedance_RLC4_series(self):
        filepath = "test_task3_output_RLC4_series.csv"
        figname = "test_task3_plot_RLC4_series.png"

        if os.path.isfile(figname): # if file pre-exists, remove it
            os.remove(figname)

        # read saved file and plot
        data = np.loadtxt(filepath, delimiter=",")

        plt.close('all')
        task3.plot_impedance(data[:,0], data[:,1], data[:,2], figname)
        plt.close('all')

        self.assertTrue(os.path.isfile(figname)) # check fig is created
        

if __name__ == "__main__":
    unittest.main()