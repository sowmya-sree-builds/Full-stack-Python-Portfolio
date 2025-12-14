# ```python
# print("Numbers from 1 to 5:")
# i = 0
# while i < 5:
#     i += 1
#     if i in range(1, 6):
#         print(i, end=' ')

# print("Even numbers from 1 to 10:")
# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         print(i, end=' ')
#     i += 1

# print("Sum of numbers from 1 to 10:")
# i = 1
# sum = 0
# while i <= 10:
#     sum += i
#     i += 1
# print(sum)

# num = int(input("Enter a number to print each digit: "))
# digits = str(num)
# i = 0
# while i < len(digits):
#     print(digits[i], end=' ')
#     i += 1

# i = 10
# while i >= 1:
#     print(i, end=' ')
#     i -= 1

# print("Numbers from 1 to 10:")
# for i in range(1, 11):
#     print(i, end=' ')

# print("Characters in 'banana':")
# for char in "banana":
#     print(char, end=' ')

# print("Square numbers from 1 to 5:")
# for i in range(1, 6):
#     print(i**2, end=' ')

# print("Even numbers from the list [2,5,8,9,10]:")
# numbers = [2, 5, 8, 9, 10]
# for num in numbers:
#     if num % 2 == 0:
#         print(num, end=' ')

# print("Numbers from 1 to 20 divisible by 3:")
# for i in range(1, 21):
#     if i % 3 == 0:
#         print(i, end=' ')
# print()

# print("Star Pattern:")
# rows = 3
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end="")
#     print()
# print()

# print("Number Pattern (same row repeated):")
# for i in range(3):
#     for j in range(1, 4):
#         print(j, end=" ")
#     print()
# print()

# print("Triangle Number Pattern:")
# rows = 3
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# print()

# print("Multiplication Table of 2:")
# for i in range(1, 11):
#     print(f"2 x {i} = {2*i}")
# print()

# print("Characters in each word from the list:")
# words = ["hey", "viewer"]
# for word in words:
#     for char in word:
#         print(char, end=" ")
#     print()

# print("Numbers with Even/Odd:")
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i, ": is Even")
#     else:
#         print(i, ": is Odd")
# print()

# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     if num % 2 == 0:
#         print(f"{num} is Even")
# print()

# print("Enter numbers (negative number to stop):")
# while True:
#     num = int(input("Enter a number: "))
#     if num < 0:
#         print("Negative number entered. Stopping.")
#         break
#     print(f"You entered: {num}")
# print()

# word = input("Enter a word to print vowels: ")
# print(f"Vowels in the word:{word}")
# for char in word.lower():
#     if char in "aeiou":
#         print(char, end=" ")

# word = input("Enter a word to count vowels: ")
# print(f'The number of vowels in : {word}')
# count = 0
# for char in word.lower():
#     if char in "aeiou":
#         count += 1
# print(f"Number of vowels: {count}")

# print("Task 21: Print 'Hello' 5 times")
# for i in range(5):
#     print("Hello")
# print()

# print("Ask favorite colour 3 times")
# for i in range(3):
#     color = input(f"Enter your favorite color ({i+1}/3): ")
#     print(f"You entered: {color}")
# print()

# print("Pattern A, BB, CCC")
# for i in range(1, 4):
#     print(chr(64 + i) * i)
# print()

# word = "banana"
# count_a = 0
# for char in word:
#     if char == 'a':
#         count_a += 1
# print(f"'a' appears {count_a} times in '{word}'")
# print()

# print("Numbers with small/big")
# for i in range(1, 11):
#     if i < 5:
#         print(i, "small")
#     else:
#         print(i, "big")
