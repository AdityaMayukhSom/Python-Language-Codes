T = list()
temp = int()

n = int(input("Enter number of elements: "))

for i in range(0, n):
    T.append(int(input(f"Enter {i} element: ")))

print("Your Given Array Is : ", end=" ")
for i in range(0, n):
    print(T[i], end=" ")

print()  # To print a blank line

# Swapping The Array

for i in range(0, int(n/2)):
    # n-i-1 should be the intex because for i = 0, it corresponds to index n-1 and not n
    T[n-1-i] = T[i]-T[n-1-i]
    T[i] = T[i]-T[n-1-i]
    T[n-1-i] = T[i]+T[n-1-i]

print("Your Array After Swapping Is : ", end=" ")
for i in range(0, n):
    print(T[i], end=" ")
