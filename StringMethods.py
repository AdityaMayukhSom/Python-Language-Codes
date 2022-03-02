name = 'My Name Is Dipta Majhi And I Live In Anantapur'

print("Hello World")
print('We Are Learning Python')
print(name)

# Now we are using string methods

# We are now calculating length of a given string
# There are two ways to do this

# First Way
print(len(name))

# Second Way
print(name.__len__())
# len function is used to calculate length of a string
# len function counts blank spaces as well

# find() method is used to match given string with the original string
print(name.find('ipz'))
# returns index of initial letter if match exists
# if match does not exist , it returns -1

# capitalize() method is used to capitalize only the initial letter of a string
# remember if the string contains space and then again words, it is not going to capitalize first letter of each word
# It also makes all the other words in the string lower case
print(name.capitalize())

# To Make Strings UpperCase use upper()
print(name.upper())

# To Make Strings LowerCase use lower()
print(name.lower())

# count() returns the number of times the passed argument appears in the string
# This count() method is case sensitive, that is count of 'a' and 'A' are different
print(name.count("a"))
print(name.count("A"))

# * prints the string multiple times
# print(name*4)
