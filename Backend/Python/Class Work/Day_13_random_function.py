# 💡 PYTHON RANDOM MODULE — EXAMPLES

import random

# -----------------------------------------------
# 1️⃣ random.random()
# Returns a random float number between 0.0 and 1.0
print("Random float (0–1):", random.random())

# -----------------------------------------------
# 2️⃣ random.randint(a, b)
# Returns a random integer between a and b (inclusive)
print("Random integer (1–10):", random.randint(1, 10))

# -----------------------------------------------
# 3️⃣ random.randrange(start, stop, step)
# Works like range(), but picks one random value from it
print("Random number (range 0–50 step 5):", random.randrange(0, 51, 5))

# -----------------------------------------------
# 4️⃣ random.uniform(a, b)
# Returns a random float number between a and b
print("Random float (1–100):", random.uniform(1, 100))

# -----------------------------------------------
# 5️⃣ random.choice(sequence)
# Picks a random element from a list, tuple, or string
fruits = ["apple", "banana", "cherry", "mango"]
print("Random fruit:", random.choice(fruits))

# -----------------------------------------------
# 6️⃣ random.choices(sequence, k=n)
# Returns a list of 'k' random elements (with replacement)
print("Random 3 fruits (with replacement):", random.choices(fruits, k=3))

# -----------------------------------------------
# 7️⃣ random.sample(sequence, k=n)
# Returns a list of 'k' unique elements (without replacement)
print("Random 2 fruits (without replacement):", random.sample(fruits, 2))

# -----------------------------------------------
# 8️⃣ random.shuffle(list)
# Shuffles the elements of a list in place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled numbers:", numbers)

# -----------------------------------------------
# 9️⃣ random.seed(x)
# Sets the seed value so random numbers are reproducible
random.seed(10)
print("Random number with seed 10:", random.randint(1, 100))

# -----------------------------------------------
# 🔟 random.getrandbits(n)
# Returns an integer with n random bits
print("Random number with 4 bits:", random.getrandbits(4))  # Range 0–15

# -----------------------------------------------
# BONUS 🎲
# Simulate a dice roll (1 to 6)
dice = random.randint(1, 6)
print("Dice rolled:", dice)

# Simulate a coin toss
coin = random.choice(["Heads", "Tails"])
print("Coin toss:", coin)
