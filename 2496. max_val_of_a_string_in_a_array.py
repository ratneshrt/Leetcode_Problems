def maximumValue(strs):
    c = []
    for i in range(len(strs)):
        if strs[i].isdecimal():
            c.append(int(strs[i]))
        elif strs[i].isalpha():
            c.append(len(strs[i]))
        else:
            c.append(len(strs[i]))
    result = max(c)
    return result