"""
Task3: Implement the following functions according to the
specification provided in the comments below.
"""
import numpy as np
import csv
import task2
import matplotlib.pyplot as plt
import cmath
import math


def frequency_analyzer(infile: str, outfile: str, circuit_type: str,
                       fstart: float, fstop: float, n: int) -> float:
    """
    Samples the impedance of a circuit inside a given frequency interval.
    The list of devices which form the circuit is read from an input file (e.g. "input_RLC.csv").
    The frequency (Hz), impedance magnitude (Ohm), and impedance phase (degree) are written to an output file in csv-format using "," as delimiter:

    # Frequency (Hz), Impedance (Ohm), Phase (degree)
    float, float, float
    ...
    ...
    
    Parameters
    ----------
    infile : str
        Filepath of the input file containing a list of devices which form a circuit 
    outfile : str
        Filepath of the output file, where the results are written to
    circuit_type : str
        Either "Series" for serial or "Parallel" for a parallel configuration of the devices
    fstart: float
        Start of the frequency interval
    fstop: float
        End of the frequency interval
    n : int
        Number of frequencies to sample inside the frequency interval.
        Hint: use 'numpy.logspace' for creating an array of frequencies evenly spaced on a logarithmic scale

    Returns
    -------
    float
        Frequency at which the magnitude of the circuit impedance is minimum (for a series circuit) or maximum (for a parallel circuit).
        Hint: check the functions 'numpy.argmin' and 'numpy.argmax'
    """

    with open(infile, "r") as file:
        file.readline()
        data = [line.strip().split() for line in file if line.strip()]
    devices = []
    for d in data:
        #print(data)
        devices.append(task2.Device(d[0], float(d[1])))

    #print("DEVICES::::")
    #for dev in devices:
    #    print(dev.dev_val)
    circ = task2.Circuit(circuit_type, devices)

    x = np.logspace(np.log10(fstart), np.log10(fstop), n)
    y = [(circ.impedance(xn)) for xn in x]
    with open(outfile, "w") as file:
        file.write("# Frequency (Hz), Impedance (Ohm), Phase (degree) \n")
        for n in range(len(x)):
            file.write(f"{x[n]}, {abs(y[n])}, {math.degrees(cmath.phase(y[n]))}\n")
    plt.plot(x, y)
    plt.show()
    if circuit_type == 'Series':
        return x[np.argmin([abs(yn) for yn in y])]
    elif circuit_type == 'Parallel':
        return x[np.argmax([abs(yn) for yn in y])]
    pass


def plot_impedance(frequencies: list[float], magnitudes: list[float],
                   phases: list[float], filename: str) -> None:
    """
    Plots the magnitude and the phase of the impedance as a function of the frequency.
    The plot should contain meaningful labels for the axes and units.

    Hint: use a log scale for the frequency and the magnitude, and a linear scale for the phase.

    Parameters
    ----------
    frequencies : list[float]
        Frequencies (x-axis)
    magnitudes : list[float]
        Magnitude of the impedance (y-axis)
    phases : list[float]
        Phase of the impedance (y-axis)
    filename : str
        Filepath for the generated plot.
    """
    fig, ax1 = plt.subplots()
    
    ax1.plot(frequencies, magnitudes)
    ax1.set_ylabel("Magnitude")
    ax1.set_xlabel("Frequencies")
    
    ax2 = ax1.twinx()
    ax2.set_ylabel("Phase")
    ax2.plot(frequencies, phases, color='orange')
    
    plt.savefig(filename)
    plt.show() 
    pass


if __name__ == '__main__':
    """ You can call your functions here to perform your own test. """
    #print(frequency_analyzer("input_RL.csv", "output_LC.csv", "Parallel", 1, 10, 30))

    #plot_impedance(, magnitudes: list[float],
    #               phases: list[float], filename: str)

    infile = "input_RC.csv"
    outfile = "test_task3_output_RC_parallel.csv"


    f1 = 100 # Hz
    fn = 1e6 # Hz
    n = 1000
    f0 = frequency_analyzer(infile, outfile, "Parallel", f1, fn, n)
    print(f0)
    pass
