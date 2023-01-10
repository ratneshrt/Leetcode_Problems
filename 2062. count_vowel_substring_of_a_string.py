def countVowelSubstrings(word):
    vowels = {'a','e','i','o','u'}
    res= 0
    for l in range(len(word)):
        s = set()
        for r in range(l, len(word)):
            if word[r] in vowels:
                s.add(word[r])
                if s == vowels:
                    res+=1
            else:
                break
    return res