name = input("Please enter the string to check: ")
lenght = len(name)
flag = 0

for i in range(0, lenght):
    if name[i] != name[lenght-1-i]:
        flag = 1
        break
    else:
        continue
if flag != 0:
    print("String is not paindrome!")
else:
    print("String is palindrome!")
