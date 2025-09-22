"""Nested If-else: it is used to make decisions based on a certain conditions, Helpful to execute conditions layer by layer"""

# Example 1
"""age = int (input('enter age:'))
license = input('Do you have license:')
if age>=18 and license == '67':
  print('You can drive')
else:
    print('You cant drive')"""
# Example 2
"""
# grading using nested loops
marks = int(input('Enter your Marks: '))
if marks>=35:
    if marks>=90:
        print('You got an O')
    elif marks >= 75:
        print('you got an A')
    elif marks >= 65:
        print('You got a B')
    else:
        print('Parents: mak nuv fail ee raw')
else:
    print('You got an F,Sar Sarle enneno anukuntam')"""

# write a nested if program such that first if else should check whether the given number is positive or noot,
# second if else with in first one must check whether the given number is even or not 
# ,third if else should check whther the number is greater than 50 or not
"""num = int(input('Enter Your number:'))
if num >=0:
    print('Number is positive')
    if num%2 == 0:
        print('Given number is even')
        if num>=50:
            print('given number is greater than 50')
        else:
            print('given number is less than 50')
    else:
        print('Number is odd')    
else:
    print('Number is negative')"""

#ternary operator: it is a way to write an if else condition within a single line
"""              Syntax: value_if_true if codition else value_if_false
                 print('eligible to vote' if age > 18 else 'not eligible')
n = int(input('Enter n:'))
print('even' if n%2==0 else'odd' )"""

"""Loops: Repetition of a task for a certain number of times.
Types of loops: For Loop, While Loop
for loop: it is used to iterate over a sequence of data
syntax: for  Variable name in sequence name:

range(): It is used to generate numbers over a limit.
len(): It returns the number of values in a sequence.

Syntax: range(start,stop,skip)

while loop:  it runs until the condition passed to it is satisfied or true
Click ctrl + c to kill a program execution in the middle."""


#Example 1 - for loop
"""
lists = list(range(1,51))
len(lists)
for i in lists:
    print('Hello',i)
lists = list(range(1,51))
print(lists)
print(len(lists))
"""

"""# print a sequence of values using for and range
for i in range(1,11,2):
    print(i)"""

"""lists = ['Mango','banana','apple','orange','litchi','Custard apple']
playing with len()
for i in range(len(lists)):
    print(i+1,lists[i])"""


# string is a sequential data which contains a sequence of characters combined together
# end='' is used to print all the chrcs in same line 
"""string='Sowmya Sree Alla'
for i in range(len(string)):
    print(i,string[i])"""

# it is a for loop writen inside a for loop.
"""for i in range(5):
    for j in range(5):
        print('i Value',i,'j Value:',j)

list1 = ['Alla']
list2 = ['Nagesh', 'Rupa', 'sowmya', 'Dhanu']
for i in list1:
    for j in list2:
         print(i,j)"""

# Example 2 - while loop
"""i = 10
while i>0:
    print('Bahubali 2')
    i-=1 # i = i-1"""
"""i = 10
j = 10
while i>0:
    while j>0:
        j -= 1
    print(i,j)
    i -= 1
"""
i = 10
j = 10
while i>0 and j>0:
    print(i,j)
    j-=1
    i-=1

