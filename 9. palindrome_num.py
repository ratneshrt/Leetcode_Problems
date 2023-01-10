def isPalindrome(x):
    temp = x
    rev = 0
    while x>0:
        dig=x%10
        rev=rev*10+dig
        x=x//10
    return temp==rev

    # OR
    # return str(x)==str(x)[::-1]