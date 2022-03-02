import time  # Importing Time Module


# while loop = a statement will execute it's block of code, as long as it's condition remains true

# name = ''
# while not(name):
#     name = input('Enter your name darling: ')
# print('Hello ' + name)


# for loop = a statement that will execute it's block of code for a limited amount of time

# for i in range(0, 40, 10):
#     print(i)

# print()

# for i in "Dipta":
#     print(i)

# print()

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")
# print()

# Nested Loops

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter A Symbol: ")

# for i in range(rows):
#     for j in range(columns):
#         # the end="" stops the print to get to a new line
#         print(symbol, end="")
#     print()
# print("Expeli\nArmus")

# Loop Control Statements In Python

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing , acts as a placeholder

phNum = "123-456-7890"

for i in phNum:
    if i == '-':
        continue
    print(i, end='')


for i in range(1, 21):
    if i == 13:
        continue
    else:
        print(i)

print()

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)
