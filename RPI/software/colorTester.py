# Using a method to determine hsv per pixel is getting cpu intensive and complicated fast.
# Use http://www.rapidtables.com/convert/color/rgb-to-hsv.htm to experiment with the color ranges.

import shapeRecognition as sr

colors = sr.ColorRange()
#colors.getColorRanges()
colors.RGBtoHSV(50,80,140)