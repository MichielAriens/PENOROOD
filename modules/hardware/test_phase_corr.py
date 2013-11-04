import phase_corr
from PIL import Image
import numpy as np
from numpy import array
import phase_corr2

def test():
    image2 = Image.open("./image01.jpg","r")
    image1 = Image.open("./image02.jpg","r")
    arr1 = array(image1)
    arr2 = array(image2)
    corr = phase_corr2.phaseCorrel(arr1,arr2)
    print corr
    phase_corr2.showNormalized(corr)
    test = phase_corr2.getDispl(corr)
    print test
    
    """
    corr = phase_corr.phase_correlation(arr1, arr2)
    test_corr = Image.fromarray(corr, 'jpg')
    test_corr.save('./my_img.jpg')
    test = corr.argmax()
    print corr
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
