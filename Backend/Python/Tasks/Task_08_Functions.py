# Tasks on return Statement & Return Values

# Write a function that returns the cube of a number.
# def cube():
#     n = int(input('Enter a number:'))
#     return n ** 3
# print(cube())

# Write a function that takes two numbers and returns their average.
# def avg(n,m):
#     return (n+m)/2
# print(avg(2,3))

# Write a function that returns both the square and square root of a number.
# def squ(n):
#     return n ** 2,n ** (1/2)

# print(squ(4))

# Create a function is_odd(n) that returns True if the number is odd, else False.
# def is_odd(n):
#     return True if n%2 != 0 else False
# print(is_odd(3))

# Write a function sum_digits(n) that returns the sum of digits of a number. (e.g., sum_digits(1234) should return 10)
# def sum(n):
#     s = 0
#     while n > 0:
#         d = n % 10
#         s += d
#         n //= 10
#     return s
# print(sum(1234))

# Tasks on Functions with Default Parameters
# 6. Create a function greet(name='Guest') that returns 'Hello, !'. price.

# def greet(name ='Guest'):
#     return 'Hello, !'
# print(greet())

# Create a function power(base, exponent=2) that returns base ** exponent.
# def power(base,exponent=2):
#     return base**exponent
# print(power(3,4))

# Create a function total_bill(item='Sandwich', quantity=1, price=50) that returns the total
# def total_bill(item='Sandwich', quantity=1, price=50):
#     return quantity * price
# print(total_bill(item='Sandwich', quantity=3, price=50))

# Create a function employee_info(name, age=30, department='HR') that returns a formatted string.
# def employee_info(name, age=30, department='HR'):
#     s = f'hi my name is {name} and my age is about {age} and i belong to the {department}'
#     return s

# print(employee_info(name = 'akhila', age=30, department='HR'))

# Create a function circle_area(radius=1) that returns the area of a circle. (area = 3.14 * radius * radius)
# def circle_area(radius=1):
#     area = 3.14 *radius * radius
#     return area
# print(circle_area(4))

# Tasks on Loops with Return
# 11. Write a function that takes a number and returns the sum of all even numbers up to that number.

# def sume(n):
#     s = 0
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             s += i
#     return s
# print(sume(5))

# Write a function that returns the largest number from a list of numbers passed as a parameter.
# def fun(n):
#     lar = n[0]
#     for i in n:
#         if i > lar:
#             lar = i
#     return lar
# print(fun([1,2,3,4,5]))
            
# Tasks with Multiple Return Values
# 13. Create a function min_max(numbers) that returns the minimum and maximum values in a list.

# def min_max(num):
#     ma = num[0]
#     mi = num[0]
#     for i in num:
#         if i > ma:
#             ma = i
#         if i < mi:
#             mi = i
#     return ma,mi
# print(min_max([1,2,3,4,0,2,6]))

# Create a function student_summary(name, marks) that returns the student’s name, total marks, and average marks.
# def student_summary(name, marks):
#     tm = 0  # total marks
#     for i in marks:
#         tm += i
#     n = len(marks)
#     avg = tm / n
#     return name, tm, avg

# print(student_summary('sowmya', [1, 2, 3, 4, 5]))

# Logical Task
# 15. Create a function calculate(num1, num2, operator='+') that does: - '+' → return sum - '-' → return difference - '*' → return product - '/' → return quotient Use return and default parameter for operator.

# def calculate(num1, num2, operator='+'):
#     if operator == '+':
#         return num1 + num2
#     if operator == '-':
#         return num1 - num2
#     if operator == '*':
#         return num1 * num2
#     if operator == '/':
#         return num1 / num2
#     else:
#         return 'Invalid operator'
# print(calculate(11,10,'*'))
    
    
# 
