# 4. Perimeter of Square
side = 6
print("4. Perimeter of square is:", 4 * side)

# 5. Perimeter of Rectangle
length = 5
breadth = 3
print("5. Perimeter of rectangle is:", 2 * (length + breadth))

# 6. Perimeter of Triangle
s1, s2, s3 = 5, 6, 7
print("6. Perimeter of triangle is:", s1 + s2 + s3)

# 7. Break Amount
amount = 3765
thou = amount // 1000                  # 3
five_hun = (amount % 1000) // 500      # 5
hun = (amount % 1000) // 100           # 7
tens = (amount % 100) // 10            # 6
ones = (amount % 10)                   # 5

print(f'amount {amount} = {thou*1000} + {hun*100} + {tens*10} + {ones}')


# 8. Convert seconds
total_sec = 3672
hours = total_sec // 3600               # 1
minutes = (total_sec % 3600) // 60      # 1
seconds = total_sec % 60                # 12
print("8. Time → Hours:", hours, "Minutes:", minutes, "Seconds:", seconds)

# 9. Sum of marks
maths, physics, chemistry = 85, 90, 88
print("9. Total marks:", maths + physics + chemistry)

# 10. Average of marks
avg = (maths + physics + chemistry) / 3
print("10. Average marks:", round(avg, 2))

# 1. Even or Odd
num = 6
print("1. Even/Odd:", "Even" if num % 2 == 0 else "Odd")

# 2. Divisible by 5 but not 10
num = 25
print("2. Divisible by 5 not 10:", "Satisfy" if num % 5 == 0 and num % 10 != 0 else "Not satisfy")

# 3. Biggest Among Two
A, B = 4, 7
print("3. Biggest is:", A if A > B else B)

# 4. Smallest Among Two
print("4. Smallest is:", A if A < B else B)

# 5. Divisible by 2, 3, 6
num = 18
print("5. Divisible by 2,3,6:", "Satisfy" if num % 2 == 0 and num % 3 == 0 else "Not satisfy")

# 6. Voting Eligibility
age = 19
print("6. Voting eligibility:", "Eligible" if age >= 18 else "Not eligible")

# 7. Pass/Fail (all >= 35)
m, p, c = 40, 36, 30
print("7. Pass/Fail:", "Pass" if m >= 35 and p >= 35 and c >= 35 else "Fail")

# 8. Pass if any one subject >= 35
m2, p2, c2 = 20, 38, 25
print("8. Pass any one:", "Pass" if m2 >= 35 or p2 >= 35 or c2 >= 35 else "Fail")

m3, p3, c3 = 40, 20, 36

passed = 0

if m3 >= 35:
    passed += 1
if p3 >= 35:
    passed += 1
if c3 >= 35:
    passed += 1

print("9. Pass any two:", "Pass" if passed >= 2 else "Fail")


# 10. Biggest Among Three
A, B, C = 7, 4, 9

biggest = A

if B > biggest:
    biggest = B

if C > biggest:
    biggest = C

print("10. Biggest is:", biggest)


# 11. Smallest Among Three
smallest = A

if B < smallest:
    smallest = B

if C < smallest:
    smallest = C

print("11. Smallest is:", smallest)


# 12. Perfect Square
num = 49
print("12. Perfect square:", "Yes" if int(num ** 0.5) ** 2 == num else "No")

# 13. Cars needed (max 5 per car)
members = 17
cars = (members + 4) // 5
print("13. Cars needed:", cars)

# 14. Second Biggest Among Three
A, B, C = 10, 25, 18

if (A > B and A < C) or (A < B and A > C):
    second_biggest = A
elif (B > A and B < C) or (B < A and B > C):
    second_biggest = B
else:
    second_biggest = C

print("Second biggest:", second_biggest)

# 15. Leap Year
year = 2024
leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("15. Leap year:", "Yes" if leap else "No")



# Square, Rectangle, and Triangle Patterns (1–15)
# 1.Solid Square Pattern
# Problem: Print a solid square of stars of size n.
# Input: n = 4
# Output:
# * * * *
# * * * *
# * * * *
# * * * *
n = 4
for i in range(n):
    for j in range(n):
        print('* ',end='')
    print()

# 2.Solid Rectangle Pattern
# Problem: Print a solid rectangle of m rows and n columns.
# Input: m = 3, n = 5
# Output:
#   * * * * *
# 	* * * * *
# 	* * * * *
m = 3 
n= 5
for row in range(m):
    for col in range(n):
        print('*',end=' ')
    print()

# 3.Right-Angled Triangle (Left-Aligned)
# Problem: Print a left-aligned right-angled triangle.
# Input: n = 5
# Output:
#   *
# 	* *
# 	* * *
# 	* * * *
# 	* * * * *
n = 5
for i in range(n+1):
    for j in range(i):
        print('*',end=' ')
    print()

# 4.Right-Angled Triangle (Right-Aligned)
# Input: n = 5
# Output:
#              *
#            * *
#          * * *
#        * * * *
# 	   * * * * *
n = 5
for row in range(n+1):
    for col in range(n-row):
        print(' ',end=' ')
    for j in range(row):
        print('*',end=' ')
    print()
 
