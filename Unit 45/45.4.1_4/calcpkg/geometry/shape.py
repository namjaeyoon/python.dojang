from ..operation import element             # from ..operation.element import mul로도 가능

def triangle_area(base, height):
    return element.mul(base, height) / 2    # mul(base, height)로도 가능

def rectangle_area(width, height):
    return element.mul(width, height)       # mul(width, height)로도 가능
