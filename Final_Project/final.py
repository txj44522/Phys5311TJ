'''
This module host two functions. One to fetch omni data from cdaweb and download it. The other parses the file into
a dictionary.

Author: Tre'Shunda James
'''

# Define a function to build imf file
def build_imf_(year):
    '''
    This function fetches omni imf data from cdaweb given a specific year. That data is saved to a file.
    This function returns the specific url in which the data was downloaded from.
    :param year: str
    in format 'YYYY'
    :return: url
    '''
    # Import the necessary modules
    import urllib.request
    import urllib
    import datetime as dt

    # Make datetime object for the give year and store it as time.
    time = dt.datetime.strptime(year, '%Y')
    # Create url to download data from.
    # Start with a base_url that directs to the pool of data files
    base_url = 'https://cdaweb.gsfc.nasa.gov/pub/data/omni/low_res_omni/'
    # Now create a url unique to the year of interest. This is the url data will be downloaded from.
    url = base_url + 'omni2_{0.year}.dat'.format(time)
    # Now download the data and save it to a file
    # Create the file and while it is open, open the website, read all of the data file and write it to file.
    with open('imf_file_{0.year}.dat'.format(time), 'wb') as data:
        response = urllib.request.urlopen(url)  # Open website...
        data.write(response.read())  # "read" reads whole file, "write" saves it to file.

    return (url)

# Define a function to read imf file
def read_imf_(infile):
    '''
    This function parse and read certain imf data into a dictionary. Specifically, the keys are: Bx, By,
    Bz, AE, vBz, Mag_Mach, DST, F10.7 and Time. Additionally, this function filters out any fill data.
    :param: str
    in format 'filename.dat'
    :return: dictionary
    '''
    # Import necessary modules
    import numpy as np
    import datetime as dt
    import os

    # Check our arguments, raise "exceptions" (errors) if something is wrong.
    if type(infile) != type('str'):
        raise (TypeError('Input file name must be a string.'))
    # If the file exists. If not its because cdaweb didn't have the omni data. Raise error.
    if not os.path.isfile(infile):
        raise FileNotFoundError('cdaweb does not have omni data available for the year you are requesting.')

    # Open the file in read-only mode by creating a file object.
    f = open(infile, 'r')

    # Read the very first line.  Just like IDL, Python will remember our
    # position in the file so that no lines are read twice.
    lines = f.readlines()
    f.close()
    # How many lines do we have?  The "len()" function will tell us!
    nLines = len(lines)

    # Now we can make a container for our data.  Our container will be a
    # dictionary.  Each variable (time, bx, by, etc.) will be an key with
    # the corresponding value a vector of values.  One way to set it up is:
    data = {}  # empty dictionary.
    keys = ['Bx', 'By', 'Bz', 'AE', 'vBz', 'Mag_Mach', 'DST', 'F10.7'] # IMF parameters of interest
    data['Time'] = np.zeros(nLines, dtype='object')  # a vector of time objects!
    # For-loop to iterate through the keys ary
    for k in keys:
        # Create arrays filled with zeros as place holders
        data[k] = np.zeros(nLines)  # a vector of floats
    # For-loop to iterate through every line and parse data into dictionary.
    for i, l in enumerate(lines):
        # Split up the line into parts.
        parts = l.split()
        # Join first three entries of each line into a string
        tNow = ' '.join(parts[:3])
        # Create datetime object from the string.
        data['Time'][i] = dt.datetime.strptime(tNow, '%Y %j %H')
    # Only want certain values, so use brute force method (actually isn't too bad, since the file format is provided)
    # to assign data to the remaining arrays in the dictionary
        data['Bx'][i] = parts[12]
        data['By'][i] = parts[15]
        data['Bz'][i] = parts[16]
        data['AE'][i] = parts[41]
        data['vBz'][i] = parts[35]
        data['Mag_Mach'][i] = parts[54]
        data['DST'][i] = parts[40]
        data['F10.7'][i] = parts[50]
    # Now deal with fill data
    # For each array the fill data is represented differently, so use brute force method again.
    # This is important for plotting purposes.
    data['Bx'] = np.where(data['Bx'] == 999.9, np.nan, data['Bx'])
    data['By'] = np.where(data['By'] == 999.9, np.nan, data['By'])
    data['Bz'] = np.where(data['Bz'] == 999.9, np.nan, data['Bz'])
    data['AE'] = np.where(data['AE'] == 9999, np.nan, data['AE'])
    data['vBz'] = np.where(data['vBz'] == 999.99, np.nan, data['vBz'])
    data['Mag_Mach'] = np.where(data['Mag_Mach'] == 99.9, np.nan, data['Mag_Mach'])
    data['DST'] = np.where(data['DST'] == 99999, np.nan, data['DST'])
    data['F10.7'] = np.where(data['F10.7'] == 999.9, np.nan, data['F10.7'])


    return (data)


    # In an attempt to streamline replacing the fill data in each array with nan, I tried this loop.
    # But for some reason this loop does't work..
    #conditions = [99.9,999.9, 999.99, 99999, 9999]
    #for j in keys:
        #data[j] = np.where(data[j] == any(condition), np.nan, data[j])





