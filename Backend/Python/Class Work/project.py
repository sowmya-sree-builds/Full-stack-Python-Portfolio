# Function to check if a number is a neon number
def is_neon(number):
    square = number ** 2
    digit_sum = sum(int(digit) for digit in str(square))
    return digit_sum == number

num = int(input("Enter a number: "))
if is_neon(num):
    print(f"{num} is a Neon Number")
else:
    print(f"{num} is not a Neon Number")

price = [120,250,300,150,200]
sum = 0
for i in price:
    sum += i
print(sum)

# count number of even and odd numbers in a list

numbers = [10,25,30,47,52,61]
s=p= 0
ec=[]
oc=[]
for i in numbers:
    if i%2 == 0:
        s+=1
        ec.append(i)
    else:
        p+=1
        oc.append(i)
print(ec,oc)

print(f'Count of even numbers:{s},Count of odd numbers:{p}')


# To check whether a given username and password are correct or not and if the user 
# enters 3 times wrong 'Your acount is locked' must be printed
# username = 'admin' password ='Admin@123'


i = 3
while i>=0:
    username = input('Enter Username:')
    password = input('Enter password:')
    if username == "admin" and password == "Admin@123":
        print(f'You have unlocked your account')
    elif i<=0:
        print('Your account is locked')
    else:
        print(f'you have {i} more attempts')
    i -= 1

# factorial of a given number

n = int(input('Enter a number to find factorial:'))
for i in range(1,n):
    if n > 0:
        n = n*i
print(n)

# Print fibbinoci series upto the value n. pass n value using input()
values = [32,35,30,36,34,31,37]
for i in values:
    a,b=0,1
    for i in range(0,1):
        print(a,end=' ')
        a,b=b,a+b



# Print sum of digits of a number
# eg: num = 123 sum = 6

num = int(input('Enter a number:'))
sum = 0
while num>0:
    digit = num % 10
    sum += digit
    num //= 10
print(sum)

# Find the number of digits in a number
# eg: num = 156 then count 3
n = 156

# print reverse of a number, pass input as a integer

n = int(input('Enter a number:'))
rev = 0
while n>0:
    digit = n % 10
    rev = rev *10 + digit
    n = n//10
print(rev)

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

# Armstrong number

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

# second largest
list = [11,2,3,9,2]
sec=fir=list[0]
for i in list:
    if i>fir:
        sec=fir
        fir=i
    elif i < fir and (sec == fir or i > sec):
        sec = i
print(sec)

# first largest
list=[1,5,26,78,4]
max=list[0]
for i in list:
    if i > max:
        max=i
print(max)


string = "  python batch 66r "

vowels,consonants,numbers,spaces = ""

for ch in string:
    if ch in "aeiouAEIOU":
        vowels += ch
    elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        consonants += ch
    elif '0' <= ch <= '9':
        numbers += ch
    elif ch == ' ':
        spaces += ch

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Numbers:", numbers)
print("Spaces:", repr(spaces))

def capit(text):
    if not text:
        return ""
    first = text[0]
    if 'a' <= first <= 'z':
        first = chr(ord(first) - ord('a') + ord('A'))
    return first + text[1:]

print(capit("123abc")) 


# reverse

string = "python batch 66r"
reverse = ""

for ch in string:
    reverse = ch + reverse 

print("Reversed String:", reverse)

# prime


nums = [11, 23, 45, 56, 37, 19, 22, 29]

prime = []
rev_list = []

for n in nums:
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break
        else: 
            prime+=[n]

for p in prime:
    r = 0
    t = p
    while t > 0:
        d = t % 10
        r = r * 10 + d
        t //= 10
    rev_list+=[r]

print(prime,rev_list)

for p in prime:
    r = 0
    t = p
    while t > 0:
        d = t % 10
        r = r * 10 + d
        t //= 10
    rev_list.append(r)

print("Prime:", prime)
print("Rev:", rev_list)


