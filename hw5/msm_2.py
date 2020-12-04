'''
This script uses the minimal substorm model script created in class as its basis. Unlike the script developed in class,
this script does not require IDL. The output of this script is a figure in which DST, Solar Wind Power, and Tail Wind
Energy is plotted over time for the year 2003. The time of the substorm epochs are also saved to a file:
 substorm_epochs.txt.

Authors: Dan Welling and Tre'Shunda James
'''

import numpy as np
import matplotlib.pyplot as plt
from hw5.sciprog_ import ImfData
from hw5.sciprog3 import read_dst

# Set our plotting style:
plt.style.use('seaborn-darkgrid')

# Set D constant in seconds.
D = 2.69 * 3600.  # Hours -> seconds

# Open data file, calculate required values.  Use
# our object oriented approach.
imf = ImfData('imf.dat')
imf.calc_epsilon()  # This also calculates |V| and |B|.

#dst data
data_dst = read_dst('dstfile.dat')

# Create results containers: energy will have the
# same number of entries as our solar wind file.
# We don't know how many substorms we'll generate a priori,
# so we'll create an empty list to which we can append values.
n_pts = imf['time'].size
energy = np.zeros(n_pts)
epochs = []

# Set our initial energy condition.  Do this by assuming a substorm
# just happened, so our energy state is D*P below the energy
# threshold value (assumed to be zero, see the powerpoint file).
# Use the average epsilon value to initialize:
energy[0] = -D * imf['epsilon'].mean()

# Integrate!
# Loop over all subsequent time values.  "i" represents the
# position of t_now + delta T; i-1 is t_now.  Each iteration
# advances from t_now to t_now + delta T.
for i in range(1, n_pts):
    # Get time step from imf file.  Subtract two times, which
    # gives us a "timedelta" object.  By calling the "total_seconds"
    # method, we convert it into a floating point value.
    dt = (imf['time'][i] - imf['time'][i - 1]).total_seconds()

    # This is our actual integration step (Euler's Method):
    energy[i] = energy[i - 1] + imf['epsilon'][i] * dt

    # See if we crossed our threshold:
    if energy[i] >= 0:
        # If so, "release energy" as required by MSM:
        energy[i] = - D * imf['epsilon'][i]
        # Save epoch to list:
        epochs.append(imf['time'][i])

# Save epochs to file.  Note that we're using the "with" statement.
# See sciprog_.py for details on this.
# Note how we end each line with a newline character (\n).
with open('substorm_epochs.txt', 'w') as f:
    f.write('Substorm onsets created from the Minimal Substorm Model (MSM)\n')
    f.write(f'Input file used: {"imf_test.dat"}\n')
    for e in epochs: f.write(f'{e:%Y-%m-%d %H:%M:%S} UT \n')

# Create figure object and axes objects.
fig = plt.figure(1,figsize = (7, 6.7)) # create figure and set size

a1, a2, a3= fig.add_subplot(311), fig.add_subplot(312), fig.add_subplot(313) # add three axis to the figure


# Create line plots:
a1.plot(imf['time'], imf['epsilon'], 'r-', lw=2) # plot solar wind power vs time
a2.plot(imf['time'], energy, '-', lw=2) # plot tail energy state vs time
a3.plot(imf['time'], data_dst['dst'], color='green',lw=2) # plot dst vs time

# Create and label horizontal threshold line:
a2.text(imf['time'][0], 0.3, 'Substorm Energy Threshold') # position the label

# Place epochs onto plot, preserving y-limits.
ymin, ymax = a2.get_ylim()  # get current axis limits.
ymax = 1.2  # add some space above zero.


# Y-axes labels:
a1.set_ylabel('Solar Wind Power', size=12)
a2.set_ylabel('Tail Energy State', size=12)
a3.set_ylabel('DST', size=12)

# Y-axis ticks:
a1.set_yticklabels('')
a2.set_yticklabels('')
a3.set_yticklabels('')

fig.tight_layout()

plt.show()
