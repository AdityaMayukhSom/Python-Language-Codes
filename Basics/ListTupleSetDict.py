# # list is used to store multiple items in a single variable

# food = ['pizza', 'hamburger', 'hotdog', 'spaghetti', 'biriyani']
# # food.remove('pizza')
# # food.clear()
# food.append('ice cream')
# food.insert(3, 'cake')
# food.sort()


# value = food.pop()
# print(value)
# print()


# # printing a list

# # method 1
# for i in range(len(food)):
#     print(food[i])

# print()

# # method 2
# for i in food:
#     print(i)


# # tuple = collection which is ordered and unchangable
# #         Used to group together related data

# student = ('bro', 21, 'male')

# print(student.count('bro'))  # Counts number of time 'Bro' appears in list
# print(student.index('male'))  # Returns the index of given input

# for x in student:
#     print(x)

# if 'bro' in student:  # checks if given input is in the tuple or not
#     print('Bro is here!')


# set is a collection which is unordered, unindexed. No duplicate values.
# set is faster than list but has no indexing
# repeatation won't happen in sets

utensils = {'fork', 'spoon', 'knife', 'knife', 'knife'}
for x in utensils:
    print(x)


# dictionaries

capitals = {
    'USA': 'Washington DC',
    'India': 'New Delhi',
    'England': 'London',
    'Australia': 'Canberra',
    'China': 'Beijing',
    'Russia': 'Moscow',
    'Ukraine': 'Kyiv',
}


# print(capitals['Germany']) # Gives error is key is not present
print(capitals['England'])
print(capitals.get('England'))  # Returns none if Key is not present
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'New York'})
capitals.pop('China')
for key, value in capitals.items():
    print(key, value)
capitals.clear()
# dictionaries are mutable
