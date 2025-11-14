# core modules
import datetime
from datetime import date
import time
from time import time
# today = datetime.date.today()
# print(today)
today = date.today()
current_time = time()
# print(today)
# print(f'Time is: ', current_time)

# pip modules
import camelcase

camel = camelcase.CamelCase()
text = 'hello pabitra kumar biswas. welcome to python programming.'

print(camel.hump(text))

#Custom modules
import validator
from validator import validate_email

email = 'pabitra.pust@gmail.com'
# if validator.validate_email(email):
if validate_email(email):
    print('Email is valid')
else:
    print('Not an Email.')