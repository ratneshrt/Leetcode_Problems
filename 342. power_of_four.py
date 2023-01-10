def isPowerOffour(n):
    if n<1:
        return False
    if n==1:
        return True
    return isPowerOffour(n/4)

n =4
print(isPowerOffour(n))