# sierpinski.py
#
# author: Ted Pudlik
# created: May 12th, 2013

"""
Sierpiński gasket plotter: plot an approximation to the Sierpiński gasket of
given order.

The zeroth-order gasket is defined to be an equilateral triangle of radius 1,
centered at the origin.  To obtain the first-order gasket, divide the zeroth-
order gasket into four equally sized equilateral triangles and remove the
central one.  This process can be repeated for each of the remaining triangles
to obtain higher-order gaskets.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch

initial = {'centers':[(0, 0),], 'radius':1.0}

def Sierpinski_gasket(order):
    """ Return a dictionary containing 'centers', a list of the still-present
        triangles' centers, and 'radius', their radius.
    """
    if order < 0 or not isinstance(order, (int, long)):
        raise TypeError
    elif order == 0:
        return initial
    else:
        return finegrain(Sierpinski_gasket(order - 1))

def finegrain(gasket):
    """ Given a gasket approximation of some order, return the approximation of
        the next order.
    """
    new_centers = [newcenter for center in gasket['centers']
                    for newcenter in split_triangle(center, gasket['radius'])]
    new_radius = gasket['radius']/2
    return {'centers': new_centers, 'radius': new_radius}

def split_triangle(center, radius):
    """ Given the center and radius of an equilateral triangle, return a list of
        the centers of three equilateral triangles, each sharing a vertex with
        the original triangle and having 1/4 of its area.
    """
    return [(center[0], center[1] + radius/2),
            (center[0] + np.sqrt(3)*radius/4, center[1] - radius/4),
            (center[0] - np.sqrt(3)*radius/4, center[1] - radius/4)]

def plot_gasket(order):
    """ Plot and save (as png) an approximation to the Sierpinski gasket of
        given order.
    """
    gasket = Sierpinski_gasket(order)
    for center in gasket['centers']:
        plt.gca().add_patch(mpatch.RegularPolygon(center, 3,
                                                  radius = gasket['radius'],
                                                  edgecolor='none'))
    plt.ylim(-0.5, 1)
    plt.xlim(-np.sqrt(3)/2, np.sqrt(3)/2)
    plt.axes().set_aspect('equal')
    plt.tight_layout()
    plt.gca().axis('off')
    plt.savefig("".join(['gasket_', str(order),'.png']))
    plt.show()
