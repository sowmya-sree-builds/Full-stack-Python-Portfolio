# recursion: it is a phenomenon of calling a function within itself. each function call solves a smaller version of same problem
# 1.Base Case: to stop the recursion based on a condition.
# 2.Recursive Case: solving smaller version of the problem.
# used to generate fibonacci, factorials, matrices and grids.

# Factorial using Recursion
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
    
print(factorial(5))

# Fibonocci using recursion
def fibonacci(n):
    if n==0:
        return n
    elif n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(6):
    print(fibonacci(i),end =' ')


# sum of natural numbers
def sumofnum(num):
    if num ==0:
        return 0
    else:
        return num+sumofnum(num-1)
print(sumofnum(5))

# reverse a string using recursion
def rev(str):
    if len(str)==0:
        return str
    else:
        return rev(str[1:])+str[0]  
print(rev('sowmya'))

 


