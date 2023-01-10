def isValid(s):
    dictH = {']': '[', '}': '{', ')': '('}
    stack = []
    for letter in s:
        if letter in dictH.values():
            stack.append(letter)
        elif letter in dictH.keys():
            if stack == [] or stack.pop() != dictH[letter]:
                return False
        else:
            return False
    if stack != []:
        return False
    return True