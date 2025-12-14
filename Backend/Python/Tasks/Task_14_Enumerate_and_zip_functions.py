# Python Beginner Tasks on enumerate() and zip() Tasks on enumerate()

# Task 1: Simple Index Printing

# Write a program to print each item in the list along with its index using enumerate().

# fruits = ["apple", "banana", "cherry"]

# fruits = ["apple", "banana", "cherry"]
# for i,f in enumerate(fruits):
#     print(i," ",f)

# Task 2: Start Index from 1

# Use enumerate() with start=1 to display serial numbers for a list of student names.

# students = ["Alice", "Bob", "Charlie"]

# students = ["Alice", "Bob", "Charlie"]
# for i,s in enumerate(students,start=1):
#     print(i,' ',s)

# Task 3: Replace for with enumerate()

# Re-write this loop using enumerate():

# colors = ["red", "green", "blue"] index = 0 for color in colors: print(index, color) index += 1

# colors = ["red", "green", "blue"]
# for i,c in enumerate(colors):
#     print(i," ",c)

# Task 4: Find Index of a Specific Value

# Using enumerate(), find the index of "python" in this list:

# languages = ["java", "c++", "python", "ruby"]

# languages = ["java", "c++", "python", "ruby"]
# for i,l in enumerate(languages):
#     if l == "python":
#         print(i,' ',l)

# Task 5: Enumerate on a String

# Use enumerate() to print each character of the string "hello" with its index.

# string1 = "hello"
# for i,s in enumerate(string1):
#     print(i,' ',s)

# Tasks on zip()

# Task 6: Combine Two Lists

# Use zip() to pair elements from these lists:

# names = ["Alice", "Bob", "Charlie"] marks = [85, 90, 78]

# Expected Output:

# ("Alice", 85), ("Bob", 90), ("Charlie", 78)

# names = ["Alice", "Bob", "Charlie"]
# marks = [85, 90, 78]
# tuple1=tuple(zip(names,marks))
# print(tuple1)

# Task 7: Iterate with zip()

# Write a program that prints sentences like:

# Alice scored 85 Bob scored 90 Charlie scored 78

# using the lists above.

# names = ["Alice", "Bob", "Charlie"]
# marks = [85, 90, 78]
# result = zip(names,marks)
# for i,v in result:
#     print(f'{i} scored {v}')

# Task 8: Unzipping

# Given:

# pairs = [("a", 1), ("b", 2), ("c", 3)]

# Use zip(*pairs) to separate keys and values.

# pairs = [("a", 1), ("b", 2), ("c", 3)]
# keys,values=zip(*pairs)

# print(f'keys: {keys}')
# print(f'values: {values}')

# Task 9: Multiple Iterables

# Use zip() on three lists:

# ids = [101, 102, 103] names = ["Tom", "Jerry", "Mickey"] grades = ["A", "B", "A"]

# Expected Output:

# (101, "Tom", "A") (102, "Jerry", "B") (103, "Mickey", "A")

# ids = [101, 102, 103]
# names = ["Tom", "Jerry", "Mickey"]
# grades = ["A", "B", "A"]

# combo = zip(ids,names,grades)
# for i in combo:
#     print(i)

# Task 10: Shortest List Behavior

# Check how zip() behaves when given lists of different lengths:

# a = [1, 2, 3, 4] b = ["x", "y"]

# a=[1,2,3,4]
# b=["X","Y"]

# combo = zip(a,b)
# for i in combo:
#     print(i)
