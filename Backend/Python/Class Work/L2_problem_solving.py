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

# highest of two numbers
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

# list arrange by length
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
    
# patterns
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

# vowels
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
# def second_greatest(a, b, c):
#     if (a > b and a < c) or (a > c and a < b):
#         return a
#     elif (b > a and b < c) or (b > c and b < a):
#         return b
#     else:
#         return c

# Armstrong number from 1 to 1000
# for i in range(1,1001):
#     n=i
#     temp=i
#     powe=0
#     s=0
#     while n > 0:
#         powe += 1
#         n //= 10
#     while temp > 0:
#         d = temp % 10
#         s += d ** powe
#         temp //= 10
#     if s == i:
#         print(i)

# calculate bmi of a person . BMI = weight in kilos/(height in metres)**2
# weight = in kilos, height in cms, meteres in centimeters\100
# if BMI<18.5 underweight
        # 18.5-24.9 Normal
        # 25-29.9 overweight
        # >=30 obese

# weight = int(input('Enter you weight in kilos:'))
# height = int(input('Enter you height in cms:'))
# height *= 100
# BMIs = weight /(height)**2
# print(BMIs)
# if BMIs<18.5:
#     print('Underweight')
# elif 18.5<BMIs<24.9:
#     print('Underweight')
# elif 25<BMIs<29.9:
#     print('Overweight')
# elif BMIs >= 30:
#     print('Underweight')

#  Write a program to print frequency of a specific character in a string using function.
# def bahubali(ch, str1):
#     count = 0
#     for c in str1:
#         if c.lower() == ch.lower():
#             count += 1
#     return count

# print(bahubali('m', 'mahismati Samrajyam'))


# write a program to find char with highest frequency in a string
# def bahubali(str1):
    
# print(bahubali('mahismati Samrajyam'))

# write a program to check a palindrome ignoring spaces in a string
# string1 = 'A Man A Plan A Canal Panama'
# ord(A) = 65 ord(Z) = 90 ord(a)= 97 ord(z) = 122

# string1 = 'A Man A Plan A Canal Panama'
# for i in string1:
    # if 65<ord(i)<90: 
        #  chr+=32
         


# input  :
# number of matrices:2
# number of rows:2
# number of columns:3

# output:

# [[1,2,3]]      [[7,8,9]],
# [[4,5,6]]      [[10,11,12]]

# sum  [[8,10,11]],
#      [[14,16,18]]     


# day 3 problem solving



# reverse of a string without spaces eg: i am python developer
# str = 'i am python developer'
# rev = ''
# for ch in str:
#     if ch != ' ':
#         rev = ch + rev 
# print(rev)


# print frequency of ebery character in a string 
# str = 'Mahishmati samrajyam'
# dict1 = {}
# for ch in str:
#     if ch != ' ': 
#         if ch not in dict1:
#             dict1[ch] = 1
#         else:
#             dict1[ch] += 1
# print(dict1)

# convert the char in a string to lower case without lower

# str='10K CODERS'
# str1=''
# for ch in str:
#     if 'A'<=ch<='Z':
#         str1+=chr(ord(ch)+32)
#     else:
#         str1+=ch
# print(str1)


# reverse the cases of each character in a string:

# str1='DeVaSeNa AmAtHyA'
# str2=''
# for ch in str1:
#     if 'A'<=ch<='Z':
#         str2+=chr(ord(ch)+32)
#     elif  'a'<=ch<='z':
#         str2+=chr(ord(ch)-32)
#     else:
#         str2+=ch
# print(str2)


# check whether a list of strings is palindrome

# str1 = ['racecar', 'puri', 'madam', 'lilly']

# for word in str1:
#     rev = ''
#     for ch in word:
#         rev = ch + rev
#     if word == rev:
#         print("palindrome")
#     else:
#         print("not palindrome")


