'''
This script takes inputs from the user. The inputs are start date in the form YYYYMMDD, stop date in the form YYYYMMDD,
x-coordinate to be plotted as a string, and the y-coordinate to be plotted as a string. The start and stop dates MUSt
have the same year.
x and y are from the set of IMF data keys: Time, Bx, By, Bz, AE, vBz, Mag_Mach, DST, F10.7.
These inputs are then used to plot the desired x and y coordinates for the specified time period.

Example usage: $ python final_.py 20150527 20150911 Time Mag_Mach

Author: Tre'Shunda James
'''

# import the necessary modules
from argparse import ArgumentParser
import datetime as dt

# To parse arguments given by the caller
parser = ArgumentParser(description=__doc__)

# Add arguments:
# The first argument is the start date
parser.add_argument('start_date', help='Date to fetch solar wind data in YYYYMMDD' +
                    ' format.', type=str)
# The second argument is the end date
parser.add_argument('end_date', help='Date to fetch solar wind data in YYYYMMDD' +
                    ' format.', type=str)
# The third argument is the x coordinate to plot
parser.add_argument('x', help='IMF data key parameter for the x-axis' +
                    ' format.', type=str)
# The last argument is the y coordinate to plot
parser.add_argument('y', help='IMF data key parameter for the y-axis' +
                    ' format.', type=str)

args = parser.parse_args()


try:
    # Try to parse date into datetime object.
    time = dt.datetime.strptime(args.start_date, '%Y%m%d')
except ValueError:  # Specify the type of exception to be specific!
    # If we can't, stop the program and print help.
    print('ERROR: Could not parse date!')
    print(__doc__)
    exit()
# ----------------------------------------------------------------------------------------------
# import additional modules
import final # here function are stored
import matplotlib.pyplot as plt # for plotting purposes

# Function to build imf for the desired year. This function returns the url associated with the imf data
url = final.build_imf_('{0.year}'.format(time))
# Function to read the imf associated with the desired year and parse the data into a dictionary.
data = final.read_imf_(('imf_file_{0.year}.dat').format(time))

#print(data) # for debugging purposes

# Now plotting
# First, convert YYYYMMDD to DOY for start date and end date
start = \
    (dt.datetime.strptime(args.start_date, "%Y%m%d")-dt.datetime.strptime(f"{args.start_date[:4]}0101", "%Y%m%d")).days
end = (dt.datetime.strptime(args.end_date, "%Y%m%d")-dt.datetime.strptime(f"{args.end_date[:4]}0101", "%Y%m%d")).days
#print(start+1) # For debugging, this should be the start day
#print(end+1) # For debugging, this should be the end day.

# Start figure
plt.figure(1, figsize=(14,5))
# Set title to be the year of the data that's being plotted
plt.title('{} - {}'.format(args.start_date, args.end_date))
# Plot as a scatter plot the given x and y arguments provided by the caller for the start and end date give.
# The plot will start at the 0th hour on the given start date and end at the 23rd hour of the given end date.
# Only want line plots if it is a time series, else make a scatter plot.
if args.x == 'Time':
    plt.plot(data[args.x][start*24:(end+1)*24], data[args.y][start*24:(end+1)*24])

else:
    plt.scatter(data[args.x][start * 24:(end + 1) * 24], data[args.y][start * 24:(end + 1) * 24])
#print(data[args.x][start*24:(end+1)*24]) # For debugging. Check the range of data.

# Set x and y labels as those given by the caller and add units to figure.
# First, make dictionary for units
units = {'Time': 'UT', 'Bx':'GSM', 'By': 'GSM', 'Bz': 'GSM', 'AE': 'nT', 'vBz': 'mV/m', 'Mag_Mach': ' ', 'DST': 'nT ',
         'F10.7': 'sfu'}

# Use string formatting
units_x = units['{}'.format(args.x)]
units_y = units['{}'.format(args.y)]
plt.xlabel('{}'.format(args.x) + ' ' + '$({})$'.format(units_x))
plt.ylabel('{}'.format(args.y) + ' ' + '$({})$'.format(units_y))

# Limit the white space around the plot in the figure
plt.tight_layout()
# Show the figure
plt.show()
#------------
