import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

#######################
# plot
#######################
x = np.array([1, 8])
y = np.array([0, 150])

# plot x and y using default line style and color
plt.plot(x, y)
plt.savefig("Plot x and y using default line style and color.png")
plt.show()

# plot x and y using blue circle markers
plt.plot(x, y, 'bo')
plt.savefig("Plot x and y using blue circle markers.png")
plt.show()

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

# plot multiple points using default line style and color
plt.plot(x, y)
plt.savefig("Plot multiple points (default version).png")
plt.show()

# plot multiple points using blue circle markers
plt.plot(x, y, 'bo')
plt.savefig("Plot multiple points(blue circle marker version).png")
plt.show()

#######################
# marker
#######################

y = np.array([13, 28, 11, 100])

plt.plot(y, marker="o")
plt.savefig("Plot multiple points(circle marker version).png")
plt.show()

plt.plot(y, marker="*")
plt.savefig("Plot multiple points(star marker version.png")
plt.show()

"""
Resources: 
markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']
"""

#######################
# line
#######################

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashed", color="r")
plt.savefig("Plot multiple points(Dashed version).png")
plt.show()

plt.plot(y, linestyle="dotted", color="r")
plt.savefig("Plot multiple points(Dotted version).png")
plt.show()

plt.plot(y, linestyle="dashdot", color="r")
plt.savefig("Plot multiple points(Dashdot version).png")
plt.show()

#######################
# Multiple Lines
#######################

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.savefig("Multiple Lines.png")
plt.show()

#######################
# Labels
#######################
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)

# Title
plt.title("This is main title")
plt.xlabel("Name of X Axis")
plt.ylabel("Name of Y Axis")
plt.grid()
plt.savefig("Plotting with Title and Names of Axes.png")
plt.show()

#######################
# Subplots
#######################

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)
plt.title("First Graph")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 2, 2)
plt.title("Second Graph")
plt.plot(x, y)
plt.savefig("Positioning 2 charts as one row and 2 columns.png")
plt.show()

#######################
# Positioning 3 charts as one row and 3 columns
#######################

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("First Graph")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 3, 2)
plt.title("Second Graph")
plt.plot(x, y)

# plot 3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("Third Graph")
plt.plot(x, y)

plt.savefig("Positioning 3 charts as one row and 3 columns.png")
plt.show()
