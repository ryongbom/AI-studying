# A Simple Dictionary
## {} it is dictionary and [] it is list
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Accessing Values in a Dictionary
alien_0 = {'color': 'green'}
print(alien_0['color'])

# Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}")

# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)

# get method
alien_0 = {'color': 'green', 'speed': 'slow'}
## error!
## point_value = alien_0['points']  # KeyError!
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# Looping Through All Key-Value Pairs
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

# Looping Through All the Keys in a Dictionary
for name in favorite_language.keys():
    print(name.title())
    
# Looping Through a Dictionary’s Keys in a Particular Order
for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you!")

# Looping Through All Values in a Dictionary
for language in favorite_language.values():
    print(language.title())
    
# set()
for language in set(favorite_language.values()):
    print(language.title())
    
# A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
# A more realistic example would involve more than three aliens with
# code that automatically generates each alien. In the following example, we
# use range() to create a ﬂeet of 30 aliens
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
print(f"Total aliens: {len(aliens)}")

for alien in aliens[:5]:
    print(alien)
    
# A List in a Dictionary
## information pizza
pizza = {
    'crust': 'thick', 
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza.")
for topping in pizza['toppings']:
    print(f"\t{topping}")
    
# A Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")