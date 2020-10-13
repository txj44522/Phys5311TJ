'''
This script will read and open a given DST file and IMF file using two different modules-- the sciprog module and the
 sciprog3 module. After loading the data, the script will then explore the data by plotting different parameters.
 Specifically, plots are generated for DST vs Time, B vs Time, V vs Time,  Density vs Time and a summary plot comparing
 Bz, DST, and Density. Any of the plots can be modified as needed.
'''

import sciprog, sciprog3 # modules to read, open, parse imf and dst data
import matplotlib.pyplot as plt # import matplotlib.plt for plotting purposes

data = sciprog.read_imf('imf_jul2000.dat') # the return statement for the sciprog module
data2 = sciprog3.read_dst('Dst_July2000.dat') # the return statement for the sciprog3 module

# to check the data is opened, read and parsed as expected
#print(data)
#print(data2)

# to check the time range of interest are the same (7/15/2000 - 7/20/2000). This range covers the full recovery period.
#print(data['time'][7200:14401])
#print(data2['time'][336:457])

# plot DST vs Time
plt.figure(1, figsize = (10, 7)) # create figure, labels it as figure 1 and sets it size
plt.plot(data2['time'][336:457], data2['dst'][336:457], 'purple') # plotting dst data for the time of interest
plt.ylabel('$D_{ST}$ $(nT)$') # set y label
plt.xlabel('Time (UT)') # set x label
plt.title('"Bastille Day" Solar Storm') # creates title for the figure


# plot B-field vs Time (3 plots)
fig2 = plt.figure(2, figsize = (10, 7)) # creates and label figure 2
gs = fig2.add_gridspec(3, hspace=0) # splits the figure into 3 subplots
axs = gs.subplots(sharex=True, sharey=False) # makes x axis shared amongst the 3 plots
fig2.suptitle('Magnetic Field vs Time') # creates title for the figure

axs[0].plot(data['time'][7200:14401], data['bx'][7200:14401], linewidth=1.0) # plots time vs bx on the first axis
                                                                             # with a blavk line of thickness 1
axs[0].set_ylabel('$B_x$ $(nT)$') # creates y axis label

axs[1].plot(data['time'][7200:14401], data['by'][7200:14401],'orange', linewidth=1.0) # plots time vs by on the second
                                                                                      # axis with a orange line of
                                                                                      # thickness 1
axs[1].set_ylabel('$B_y$ $(nT)$') # creates y axis label

axs[2].plot(data['time'][7200:14401], data['bz'][7200:14401],'g', linewidth=1.0) # plots time vs by on the third axis
                                                                                 # with a  green line of thickness 1

axs[2].set_ylabel('$B_z$ $(nT)$') # creates y axis label


for ax in axs:
    ax.label_outer() # only show outer most label
    ax.set_xlabel('Time (UT)') # creates x axis label only for the outer most plot

# plot velocity vs time
plt.figure(3, figsize = (10, 7)) # creates and label figure 3
plt.plot(data['time'][7200:14401], data['vx'][7200:14401], 'k', linewidth=1.0, label= '$v_x$') # plots vx vs time
plt.plot(data['time'][7200:14401], data['vy'][7200:14401], 'blue', linewidth=1.0, label= '$v_y$') # plots vy vs time
plt.plot(data['time'][7200:14401], data['vz'][7200:14401], 'c', linewidth=1.0, label= '$v_z$') # plots vz vs time
plt.ylabel('Velocity (GSE) ($km/s$)') # creates y axis label
plt.xlabel('Time (UT)') # creates x axis label
plt.title('Velocity vs Time') # creates title for the figure
plt.legend(loc = 'lower right', fontsize = 'large') # creates legend in large font


# plot density vs time
plt.figure(4, figsize = (10, 7)) # creates and label figure 4
plt.plot(data['time'][7200:14401], data['rho'][7200:14401], 'm', linewidth=1.0) # plots density vs time
plt.ylabel('Density ($N/m^3$)') # creates y axis label
plt.xlabel('Time (UT)') # creates x axis label
plt.title('Density vs Time')  # creates title for the figure

# figure of Dst and Bz and Density
# note,the range here is adjusted to focus on the main part of the storm; it does not cover the entire recovery period
fig5 = plt.figure(5, figsize = (10, 7)) # creates and label figure 5
gs = fig5.add_gridspec(3, hspace=0) # splits the figure into 3 subplots
axs = gs.subplots(sharex=True, sharey=False) # makes x axis shared amongst the 3 plots
fig5.suptitle("Summary Plot")


axs[2].plot(data2['time'][336:385], data2['dst'][336:385], 'purple', linewidth=1.0) # plots dst vs time
axs[2].set_ylabel('$D_{st}$ $(nT)$') # creates y axis label


axs[1].plot(data['time'][7200:10087], data['rho'][7200:10087],'orange', linewidth=1.0) # plots density vs time
axs[1].set_ylabel('Density ($N/m^3$)') # creates y axis label


axs[0].plot(data['time'][7200:10087], data['bz'][7200:10087],'g', linewidth=1.0) # plots bz vs time
axs[0].set_ylabel('$B_z$ $(nT)$') # creates y axis label
axs[0].hlines(0,data['time'][7200], data['time'][10087],'r', linewidth=0.3, linestyles='dashed') # plots red horizontal
                                                                                                 # dashed line of
                                                                                                 # thickness 0.3 that
                                                                                                 # spans the data at x=0

for ax in axs:
    ax.label_outer() # only show outer most label
    ax.set_xlabel('Time (UT)') # creates x axis label only for the outer most plot




plt.tight_layout() # tight layout for all plots

plt.show() # show all plots

