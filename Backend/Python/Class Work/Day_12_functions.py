# it is a block of code which can perform a certain task or action, by creating a function 
# we can reuse that blovk of code where ever we want in the program
# we create a function by using a keyword called 'def' here def stands for define.

# Syntax: def function_name():
            # ...........
            # ...........

'''def greetings():
    name = input('Enter the name:')
    print(f'Welcome {name} to 10k coders')
    print('welcome',name,'to 10k coders')

greetings()'''

'''def greetings(name,course,institute):
    print(f'Welcome{name} to {course} at {institute}')

def numbers():
    num = int(input('Enter a number:'))
    for i in range(num+1):
        print(i)

numbers()'''

# Parameters: defined inside parenthesis of funtion to pass values to it
# variable: to assign value
# arguments: values passed to the function

# perform addition, substraction, multiplication, division
'''def calc(a,b):
    print(a+b,a-b,a*b,a/b)

calc(2,3)'''

# perform concatenation and replication of strings in a function with parameters
# Concatenation: adding of two strings 
# Replication: it is the process of replicating 2 strings 
'''def str(str1,str2,n):
    concat = str1+str2
    repli = str1 * n
    print(f'Concatination:{concat},Replication:{repli}')'''



# Try concatenation and replication of all sequence of data types

# def str(str1,str2,n):
#     concat = str1+str2
#     repli = str1 * n
#     print(f'Concatination:{concat},Replication:{repli}')

# str(('sow'),('mya'),5)

# we use parameters to decerease the complexity in the program
# function without parameters:
# return: return is used when we want to return a 
# value after performing certain action in the function
# def add(a,b):
#     return a+b
# print(add(10,20)+20)  
# def sub(a,b):
#     return a-b
# print(sub(10,20)+20)  
# def mul(a,b):
#     return a*b
# print(mul(10,20)+20)  
# def div(a,b):
#     return a/b
# print(div(10,20)+20)  
#print returns none type value it only displays we
# cant use print for further operations

# write a function that takes a list as input and find out all the even numbers
#  in that list and return sum of those even numbers.
def evensum(list1):
    sum = 0
    for i in list1:
        if i % 2 ==0:
           sum +=i
    return sum
list1 = [1,2,3,4,5,6,7,8,9,10]
print(evensum(list1))

'''with out 
with 
postional 
default 
with return 
with out return

function: bloxk of code to perform a specific task again and again in a program
function with out parameters: 
keyword arguments: it is used to pass arguments to a functiohn in any order you like, here while calling a function
you pass arguments along eith the name of the parameters'''


def details(name, age, address, course, phno):
    print(f'hello {name} as of this year you re of age {age} you live at {address}, studying {course} and your contact number is {phno}')    



# task : 
# write a keyword args function to print your personal details.
# details must cover your name,father name,mother name, your btech course , siblings etc...

# def details(name, father, mother, course, siblings):
#     print(f'hey i am {name} my father name is {father} is my mother name is {mother} is and my btech course{course} is and i have one siblings he is {siblings}')

# details(name = 'sowmya', mother = 'rupa', father = 'nagesh', siblings = 'dhanu', course = 'btech')
# print(details)


# # variable length arguments:
# #   it is used to pass multiple values to a single parameter in a function

# def number(*num):
#     m = 1
#     for i in num:
#         m *= i
#     return m

# print(number(1,2,3,4,5))

# def details(*urdetails):
#     for i in urdetails:
#         print(i)

# details('sami','vizag',20,987656542,'kavs','ruby')

def details(**urdetails):
    for i,j in urdetails.items():
        print(f'{i}:{j}')
        print(i)

details(name = 'sowmya', age = 23, address = 'vizag')


def operations(a,b):
    return a+b,a-b,a*b,a/b
add,sub,mul,div = operations(5,3)
print(add,sub,mul,div)