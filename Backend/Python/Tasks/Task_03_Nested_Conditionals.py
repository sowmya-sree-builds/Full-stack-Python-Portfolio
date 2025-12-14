
# Practice Problems: Nested if-else & Ternary Operators

# Part A: Nested if-else Statement Problems

# Juice Shop Discount If a customer buys more than 2 bottles of juice:
# If they are a regular customer -> give 15% discount.
# If not -> give 5% discount. Otherwise, no discount.


# cbuy = int(input('Enter how many juices customer bought:'))
# frequent = input('Enter how frequent the customer is:')
# price = int(input('Enter the total price:'))
# if cbuy > 2:
#     if frequent.lower() == 'regular':
#         price *= 0.85 # 15% discount
#         print(f'Your total after 15% discount is:{price}')
#     else:
#         price *= 0.95 # 15% discount
#         print(f'Your total after 5% discount is:{price}')
# else:
#     print(f'Your total is:{price}')


# Your total is:500
# Fuel Check If fuel level is below 25%:
# If the vehicle type is "car" -> print "Refuel soon at a petrol station."
# If vehicle is "bike" -> print "Refuel at nearest pump."
# Else -> print "Check vehicle type."


# fuel_level = int(input('Enter Your current Fuel level:'))
# vtype = input("Enter Your vehicle Type:")
# if fuel_level < 25:
#     if vtype.lower() == 'car':
#         print('Refuel soon at a petrol station.')
#     elif vtype.lower() == 'bike':
#         print('Refuel at nearest pump.')
#     else:
#         print('Check Vehicle Type')
# else:
#     print('good to go')


# Refuel soon at a petrol station.
# Scholarship Eligibility If student's grade is above 85:
# If income is below 3 lakhs -> eligible for full scholarship.
# If income is between 3-6 lakhs -> eligible for half scholarship.
# Else -> no scholarship.


# grade = int(input('Enter grade:'))
# income = int(input('Enter income:'))
# if grade>85:
#     if income <300000:
#         print('eligible for full scholarship.')
#     elif 300000 <= income <=600000:
#         print('eligible for half scholarship.')
#     else:
#         print('Not eligible')
# else:
#     print('no scholarship')


# eligible for half scholarship.
# Shopping Cart Offer If total cart value is over Rs1000:
# If payment method is "card" -> 10% off
# If payment method is "UPI" -> 15% off
# Else -> no discount


# cartv = int(input("Enter Your Total Cart Value:"))
# meth = input("Enter 'Card' or 'upi':")
# if cartv > 1000:
#     if meth.lower() == 'card':
#         cartv *= 0.90
#         print(f"Present Cart value with 15% discount: {cartv}")
#     elif meth.lower() == 'upi':
#         cartv *= 0.85
#         print(f"Present Cart value with 5% discount: {cartv}")
#     else:
#         print(f"Present Cart value without any discount: {cartv}")
# else:
#     print(f"Present Cart value without any discount {cartv}")


# Present Cart value with 15% discount: 900.9
# Restaurant Entry Check If age >= 18:
# If vaccinated -> "Allowed to dine in"
# If not vaccinated -> "Takeaway only" Else:
# "You must be at least 18 to dine here."


# age = int(input('Enter your age:'))
# vac = input('Are you vaccinated say (yes/no):')
# if age >= 18:
#     if vac.lower() == 'yes':
#         print("Allowed to dine in")
#     elif vac.lower() == 'no':
#         print("Takeaway only")
#     else:
#         print("Invalid input for vaccination status.")
# else:
#     print('You must be at least 18 to dine here.')


# Sports Tryouts If player age is between 14 and 18:
# If height > 160cm -> eligible
# Else -> not eligible (too short) Else -> not eligible (age out of range)


# age = int(input('Enter your age:'))
# height = int(input('Enter your height:'))
# if 14 <= age <= 18:
#     if height >160:
#         print('Eligible')
#     else:
#         print('Too short you are not eligible')
# else:
#     print('age out of range')
# Eligible


# PART B: TERNARY OPERATOR PROBLEMS

# Traffic Light If light color is "green" -> print "Go" Else -> print "Stop"

# light = input('Enter the color of the light:')
# print('go' if light.lower() == 'green' else 'stop' )

# go
# Movie Ticket Based on Age If age >= 18 -> "Adult Ticket" Else -> "Child Ticket"

# age = int(input("Enter your age:"))
# print('Adult Ticket' if age>18 else 'Child Ticket')

# Child Ticket
# Discount Offer If amount spent >= Rs500 -> "You get a free gift!"
# Else -> "No gift"

# spent = int(input('enter amount spend:'))
# print('You get a free gift' if spent >= 5000 else 'No gift')

# No gift
# Delivery Fee If location is "local" -> Rs20 delivery fee Else -> Rs50 delivery fee

# loc = input('Enter location:')
# print('Rs 20 delivery fee' if loc.lower() == 'local' else 'Rs 50 delivery fee')

# Rs 20 delivery fee
# Fever Check If temperature >= 100 -> "High Fever" Else -> "Normal"

# temp = int(input('Enter yout body temperature:'))
# print('High Fever' if temp >=100 else "Normal" )

# Normal
# Time-Based Greeting (Nested Ternary) Based on hour of day (24-hour format):
# < 12 -> "Good Morning"
# < 17 -> "Good Afternoon"
# Else -> "Good Evening"

# hour = int(input('Enter time right now:'))
# print('Good Morning' if hour<12 else 'Good Afternoon'if hour <17 else'Good Evening')
# Good Evening

# Bonus Challenge: Electricity Bill Calculator If units < 100 -> free If units between 100-300:

# If usage is residential -> Rs5 per unit
# Else (commercial) -> Rs8 per unit If units > 300:
# Rs10 per unit flat

# units = int(input('Enter Units:'))
# usage = input('Residential or commercial:')
# if units < 100:
#     print('Free')
# elif 100 <= units <= 300:
#     if usage.lower() == 'residential':
#         bill = units * 5
#     else:
#         bill = units * 8
#     print(f'Your bill is Rs {bill}')
# else:  # units > 300
#     bill = units * 10
#     print(f'Your bill is Rs {bill}')
# Your bill is Rs 500