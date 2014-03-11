# Using a method to determine hsv per pixel is getting cpu intensive and complicated fast.
# Use http://www.rapidtables.com/convert/color/rgb-to-hsv.htm to experiment with the color ranges.

import FindColorCode as fc

colors = fc.ColorRange()
#colors.getColorRanges()
d = colors.findMeanRGB([(50,0.8,0.8),(70,0.5,0.9)])

