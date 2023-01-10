def isPowerOfthree(n):
    if n<1:
        return False
    if n==1:
        return True
    return isPowerOfthree(n/3)

n =4
print(isPowerOfthree(n))