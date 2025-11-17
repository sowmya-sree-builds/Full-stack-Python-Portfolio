# check whether a year is leap year or not
year=5000
if year%4==0 and year%100!=0 or year%400==0:
    print('Leap year')
else:
    print('Not a leap year')

# Evaluate username and password such that if username is correct only then password input must be asked else it should return invalid username
username = input('Enter a name: ')
if username == 'ria':
    password=input('Enter password: ')
    if password == '123':
        print('Login successful')
    else:
        print('password error ')
else:
    print('invalid username')



# WAP to check whether a student passed or failed he should get min of 35 marks in eveyhujiklry subject and percentage must be greater than 40. else he is failed
subject_1 = int(input('Enter your marks:'))
subject_2 = int(input('Enter your marks:'))
subject_3 = int(input('Enter your marks:'))

ms1=ms2=ms3=100
p = (subject_1+subject_2+subject_3)/(ms1+ms2+ms3)
if subject_1 > 35 and subject_2 > 35 and subject_3 > 35 and p > 40:
    print('you passed')
else:
    print('You failed')


# WAP greatest among three num
a=10
b=20
c=30
# print('a is greater'if a>=b and a>=c else "b is greater" if)