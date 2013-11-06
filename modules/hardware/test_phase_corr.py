import phase_corr
from PIL import Image
import matplotlib.pyplot as plt
from scipy import misc
from pylab import *
from argparse import ArgumentParser
import numpy as np
from numpy import array
import matplotlib.pyplot
# import phase_corr2

def test():

    image1 = Image.open("C:/image1.jpg","r")
    image2 = Image.open("C:/image2.jpg","r")
    a = array(image1)
    b = array(image2)
    corr = (ifftn(fftn(a)*ifftn(b))).real
    """
    test_corr = Image.fromarray(corr, 'RBG')
    test_corr.save('C:/my_img.jpg')
    """
    result = plt.matplotlib.pyplot.imshow(corr)
    print result
    result.write_png("C:/result.jpg")
    print corr

    """
    arr1 = image1.getdata()
    arr2 = image2.getdata()
    print image1
    print arr1
    """

    """
    test1 = misc.imread(infile1)
    """


    """
    parser = ArgumentParser(description="Set parameters phase correlation calculation")

    parser.add_argument("infile1", metavar="in1", help="input image 1")
    parser.add_argument("infile2", metavar="in2", help="input image 2")
    parser.add_argument("outfile", metavar="out", help="output image file name")
    """


    # test phase_corr2
    """
    corr = phase_corr2.phaseCorrel(arr1,arr2)
    print corr
    phase_corr2.showNormalized(corr)
    test = phase_corr2.getDispl(corr)
    print test
    """

    # test phase_corr
    """
    corr = phase_corr.phase_correlation(arr1, arr2)
    # print corr
    # test_corr = Image.fromarray(corr, 'RBG')
    # test_corr.save('./my_img.jpg')
    test = corr.argmax()
    print test
    """

    """
    displ = np.array(np.unravel_index(test, corr.shape))
    for i,v in enumerate(displ):
        if v > corr.shape[i]/2:
            displ[i] = corr.shape[i] - displ[i]
    print displ
    """

test()
