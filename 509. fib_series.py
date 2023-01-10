def fib(n):
    a, b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a

n= 4
print(fib(n))


#Using recursion
# def fib1(n):
#     if n==1 or n==2:
#         return 1
#     output = fib1(n-1) + fib1(n-2)
#     return output