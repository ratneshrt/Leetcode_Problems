def climbingStairs(n):
    one, two = 1,1
    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    
    return one

n = 3
print(climbingStairs(n))