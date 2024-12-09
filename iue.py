import numpy as np

def read_devices(filename):
    """
    Reads a list of electrical devices form a file.
    Expected file format:

    # header line
    str float str
    ...
    
    where the strings have a maximum length of 10.

    Parameters
    ----------
    filename : str
        Filepath of the file to read
          
    Returns
    -------
    list[(str,float)]
        Each tuple in the list represents the first two columns of a line in the input file.
    """


    # read data into numpy array with a fitting dtype
    data = np.loadtxt(filename, dtype={'names': ('Device', 'Value', 'Unit')
                                       , 'formats': ('U10', 'float', 'U10')})
    # access data using field names 
    devs = data['Device']
    vals = data['Value']

    # create a list of tuples: (device type, value)
    devices = [(dev, val) for dev, val in zip(devs,vals)]
    
    # return list
    return devices


if __name__ == "__main__":
    # Example of usage
    infile = "input_RLC4.csv"
    devs = read_devices(infile)
    print(devs)