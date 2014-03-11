from PIL import Image
import math

# Determines the average color code of the various colors in a given picture.  Run this only once for the project to reduce
# runtime.
class ColorRange:
    def __init__(self):
        True

    def getColorRanges(self,path = 'C:\\Users\\Babyburger\\PycharmProjects\\PENOROODpy\\output\\7.jpg'):
        image = Image.open(path)
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
            (H,S,V) = self.RGBtoHSV(x,y,z)
            #print (H,S,V)
            # works well!  compare with actual pictures (and the online converter)

            if(V > 0.9 and S < 0.2):    # white condition
                whitelst.append((x,y,z))
            else:
                if(H < 50 and H > 25 and S > 0.45 and V > 0.75):   # yellow condition
                    yellowlst.append((x,y,z))
                else:
                    if(H < 13 and H > 335 and S > 0.60 and V > 0.60):   # red condition
                        redlst.append((x,y,z))
                    else:
                        if(H < 260 and H > 205 and S > 0.15 and V > 0.2 and V < 0.65):   # blue condition
                            bluelst.append((x,y,z))
                        else:
                            if(H > 60 and H < 180 and S < 0.6 and V < 0.6):     # green condition
                                greenlst.append((x,y,z))

        # set several conditions depending on the color to retrieve and put it in the corresponding list.
        # then find the average for each of those lists so 1 list of 5 tuples are returned. (one for each determined color)
        # Each of those tuples will represent the new value for the colorDistance measurement

        colorCodes = []
        colorCodes.append(self.findMeanRGB(whitelst))
        colorCodes.append(self.findMeanRGB(yellowlst))
        colorCodes.append(self.findMeanRGB(redlst))
        colorCodes.append(self.findMeanRGB(greenlst))
        colorCodes.append(self.findMeanRGB(bluelst))
        return colorCodes   # returns the list of color codes in the following order:
                #white, yellow, red, green, blue (in RGB)

    def findMeanRGB(self,lst):
        h = []
        s = []
        v = []
        if lst is not None:
            for H,S,V in lst:
                h.append(H)
                s.append(S)
                v.append(V)
        else:
            print 'A color is not found.'

        meanh = sum(h) / float(len(h))
        means = sum(s) / float(len(s))
        meanv = sum(v) / float(len(v))
        print meanh
        print means
        print meanv
        R,G,B = self.HSVtoRGB(meanh,means,meanv)
        print R
        print G
        print B
        return (R,G,B)

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
        return h, s, v

        # Follow this algorithm: http://www.rapidtables.com/convert/color/rgb-to-hsv.htm

    def HSVtoRGB(self,h,s,v):
        h = float(h)
        s = float(s)
        v = float(v)
        h60 = h / 60.0
        h60f = math.floor(h60)
        hi = int(h60f) % 6
        f = h60 - h60f
        p = v * (1 - s)
        q = v * (1 - f * s)
        t = v * (1 - (1 - f) * s)
        r, g, b = 0, 0, 0
        if hi == 0: r, g, b = v, t, p
        elif hi == 1: r, g, b = q, v, p
        elif hi == 2: r, g, b = p, v, t
        elif hi == 3: r, g, b = p, q, v
        elif hi == 4: r, g, b = t, p, v
        elif hi == 5: r, g, b = v, p, q
        r, g, b = int(r * 255), int(g * 255), int(b * 255)
        return r, g, b

