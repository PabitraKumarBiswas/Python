# dictionary
person = {
    'first_name': 'Pabitra',
    'middle_name': 'Kumar',
    'last_name': 'Biswas',
    'age': 26
}

print(person)
print(type(person))

# access value 
print(person['middle_name'])
print(person.get('first_name'))

# add value 
person['phone_num'] = '017xx-xxxxxx'

print(person)


# get keys 
print(person.keys())

# get values 
print(person.items())

# make copy 
person_2 = person.copy()
person_2['city'] = 'Rajshahi'
print(person_2)



# delete 
del(person_2['age'])
person_2.pop('last_name')
print(person_2)

# clear
person_2.clear()

print(person_2)





# using constructor
person_1 = dict(first_name = 'Pabitra', last_name= 'Kumar', age = 26)
print(type(person_1))
print(person_1)

# list of dictionaries
group = [
    {'name' : "Pabitra", 'age' :23}, 
    {'name' : "nitu", 'age': 22}
]
print(group)
print(type(group))
print(group[1]['name'])