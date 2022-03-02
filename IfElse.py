# if statement = a block of code that will execute if it's condition is true

age = int(input("How old are you?: "))
if (age < 18):
    print("You underaged shit!")
elif(age < 60):
    print("you are fucking adult!")
elif (age == 100):
    print("you are a century old")
else:
    print("Man! you are very old!")
