from skimage.io import imread, imshow, show
from skimage.color import rgb2gray

def bnw(s):
    '''
    Read an image and store it in a black and white format.

    Parameters
    ----------
    s: string
        File-name of the image in string format.

    Returns
    -------
    A 2D matrix corresponding to black and white
    image with all values within the range 0 to 1.
   
    '''
    return rgb2gray(imread(s))


def disp(img):
    '''
    to display an image.
    
    Parameters
    ----------
    img: 2D matrix 
        Input as a matrix corresponding to a particular image
    
    '''
    imshow(img)
    show()

