# str.format() = optional method that gives users more control
#                when displaying output


# Hey Diddle Diddle
# Hey, diddle, diddle, the cat and the fiddle
# The cow jumped over the moon
# The little dog laughed to see such fun
# And the dish ran away with the spoon
# Hey, diddle, diddle, the cat and the fiddle
# The cow jumped over the moon
# The little dog laughed to see such fun
# And the dish ran away with the spoon
# Hey, diddle, diddle, the cat and the fiddle
# The cow jumped over the moon
# The little dog laughed to see such fun
# And the dish ran away with the spoon


animal = 'cow'
item = 'moon'

print(f'The {animal} jumped over the {item}')
print('The {} jumped over the {}'.format(animal, item))
