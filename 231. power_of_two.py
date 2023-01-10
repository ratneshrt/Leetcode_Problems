def isPowerOfTwo(n):
    if n<1:
        return False
    if n==1:
        return True
    return isPowerOfTwo(n/2)

n =4
print(isPowerOfTwo(n))