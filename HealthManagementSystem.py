# Health Management System

import os

path = 'D:\\Coding\\Python Development\\Health.txt'


def setText(message):
    with open(path, 'a') as file:
        file.write(message)


def getInput(name):
    print(f'You are entering data for {name}...')
    exercise = input(f'What exercise does {name} do? : ')
    food = input(f'What food does {name} eat? : ')
    age = input(f'How old {name} is? : ')
    message = f'\n{name} does {exercise},\n{name} eats {food},\n{name} is {age} years old...'
    setText(message)


getInput('Aditya')
getInput('Dipta')
getInput('Aashmita')
