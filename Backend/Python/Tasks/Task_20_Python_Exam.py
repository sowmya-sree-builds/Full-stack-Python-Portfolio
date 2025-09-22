# Section A: Short Answer Questions (2 Marks Each)

# 1. Define a class in Python. How do you create an object of a class?
class MyClass:
    def display(self):
        print("Hello")
obj = MyClass()   # Creating an object
obj.display()


# 2. What is the difference between break, continue, and pass statements in Python?
# break -> exits loop
# continue -> skips current iteration
# pass -> is a placeholder (placeholder)

# 3. Write the syntax of an if-elif-else statement with an example.
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# 4. What is the purpose of __init__() method in Python classes?
# -> It is a constructor that initializes object attributes.

# 5. Write a function in Python to calculate the square of a number.
def square(num):
    return num * num
print(square(5))   # Output: 25

# Section B: Problem Solving (5 Marks Each)

# 6. Python class Car with attributes brand and model.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

c1 = Car("Toyota", "Corolla")
c2 = Car("Hyundai", "i20")
c1.display()
c2.display()

# 7. User-defined function to check whether a number is even or odd.
def check_number(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_number(7)

# 8. Print multiplication table of 5 using a for loop.
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")

# 9. Accept a number from user and check +, -, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 10. Sum of digits using while loop.
num = int(input("Enter a number: "))
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10
print("Sum of digits:", total)

# Section C: Nested Loops & Decision Making (7 Marks Each)

# 11. Pattern printing
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# 12. Prime numbers between 1 and 50
for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

# 13. Divisibility check program
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5")
elif num % 3 == 0:
    print("Divisible by only 3")
elif num % 5 == 0:
    print("Divisible by only 5")
else:
    print("Not divisible by 3 or 5")


# Section D: Loop Control Statements (10 Marks Each)


# 14. Print 1–20 but skip multiples of 3
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()


# 15. Print 1–10 but stop at 7
for i in range(1, 11):
    if i == 7:
        break
    print(i, end=" ")
print()


# 16. Pattern with odd numbers only
for i in range(1, 10, 2):  
    for j in range(1, i+1, 2):  
        print(j, end=" ")
    print()

# Section E: Long Answer (15 Marks Each)


# 17. Student Class Program
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display(self):
        grade = self.calculate_grade()
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}, Grade: {grade}")
    
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"

s1 = Student("Alice", 101, 95)
s2 = Student("Bob", 102, 78)
s3 = Student("Charlie", 103, 65)
s1.display()
s2.display()
s3.display()


# 18. Prime number program with decision-making
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is Prime")
    print("Prime numbers up to", num, ":")
    for i in range(2, num+1):
        if is_prime(i):
            print(i, end=" ")
else:
    print(f"{num} is Not Prime")
