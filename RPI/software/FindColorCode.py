from PIL import Image

# Determines the average color code of the various colors in a given picture.  Run this only once for the project to reduce
# runtime.
class ColorRange:
    def __init__(self):
        True

    def getColorRanges(self,image=Image.open('C:\\Users\\Babyburger\\PycharmProjects\\PENOROODpy\\output\\7.jpg')):
        rgb_im = image.convert('RGB')
        pixels = list(rgb_im.getdata())

        #pixels = np.array(image.getNumpy()).reshape(-1, 3)
        redlst = []
        greenlst = []
        bluelst = []
        whitelst = []
        yellowlst = []

        for pixel in pixels:
            (x,y,z) = pixel
            (a,b,c) = self.RGBtoHSV(x,y,z)
            # works well!  compare with actual pictures (and the online converter)
            print (a,b,c)
            # set several conditions depending on the color to retrieve and put it in the corresponding list.
            # then find the average for each of those lists so 1 list of 5 tuples are returned. (one for each determined color)
            # Each of those tuples will represent the new value for the colorDistance measurement

    def RGBtoHSV(self,R,G,B):
        r, g, b = R/255.0, G/255.0, B/255.0
        mx = max(r, g, b)
        mn = min(r, g, b)
        df = mx-mn
        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g-b)/df) + 360) % 360
        elif mx == g:
            h = (60 * ((b-r)/df) + 120) % 360
        elif mx == b:
            h = (60 * ((r-g)/df) + 240) % 360
        if mx == 0:
            s = 0
        else:
            s = df/mx
        v = mx
        print (h,s,v)
        return h, s, v

        # Follow this algorithm: http://www.rapidtables.com/convert/color/rgb-to-hsv.htm

