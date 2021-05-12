import random
player1_name = input('Who is rolling dice today?')
def yesorno(question):
    prompt = f'{question}? (y/n): '
    ans = input(prompt).strip().lower()
    if ans not in ['y', 'n']:
        print("Invalid input, try again")
        return yesorno(question)
    if ans == 'y':
        return True
    else:
        return False
player2_var = yesorno("Anybody else rollin'")
if player2_var == True:
    player2_name = input('Who?')
dice_rolls = int(input('How many dice would you like to roll? '))
dice_size = int(input('How many sides are the dice? '))
def rolling1():
    dice_sum = 0
    for i in range(0, dice_rolls):
        player1_roll = random.randint(1, dice_size)
        dice_sum += player1_roll
        if player1_roll == 1:
            print(f'{player1_name} rolled a {player1_roll}! Critical Fail')
        elif player1_roll == dice_size:
            print(f'{player1_name} rolled a {player1_roll}! Critical Success!')
        else:
            print(f'{player1_name} rolled a {player1_roll}')
    if dice_rolls > 1:    
        print(f'{player1_name} has rolled a total of {dice_sum}')
def rolling2():
    dice_sum = 0
    for i in range(0, dice_rolls):
        player2_roll = random.randint(1, dice_size)
        dice_sum += player2_roll
        if player2_roll == 1:
            print(f'{player2_name} rolled a {player2_roll}! Critical Fail')
        elif player2_roll == dice_size:
            print(f'{player2_name} rolled a {player2_roll}! Critical Success!')
        else:
            print(f'{player2_name} rolled a {player2_roll}')
    if dice_rolls > 1:    
        print(f'{player2_name} has rolled a total of {dice_sum}')
rolling1()
if player2_var == True:
    rolling2()