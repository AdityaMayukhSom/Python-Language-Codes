# function is a block of code which is executed only when it is called
# return statement = Function sends Python values/objects back to the caller.
# These values/objects are known as the function's return value

myList = ['Aditya', 'Dipta', 'Debosmita', 'Rima']


def hello(name):
    print(f'Hello {name}!')
    print('Have a nice day!')


for i in range(4):
    print(i)
    hello(myList[i])
