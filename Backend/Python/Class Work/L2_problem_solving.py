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
lst = []
for num in range(1500, 2500):
    Flag = True
    for j in range(2, (num // 2) + 1):
        if num % j == 0:
            Flag = False
            break
    if Flag:
        lst += [num]

print(lst)


# nearest prime number
# n = 16
# def nearest_prime(n):   
#     for i in range(2, (n // 2)+1):
        