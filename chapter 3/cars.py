cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)

# sorting list temporarily with the sorted

print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars)) 
print("\nHere is the original list again:")
print(cars)

# printing lists in reverse order

print(cars)
cars.reverse()
print(cars)

# finding length of lists

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))