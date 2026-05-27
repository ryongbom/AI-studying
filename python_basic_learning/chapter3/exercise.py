# 3-10. Every Function: Think of things you could store in a list. For example, you
# could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items and
# then uses each function introduced in this chapter at least once.
numbers = [1, 4, 5, 6, 7, 3, 11]
print(numbers)

print("Here is sorting list:")
print(sorted(numbers))

print("\nHere is original list:")
print(numbers)

cities = ['hamhung', 'choljin', 'Pyongyang', 'sinchon', 'haju']
cities.append('Sariwon')
print(cities)

cities.insert(1, 'wonsan')
print(cities)

del cities[5]
print(cities)

print(cities.pop(-3))
print(cities)

print(len(cities))