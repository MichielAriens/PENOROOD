import modules.hardware.imreg as imreg
import modules.hardware.camera as cam
from PIL import Image
import numpy as np


def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray(img)[:,:,0]
    return data

mycam = cam.Camera(height = 500, width = 500)
mycam.click()
pivot = load_image("data/cam/still.jpg")
while(True):
    raw_input("go\n>")
    mycam.click()
    nextImg = load_image("data/cam/still.jpg")
    (result, scale, angle, trans) = imreg.similarity(pivot, nextImg)
    print "scale = " + str(scale) + "\nangle = " + str(angle) + "\ntranslation = " + str(trans) + "\n\n"
    t = imreg.translation(pivot, nextImg)
    print "translation = " + str(t)
    
    