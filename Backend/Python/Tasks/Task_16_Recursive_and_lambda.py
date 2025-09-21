# 1. Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial(5):", factorial(5))  # 120

# 2. Sum of first N natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

print("Sum first 5 natural numbers:", sum_natural(5))  # 15

# 3. Reverse a string
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print("Reverse of hello:", reverse_string("hello"))  # "olleh"

# 4. Nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(6):", fibonacci(6))  # 8

# 5. Sum of digits of a number
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print("Sum of digits 1234:", sum_digits(1234))  # 10

# 6. Check if string is palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print("Is madam palindrome?", is_palindrome("madam"))  # True
print("Is hello palindrome?", is_palindrome("hello"))  # False

# 7. Power of a number (x^n)
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print("Power(2,3):", power(2, 3))  # 8

# Beginner level
even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Even or Odd(5):", even_or_odd(5))  # Odd

maximum = lambda a, b: a if a > b else b
print("Maximum(10,7):", maximum(10, 7))  # 10

square = lambda x: x * x
print("Square(6):", square(6))  # 36

# Intermediate level
# Convert Celsius to Fahrenheit using map
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Celsius to Fahrenheit:", fahrenheit)

# Extract even numbers using filter
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)

# Product of all numbers using reduce
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print("Product of numbers:", product)  # 24

# Sort list of tuples by second element
tuples_list = [(1, 3), (2, 1), (4, 2)]
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print("Sorted tuples by second element:", sorted_list)  # [(2,1), (4,2), (1,3)]
