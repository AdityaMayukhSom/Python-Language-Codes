# scope = The region that a variable is recognized
# A variable iis only available from inside the region it is created.
# A global and locally scoped versions of a variable can be created.

name = 'Debosmita Paul'  # Global Scope , available inside and outside function
print(name)


def displayName():
    # Local scope, available only inside function
    name = 'Aditya Mayukh Som'
    print(name)


displayName()
print(name)

# Python follows LEGB principle
# L = Local
# E = Enclosing
# G = Global
# B = Built-In