# Reverse the positions of words in a string str= ' Sowmya Sree Alla ' output - allA Sree Sowmya , Alla Sree Sowmya , allA eerS aymwoS
# str='Sowmya Sree Alla'
# word=rev=''
# for ch in str:
#     if ch !=' ':
#        word += ch
#     elif ch == ' ':
#         rev = word+rev
#         word=''
# print(word,rev)



# day-4 Problem Solving

# Pattern Problems 
# 1.SQUARE
# s=5
# for i in range(5):
#     for j in range(5):
#         print('*',end=' ')
#     print()



# 2.RECTANGLE
# for i in range(3):
#     for j in range(5):
#         print('*',end=' ')
#     print()



# 3.INVERSE RECTANGLE
# for i in range(5):
#     for j in range(3):
#         print('*',end=' ')
#     print()



# 4.LEFT ALIGNED TRIANGLE
# for row in range(5):
#     for col in range(row+1):
#         print('*',end=' ')
#     print()



# 5.LEFT ALIGNED TRIANGLE
# s=5
# for row in range(s):
#     for col in range(s-row):
#         print('*',end=' ')
#     print()



# 6.RIGHT ALIGNED TRIANGLE
# s=5
# for row in range(1,s+1):
#     for col in range(0,s-row):           #n-row+1
#         print(' ',end=' ')
#     for col in range(row):
#         print('*',end=' ')
#     print()



# 7.PYRAMID
# s=5
# for row in range(s,0,-1):
#     for col in range(0,s-row):   
#         print(' ',end=' ')
#     for col in range(row):
#         print('*  ',end=' ')
#     print()



# 8. PYRAMID 
# s=5
# for row in range(1,s+1):
#     for col in range(0,s-row):           
#         print(' ',end=' ')
#     for col in range(row):
#         print('*  ',end=' ')
#     print()



# 9.HOLLOW SQUARE
# n=5
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()



#                                                                  Problem solving
# Reverse of a number
# num = 2356
# rev = 0
# while num>0:
#     rev = rev * 10 + num % 10
#     num //= 10
# print('Reversed num:',rev)



# List of numbers first half ascending, second half descending




# Second smallest and second largest in a sequence.
list1 = [5,96,46,13,30,43]




# Remove braces from an equation eg: 'a+((b-c)+d)'  output: 'a+b-c+d'
# expr = 'a+((b-c)+d)'
# result = ""
# for ch in expr:
#     if ch not in '()[]{}':
#         result += ch
# print(result)


# Palindrome numbers between 10-50  and 100-500

# for num in range(10,50):
#     temp = num
#     rev = 0
#     while temp > 0:
#         rev = rev * 10 + num % 10
#         temp //= 10
#     if rev == num:
#         print(num)

# for num in range(100,500):
#     temp = num
#     rev = 0
#     while temp > 0:
#         rev = rev * 10 + num % 10
#         temp //= 10
#     if rev == num:
#         print(num)


# Arrange 'dskgrbg' in alphabetical order.
str = 'dskgrbg'




# WAP to remove duplicate elements in an array without using membership operators and built in methods
# list1 = [1,2,1,3,4,5,5,5,5,7,6]
# list2 = []
# flag=False
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i]==list2[j]:
#             flag=True
#             break
#         else:
#             flag=False
#     if flag == False:
#         list2+=[list1[i]]
# print(list2)

# WAP shift all Zeroes to end of the list
# list1=[0,1,0,2,0,3,0,4,0,5]
# shift=[]
# zerocount=0
# for i in list1:
#     if i == 0:
#         zerocount += 1
#     else:
#         shift += [i]
# for i in range(zerocount):
#     shift+=[0]
# print(shift)

# WAP take a tuple take a input as num 
tuple1 = (1,2,3,4,5,6,7,8,9,0,10)
pair=()
n = int(input('Enter a number:'))
for i in range(len(tuple1)):
    for j in range(i+1,len(tuple1)):
        if tuple1[i]+tuple1[j]==n:
            pair += (tuple1[i],tuple1[j])
print(pair)
           
