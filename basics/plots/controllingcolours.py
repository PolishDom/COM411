# marker styles can be specified using single characters
# these include o for circles, s for squares, ^ for triangle up, v for triangle down

plt.plot(x, y, 'o')   # will display circle markers
plt.plot(x, y, 's')   # will display square markers

# similarly, we can control the line styles
# these include - for solid lines, -- for dashed lines, -. for dash-dot lines, : for dotted lines

plt.plot(x, y, 'o-')  # will display circle markers with a solid line
plt.plot(x, y, 'o--') # will display circle markers with a dashed line
plt.plot(x, y, 'o:')  # will display circle markers with a dotted line

# colors can be specified using single characters where r is red, b is blue, g is green, etc.
# supported colours include red, blue, green, cyan, magenta, yellow, black and white.

plt.plot(x, y, 'yo')   # will display yellow markers
plt.plot(x, y, 'ro--') # will display a red dashed line