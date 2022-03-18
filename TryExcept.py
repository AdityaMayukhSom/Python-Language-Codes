from logging import exception


try:
    num1 = int(input("Enter Num 1: "))
    num2 = int(input("Enter num 2: "))
    print(f'The sum of these two number is {num1+num2}')
except Exception as e:
    print(e)

print('This line is very important')
