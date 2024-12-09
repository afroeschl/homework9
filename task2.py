"""
Task2: Implement the following classes according to the
specification provided in the comments below.
"""


class Device:
    """ Represents an ideal electrical device/component (resistor, capacitor, inductor)

    Attributes
    ----------
    type : str
        "R", "L", or "C": determines if the device object is a resistor, inductor, or capacitor, respectively.
    value : float
        nominal value of the device

    Methods
    -------
    impedance
        Calculates the impedance for a given frequency
    __init__
        Initializer
    __str__
        Informative string
    __eq__
        Equality operator (==)
    """


    def __init__(self, dev_type: str, dev_val: float) -> None:
        """ Initializes the class with the provided device type and value

        Parameters
        ----------
        dev_type : str
            type of device: "R", "L" or "C"
        dev_val : float 
            nominal value of the device
        """
        pass
    
    def __str__(self) -> str:
        """ Generates a string describing the object's state.
        
        Returns
        -------
        str
            Informative string (including values of the attributes)
        """
        pass
    
    def __eq__(self, other: 'Device') -> bool:
        """ Equality operator (==).
        Compares the object with another object for equality.
        Two devices are equal if the 'type' and the 'value' are equal for both devices.

        Parameters
        ----------
        other : Device
            Other object of the same type (class)

        Returns
        -------
        bool
            True if devices are equal, false otherwise
        """
        pass

    def impedance(self, freq: float) -> complex:
        """ Calculates the impedance for a given frequency.

        Parameters
        ----------
        freq : float
            Frequency for which the impedance is computed

        Returns
        -------
        complex
            Impedance
        """
        pass


class Circuit:
    """ Represents a circuit consisting of a set of Devices
    which are either connected in a serial or parallel configuration.

    Attributes
    ----------
    type : str
        "Series" or "Parallel": determines if the devices are connected in series or in parallel.
    devices : list[Device]
        List of devices

    Methods
    -------
    impedance
        Calculates the impedance of the circuit for a given frequency
    __init__
        Initializer
    __str__
        Informative string
    """


    def __init__(self, circ_type: str, devices: list['Device']) -> None:
        """ Initializes the class with the provided type and list of Devices

        Parameters
        ----------
        circ_type : str 
            "Series" or "Parallel" 
        devices : list[Device]
            List of devices
        """
        pass

    def __str__(self) -> str:
        """ Generates a string describing the object's state.
        
        Returns
        -------
        str
            Informative string (including at least the circuit type and number of the devices)
        """
        pass
    
    def impedance(self, freq:float) -> complex:
        """ Calculates the impedance of the circuit for a given frequency.

        Hint: the impedance calculation should take into account if the devices are connected in series or in parallel.

        Parameters
        ----------
        freq : float
            Frequency for which the impedance is computed

        Returns
        -------
        complex
            Total impedance
        """
        pass
    
    
if __name__ == "__main__":
    """
    You can carry out your own tests here.
    Instantiate objects of both classes and apply their methods.
    """
    pass
