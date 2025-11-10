# create list 
nums = [1, 3, 4, 6, 5]

print(type(nums))
print(nums)

# using construtor
nums = list((1, 2, 4, 5, 6))
print(nums)
print(type(nums))

fruits = ['Apple', 'Orange', 'Raspberrypi', 'Banana']
print(type(fruits))
print(fruits)

# get Value
print(fruits[2])
print(len(fruits))

# append
fruits.append ('Mango')

print(fruits)

# REMOVE
fruits.remove('Banana')
print(fruits)

# insert
fruits.insert(3, 'Strawberry')
print(fruits)

# remove the position
fruits.pop(0)
print(fruits)

# Reverse 
fruits.reverse()
print(fruits)

# sort 
fruits.sort()
print(fruits)

# reverse sort 
fruits.sort(reverse=True)

print(fruits)