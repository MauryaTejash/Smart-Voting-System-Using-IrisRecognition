from rectangulate import *
from numpy import zeros
from sys import argv


def engroup(fname):

    ''' 
    Generate the feature vector correspoonding to an iris 
    by using the rectangular iris image generated from 
    rectangulate.py;
    From the normalized eye image obtained in the rectangle function
    of rectangulate.py, the algorithm proposed by Jong Gook Ko et. al.
    is used to obtain a set of feature vectors. These feature vectors
    vary slightly among different images of the same eye, but show
    wide variation among different eyes.
    
    Parameters
    ----------
    fname: string
    The name of the image in string format.

    Returns
    -------
    [Horizontal groups, Vertical groups]
    Horizontal groups: A list of sequences of feature vectors
    evaluated along the rows
    Vertical groups: A list of sequences of feature vectors 
    evaluated along the columns.
 
    '''
    strip = rectangle(fname)
    disp(strip)
    grid = zeros([13, 36])
    for i in range(13):
        for j in range(36):
            block = strip[3*i:3*i+3, 10*j:10*j+10]
            for row in block:
                grid[i, j] += sum(row)

    # Group encoding
    def encode(group):
        avg = sum(group) / 5
        group -= avg
        for i in range(1, 5):
            group[i] = sum(group[: i+1])
        code = ''
        argmax = 0
        argmin = 0
        for i in range(5):
            if group[i] == max(group): 
                argmax = i
            if group[i] == min(group): 
                argmin = i
        for i in range(5):
            if i < argmax and i < argmin: 
                code += '0'
            if i > argmax and i > argmin: 
                code += '0'		
            if i >= argmax and i <= argmin: 
                code += '2'
            if i <= argmax and i >= argmin: 
                code += '1'
        return code

    # Horizontal grouping
    horgroups = []
    for row in range(13):
        horgroups.append([])
        for col in range(32):
            group = zeros(5)
            for i in range(5): 
                group[i] = grid[row, col+i]
            horgroups[row].append(encode(group))

    # Vertical grouping
    vergroups = []
    for col in range(36):
        vergroups.append([])
        for row in range(9):
            group = zeros(5)
            for i in range(5): 
                group[i] = grid[row+i, col]
            vergroups[col].append(encode(group))
    return [horgroups, vergroups]

