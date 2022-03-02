import random

x = random.randint(1, 6)
print(x)
y = random.random()
print(y)

myList = ['Rock', 'Paper', 'Scissors']
z = random.choice(myList)
print(z)

cards = []
for i in range(1, 14):
    if(i < 10):
        cards.append(i)
    elif(i == 10):
        cards.append('J')
    elif(i == 11):
        cards.append('Q')
    elif(i == 12):
        cards.append('K')
    else:
        cards.append('A')
print(cards)
random.shuffle(cards)
print(cards)
