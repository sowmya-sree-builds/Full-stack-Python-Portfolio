n = int(input("Enter a number: "))
s = (n + 1) ** 0.5
if int(s) * int(s) == n + 1:
    print("It is a Sunny number")
else:
    print("It is not a Sunny number")
