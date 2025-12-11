# num = int(input('Enter a Number: '))
# if num > 1:
#     for i in range(2, (num // 2) + 1):
#         if num % i == 0:
#             print('It is not a prime number')
#             break
#     else:
#         print('It is a prime number')
# else:
#     print('It is not a prime number')


# check whether a number is perfect square or not
# num = int(input('Enter a number: '))
# is_perfect_square = False

# for i in range(1, num + 1):
#     if i * i == num:
#         is_perfect_square = True
#         break

# if is_perfect_square:
#     print('Perfect square')
# else:
#     print('Not a perfect square')



# check number is sunny or not
# num = int(input('Enter a number: '))
# is_sunny = False

# for i in range(1, num + 2):
#     if i * i == num + 1:
#         is_sunny = True
#         break

# if is_sunny:
#     print(f'{num} is a Sunny number')
# else:
#     print(f'{num} is not a Sunny number')


# sum of digits in a number eg: 123
# n = int(input('Enter a number: '))
# total = 0
# while n > 0:
#     digit = n % 10
#     total += digit
#     n //= 10
# print('Sum of digits:', total)


# count digits in a number
# n = int(input('Enter a number: '))
# count = 0
# while n > 0:
#     count += 1
#     n //= 10
# print('Total digits:', count)



# reverse a number
# n = int(input('enter a number:'))
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10
# print(rev)

# print each digit in a number individually  number:123
# n = int(input('Enter a number:'))
# nrm = 0
# while n > 0:
#     digit = n % 10
#     nrm = nrm*10+digit
#     n//=10

# while nrm > 0:
#     digit = nrm % 10
#     print(digit)
#     nrm//=10

# check number is palindrome
# n = int(input('Enter a number:'))
# num = n
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev*10+digit
#     n//=10
# if num ==rev:
#     print('The number is palindrome')
# else:
#     print('the number is not palindrome')

# print all prime numbers from 1500 to 2500
# lst = []
# for num in range(1500, 2500):
#     Flag = True
#     for j in range(2, (num // 2) + 1):
#         if num % j == 0:
#             Flag = False
#             break
#     if Flag:
#         lst += [num]

# print(lst)


#highest of two numbers
# def gcd(a, b):
#     while b:
#         a, b = b, a%b
#     return a

# def lcm(a, b):
#     return(a * b) // gcd(a, b)
# print(lcm(20,30))


# n1, n2 = 10, 20
# if n1 > n2:
#     greatest = n1
# else:
#     greatest = n2
# while True:
#     if greatest % n1 == 0 and greatest % n2 == 0:
#         lcm = greatest
#         break
#     greatest += 1
# print(lcm) 


# #list arrange by length
# list1 = ['a','ccc','bb','dddd']
# d={}
# for i in list1:
#     count=0
#     for j in i:
#         count+=1
#     d[i]=count
# print(d)
# for i,j in d.items():
#     print(i)

    
# #patterns
# rows=5
# for i in range(rows, 0, 1):
#     print("*" , i)

# n=5
# alp=65
# s=0
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(alp+s),end=' ')
#         s+=1
#     print()


# #vowels
# def vowels(str):
#     vowels='aeiou'
#     num=0
#     for i in str:
#         if i in vowels:
#             num+=1
#     return num
# print(vowels('function'))


# def vowels(str):
#     vowels='aeiou'
#     num=0
#     for i in str:
#         if 'A'<=i<='Z':
#             if i not in vowels:
#                 num+=1
#     return num
# print(vowels('function'))


#longest substring


# Day-2 of PROBLEM SOLVING


# check whether a number is even or odd
# def eve_or_odd(n):
#     if n%2 == 0:
#         print('even')
#     else:
#         print('Odd')

# def eve_or_odd_list(n):
#     odd_list=[]
#     even_list=[]
#     for i in range(n):
#         if i % 2 == 0:
#             even_list +=[i]
#         else:
#             odd_list +=[i]
#     return even_list,odd_list
# print(eve_or_odd_list(100))


# list1=[]
# for i in range(1,251):
#     if i%5 == 0 and i % 10 != 0:
#         list1 = list1+[i]
# print(list1)

# def greater_num(a,b,c):
#     if a >b and a >c:
#         return a
#     elif b >a and b >c:
#         return b
#     else:
#         return c
# print(greater_num(1,2,3))

# def smallest_num(a,b,c):
#     if a < b and a < c:
#         return a
#     elif b < a and b < c:
#         return b
#     else:
#         return c
# print(smallest_num(1,2,3))

# def t_a(m,p,c):
#     total=0
#     if m >35 and p> 35 and c>35:
#         total = m+p+c
#         avg = total/3
#     else:
#         print('Fail')
#     return total,avg
# print(t_a(36,36,36))

# check how many number of cars are required for a given number of persons such that each one caries 5 persons
# p = 24
# cars = p // 5
# p = p % 5
# if p >0:
#     cars+=1
#     print(cars)
# else:
#     print(cars)


# check whether  year is leap year or not
# year=2004
# if (year%4 == 0 and year%100 != 0) or year%400 == 0:
#     print('leap year')
# else:
#     print('not a leap year') 


# List of leap years from 1 to 2025
# list1=[]
# for i in range(1,2025):
#     if (i%4 == 0 and i%100 != 0) or i%400 == 0:
#         list1 += [i]
# print(list1)

# print second greatest among three numbers
# def greater_2nd(a,b,c):
#     if a >b and a >c:
#         lar = a
#         if  b > c:
#             print(b) 
#     elif b >a and b >c:
#         lar = b
#         if  a > c:
#             print(b)
#     else:
#         lar = c

# print(greater_2nd(1,2,3))

# second largest using nested conditions 





# Matrix Manipulations
# define a matrix
A = [[1,2,3],[4,5,6],[7,8,9]]
rows=len(A)
cols=len(A[0])
for i in range(rows):
    for j in range(cols):
        print(A[i][j],end=" ")
    print()


A = [[1,2,3],[4,5,6],[7,8,9]]
rows=len(A)
cols=len(A[0])
sum=0
for i in range(rows):
    print(A[i][j],end=" ")
    sum += A[i][i]
print()
print('sum',sum)



# calculate transpose of the matrix
rows=len(A)
cols=len(A[0])
trans=[[0]*cols for i in range(rows)]
for i in range(rows):
    for j in range(rows):
        trans[i][j]=A[j][i]
print(trans)



# Sum of each element in a row and in column
rowsum=colsum=0
for i in range(len(A)):
    rowsum=colsum=0
    for j in range(len(A[0])):
        rowsum += A[i][j]
        colsum += A[j][i]
    print(rowsum,colsum)

# sum matrix
B=[[10,11,12],[13,14,15],[16,17,18]]
row=len(B)
col=len(B[0])
sum = [[0]*3 for i in range(row)]
for i in range(row):
    for j in range(col):
        sum[i][j]=A[i][j]+B[i][j]
print(sum)
