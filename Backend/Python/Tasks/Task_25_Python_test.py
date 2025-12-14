# ASSIGNMENT 

# Date:19-09-2025
# Tech stack : python
# Topic : Test
# Dead line :  2days 
# _______________________________________________________

# Task: Write the answers and upload as a pdf
# 67R Python test

# Date:19/9/25

# 1. WAP to product of 2 matrices...
# I/p:  ar=2 ac=2       br=2 bc=3     O/P: 5 4 1
#       1 2             1 -2 3             1 -9 10
#       3 -1            2 3 -1
A = [[2,2],[1,2],[3,-1]]
B = [[2,3,1],[1,-2,3],[2,3,-1]]

rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])

if cols_A != rows_B:
    print("Matrix multiplication not possible")
else:
    result = []
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            val = 0
            for k in range(cols_A):
                val = val + A[i][k] * B[k][j]
            row+=[(val)]
        result+=[(row)]

    print("Matrix Multiplication Result:")
    for r in result:
        print(r)



# 2. WAP to get nearest prime of given number...
# I/p: 7      10      11
# O/p: 5      11      13

n = int(input('Enter a value: '))
def is_prime(x):
    if x < 2:
        return False
    i = 2
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True
d = 1
while True:
    left = n - d
    right = n + d
    if left >= 2 and is_prime(left):
        print('Nearest number is small: ',left)
        break
    if is_prime(right):
        print('Nearest number is big: ',right)
        break
    d += 1

# 3. WAP to find repeated values in a list...
# I/p: [1,2,3,4,3,6,7,2]
# o/p: [2,3]
lst = [1,2,3,4,3,6,7,2]
res = []
i = 0
while i < len(lst):
    j = i + 1
    while j < len(lst):
        if lst[i] == lst[j]:
            k = 0
            found = False
            while k < len(res):
                if res[k] == lst[i]:
                    found = True
                k += 1
            if not found:
                res.append(lst[i])
        j += 1
    i += 1
print(res)



# 4. WAP to print hallow diamond...
#      *
#     * *
#    *   *
#   *     *
#  *       *
#   *     *
#    *   *
#     * *
#      *
n = 5
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end="")
        j += 1
    k = 1
    while k <= 2 * i - 1:
        if k == 1 or k == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
        k += 1
    print()
    i += 1

i = n - 1
while i >= 1:
    j = 1
    while j <= n - i:
        print(" ", end="")
        j += 1
    k = 1
    while k <= 2 * i - 1:
        if k == 1 or k == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
        k += 1
    print()
    i -= 1

# 5. WAP for replace built in function of string...

# I/p: "iam a java trainer"       "Sravan"

#     old="java" new="python"    old="a" new="b"

# O/p: "iam a python trainer"     "Srbvbn"
s = "iam a java trainer"
old = "java"
new = "python"

res = ""
i = 0
while i < len(s):
    j = 0
    match = True
    while j < len(old):
        if i + j >= len(s) or s[i + j] != old[j]:
            match = False
            break
        j += 1
    if match:
        k = 0
        while k < len(new):
            res += new[k]
            k += 1
        i += len(old)
    else:
        res += s[i]
        i += 1
print(res)

s = "Sravan"
old = "a"
new = "b"

res = ""
i = 0
while i < len(s):
    if s[i] == old:
        res += new
    else:
        res += s[i]
    i += 1
print(res)





