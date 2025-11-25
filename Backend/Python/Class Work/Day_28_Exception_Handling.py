# Exception Handling
# 
# 
# Exception it is a type of error occurs in a program when there is a runtime error
# Error:
# It is an interuption in our program which stops the flow of execution abruptly
# Types of Errors:
# 1.Compile time error/syntax error:  these are the errors which occur during compling a program.
# print('hello' world)
# 2.Exception/run-time Error:  these errors occurs during execution or runtime of a program..
#                              Zero division error, index error, Value Error, 
# print(10/0)  -- gives zero division error
# Inorder to handle these exceptions so that the flow of execution of program won't be interrupted we use the mechanism called exception handling.
# for Exception handling we use 2 main keywords:   'try' and 'except'
# try:
# in try block we write the code which has the possibilty of raising an exception.
# except:
#  in this block we write the code that should happen when an exceptioon is occurred.
# we cannot write a try block without an except block.
# in try block the execution stops at the moment it encounters an exception and the execution enters the except block.
# once the execution enters the except block it cant roll back to try block. except with known errors
# By default an except block specified error can only handle that one error. 
# if your program can raise multiple types of exceptions then your program might need multiple except blocks to handle them.
# Incase if we dont know the type of error the program gonna raise then we use only except keyword without mentioning specific error name.
# using this type of exception we can handle multiple exception with one except block.
# though the type of exception handling is easy it is not advisable as it is not specifying what exactly went wrong specifying what exactly went wrong 
# in case if we DK the error but want to know excatly what went wrong in that case i can access that exception with a variable and print that exact error message. 

# Finally: block is executed wether an exception is raised or not.

# Differences between else and finally:
# else executes when no exception is raised where as finaaly executes whether an exception is raised or not.

# raise keyword:
# it is used to raise an exception manually.(we are raising the error here)
# we can raise which ever type of exsisting error, with an custom message using a raise keyword. 

# try:
#     num1 = int(input('Enter a number:'))
#     num2 = int(input('Enter another number:'))
#     div = num1/num2
# except ZeroDivisionError:
#     print('Cannot divide a number by zero')
# print('Execution continued even after an exception occured')

# Nested Exceptions
# try:
#     list1 = [2,3,4,5,6,8]
#     iv = int(input('Enter another number:'))
#     print(list1[iv])

# except IndexError:
#     print('index value not available')

# except ValueError:
#     print(' value not available')

# print('Execution continued even after an exception occured')

# try:
#     list1 = [2,3,4,5,'charge',6,7,8]
#     sum=0
#     for i in list1:
#         sum+=i
#     print(sum)
# except TypeError:
#     print('Huh there is a string in list')

# try:
#     num1=int(input('Enter the number:'))
#     num2=int(input('Enter another number'))
#     div = num1/num2
#     print(div)

# except ZeroDivisionError:
#     print('cannot divide a number by zero')
# except ValueError:
#     print('pass only integers')

# WAP to calculate profit per item when the total profit and number of items are given.
# try:
#     tp = int(input('Enter the profit:'))
#     noOfitems = int(input('Enter no of items'))
#     profit = tp/noOfitems
#     print('profit per item is', profit)
# except:
#     print('You paased some wrong value please check')

# try:
#     num1=int(input('Enter the number:'))
#     num2=int(input('Enter another number'))
#     print('add: ',num1+num2)

# except Exception as e:
#     print(e)


# wap to check whether a number is prime or not and handle any kind of exception that can be raised in it by printing the exact error message.
# try:
#     num = int(input('Enter a number to check if its prime:'))


# Exception handling with else

# product of values in a list
# try:    
#     list1 = [1,4,7,9,8,6,2]
#     product = 1
#     for i in list1:
#         product *=i
#     print(product)

# except Exception as e:
#     print(e)

# else:
#     print('No exception raised')
# if there is exception else block wont be excecuted
# if we want a specific block of code to be excecuted when no exception is raised, in that case we can use an else block with exception handling. 

# try:
#     list1=[1,2,3,'3',4,5]
#     sum = 0
#     for i in range(len(list1)):
#         sum += list1[i+1]
#     print(sum)

# except (TypeError, IndexError) as e:
#     print(e)

# finally:
#     print('the program execution has been completed')     # executed after completion of the program



# try:
#     num=int(input('Enter a number:'))

# except ValueError as e:
#     print(e)

# else:
#     if num % 2 == 0:
#         print('even ')
#     else:
#         print('odd ')


# try:
#     num = int(input('Enter a number: '))

# except ValueError:
#     print('enter a number instead of a string')

# else:
#     count = 0
#     for i in range(1,num+1):
#         if num%i == 0:
#             count += 1
#     if count == 2:
#         print('prime')
#     else:
#         print('not prime')

# finally:
#     print('program Exceution completed successfully')


# age = 45
# if age > 18:
#     print('Major')

# else:
#     raise KeyError('Person must be above 18')

# raise ValueError('Na istam')


# raise: used to raise exceptions manually

# creating custom exception:
        # we create custom exceptions so that we can debug large projects efficiently.
        # we can create a custom exception by creating a class which inherits the exception class.

# class sowmyaError(Exception):
#     pass

# raise sowmyaError('i am raising the error')


# class ListError(Exception):
#     pass
# try:
#     list1 = ['sowmya','rishi','booma']
#     if len(list1) <0:
#         raise ListError('list cannot be empty')
#     print(list1)
# except ListError as e:
#     print(e)


# WAP to create an exception LowBalanceError and raise it when balance is less than 500.
# class LowBalanceError(Exception):
#     pass
# try:
#     balance = int(input('enter a number: '))
#     if balance < 500:
#         raise LowBalanceError('Your balance is below 500')
#     print('heres is your balance' , balance)
# except LowBalanceError as e:
#     print(e)


# assert keyword: it is also used to raise an exception just like raise but assert exception is raised when the condition passed to it turns False.
#                 assert is generally used to debug or to evaluate conditions in our program.

# raise KeyError('raising this to check')

# name='sam'
# assert len(name)>10, 'name must be atleast 10 characters'
# print(name)


# try:
#     name = input('enter your name:')
#     assert len(name)>=10, 'Name must have atleast 10 characters'

# except AssertionError as e:
#     print(e)



# WAP to check whether a string has @ in it if not raise an AssertionError.
# s = 'yametey anata'
# assert '@' in s, 'The string does not contain @'
# print(s)



# wap to check the validity of username and password, if username is wrong raise an customized UsernameError and if password is wrong then raise custmoized exception passwordError.


class UsernameError(Exception):
    pass
class PasswordError(Exception):
    pass

try:
    username = input('enter name: ')
    password = input('enter password: ')
    if username != 'sam0124':
        raise UsernameError('user name not found')
    try:
        if password != '1234':
            raise PasswordError('password is incorrect')
    except PasswordError as e:
        print(e) 
except UsernameError as e:
    print(e)
