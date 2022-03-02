import csv

path = 'D:\\Coding\\Python Development\\OOP\\Computer.csv'


class Item:

    # Everytime an instance is created, python calls these dunder method __init__ this if we pass an print statement like print('I am created'), it will be printed as many time as the method is called.

    # Class Attributes

    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    # Instance Attributes

    # __init__ method is called as soon as any instance of a class is created
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to received arguments otherwise print statement written beside the assert statement
        assert price >= 0, f'Price {price} is less than zero!'
        assert quantity >= 0, f'Quantity {quantity} is less than zero!'

        # Assigns arguments to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute when an instance is created
        Item.all.append(self)

    def __str__(self):
        information = f'name = {self.name} , price = {self.price} , quantity = {self.quantity}'
        return information

    def calculate_total_price(self):
        # It creates another property for our object
        self.total_price = self.price*self.quantity
        return self.total_price

    def apply_discount(self):
        # This changes the actual price of the price property
        # self.price = self.price * self.pay_rate

        # This doesn't change the price, only sends back the price after discount
        return self.price*self.pay_rate

    '''
    This should also do something that has a relationship with the class, but usually, those are used to manipulatte different structures of data to instantiate objects, like we have done with CSV.
    '''

    @classmethod
    def instanciate_from_csv(cls):
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # you can not start csv file headings with blank space
            # ' heading' will cause error
            # 'heading' is the correct format
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    '''
    This should do something that has a relationship with class, but not something that must be unique per instance!
    '''
    @staticmethod
    def is_integer(num):
        # We will count out floats that are point zero
        # For i.e: 5.0,10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


print()

# Item1 = Item('phone', 100, 5)
# Item2 = Item('laptop', 500, 3)

# print(Item.__dict__)  # All the attributes for class level
# print(Item1.__dict__)  # All the attributes for instance level
# print(Item2.__dict__)  # All the attributes for instance level

# print(Item1.apply_discount())
# print(Item2.apply_discount())

# print(Item1.calculate_total_price())
# print(Item2.calculate_total_price())

# print(Item1.__dict__)  # All the attributes for instance level
# print(Item2.__dict__)  # All the attributes for instance level

# CSV = Comma Seperated Values

Item.instanciate_from_csv()

for i in Item.all:
    print(i)
