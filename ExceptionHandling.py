# exception = events detected during execution othat interrupt the flow of a program

try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator/denominator
except ZeroDivisionError as e:
    print("You can't divide by zero, idiot")
    print(e)
except ValueError as e:
    print("Enter only numbers please!")
    print(e)
except Exception as e:
    print("Something Went Wrong")
    print(e)
else:
    print(result)
finally:
    print('This will always execute at the end!')
