import scipy as sp
from scipy import ndimage
from PIL import Image
from math import *
import numpy as np

from numpy import array

def logpolar(input,silent=False):
    # This takes a numpy array and returns it in Log-Polar coordinates.

    if not silent: print("Creating log-polar coordinates...")
    # Create a cartesian array which will be used to compute log-polar coordinates.
    coordinates = sp.mgrid[0:max(input.shape)*2,0:360]
    # Compute a normalized logarithmic gradient
    log_r = 10**(coordinates[0,:]/(input.shape[0]*2.)*log10(input.shape[1]))
    # Create a linear gradient going from 0 to 2*Pi
    angle = 2.*pi*(coordinates[1,:]/360.)

    # Using scipy's map_coordinates(), we map the input array on the log-polar 
    # coordinate. Do not forget to center the coordinates!
    if not silent: print("Interpolation...")
    lpinput = ndimage.interpolation.map_coordinates(input,
                                            (log_r*sp.cos(angle)+input.shape[0]/2.,
                                             log_r*sp.sin(angle)+input.shape[1]/2.),
                                            order=3,mode='constant')

    # Returning log-normal...
    return lpinput

def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data

def save_image( npdata, outfilename ) :
    img = Image.fromarray( np.asarray( np.clip(npdata,0,255), dtype="uint8"), "L" )
    img.save( outfilename )

image = load_image("C:/index1.jpg")
target = load_image("C:/index2.jpg")

# Conversion to log-polar coordinates
lpimage = logpolar(image)
lptarget = logpolar(target)

# Correlation through FFTs
Fcorr = np.fft.fft(lpimage)*np.fft.fft(lptarget)
correlation = np.fft.ifft(Fcorr)

"""
# Correlation
# alternative to FFTs
correlation = np.correlate(lpimage,lptarget)
"""

