#open a file
my_file = open('my_file.txt', 'w')


#get some info
print('Name: ', my_file.name)
print('Is_closed: ', my_file.closed)
print('Opening_mode: ', my_file.mode)

#write to file
my_file.write('I love you Darling...')
my_file.write(' and i also Love my Bangladesh.')
my_file.close()

# append to file 
my_file = open('my_file.txt', 'a')
my_file.write('I also love Premalu')
my_file.close()


# read from file 
my_file = open('my_file.txt', 'r+')
text = my_file.read(1000)
print(text)