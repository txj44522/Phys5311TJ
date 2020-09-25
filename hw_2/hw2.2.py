"""
This script will open DST file from KYPTO, parse the data, and load the hourly DST data into a one-dimensional
numpy array and the date-time objects into 1-D array; both arrays will print to screen.
It will also print to screen min, max, mean, median, and std of hourly DST data.

Author: Tre'Shunda James
"""
# Import numpy package
import numpy as np
# Import datetime package
import datetime as dt

# Open DST file
f = open('Dst_July2000.dat')
# Read the lines in the file and assign them to a variable called lines
lines = f.readlines()
# Close the file
f.close()
#print(lines) to check the data is opened, read and assigned as expected

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


    # now for-loop to increment the hour by 1 from 0-23 (24 hours).
    for k in range(0, 24, 1):
        data3 = (l1[11:13]+l1[1:3]+l1[2:4]+l1[5:7]+str(k)) # Stringing together only the parts that contribute to
                                                           # date-time. First two digits of year+ second two
                                                           # digits of year+month+date+ str(hour) and assign to data3
        time.append(data3) # data3 is added to empty time array

# Now for-loop to convert time from a list of  string of numbers into a list in datetime format
for item in time: # For every string in the time array
    date = str(dt.datetime.strptime(item, '%Y%m%d%H')) # Use the datetime.strptime function on string in time array
                                                       # that has the format YYYYMMDDH to convert it to date-time
                                                       # object. Assign date a string of date-time objects.
    date_time.append(date) # date is added to empty date_time array

# Now for the print statements.

# Print to screen the 1-D array of hourly DST data. Just for visualization purposes.
#print('Here is the hourly DST data in a 1-D array: \n {} \n'.format(data))

# Print to screen the 1-D array of date-time objects. Just for visualization purposes.
#print('Here is a array of date-time objects to match the hourly DST data array:  \n {}\n'.format(date_time))

# Exploring the hourly DST data. Print to screen the min, maximum, mean, median, and std of hourly DST
print('The minimum hourly DST: {:.2f} \n'.format(np.min(data))) # Minimum DST is formatted with 2 decimal places
print('The maximum hourly DST: {:.2f} \n'.format(np.max(data))) # Maximum DST is formatted with 2 decimal places
print('The mean hourly DST: {:.2f} \n'.format(np.mean(data))) # Mean DST is formatted with 2 decimal places
print('The median hourly DST: {:.2f} \n'.format(np.median(data))) # Median DST is formatted with 2 decimal places
print('The standard deviation in hourly DST: {:.2f} \n'.format(np.std(data))) # Std of DST is formatted with 2
                                                                              # decimal places





