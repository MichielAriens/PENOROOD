# look into SimpleCV.Features.Blob -> can determine left/right/above/below positioning between two shapes

# template matching can find an input picture within a larger picture:
#   http://docs.opencv.org/doc/tutorials/imgproc/histograms/template_matching/template_matching.html

# help('modules')

from SimpleCV import Color, Image

# 0) need a way to distinguish colors
# 1) determine size per frame for blob detection
# 2) determine shape with SimpleCV.Features.Blob.Blob isCircle isRectangle isSquare method
#       (define own class for star and heart shape)


image = Image('C:\Users\Babyburger\Desktop\shapes.jpg')
binarized = image.binarize(220).invert()
blobs = binarized.findBlobs()
for blob in blobs:
    blob.draw()
    print blob
    binarized.show()
    raw_input()


# filtering method: http://stackoverflow.com/questions/14036944/how-do-i-locate-the-rabbit


# java method for detecting figures: https://opencv-code.com/tutorials/detecting-simple-shapes-in-an-image/


