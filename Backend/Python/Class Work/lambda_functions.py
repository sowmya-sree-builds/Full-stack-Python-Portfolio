sq = lambda x:x*x
print(sq(6))

# lambda with two args
add = lambda a,b:a+b
print(add(3,4))

# lambda with default args
default1 = lambda a=10,b=20: a+b
print(default1())

# lambda with nested lambda
nes1 = lambda x: lambda y:x*y
print(nes1(3)(4))


# lambda with no args
name = lambda:'sowmya'
print(name())