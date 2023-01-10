def mySqrt(x):
    l=0
    r=x
    while l<r:
        mid=(r+l)//2
        if mid**2==x:
            return mid
        if mid**2>x:
            r = mid
        else:
            l = mid+1
        return l-1 if l>1 else l