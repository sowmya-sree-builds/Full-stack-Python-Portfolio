# Tasks:
# 1. Print reverse of a string(without built in function).
# 2. Average of marks of five students.
# 	marks=[400, 450, 530, 550, 570]
# 3 check whether the given sides form a triangle or not:a=5, b=5, c=5
# (Triangle rule: sum of any two sides is greater than the third side)


# Code 1
n = "This is reverse of a string"
print (n[::-1])


# Code 2

def avg():
    marks=[400, 450, 530, 550, 570]
    sum = 0
    count = 0
    for i in marks:
        sum += i
        count += 1
    average = sum / count if count != 0 else 0  # avoid ZeroDivisionError
    return average
print(avg())


# Code 3
def is_triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        return True
    return False

print(is_triangle(1, 2, 9))   # False
print(is_triangle(5, 5, 5))   # True
