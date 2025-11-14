# creat function 
# def say_hello(name):
#     print('hello ' + name)

# say_hello('Pabitra Kumar')

def say_hello(name = 'Pabitra Kumar'):
    print('hello ' + name)
"""'say_hello' functions override the name 'Pabitra Kumar'. """
say_hello('Priya Sarker')


# return value 
def get_sum(num1, num2):
    total = num1 + num2
    return total
print(get_sum(13, 7))

num_sum = get_sum(21, 13)
print(num_sum)

def add_one_to_num(number):
    # number = number + 1
    number += 1 #short form
    return number
# print(add_one_to_num(5))
number = 10
new_number = add_one_to_num(number)
print(new_number)

# lambda function
get_sum = lambda num1, num2 : num1 + num2 + num1
print(get_sum(9, 1))
add_five_to_num = lambda num : num + 5
print(add_one_to_num(15))