# 36. Print All Prime Numbers from m to n
# Problem: Given a range from m to n, print all prime numbers in that range.
# Input: m = 10, n = 30
# Output: 11 13 17 19 23 29
# Explanation: A prime number has only two factors: 1 and itself.
m = 10
n = 30
for i in range(m,n):
    for j in range(2,(i//2)+1):
        if i%j == 0:
            break
    else:
        print(i,end=' ')
            

# 37. Count of All Prime Numbers from m to n
# Problem: Count how many prime numbers are there between m and n.
# Input: m = 1, n = 10
# Output: 4
# Explanation: Prime numbers are: 2, 3, 5, 7
m = 1
n = 10
count = 0

for i in range(m, n + 1):
    if i < 2:
        continue
    is_prime = True
    for k in range(2, (i // 2) + 1):
        if i % k == 0:
            is_prime = False
            break
    if is_prime:
        count += 1

print('count:',count)



# 38. Print All Armstrong Numbers in a Range
# Problem: Print all Armstrong numbers between m and n.
# Input: m = 1, n = 500
# Output: 1 153 370 371 407
# Explanation: Armstrong number = sum of each digit raised to the power of number of digits.

m = 1
n = 500
for i in range(m, n + 1): 
    num = i
    temp = i
    power = 0
    total = 0
    while num > 0:
        power += 1
        num //= 10
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    if i == total:
        print(i)

# 39. First Prime Number from m to n
# Problem: Find the first prime number in the given range.
# Input: m = 10, n = 25
# Output: 11
m=10
n=25
for i in range(m,n):
    is_prime = True
    for j in range(2,(i//2)+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print('Prime:',i)
        break
        
# 40. Last Prime Number from m to n
# Problem: Find the last prime number in the given range.
# Input: m = 10, n = 25
# Output: 23
m=10
n=25
for i in range(n,m,-1):
    is_prime = True
    for j in range(2,(i//2)+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print('Prime:',i)
        break

# 41. First Vowel in a Name
# Problem: Given a string, find the first vowel in the string.
# Input: name = "Krishna"
# Output: i
# Explanation: First vowel from left is ‘i’
name = "Krishna"
for ch in name:
    if ch in 'aeiouAEIOU':
        print(ch)
        break


# 42. Last Vowel in a Name
# Problem: Given a string, find the last vowel in the string.
# Input: name = "Ramakrishna"
# Output: a
# Explanation: Last vowel is ‘a’
# 43. Print All Even Numbers Using Continue
name = "Ramakrishna"
rev=''
for ch in name:
    rev = ch+rev
for ch in rev:
    if ch in 'aeiouAEIOU':
        print(ch)
        break

# Problem: Use continue statement to skip odd numbers and print only even numbers between 1 and n.
# Input: n = 10
# Output: 2 4 6 8 10
n = 10

for i in range(1, n + 1):
    if i % 2 != 0:   
        continue
    print(i,end=' ')
print()


# 44. Print All Odd Numbers Using Continue
# Problem: Use continue statement to skip even numbers and print only odd numbers.
# Input: n = 10
# Output: 1 3 5 7 9
n = 10

for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    print(i,end=' ')


# 45. Count of Prime and Composite Numbers from m to n
# Problem: Count how many are prime and how many are composite numbers in range m to n.
# Input: m = 1, n = 10
# Output: Prime: 4, Composite: 4
# Explanation: Prime: 2,3,5,7 | Composite: 4,6,8,9
m=1
n=10
prime,composite = 0,0
for i in range(m, n + 1):
    if i <= 1:
        continue
    is_prime = True
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime += 1
    else:
        composite += 1
print(f'Prime: {prime} | Composite: {composite}')

# String and Text Manipulation – Interview Questions

# 46. Remove Spaces from Given Text
# Problem: Write a function to remove all spaces from the input string. Explanation: Remove any white space characters. Input: "he llo wor ld" Output: "helloworld"
str1 = "he llo wor ld"
new = ''
for ch in str1:
    if ch == ' ':
        continue
    else:
        new += ch
print(new)

# 47. Reverse a String
# Problem: Write a function to reverse the characters in a string. Input: "hello" Output: "olleh"
str1 = "hello world"
rev = ''
for ch in str1:
    rev = ch+rev
print(rev)

# 48. Reverse a String After Removing Spaces
# Problem: Write a function to reverse a string after removing all spaces. Input: "he llo world" Output: "dlrowolleh"
str1 = "he llo wor ld"
rev = ''
for ch in str1:
    if ch==' ':
        continue
    else:
        rev = ch+rev
print(rev)
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
