"""Types of Operators
   1. Arthimetic Operators:  These Operators are used to perform mathemamtical Operations like +, - , *, /, //, %, **
   2. Assignment operators: These Operators are used to assign and operate and assign Like =, +=, -=, *=, /=, //=, %=, **= 
   3. Comparision operators: These operators compares 2 values and returns a Boolean Value like ==, !=, >=, <=, >, <
   4. Logical operators: AND, OR, NOT
   5. Identity operators: These checks whether two variables pointing to the same value like is,isnot for 
      these they mainly check the memory location of the variables that we are comparing to
   6. Membership operators: these checks whether a value is present in a sequence of data
   7. Bitwise operators: these operators works similar to logical operators but operates bit by bit
   -- it is the smallest value in a computer memory
   -- AND-'&', OR-'|',ExOR-'^', negation-'~', <<, >>
   -- 0.0000, 1.0001, 2.0010, 3.0011, 4.0100, 5.0101, 6.0110, 7.0111, 8.1000, 9.1001, 10.1010   """
"""# Arthimetic.....
x = 5
y = 3

# addition
print('addition:', x + y)

# subtraction
print('subtraction:', x - y)

# multiplication
print('multiplication:', x * y)

# division - gives the exact value 
print('division:', x / y)

# floor division - it removes the decimal part
print('floor division:', x // y)

# modulus - it gives the remainder of a equation
print('modulus:', x % y)

# exponential
print('exponential:', x ** y)

# Assignment.....
X = 5
# X = X+3 Add and Assign
X += 3
print(X)
# Substract and Assign
X -= 3
print(X)
# Multiply and Assign
X *= 3
print(X)
# Division and Assign
X /= 3
print(X)
# Floor Division and Assign
y=50
y //= 3
print(y)
# Modulo and Assign
y %= 3
print(y)
# Exponential and Assign
X **= 3
print(X)

# Comparision.....
a = 5
b = 4
# is equal to
print(a==b)
# not equal to
print(a!=b)
# greator equal to
print(a>=b)
# less equal to
print(a<=b)
# greator than
print(a>b)
# less than
print(a<b)


#Logical Operators
print(3>2 and 5<3)
print(5>=5 or 8<89)
print(not True)

# identity operators
a =[1,2,3]
b=a
c=[1,2,3]
print(a is b)
print(a is not c)
print(10 not in a)"""

# Bitwise operators
print(5&4)
print(5|4)
print(~8)
print(6>>2)