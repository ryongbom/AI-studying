# creation list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[2])

# Index Positions Start at 0, Not 1
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])

# Using Individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Appending Elements to the End of a List
motorcycles.append('royal')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserting Elements into a List
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing an Item Using the del Statement
del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method
popped = motorcycles.pop()
print(motorcycles)
print(popped)

# Popping Items from Any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
first = motorcycles.pop(0)
print(first)
print(motorcycles)

# Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

to_expensive = 'ducati'
motorcycles.remove(to_expensive)
print(motorcycles)
print(f"\nA {to_expensive.title()} is too expensive for me.")

# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list:")
print(cars)

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()
print(cars)

# Finding the Length of a List
print(len(cars))

# index error
# empty = []
# print(empty[-1])

