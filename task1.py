"""
Task1: Implement the following functions according to the
specification provided in the comments below.
"""

def device_impedance(dev_type: str, dev_val: float, freq: float) -> complex:
    """ Calculates the impedance (complex number) of a device at a given frequency.

    Parameters
    ----------
    dev_type : Type of device: "R", "L", or "C"
    dev_val : Nominal value of the device
    freq : Frequency for which the impedance is computed

    Raises
    ------
    exception : ValueError
        if type of device is different from "R", "L", or "C", e.g.:
        raise ValueError(f"Message with a brief explanation of the reason for the Exception being raised")

    Returns
    -------
    Impedance of the device as a complex number
    """
    pass


def series_impedance(devices: list[tuple[str, float]], freq: float) -> complex:
    """ Calculates the total impedance for a set of devices connected in series.

    Parameters
    ----------
    devices : Each tuple in the list represents a device:
                First item: type of device: "R", "L", or "C"
                Second item: nominal value of device
    freq : Frequency for which the impedance is computed

    Returns
    -------
        Total impedance as a complex number
    """
    pass


def parallel_impedance(devices: list[tuple[str, float]], freq: float) -> complex:
    """ Calculates the total impedance for a set of devices connected in parallel.

    Parameters
    ----------
    devices : Each tuple in the list represents a device:
                First item: type of device: "R", "L", or "C"
                Second item: nominal value of device
    freq : Frequency for which the impedance is computed

    Returns
    -------
    complex
        Total impedance as a complex number
    """
    pass


if __name__ == '__main__':
    """ You can call your functions here to perform your own tests. """
    pass