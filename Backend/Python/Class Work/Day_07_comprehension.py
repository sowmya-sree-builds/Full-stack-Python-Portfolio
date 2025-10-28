# 💡 PYTHON COMPREHENSIONS — All Data Types in One File

# -----------------------------------------------
# 1️⃣ LIST COMPREHENSION
# -----------------------------------------------
numbers = [1, 2, 3, 4, 5]
# Normal way
squares = []
for i in numbers:
    squares.append(i * i)
print("List (normal):", squares)

# Using list comprehension
squares_comp = [i * i for i in numbers]
print("List comprehension:", squares_comp)

# With condition
even_squares = [i * i for i in numbers if i % 2 == 0]
print("Even squares:", even_squares)


# -----------------------------------------------
# 2️⃣ TUPLE COMPREHENSION
# (Actually uses generator expression inside tuple())
# -----------------------------------------------
nums = (1, 2, 3, 4, 5)
tuple_comp = tuple(i ** 3 for i in nums if i % 2 != 0)
print("Tuple comprehension:", tuple_comp)


# -----------------------------------------------
# 3️⃣ SET COMPREHENSION
# -----------------------------------------------
values = [10, 20, 30, 20, 10, 40]
set_comp = {v // 10 for v in values if v > 10}
print("Set comprehension:", set_comp)  # removes duplicates automatically


# -----------------------------------------------
# 4️⃣ DICTIONARY COMPREHENSION
# -----------------------------------------------
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict_comp = {k: v ** 2 for k, v in zip(keys, values)}
print("Dictionary comprehension:", dict_comp)

# With condition
filtered_dict = {k: v for k, v in dict_comp.items() if v > 2}
print("Filtered dictionary:", filtered_dict)


# -----------------------------------------------
# 5️⃣ STRING COMPREHENSION (using join)
# -----------------------------------------------
text = "Comprehension"
# Extract only vowels
vowels = ''.join([ch for ch in text if ch.lower() in 'aeiou'])
print("Vowels in string:", vowels)


# -----------------------------------------------
# 6️⃣ NESTED COMPREHENSION
# -----------------------------------------------
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened list:", flattened)

# Multiplying each number by 2 inside nested loop
double_nested = [[num * 2 for num in row] for row in matrix]
print("Nested list comprehension:", double_nested)


# -----------------------------------------------
# 7️⃣ COMPREHENSION WITH FUNCTION
# -----------------------------------------------
def cube(n):
    return n ** 3

cube_list = [cube(i) for i in range(1, 6)]
print("List of cubes using function:", cube_list)


# -----------------------------------------------
# 8️⃣ MIXED EXAMPLE (multiple comprehensions)
# -----------------------------------------------
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List → only even squares
even_square_list = [i ** 2 for i in data if i % 2 == 0]

# Set → cubes of numbers divisible by 3
cube_set = {i ** 3 for i in data if i % 3 == 0}

# Dict → number: square for numbers < 6
square_dict = {i: i ** 2 for i in data if i < 6}

print("Even square list:", even_square_list)
print("Cube set:", cube_set)
print("Square dict:", square_dict)
