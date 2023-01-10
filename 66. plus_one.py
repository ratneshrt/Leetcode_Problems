def plusOne(digits):
    a=''
    for i in digits:
        a+=str(i)
    a=int(a)+1
    a=str(a)
    l=[]
    for i in a:
        l.append(int(i))
    
    return l