#classes are basically used for creating object
#create class
class user:
    #constructor or initializer
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # def gretting(self):
    #     return f'My name is {self.name} and I am {self.age} years old.'
    
#     def birthday(self):
#         self.age += 5
    
# # init user
# pabitra = user('Pabitra Kumar Biswas', 'pabitra.pust@gmail.com', 25)
# pulak = user('Pulak Kumar Biswas', 'pulak@gmail.com', 35)

# pabitra.age = 30

# print(pabitra.name)
# print(pabitra.email)
# print(pabitra.age)

# print(f'{pulak.name}, {pulak.email}')

# pulak.birthday()

# #call Method
# print(pulak.gretting())

class customer(user):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance =0
    
    def set_balance(self, balance):
        self.balance = balance

    def gretting(self):
        return f'My name is {self.name} and I am {self.age} years old. I owe '

# init customer
porom = customer('Porom Biswas', 'porom.mail.com', '10')

porom.set_balance(1000)

print(porom.name)
print(f'I am {porom.name} and i am {porom.age} and i owe of a {porom.balance} and my email is {porom.email}')