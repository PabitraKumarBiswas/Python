name = 'Pabitra Kumar Biswas'

age = 30

# concatenate

print('Hello World')
print('Hello ' + name + '. Welcome to python world. You are ' + str(age) + ' years old.')

# arguments by position
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}, {3}'.format('a', 'b', 'p', 'k'))

# Arguments by name
print('My name is {name} and i am {age}'. format(name = name, age = age))

# F string 
print(f'My name is {name} and i am {age}')

# Sting method 
p = 'hi, welcome to Python world!'
name = "pabitre   kumar biswas"

# capitalize first letter
print(p.capitalize())
# capatalize all letter
print(p.upper())

# lower case all letter
print(p.lower())

# swap case 
print(p.swapcase())

# length
print(len(name))

# replace
print(p.replace('Python', 'Programming'))

# count
count = 'pabitra'
print(name.count(count))