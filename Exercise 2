import itertools
import pprint

def rectangle_is(a, b, c, d):
    # sort out coordinates by a,b,c,d for rectangles 4 points
    a, b, c, d = sorted([a, b, c, d])

    # check rectangle, 90 degree
    return a[0] == b[0] and c[0] == d[0] and a[1] == c[1] and b[1] == d[1]

def rectangles_number(coordinates):

    # output for the number of rectangles
    return sum([rectangle_is(a, b, c, d) for (a, b, c, d) in itertools.combinations(coordinates, 4)])

def rectangles_get(coordinates):

    # return each rectangle
    return [[a, b, c, d] for (a, b, c, d) in itertools.combinations(coordinates, 4) if rectangle_is(a, b, c, d)]

"""
example coordinates are:
[(0,0),(0,1),(1,1),(1,0),(2,1),(2,0),(3,1),(3,0)]
"""

coordinates = [(0, 0), (0, 1), (1, 1), (1, 0), (3, 1), (3, 0), (2,1), (2,0), (4,0), (4,1), (0,2), (4,2)]

print(f'In total, there are {rectangles_number(coordinates)} rectangles.')

print(f'Below are the co-ordinates (x,y) for the {rectangles_number(coordinates)} rectangles:')
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(rectangles_get(coordinates))
