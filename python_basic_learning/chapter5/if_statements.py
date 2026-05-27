# simple example
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# combinations
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

# and, or
age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)

#in, not in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

banned_users = ['andrew', 'caroline', 'david']
user = 'marie'
print(user not in banned_users)

#if statement
age = 19
if age >= 18:
    print("You are old enough to vote!")

age = 17
if age >= 18:
    print("You can vote!")
else:
    print("Sorry, you are too young to vote.")
    
#if-elif-else
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
    
print(f"Your cost is ${price}.")

# Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    
# Checking for Special Items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, out of green peppers.")
    else:
        print(f"Adding {requested_topping}.")
        
# Checking That a List Is Not Empty
requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}")
else:
    print("Are you sure you want a plain pizza?")
    
# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested in requested_toppings:
    if requested in available_toppings:
        print(f"Adding {requested}.")
    else:
        print(f"Sorry, we don't have {requested}.")