# 5.Inverted Triangle (Left-Aligned)
# Input: n = 5
# Output:
#   * * * * *
# 	* * * *
# 	* * *
# 	* *
# 	*
n = 5
for row in range(n,0,-1):
    for col in range(1,row):
        print('*',end=' ')
    print()


# 6.Inverted Triangle (Right-Aligned)
# Input: n = 5
# Output:
#    * * * * *
#      * * * *
#        * * *
#  	       * *
#     	     *
n = 5 
for row in range(n,0,-1):
    for col in range(n-row):
        print(' ',end=' ')
    for col in range(row):
        print('*',end=' ')
    print(' ')
# 7.Centered Pyramid Pattern
# Input: n = 4
# Output:
#       *
#     * * *
#   * * * * *
# * * * * * * *
n = 4
for row in range(1,n+1):
    for col in range(n-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print('*',end=' ')
    print()


# 8.Diamond Pattern
# Input: n = 3
# Output:
#     *
#   * * *
# * * * * *
#   * * *
#     *
n =3
for row in range(1,n+1):
    for col in range(n-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print('*',end=' ')
    print()
for row in range(n-1,0,-1):
    for col in range(n-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print('*',end=' ')
    print()

# 9.Butterfly Pattern
# Input: n = 4
# Output:
# *       *
# * *   * *
# * * * * *
# * *   * *
# *       *
n = 4

# Upper half
for row in range(1, n + 1):
    # Left stars
    for col in range(row):
        print("*", end=" ")

    # Middle spaces (corrected)
    for col in range(2 * (n - row)):
        print("  ", end=" ")

    # Right stars
    for col in range(row):
        print("*", end=" ")

    print()

# Lower half
for row in range(n, 0, -1):
    # Left stars
    for col in range(row):
        print("*", end=" ")

    # Middle spaces (corrected)
    for col in range(2 * (n - row)):
        print("  ", end=" ")

    # Right stars
    for col in range(row):
        print("*", end=" ")

    print()

  

# 10.Left-Aligned Half Diamond
# Input: n = 4
# Output:
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
# 11.Right-Aligned Half Diamond
# Input: n = 4
# Output:
#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *
# 12.Sandglass Pattern
# Input: n = 4
# Output:
# * * * *
#   * * *
#     * *
#       *
#     * *
#   * * *
# * * * *
# 13.Increasing Width Triangle
# Input: n = 5
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
# 14.Decreasing Width Triangle
# Input: n = 5
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *
# 15.Right-Aligned Hill Pattern
# Input: n = 4
# Output:
#       *
#     * *
#   * * *
# * * * *
# 🔲 Hollow Patterns (16–25)
# 16.Hollow Square Pattern
# Problem: Print a hollow square of stars of size n.
# Input: n = 4
# Output:
# * * * *
# *     *
# *     *
# * * * *
# 17.Hollow Rectangle Pattern
# Problem: Print a hollow rectangle of m rows and n columns.
# Input: m = 4, n = 5
# Output:
# * * * * *
# *       *
# *       *
# * * * * *
# 18.Hollow Right-Angled Triangle (Left-Aligned)
# Input: n = 5
# Output:
# *
# * *
# *   *
# *     *
# * * * * *
# 19.Hollow Right-Angled Triangle (Right-Aligned)
# Input: n = 5
# Output:
#         *
#       * *
#     *   *
#   *     *
# * * * * *
# 20.Hollow Inverted Triangle (Left-Aligned)
# Input: n = 5
# Output:
# * * * * *
# *     *
# *   *
# * *
# *
# 21.Hollow Inverted Triangle (Right-Aligned)
# Input: n = 5
# Output:
# * * * * *
#   *     *
#     *   *
#       * *
#         *
# 22.Hollow Pyramid Pattern
# Input: n = 4
# Output:
#       *
#     *   *
#   *       *
# * * * * * * *
# 23.Hollow Diamond Pattern
# Input: n = 3
# Output:
#     *
#   *   *
# *       *
#   *   *
#     *
# 24.Hollow Butterfly Pattern
# Input: n = 4
# Output:
# *       *
# * *   * *
# *   *   *
# *       *
# *   *   *
# * *   * *
# *       *
# 25.Hollow Hourglass Pattern
# Input: n = 5
# Output:
# * * * * *
# *       *
#   *   *
#     *
#   *   *
# *       *
# * * * * *
# 🔢 Number-Based Patterns (26–35)
# 26.Increasing Number Triangle
# Problem: Print numbers from 1 to n in triangle form.
# Input: n = 5
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 27.Repeating Row Number Triangle
# Input: n = 5
# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 28.Continuous Number Triangle
# Input: n = 4
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 29.Reverse Row Number Triangle
# Input: n = 5
# Output:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# 30.Inverted Number Triangle
# Input: n = 5
# Output:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# 31.Right-Aligned Number Triangle
# Input: n = 5
# Output:
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
# 32.Pyramid Number Pattern
# Input: n = 4
# Output:
#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1
# 33.Even Number Triangle
# Input: n = 5
# Output:
# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10
# 34.Odd Number Triangle
# Input: n = 5
# Output:
# 1
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9
# 35.Pascal’s Triangle
# Input: n = 5
# Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1