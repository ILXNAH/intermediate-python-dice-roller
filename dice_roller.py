#!/usr/bin/env python3
import random
player1_name = input('Who is rolling dice today? ')
def yesorno(question):
    prompt = f'{question}? (y/n): '
    ans = input(prompt).strip().lower()
    if ans not in ['y', 'n']:
        print('Invalid input, try again')
        return yesorno(question)
    if ans == 'y':
        return True
    else:
        return False
player2_var = yesorno("Anybody else rollin'")
if player2_var == True:
    player2_name = input('Who?')
def dice_size_function():
    prompt = 'How many sides are the dice? '
    ans = input(prompt).strip()
    try:
        type(ans) == int
        if int(ans) > 0:
            return int(ans)
        elif int(ans) < 0:
            print('Invalid input, try again')
            return dice_size_function()
    except ValueError:
        print('Invalid input, try again')
        return dice_size_function()
    except AttributeError:
        print('Invalid input, try again')
        return dice_size_function()
dice_rolls = int(input('How many dice would you like to roll? '))
dice_size = dice_size_function()
dice_sum_p1 = 0
def player1_rolls():
    for i in range(0, dice_rolls):
        player1_roll = random.randint(1, dice_size)
        global dice_sum_p1
        dice_sum_p1 += player1_roll
        if player1_roll == 1:
            print(f'{player1_name} rolled a {player1_roll}! Critical Fail!')
        elif player1_roll == dice_size:
            print(f'{player1_name} rolled a {player1_roll}! Critical Success!')
        else:
            print(f'{player1_name} rolled a {player1_roll}')
dice_sum_p2 = 0
def player2_rolls():
    for i in range(0, dice_rolls):
        player2_roll = random.randint(1, dice_size)
        global dice_sum_p2 
        dice_sum_p2 += player2_roll
        if player2_roll == 1:
            print(f'{player2_name} rolled a {player2_roll}! Critical Fail!')
        elif player2_roll == dice_size:
            print(f'{player2_name} rolled a {player2_roll}! Critical Success!')
        else:
            print(f'{player2_name} rolled a {player2_roll}')
player1_rolls()
if player2_var == True:
    player2_rolls()
#to define results for player1 and player2
global player1_result
global player2_result
player1_result = dice_sum_p1
player2_result = dice_sum_p2
#to define comparison function
def compare_results():
    global player1_result
    global player2_result
    if player1_result > player2_result:
        print (f'The WINNER is {player1_name} with the score of {player1_result}, congrats! \U0001F973')
    elif player2_result > player1_result:
        print (f'The WINNER is {player2_name} with the score of {player2_result}, congrats! \U0001F973')
    else:
        print (f"Well, that's a bummer, it's a TIE with {player1_result} each. \U0001F631")
    global rematch
    #rematch option loop
    rematch = yesorno("Do you want a rematch")
    if rematch == True:
        global dice_sum_p1
        dice_sum_p1 = 0
        global dice_sum_p2
        dice_sum_p2 = 0
        player1_rolls()
        player2_rolls()
        player1_result = dice_sum_p1
        player2_result = dice_sum_p2
        compare_results()
#final scores and comparison
if player2_var == True:
    compare_results()
elif player2_var == False and dice_rolls > 1:
    print(f'{player1_name} has rolled a total of {dice_sum_p1}')