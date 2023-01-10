def lengthOfLastWord(s):
    if " " not in s:
        return len(s)
    lst = s.split(" ")
    for item in lst[::-1]:
        if item != "":
            return len(item)