# Q1: Numbers divisible by 3 or 5 but not both (1 to 100)

for num in range(1, 101):
    # Check divisibility
    if (num % 3 == 0 or num % 5 == 0) and not (num % 3 == 0 and num % 5 == 0):
        print(num, end=" ")

# Q2: Find the second largest number without using max() or sorted()

numbers = [10, 5, 8, 20, 15, 20]  # example list

# Initialize two variables for largest and second largest
largest = second_largest = float('-inf')

for n in numbers:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

print("Second largest number:", second_largest)

# Q3: Check if a string is a palindrome ignoring spaces, punctuation, and case

text = input("Enter a string: ")

# Remove all non-alphanumeric characters and convert to lower case
cleaned = ""
for ch in text:
    if ch.isalnum():  # keep only letters and numbers
        cleaned += ch.lower()

# Check palindrome
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

"""
*
**
***
*****
*******
*********"""
# Q4: Print the pattern for n=5

n = 5
for i in range(1, n + 1):
    # number of stars increases as 2*i - 1 for second half
    if i <= 3:  # first three rows: 1, 2, 3 stars
        print("*" * i)
    else:       # remaining rows: 5, 7, 9 stars
        print("*" * (2 * (i - 2) + 1))


# Q5: Find GCD of two numbers without math module

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Using Euclidean algorithm
while b != 0:
    a, b = b, a % b

print("GCD is:", a)

# Q6: Print a new list containing only prime numbers from input list

numbers = [10, 3, 5, 12, 7, 19]  # example list

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_list = []
for num in numbers:
    if is_prime(num):
        prime_list.append(num)

print("Prime numbers:", prime_list)

# Q7: Count frequency of each word in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()
freq = {}

for word in words:
    word = word.lower()  # optional: make it case-insensitive
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word frequency:", freq)

# Q8: Generate a list of the first N prime numbers

N = int(input("Enter N: "))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
num = 2
while len(primes) < N:
    if is_prime(num):
        primes.append(num)
    num += 1

print("First", N, "prime numbers:", primes)

# Q9: Find all pairs in list whose sum equals a given target

numbers = [2, 4, 3, 7, 5]
target = 7

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("(", numbers[i], ",", numbers[j], ")")

# Q10: Check if a number is an Armstrong number

num = int(input("Enter a number: "))

# Convert to string to count digits
num_str = str(num)
power = len(num_str)

sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** power

if sum_of_powers == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")