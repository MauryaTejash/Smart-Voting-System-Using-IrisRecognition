from locate import *
from math import sin, cos, radians
from imworks import disp

def rectangle(fname):

    '''
    Returns a rectangular image corresponding to the iris
    using locate.py

    Parameters
    ----------
    fname: string
        The name of the image in string format.

    Returns
    -------
    newmap:
        A rectangular in the circular iris is converted to 
        a rectangular slot.

    '''

    img = bnw(fname)
    img = img[22:, 22:]
    #disp(img)
    params = locate(fname)
    Ri = params[0]  # Inner (pupil) radius
    Ro = params[1]  # Outer (iris) radius
    y, x = params[2]  # center coordinates
    x -= 10
    y -= 10
    H = int(Ro - Ri)
    W = 360
    newmap = zeros([H, W])
    for r in range(H):
        for c in range(W):
            mapped_point_col = int(x + (Ri + r) * cos(radians(c)))
            mapped_point_row = int(y + (Ri + r) * sin(radians(c)))
            dot = img[min([img.shape[0]-1, mapped_point_row]), min([img.shape[1], mapped_point_col])]
            newmap[r, c] = dot
    print('Center: ( ' + str(x) + ' , ' + str(y) + ' )')
    #disp(newmap)
    return newmap
    
#rectangle("left.bmp")