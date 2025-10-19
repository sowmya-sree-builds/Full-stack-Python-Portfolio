# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(5)


# for i in range(1, 11):
#     fact = 1
#     for j in range(1, i + 1):
#         fact *= j
#     print(f"Factorial of {i} is {fact}")



l = []
for n in range(1, 100000001):
    s = 0
    t = n
    digits = len(str(n))
    while t > 0:
        d = t % 10
        s += d ** digits
        t //= 10
    if s == n:
        l+=[n]
print(l)