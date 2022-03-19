# position, name, age, level, salary
se1 = ['Software Engineer', 'Max', 20, 'Junior', 5000]
se2 = ['Software Engineer', 'Lisa', 25, 'Senior', 7000]
d1 = ['Designer', 'Philipp']


# Class

# Dunded methods are names that are preceded and succeeded by double underscores, hence the name dunder. They are also called magic methods and can help override functionality for built-in functions for custom classes
# Implementing dunder methods for classes is a good form of Polymorphism.

# Dunder Methods

# init
# str
# setitem
# getitem
# delitem
# len
# contains
# iadd
# call

# __add__  for addition(+)
# __sub__ for subtraction(-)
# __mul__ for multiplication(*)
# __truediv__ for division(/)
# __eq__ for equality (==)
# __lt__ for less than(<)
# __gt__ for greater than(>)
# __le__ for less than or equal to (≤)
# __ge__ for greater than or equal to (≥)


class SoftwareEngineer:
    # Class Attributes
    alias = 'Keyboard Magician'

    # The init method is used to create instance of a class

    def __init__(self, name, age, level, salary):
        # Instance Attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # Instance Method
    def code(self):
        print(f'{self.name} is writing code...')

    def codeInLang(self, language):
        print(f'{self.name} is writing code in {language}...')

    def __str__(self):
        information = f'name = {self.name} , age = {self.age} , level = {self.level}'
        return information

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age and self.level == other.level and self.salary == other.salary:
            return True
        else:
            return False


print()

# Instance Of The Calss
se1 = SoftwareEngineer('Max', 20, 'Junior', 5000)
se2 = SoftwareEngineer('Lisa', 25, 'Senior', 7000)
se3 = SoftwareEngineer('Lisa', 25, 'Senior', 7000)
print(se1.name, se1.age, se1.level, se1.salary)
print(se2.name, se2.age, se2.level, se2.salary)
print(SoftwareEngineer.alias)


se1.code()
se2.code()
se1.codeInLang('JavaScript')
se2.codeInLang('GoLang')
print(se1)  # Uses __str__ method by default
print(se2)  # Uses __str__ method by default
print(se2 == se3)  # Generally It Compares Memory Address But As We Have Manupulated Default Behaviour Of Double Equal To For This Class, It Returns True

print()
