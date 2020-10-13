"""
This script will open DST file from KYPTO, parse the data, and load the hourly DST data into a one-dimensional
numpy array and the date-time objects into 1-D array; both arrays will print to screen.
It will also print to screen min, max, mean, median, and std of hourly DST data.
Next, import the module:
#>>>import sciprog2
Author: Tre'Shunda James
"""

def read_dst(infile, debug=False):
    '''
    This functionopen DST file from KYPTO, parse the data, and load the hourly DST data into a one-dimensional
    numpy array and the date-time objects into 1-D array; both arrays will print to screen.
    It will also print to screen min, max, mean, median, and std of hourly DST data.

    Usage:
    #>>>data = read_dst('some_file_name.dat')

    The returned value is a dictionary of values read from the file.

    The *debug* kwarg, if set to **True**, will create debug print outs.

    This function serves as a simple example; in real-life, creating a class
    that knows how to read, write, and plot these types of files is way more
    useful!
    '''


    # Import datetime package
    import datetime as dt

    # Open DST file
    f = open('Dst_July2000.dat')
    # Read the lines in the file and assign them to a variable called lines
    lines = f.readlines()
    # Close the file
    f.close()
    #print(lines) to check the data is opened, read and assigned as expected
    nLines = len(lines)

    #data2 = {}  # empty dictionary.

    #data2['time'] = np.zeros(nLines, dtype='object')
    #data2['dst'] = np.zeros(nLines)
    # Empty array for the DST values
    data = []
    # Empty array for list of date-time strings
    time = []
    # Empty array for converted list of date-time objects (Bonus)
    date_time = []

        ## Planning  for parsing the DST data
        #For each line:
        #   Skip first 20 characters and stop before the last 4 characters and save it as l2
        #   For character in l2:
        #       Split l2 every 4 characters
        #       Make string to int and save as data2
        #   Append data2 to data array

    # For loop to go through each line in file
    for j,l in enumerate(lines):
        l2 = l[20:117] # Hourly DST data starts at character 20 and ends with character 116 for each line assigned
                   # to list l2
        l1 = l[3:17] # String of characters that include the date and time for each line assigned to list l1
        n = 4 # Number of characters used for each hourly DST value

        # for-loop to parse l2 every four characters
        for i in range(0, len(l2)-1, n):
            data2 = int(l2[i:i+n]) # Every set of four characters is converted into an integer and assigned to data2
            data.append(data2) # data2 is added to the empty data array
            #data2['dst'][j] = data4

        # now for-loop to increment the hour by 1 from 0-23 (24 hours).
        for k in range(0, 24, 1):
            data3 = (l1[11:13]+l1[1:3]+l1[2:4]+l1[5:7]+str(k)) # Stringing together only the parts that contribute to
                                                           # date-time. First two digits of year+ second two
                                                           # digits of year+month+date+ str(hour) and assign to data3
            time.append(data3) # data3 is added to empty time array

        # Now for-loop to convert time from a list of  string of numbers into a list in datetime format
    for item in time: # For every string in the time array
            date= dt.datetime.strptime(item, '%Y%m%d%H') # Use the datetime.strptime function on string in time array
                                                             # that has the format YYYYMMDDH to convert it to date-time
                                                             # object. Assign date a string of date-time objects.
            #data2['time'][j] = dt.datetime.strptime(data3, '%Y%m%d%H')
            date_time.append(date) # date is added to empty date_time array


    data2 = {}  # empty dictionary.

    data2['time'] = date_time # add the date_time array to data2 dictionary under keyword time
    data2['dst'] = data # add the data array to data2 dictionary under keyword time

    return(data2)






