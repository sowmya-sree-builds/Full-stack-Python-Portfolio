# Tasks on Python Lambda Functions 
# Basic Level

# 1 Square of a Number: Write a lambda function to find the square of a number. Example: square(5) → 25.
square1= lambda x:x*x
print(square1(25))
# 2 Check Even or Odd: Use lambda to check if a number is even or odd. Example: is_even(4) → True 
is_even= lambda x:x%2==0
print(is_even(4))
# 3 Find Maximum of Two Numbers: Write a lambda to return the larger of two numbers. Example: max_num(10, 20) → 20
max_num= lambda a,b: a if a>b else b
print(max_num(19,20))
# 4 Add Two Numbers: Write a lambda function that takes two arguments and returns their sum. Example: add(4, 6) → 10
add = lambda a,b:a+b
print(add(4,6))
# Intermediate Level

# 1 Sort a List of Tuples: Given [(1, 5), (2, 3), (4, 1)], sort the list by the second element using lambda.
data = [(1, 5), (2, 3), (4, 1)]
sorted_data = []  # store result

get_key = lambda x: x[1]  # lambda to get second element

while data:   # until original list empty
    j = data[0]
    for t in data:
        if get_key(t) < get_key(j):  # use lambda here
            j = t
    sorted_data.append(j)
    data.remove(j)
print(sorted_data)  # [(4, 1), (2, 3), (1, 5)]


# 2 Filter Even Numbers: Use filter() with a lambda to extract even numbers from [1,2,3,4,5,6,7,8,9,10].
numbers=[1,2,3,4,5,6,7,8,9,10]
filter=list(filter(lambda x:x%2==0,numbers))
print(filter)

# 3 Map with Lambda: Use map() and lambda to cube each number in [1, 2, 3, 4, 5].
nums = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x ** 3, nums))
print(cubes)  # [1, 8, 27, 64, 125]

# 4 Reduce with Lambda: Use reduce() and lambda to find the product of [2, 3, 4, 5].
from functools import reduce
nums = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 120

# Advanced Level 

# 1 Sort by Name Length: Given ["apple", "banana", "kiwi", "grapes"], sort by length using sorted() and lambda.
fruits = ["apple", "banana", "kiwi", "grapes"]
sorted_fruits = sorted(fruits, key=lambda x: len(x))
print(sorted_fruits)  # ['kiwi', 'apple', 'grapes', 'banana']



# 2 Find Palindromes: Use filter() with lambda to find palindromes from ["madam", "python", "level", "world"]. 
"""words = ["madam", "python", "level", "world"]
palindromes = list(filter(lambda w: w == w[::-1], words))
print(palindromes)  # ['madam', 'level']"""
  
# 3 Custom Sorting (Case-Insensitive): Sort ["Cat", "apple", "Banana", "dog"] in case-insensitive order using lambda.
items = ["Cat", "apple", "Banana", "dog"]
sorted_items = sorted(items, key=lambda x: x.lower())
print(sorted_items)  # ['apple', 'Banana', 'Cat', 'dog']

# 4 Conditional Lambda (Ternary): Write a lambda function that returns "Positive", "Negative", or "Zero" based on input. 
check_num=lambda x: "positive" if x > 0 else("negative" if x < 0 else "zero")
print(check_num(10))   # Positive
print(check_num(-5))   # Negative
print(check_num(0))    # Zero

# 5 Dictionary Sorting by Values: Given {'a': 3, 'b': 1, 'c': 2}, sort dictionary items by values using lambda. 6 Multiple Conditions in Lambda: Write a lambda to return: 'Even & >10' if number is even and greater than 10, 'Odd' if odd, 'Other' otherwise
dict1 = {'a': 3, 'b': 1, 'c': 2}
sorted_items = sorted(dict1.items(), key=lambda x: x[1])
print(sorted_items)  # [('b', 1), ('c', 2), ('a', 3)]
