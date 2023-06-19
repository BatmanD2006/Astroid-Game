import math

def get_distance_between(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = x2 - x1 #change in x
    dy = y2 - y1 #change in y
    distance = math.sqrt(dx ** 2 + dy ** 2) #distance between points 
    return distance

