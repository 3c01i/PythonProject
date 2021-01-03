import math
def circle_len_r(r, a=360):
    circle_len = (( 2 * math.pi * r * a ) / 360 )
    return(circle_len)
def circle_area_r(r, a=360):
    circle_area = (( math.pi * (r**2) * a ) / 360 )
    return(circle_area)
def circle_r_l(l):
    r = ( l ) / ( 2 * math.pi )
    return(r)
def circle_area_l(l, a=360):
    return(circle_area_r(circle_r_l(l),a))