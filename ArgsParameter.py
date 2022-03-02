# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

# Tuples are iterable
# Tuples are immutable
# Lists are mutable

# To change any given parameter, we need to cast the tuple into a list

def add(*numbers):
    numbers = list(numbers)  # cast tuple into a list
    numbers[0] = 55  # now mutate the list
    sum = 0
    for i in numbers:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))
