import random
choices = ['rock', 'paper', 'scissor']
computer = None  # Initially declare the variable computer
player = None  # Initially declare the variable player
playerScore, computerScore = 0, 0
winningScore = 5  # Score required to win this game


def compare(player, computer):
    if((player == 'scissor' and computer == 'paper') or (player == 'paper' and computer == 'rock') or (player == 'rock' and computer == 'scissor')):
        return player
    else:
        return computer


# Game Logic
# The game continues until any one of the player has score equal to winning score, thus we are using 'and'
while ((playerScore < winningScore) and (computerScore < winningScore)):
    while player not in choices:
        computer = random.choice(choices)
        player = input('rock, paper or scissors? : ').lower()
        print('Computer : ' + computer)
        print('Player : ' + player)
    if(player == computer):
        print('It was a tie, continue playing!')
    else:
        winner = compare(player, computer)  # Calling the compare() function
        if(winner == player):
            print('Player Got 1 point.')
            playerScore += 1  # Increament Player Score By 1
        else:
            print('Computer Got 1 point.')
            computerScore += 1  # Increament Computer Score By 1

        print(
            f'Current Score Board Is Player : {str(playerScore)} , Computer : {str(computerScore)}.')
    player = None  # Changing player choice to None, so that player continues to be 'not in choices'

if(playerScore == winningScore):
    print('Player Wins The Game')
else:
    print('Computer Wins The Game')
