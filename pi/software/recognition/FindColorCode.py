from PIL import Image
import math

# Determines the average color code of the various colors in a given picture.  Run this only once for the project to reduce
# runtime.
class ColorRange:
    def __init__(self):
        True

    def getColorRanges(self, path = 'C:\\Users\\Babyburger\\PycharmProjects\\PENOROODpy\\output\\19.jpg', brightness = "light"):
        image = Image.open(path)
        rgb_im = image.convert('RGB')
        pixels = list(rgb_im.getdata()) # List of all the pixels with RGB values

        #pixels = np.array(image.getNumpy()).reshape(-1, 3)
        redlst = []
        greenlst = []
        bluelst = []
        whitelst = []
        yellowlst = []

        # This loop will append pixels to the respective list (whitelst, ..) if the pixel is within the defined
        # HSV spectrum of the corresponding list.
        for pixel in pixels:
            (x,y,z) = pixel

            (H,S,V) = self.RGBtoHSV(x,y,z)

            if(S < 0.2 and V > 0.9):    # white condition
                whitelst.append((H,S,V))
            else:
                """
                if(S < 0.1 and V > 0.25 and V < 0.6):    #indicates background
                    True
                else:
                """
                if(H < 55 and H > 25 and S > 0.45 and V > 0.80):   # yellow condition
                    yellowlst.append((H,S,V))
                else:
                    if((H < 13 or H > 335) and S > 0.60 and V > 0.60):   # red condition
                        redlst.append((H,S,V))
                    else:
                        if(H < 260 and H > 200 and S > 0.15 and V > 0.2 and V < 0.65):   # blue condition
                            bluelst.append((H,S,V))
                        else:
                            if(H > 80 and H < 200 and S > 0.20 and S < 0.60 and  V < 0.6):     # green condition
                                greenlst.append((H,S,V))
                            """
                            if(brightness == "light" and H > 100 and H < 200 and S > 0.25 and S < 0.60 and  V < 0.6):     # green condition
                                greenlst.append((H,S,V))
                            else:
                                if(brightness == "dark" and H > 60 and H < 200 and S > 0.25 and V < 0.35):     # green secondary condition (dark environment)
                                    greenlst.append((H,S,V))
                            """

        # set several conditions depending on the color to retrieve and put it in the corresponding list.
        # then find the average for each of those lists so 1 list of 5 tuples are returned. (one for each determined color)
        # Each of those tuples will represent the new value for the colorDistance measurement

        colorCodes = []
        colorCodes.append(self.findMeanRGB(whitelst))
        colorCodes.append(self.findMeanRGB(yellowlst))
        colorCodes.append(self.findMeanRGB(redlst,"red"))
        colorCodes.append(self.findMeanRGB(greenlst))
        colorCodes.append(self.findMeanRGB(bluelst))
        return colorCodes   # returns the list of color codes in the following order:
                #white, yellow, red, green, blue (in RGB)


    # THE RGB RESULT FROM HSVtoRGB SEEMS TO BE WRONG: tested it => renew the algorithm (or reverse engineer it  :p )

    def findMeanRGB(self,lst,color=""):
        h = []
        s = []
        v = []
        for element in lst:
            H,S,V = element
            h.append(H)
            s.append(S)
            v.append(V)

        # This checks whether the list is empty or not. If h = [], then so are s and v.
        if(len(h) == 0):
            # print 'A color is not found.'
            return (0,0,0)
        if(color == "red"):     # The average between polar coordinates 350 and 10 should be zero in our case, but doesn't work that
            meanh = 0           # way mathematically. This adjusts it to work for red colors.
            for i in h:
                if(i < 13):     # 13 is a boundary polar coordinate set for red color
                    meanh = meanh + i + 360
                else: meanh = meanh + i
            meanh = meanh / float(len(h))
        else: meanh = sum(h) / float(len(h))

        means = sum(s) / float(len(s))
        meanv = sum(v) / float(len(v))
        R,G,B = self.HSVtoRGB(meanh,means,meanv)

        return (R,G,B)

    # Gives the HSV value for the given RGB pixel
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

    # Gives the RGB value for the given HSV pixel (in the name of all that is holy, use decimals for percentages!!)
    # so 19% = 0.19, not 19 (for S and V only; H is in polar degrees)
    #  0 <= H <= 360 ; 0 <= S <= 1 ; 0 <= V <= 1
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
