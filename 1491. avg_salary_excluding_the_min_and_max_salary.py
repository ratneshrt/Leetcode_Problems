def average(salary):
    salary.sort()
    salary.pop()
    del salary[0]
    return sum(salary)/len(salary)