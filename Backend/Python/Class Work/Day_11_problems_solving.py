
# # write a program to print sum of price of items from a list using a loop
# price = [120,250,300,150,200]
# sum = 0
# for i in price:
#     sum += i
# print(sum)

# # count number of even and odd numbers in a list

# numbers = [10,25,30,47,52,61]
# s=p= 0
# ec=[]
# oc=[]
# for i in numbers:
#     if i%2 == 0:
#         s+=1
#         ec.append(i)
#     else:
#         p+=1
#         oc.append(i)
# print(ec,oc)

# print(f'Count of even numbers:{s},Count of odd numbers:{p}')



# # find maximum among a sequence of values

# values = [32,35,30,36,34,31,37]
# s = values[0]
# for i in values:
#     if i > s:
#         s = i
# print(s)


# # To check whether a given username and password are correct or not and if the user 
# # enters 3 times wrong 'Your acount is locked' must be printed
# # username = 'admin' password ='Admin@123'


# i = 3
# while i>=0:
#     username = input('Enter Username:')
#     password = input('Enter password:')
#     if username == "admin" and password == "Admin@123":
#         print(f'You have unlocked your account')
#     elif i<=0:
#         print('Your account is locked')
#     else:
#         print(f'you have {i} more attempts')
#     i -= 1

# for i in range(3,-1):
#     username = input('Enter Username:')
#     password = input('Enter password:')
#     if username == "admin" and password == "Admin@123":
#         print(f'You have unlocked your account')
#     elif i<=0:
#         print('Your account is locked')
#     else:
#         print(f'you have {i} more attempts')
#     i -= 1

# # write a program to print discount of 100 rs to passengers with seat numbers which are divisible of 3 and 5.

# seatNumbers = [5,25,13,15,27,55,11,30]
# for i in seatNumbers:
#     if i % 3== 0 and i % 5 == 0:
#         print(f'Seat no {i} You got a discount of 100 rupees')
#     else:
#         print(f'Seat no {i} Not eligible for a discount')

# to check whether a given item is in your store or not.
# display whether the item is available or not 
# items =['apples','banana','capsicums','bread','onions']
# item = input('Enter your item:')
# for i in items:
#     if i == item:
#         print(f'{item} is available')
#         continue
# else:
#     print(f'{item} is not available')

# factorial of a given number

# n = int(input('Enter a number to find factorial:'))
# for i in range(1,n):
#     if n > 0:
#         n = n*i
# print(n)

# Print fibbinoci series upto the value n. pass n value using input()
# 0,1,1,2,3,5,8,13
# n = n-1 + n-2
# n = 9
# n1,n2 = 0,1
# for i in range(2,n):
#     n3 = n1+n2
#     n2 = n1
#     n1 = n3
#     print(n3)


# check whether a number is perfect square or not use input()
# if square root of a number returns a integer then the number is called a perfect square
#  16 ** 1/2 = 4

# n = int(input('Enter a number: '))
# s = (n ** (1/2))
# print(s)
# if n%s == 0:
#     print('perfect square')
# else:
#     print('not a Perfect square')


# Print sum of digits of a number
# eg: num = 123 sum = 6

# num = int(input('Enter a number:'))
# sum = 0
# while num>0:
#     digit = num % 10
#     sum += digit
#     num //= 10
# print(sum)

# Find the number of digits in a number
# eg: num = 156 then count 3
n = 156

# print reverse of a number, pass input as a integer

# n = int(input('Enter a number:'))
# rev = 0
# while n>0:
#     digit = n % 10
#     rev = rev *10 + digit
#     n = n//10
# print(rev)

# check whether a given number is palindrome or not.

n = int(input('Enter a number:'))
s = n
rev = 0
while n>0:
    digit = n % 10
    rev = rev *10 + digit
    n = n//10
if s == rev:
    print('Palindrome')
else:
    print('Not a palindrome')

n = int(input("Enter a number: "))
temp = n
digits = len(str(n))
s = 0
while temp > 0:
    d = temp % 10
    s += d ** digits
    temp //= 10
if s == n:
    print(n, "is an Armstrong Number")
else:
    print(n, "is not an Armstrong Number")

# n = 12345
# if n<10:
#     print('cant swap')
# else:
#     last = n % 10
#     second_last = (n//10)%10
#     num = n//100 
#     res = num*100+last*10+second_last
#     print(res)

# list = [11,2,3,9,2]
# sec=fir=list[0]
# for i in list:
#     if i>fir:
#         sec=fir
#         fir=i
#     elif i < fir and (sec == fir or i > sec):
#         sec = i
# print(sec)



# # list lo 2 nd maximum find second minimum                                                  