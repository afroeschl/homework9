"""
Task2: Implement the following classes according to the
specification provided in the comments below.
"""

import task1
import math

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
        self.dev_type = dev_type
        self.type = dev_type
        self.dev_val = dev_val
        self.value = dev_val
        pass

    def __str__(self) -> str:
        """ Generates a string describing the object's state.
        
        Returns
        -------
        str
            Informative string (including values of the attributes)
        """
        return f"This is a {self.dev_type} with a nominal value of {self.dev_val}"
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

        if self.dev_type == other.dev_type and self.dev_val == other.dev_val:
            return True
        else:
            return False
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
        if self.dev_type == 'R':
            return complex(self.dev_val, 0)
        elif self.dev_type == 'C':
            return complex(0, -1 * (1 / (2 * math.pi * freq * self.dev_val)))
        elif self.dev_type == 'L':
            return complex(0, 2 * math.pi * freq * self.dev_val)
        else:
            raise ValueError()
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
        self.circ_type = circ_type
        self.devices = devices
        self.type = circ_type
        pass

    def __str__(self) -> str:
        """ Generates a string describing the object's state.
        
        Returns
        -------
        str
            Informative string (including at least the circuit type and number of the devices)
        """
        return f"This is a {self.dev_type} with a nominal value of {self.dev_val}"
        pass

    def impedance(self, freq: float) -> complex:
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
        if self.circ_type == "Series":
            '''print(([d.dev_type
                  for d in self.devices], [d.dev_val for d in self.devices]),
                freq)'''
            return task1.series_impedance([(d.dev_type, d.dev_val)
                                           for d in self.devices], freq)
        elif self.circ_type == "Parallel":
            '''print(([d.dev_type
                    for d in self.devices], [d.dev_val for d in self.devices]),
                  freq)'''
            return task1.parallel_impedance([(d.dev_type, d.dev_val)
                                           for d in self.devices], freq)
        else:
            raise ValueError
        pass


if __name__ == "__main__":
    """
    You can carry out your own tests here.
    Instantiate objects of both classes and apply their methods.
    """
    R1 = Device("R", 1e3)
    C1 = Device("C", 1e-6)
    L1 = Device("L", 1e-3)
    print(R1.dev_type)
    print(C1.dev_val)
    print(L1.__str__())
    Circ = Circuit("Series", (R1, R1))
    print(Circ.impedance(1000))
    Circ = Circuit("Parallel", (R1, R1))
    print(Circ.impedance(1000))

    R1 = Device("R", 1e3)
    C1 = Device("C", 2e-6)
    L1 = Device("L", 2e-4)
    devs = [R1, C1, L1]
    f = 5e4/(2*math.pi)

    rlc = Circuit("Parallel", devs)
    #for d in devs:
    #print(f"Type: {d.dev_type}, val: {d.impedance(f)}")
    print(rlc.impedance(f))
    pass
