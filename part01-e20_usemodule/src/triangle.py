# Enter you module contents here
from math import sqrt

def __init__():
    pass

def hypotenuse(a:int,b:int):
    """This function returns the length of the hypotenuse,
    when given the lengths of the two sides of a right-angled triangle:
    --parameters:
    a : int 
        first side
    b : int
        other side
    -----
    returned value : float : length of the hypotenuse
    """
    return sqrt(a**2 + b**2)

def area(x:int, y:int):
    """
    This function returns the area of the right-angled triangle
    when two sides , perpendicular to each other, are given
    ---parameters
    x : int 
        one side
    y : int
        other side
    ---
    returned value : int : area of the triangle
    """
    return 0.5*x*y

def __version__():
    pass

def __author__():
    pass

    