def appendCharacters(s,t):
    k = 0
    for i in range(len(s)):
        if s[i]==t[k]:
            k+=1
        if k == len(t):
            return 0
    return len(t)-k