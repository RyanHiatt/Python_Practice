# String Concatenation
names = ['Jeff', 'Gary', 'Jill', 'Samantha']

# Method 1 and 2
#for name in names:
#    print('Hello there, ' + name)
#    print(' '.join(['Hello there,', name]))

# Method 3 "Correct Method"
#print(', '.join(names))

# Method 4
# This method reads a file from the os and prints it
'''
import os

location_of_files = 'D:\\Programming\\Python\\Files'
file_name = 'String Concatenation and Formatting Test File.txt'

print(location_of_files + '\\' + file_name)

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())
'''


# String Formatting Example
# Gary bought 12 apples today!
who = 'Gary'
how_many = 12

# Method 1
print(who, 'bought', how_many, 'apples today!')

# Method 2 "Correct Method"
print('{} bought {} apples today!'.format(who, how_many))
