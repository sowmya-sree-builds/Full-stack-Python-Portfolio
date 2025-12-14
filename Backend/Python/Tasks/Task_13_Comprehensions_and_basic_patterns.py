# Comprehension Tasks

# Squares of odd numbers Generate a list of squares of odd numbers from 1 to 20.
# n=[]
# sq=[i**2 for i in range(1,21)]
# print(sq)

# Cube dictionary Create a dictionary where keys are numbers 1–10 and values are their cubes.
# cu={i:i**3 for i in range(1,11)}
# print(cu)

# 3.Set of vowels From the string "programming in python", extract unique vowels using a set comprehension.
# string1 = "programming in python"
# vow={ch for ch in string1 if ch in 'aeiou'}
# print(vow)

# Reverse dictionary Given d = {'a': 1, 'b': 2, 'c': 3}, create a new dictionary where keys become values and values become keys.
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# reversed_dict = {}

# for key in my_dict:
#     value = my_dict[key]
#     reversed_dict[value] = key   
# print(reversed_dict)

# Multiplication table (list of tuples) Generate a list of tuples (n, n2, n3) for numbers from 1 to 5.
# table = []
# for n in range(1, 6):
#     table.append((n, n*2, n*3))
# print(table)

# Filter positive numbers From a list nums = [-3, -1, 0, 2, 4, -6], create a new list containing only positive numbers.
# nums = [-3,-1,0,2,4,-6]
# pos=[i for i in nums if i > 0]
# print(pos)

# Word lengths From the sentence "Python makes coding easier", generate a dictionary where key = word, value = length of the word
# dic="Python makes coding easier"
# s={i:len(i) for i in dic.split() }
# print(s)

# Even or Odd labeling Generate a list: ["Even", "Odd", "Even", ...] for numbers from 1 to 10.
# s = ['even' if i%2==0 else 'odd' for i in range(1,101) ]
# print(s)

# Squares as tuple Create a tuple of squares of numbers from 1 to 7 using a generator expression.
# squares = tuple(n*n for n in range(1, 8))
# print(squares)

# Remove duplicates From the list [1,2,2,3,4,4,5,5,6], generate a new sorted list without duplicates.
# list1 = [1,2,2,3,4,4,5,5,6]
# list2 = sorted(set(list1))
# print(list2)

# n = 0
# rows = 5
# for row in range(1, rows+1):
#     for column in range(rows-row):
#         print(" ", end=" ")
#     for column in range(row):
#         print("*", end=" ")
#     print()

# n=1
# for row in range(n,6):
#     for column in range(n,6):
#         print(row,end=" ")
#     print('')

# for row in range(1,6):
#     for column in range(1,row+1):
#         print(column,end=" ")
#     print(' ')    

# for row in range(0,6):
#     for column in range(1,row+1):
#         print(row,end=" ")
#     print(' ')   

# rows = 6
# for row in range(rows, 1, -1):      
#     for column in range(1, row):
#         print(column, end=" ")
#     print()

# for row in range(1,4):
#     for col in range(1,7):
#         print(col,end=" ")
#     print(' ')

# n=5
# for row in range(n):
#     for col in range(n):
#         if row ==0 or row == n-1 or col == 0 or col == n-1:
#             print('*',end=" ")
#         else:
#             print(' ',end=" ")
#     print(" ")

# rows = 5
# for row in range(1, rows+1):
#     for space in range(rows - row):
#         print(" ", end="")
#     for star in range(row):
#         print("* ", end="")
#     print()

# rows = 5
# for row in range(1, rows+1):
#     for space in range(rows - row):
#         print(" ", end="")
#     for star in range(row):
#         print("* ", end="")
#     print()

# for row in range(rows-1, 0, -1):
#     for space in range(rows - row):
#         print(" ", end="")
#     for star in range(row):
#         print("* ", end="")
#     print()
