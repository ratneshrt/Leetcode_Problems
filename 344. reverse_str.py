def reverseString(s):
    i = 0
    j = len(s) - 1
    while(i<j):
        s[i],s[j] = s[j],s[i]
        i+=1
        j-=1