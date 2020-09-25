"""
This script will open, read, and parse .dat file using the sciprog module. The script also calculate |B|
 and |V| and the mean values for both over the time period covered by the file. Then calculations for |B| and |V| are
 stored to file named hw2_b.txt in a manner easy to check the calculations. The mean value for |B| and |V| are printed
 to screen.
Author: Tre'Shunda James
"""
# import numpy package
import numpy as np
# specifically imports the sqrt function from the math module. This function will be needed to calculate magnitude.
from math import sqrt

# import this module (sciprog) to read and parse imf data file.
import sciprog
# the return statement for the sciprog module
data = sciprog.read_imf('imf_aug2005.dat')
#print(data) ; to check the data is opened, read and parsed as expected


# define nlines as the number of lines in bz
nLines = len(data['bz'])

#Add magb  and magv to the dictionary and fill magb and magv arrays with as many zeros as the number of lines of bz
data['magb'] = np.zeros(nLines, dtype='object')
data['magv'] = np.zeros(nLines, dtype='object')

#open the write to file and write
with open('hw2_b.txt', 'w') as f:
    f.write('Here is the data.\n \n')
    # formats the column names to be right aligned and separated by 8 characters
    f.write('{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}'.format('Bx','By','Bz','|B|','vx','vy','vz','|v|'))

    # for-loop to calculate |B| and |V| for each row in data
    for j in range(nLines):
      mag_magnetic_field = sqrt(data['bx'][j]**2 + data['by'][j]**2 + data['bz'][j]**2) # For each row calculates |B|
      data['magb'][j] = mag_magnetic_field # adds the calculated |B| for each row to the  magb array

      mag_velocity = sqrt(data['vx'][j]**2 + data['vy'][j]**2 + data['vz'][j]**2) # For each row calculates |V|
      data['magv'][j] = mag_velocity # adds the calculated |V| for each row to the magv array

      #make new array called newdata that has all the relevant arrays of data
      newdata = np.array([data['bx'][j], data['by'][j], data['bz'][j], data['magb'][j], data['vx'][j],
                         data['vy'][j], data['vz'][j], data['magv'][j]])

      f.write("\n") # start new line after each j in loop

      # format the data for each object in newdata array
      for object in newdata:
        f.write('{:+4.1f}\t'.format(object)) # each object (float value) will take up 4 characters not including the
                                             # sign and have one decimal place



#(Question #2) Print statements for the calculated values for the mean of |B| and |V|
print('The mean |B| is: {:.1f} \n'.format(np.mean(data['magb']))) # the mean |B| is formatted to have 1 decimal place
print('The mean |V| is: {:.1f} \n'.format(np.mean(data['magv']))) # the mean |V| is formatted to have 1 decimal place



