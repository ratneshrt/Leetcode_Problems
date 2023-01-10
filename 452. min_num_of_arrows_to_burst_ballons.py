def findMinArrowShots(points):
    if not points:
        return 0
    points.sort(key=lambda x: x[1])
    res = 1
    curr_end = points[0][1]
    for i in range(1, len(points)):
        if points[i][0]>curr_end:
            res+=1
            curr_end = points[i][1]
    return res