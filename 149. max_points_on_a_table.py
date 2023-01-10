from collections import defaultdict
from math import gcd

def maxPoints(points):
    points.sort()
    slope, m = defaultdict(int), 0
    for i, (x1,y1) in enumerate(points):
        slope.clear()
        for x2, y2 in points[i+1:]:
            dx, dy = x2 - x1, y2 - y1
            g = gcd(dx, dy)
            M = (dx//g, dy//g)
            slope[M] += 1
            if slope[M] > m: m = slope[M]
    return m+1