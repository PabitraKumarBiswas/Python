f_tuple = ('apple', 'orange', 'raspberrypi', 'Banana', 'Mango') 
print(type(f_tuple))
print(f_tuple)

# constuctor
fruit_t = tuple(('Mango', 'Banana', 'Apple'))
print(type(fruit_t))
print(fruit_t)

# single value 
print(fruit_t[0])

# tuple is constant and can not changable
# fruit_t[0] = 'Raspberry'

# print(fruit_t)

# Tuples with one value should have trailling comma
# fruit_t2 = ('apple',)
# # delete
# del fruit_t2
# print(type(tuple))
# print(fruit_t2)
# print(len(fruit_t2))

# create set 

fruit = {'apple', 'Mango', 'banana', 'mango'}
print(type(fruit))
print(fruit)

# check on set 
print('Mangos' in fruit)

# add in set
fruit.add('raspberry')

print(fruit)

# remove from set 
fruit.remove('apple') 

# clear set 
fruit.clear()

# delete
del fruit
print(fruit)
