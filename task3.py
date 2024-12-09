"""
Task3: Implement the following functions according to the
specification provided in the comments below.
"""

def frequency_analyzer(infile: str, outfile: str, circuit_type: str, fstart: float, fstop: float, n: int) -> float:
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
    pass


def plot_impedance(frequencies: list[float], magnitudes: list[float], phases: list[float], filename: str) -> None:
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
    pass


if __name__ == '__main__':
    """ You can call your functions here to perform your own test. """
    pass