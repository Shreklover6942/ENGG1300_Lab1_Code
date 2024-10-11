#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code documentation for Experiment 1 of the Shear Force and Bending Moment 
sections of LAB 1 - ENGG1300

Student ID: z5587706
"""

import matplotlib.pyplot as plt
import numpy as np
import math

#%%
#Shear Force Point Load code

#Define constants
a = 0.260
l = 0.440

# Make theoretical line values
loads = 9.8* np.linspace(0.1, 0.5, 1000)
sf = (loads * a)/l

# Format plot
fig1, ax1 = plt.subplots()
ax1.set_xlabel("Point Load(N)")
ax1.set_ylabel('Shear Force(N)')
ax1.set_title("The Effect of Varying Point Loads on the Shear Force", 
              fontsize = '20', pad = '20')
ax1.grid(True)

#Plot the theoretical prediction
ax1.plot(loads, sf, label = 'Theoretical Prediction')

# Loads
loads1 = [0.9996,1.9502, 2.9302,3.8906, 4.8706]
#Display Shear Force list
disp_sf = [0.6, 1.1,1.6, 2.2, 2.8]
# Plot the scatter the experimental data
ax1.scatter([0.9996,1.9502, 2.9302,3.8906, 4.8706],[0.6, 1.1,1.6, 2.2, 2.8],
            color = 'orange',
            marker = 'x',
            label = 'Experimental Data')

# Create yellow line of best fit
fit1 = np.polyfit(loads1, disp_sf,1)
poly1 = np.poly1d(fit1)
ax1.plot(loads1,poly1(loads1), color = 'yellow', linestyle = '--')

# Make legend
ax1.legend(loc = 'lower right', fontsize = '12')


#%%
# BENDING MOMENT CODE

# Define constants
a=0.3
l = 0.440

# Create theoretical loads to plot the theoretical line
loads = 9.81 * np.linspace(0.1,0.5,1000)
bm = (loads * a * (l-a))/l


# Format plot
fig2, ax2 = plt.subplots()
ax2.set_xlabel("Point Load(N)")
ax2.set_ylabel('Bending Moment (Nm)')
ax2.set_title("The Effect of Varying Point Loads on the Bending Moment", 
              fontsize = '20', pad = '20')
ax2.grid(True)

# Plot Theoretical Prediction
ax2.plot(loads,bm, label = 'Theoretical Prediction')

# Convert from display force readings to bending moment with given formula
force_list = [0.7,1.4, 2.0,2.7,3.2]
experimental_bm = [0.125*i for i in force_list]
loads2 = [0.981,1.962,2.943,3.924,4.905]

# Use previous lists to plot the experimental data and format it
ax2.scatter(loads2, experimental_bm,
            color = 'orange',
            marker = 'x',
            label = "Experimental Data")

# Create yellow line of best fit
fit = np.polyfit(loads2, experimental_bm,1)
poly = np.poly1d(fit)
ax2.plot(loads2,poly(loads2), color = 'yellow', linestyle = '--')

# Create legend
ax2.legend(loc = 'lower right', fontsize = '12')
specific_loads = [0.981, 1.962, 2.943, 3.924, 4.905]

# Compute the theoretical bending moments for these loads(for report table)
# print(np.round([(load * a * (l - a)) / l for load in specific_loads],3))
