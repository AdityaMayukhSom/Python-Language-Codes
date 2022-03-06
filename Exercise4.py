'''
Pattern Printing
Input = any integer n
Boolean = True or False
if n == 4 and Boolean == True
*
**
***
if Boolean == False
***
**
*
'''

i = int()
j = int()
n = int(input('Please enter number of lines to print: '))
while True:
    boolean = input(
        'Please enter T for increasing triangle F for decreasing triangle: ')
    if boolean.upper() == 'T':
        boolean = True
        break
    elif boolean.upper() == 'F':
        boolean = False
        break
    else:
        continue


# Using While Loop
'''
if boolean:
    for i in range(1, n+1):
        j = 0
        while j != i:
            print('*', end='')
            j = j+1
        print()
else:
    for i in range(1, n+1):
        j = n+1-i
        while j != 0:
            print('*', end='')
            j = j-1
        print()
'''

# Using For Loop

if boolean:
    for i in range(1, n+1):
        for j in range(0, i):
            print('*', end='')
        print()
else:
    for i in range(1, n+1):
        for j in range(n+1-i, 0, -1):
            print('*', end='')
        print()
