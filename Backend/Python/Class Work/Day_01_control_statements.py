'''
Break: break is used to come out of the loop at a certain point.
Continue: it skips the iteration that is currently happening and restart.
pass: it is used to reserve a particular space for the user.'''
# i = 0
# sum = 0
# while True:
#     print(i)
#     if i == 1000:
#         break
#     i+=1
# l = {1,2,3,4,5,6,7,8,9,10}
# for i in l:
#     print(i)
#     if i == 5:
#        break
#     i += 1

# i = 0
# while(i<=11):
#     if i ==5:
#         i+=1
#         continue
#     print(i)
#     i+=1

# for i in range(10):
#     if i ==5:
#         continue
#     print(i)


# using for loop take a range from 1 to 100 and print numbers, if numbers are divisible by 57 
# then the loop must break and exit printing the current number is divisible by 57.

# for i in range(1,101):
#     if i % 57 == 0:
#         print(f'{i} is divisible by 57')
#         break
#     print(i)   


# using while loop pass names as input using input function if the given input is 'exit' or 'quit'
# then the loop must exit printing 'have a good day'

# while True:
#     string = input('Enter a value(enter "quit" or "exit") to exit the loop:')
#     if string.lower() =='exit' or string.lower() == 'quit':
#         print('Have a good day')
#         break
#     print(string)

#  skip all even numbers in a range from 1 to 50 using continue statement use for loop and also try with while.

# for i in range(1,101):
#     if i % 2 == 0:
#         continue
#     print(f'{i} is odd')  

# i = 100
# while i <=100:
#     i-=1
#     if i % 2 == 0:
#         print('number is odd') 
#         continue

# Skip all vowels in a given string using continue, eg if string = 'education' then print 'dctn'
# list = ['exit','quit','i am good']
# vowels = 'aeiou'
# for i in list:
#     if i.lower() in vowels:
#         continue
#     print(i,end='')
    
while True:
    string = input('Enter a value(enter "quit" or "exit") to exit the loop:')
    if string.lower() in ['exit','quit','nothing', 'done']:
        print('Have a nice day')
        break
    print(string)