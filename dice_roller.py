import random
player_name = input('Who is rolling dice today?')
dice_rolls = int(input('How many dice would you like to roll? '))
dice_size = int(input('How many sides are the dice? '))
dice_sum = 0
for i in range(0, dice_rolls):
    roll = random.randint(1, dice_size)
    dice_sum += roll
    if roll == 1:
        print(f'{player_name} rolled a {roll}! Critical Fail')
    elif roll == dice_size:
        print(f'{player_name} rolled a {roll}! Critical Success!')
    else:
          print(f'{player_name} rolled a {roll}')
if dice_rolls > 1:    
    print(f'{player_name} has rolled a total of {dice_sum}')