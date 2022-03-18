import itertools
from random import getstate

nums = [1, 2, 3, 4]
data = [100, 200, 300, 400]
letters = ['a', 'b', 'c', 'd']
names = ['Ankana', 'Reetama', 'Rima', 'Debasmita']
people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]


# we can loop over tuples, dictionaries, files, generator, strings
# Iterators remember where the last time iteration was stopped

# combined = nums + data + letters + names

def get_state(person):
    return person['state']


person_group = itertools.groupby(people, get_state)
for key, group in person_group:
    print(key)
    for person in group:
        print(person)
    print()


'''

combined = itertools.chain(nums, data, letters, names)
for i in combined:
    print(i)

'''

'''

result = itertools.combinations(letters, 2)
for item in result:
    print(item)

print('Blank Line OP!')

result = itertools.permutations(letters, 2)
for item in result:
    print(item)

print('Blank Line OP!')

result = itertools.product(letters, repeat=2)
for item in result:
    print(item)

'''

'''

for num in nums:
    print(num)

print(dir(nums))

'''
'''

counter = itertools.count(start=10, step=-1)
daily_data1 = list(zip(counter, data))
daily_data2 = list(itertools.zip_longest(range(10), data))
print(daily_data1)
print(daily_data2)

'''
'''

booleanVar = ['On', 'Off']
counter = itertools.cycle(booleanVar)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

'''
'''
counter = itertools.repeat('2002', times=3)
# for i in counter:
#     print(i)

print(counter.__next__())

squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))
'''
