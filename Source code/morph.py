from numpy import zeros


def erode(img, size=3):

    '''
    Performs morphological erosion by square mask of 
    size given by input argument.

    Parameters
    ----------
    img: 2D matrix
         Input as a matrix corresponding to a particular image
    size: integer
         Positive integer which determines the size of the mask.
         If size = n means the square mask is of size n by n.

    Returns
    -------
    gmi: 2D matrix
         Ouptput the 2D matrix corresponding to morphologically erosed image.

    '''

    pad = int(size/2)
    gmi = zeros([img.shape[0]-2*pad, img.shape[1]-2*pad])
    for i in range(gmi.shape[0]):
        for j in range(gmi.shape[1]):
            result = True
            for u in range(-pad, pad+1):
                for v in range(-pad, pad+1):
                        if img[i+u+pad, j+v+pad] == 0:
                            result = False
                gmi[i, j] = int(result)
    return gmi


def dilate(img, size=3):

    '''
    Performs morphological dilation for an image.

    Parameters
    ----------
    img: 2D matrix
         Input as a matrix corresponding to a particular image
    size: integer
         Positive integer which determines the size of the mask.
         If size = n means the square mask is of size n by n.

    Returns
    -------
    gmi: 2D matrix
         Ouptput the 2D matrix corresponding to morphologically erosed image.

    '''

    pad = int(size/2)
    gmi = zeros([img.shape[0]-2*pad, img.shape[1]-2*pad])
    for i in range(gmi.shape[0]):
        for j in range(gmi.shape[1]):
            result = False
            for u in range(-pad, pad+1):
                for v in range(-pad, pad+1):
                    if img[i+u+pad, j+v+pad] == 1:
                        result = True
            gmi[i, j] = int(result)
    return gmi

