import cv2
from PIL import Image
from numpy import zeros, arange
from matplotlib.pyplot import figure, show
from skimage.color import rgb2gray
import cv2 as cv
from sys import argv
from morph import *
from imworks import *


def pupil_detect(fname):

    '''
    Mark the pupil region for an eye image.

    Parameters
    ----------
    fname: string
        Name of the image given in string format.

    Returns
    -------
    pupil:
        A new binary image in which the the pupil is marked
        as object(white) and the rest of the region is marked
        background(black).

    '''

    img = cv2.imread(fname)
    orig = zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                orig[i, j, k] = img[i, j, k]
    pos1 = zeros([img.shape[0], img.shape[1]])
    im = Image.open(fname)
    pix = im.load()
    height, width = img.shape[:2]
    height = height-1
    width = width-1
    count = 0
    for eh in range(height):
        for ew in range(width):
            r, g, b = pix[ew, eh]
            if r <= 30 and g <= 30 and b <= 30:
                cv2.circle(img, (ew, eh), 1, (0, 255, 0), 1)
                cv2.circle(pos1, (ew, eh), 1, 255, 1)
    # pos1 is the pupil
    pupil = erode(pos1, 15)
    pupil = dilate(pupil, 8)
    return pupil

# iris_img = pupil_detect("left.bmp")
# disp(iris_img)