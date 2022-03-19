num = int(input('Enter Number: '))
reverse = 0

while num != 0:
    temp = num % 10
    reverse = ((reverse*10) + temp)
    # Here num/10 will produce a float value so we have to typecast it to integer
    num = int(num/10)

print(f'Reversed Number: {reverse}')
