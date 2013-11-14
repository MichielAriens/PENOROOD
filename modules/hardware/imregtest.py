import imreg
from PIL import Image
import numpy as np

"""
image = Image.open("C:/red-imagetesting/imagex1.jpg")
target = Image.open("C:/red-imagetesting/imagex2.jpg")
"""

def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data

def save_image( npdata, outfilename ) :
    img = Image.fromarray( np.asarray( np.clip(npdata,0,255), dtype="uint8"), "L" )
    img.save( outfilename )

image = load_image("C:/red-imagetesting/originalimage.jpg")[:,:,0]
target = load_image("C:/red-imagetesting/scale80.jpg")[:,:,0]

(result, scale, angle, [a, b]) = imreg.similarity(image, target)

save_image(result,"C:/red-imagetesting/result.jpg")

print result
print scale
print angle
print a
print b