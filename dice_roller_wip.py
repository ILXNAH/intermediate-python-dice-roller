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
dice_sum_p1 = 0
def player1_rolls():
    for i in range(0, dice_rolls):
        global player1_roll
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
        global player2_roll
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
def compare_results():
    #to define results for player1 and player2
    if dice_rolls > 1:
        player1_result = dice_sum_p1
        player2_result = dice_sum_p2
    else:
        player1_result = player1_roll
        player2_result = player2_roll
    #to define comparison function
    if player1_result > player2_result:
        print (f'The WINNER is {player1_name} with the score of {dice_sum_p1}, congrats! \U0001F973')
    elif player2_result > player1_result:
        print (f'The WINNER is {player2_name} with the score of {dice_sum_p2}, congrats! \U0001F973')
    else:
        print (f"Well, that's a bummer, it's a TIE with {dice_sum_p1} each. \U0001F631")
    #rematch option
    global rematch_var
    rematch_var = yesorno("Do you want a rematch")
    if rematch_var == True:
        dice_sum_p1 = 0
        dice_sum_p2 = 0
        player1_roll = 0
        player2_roll = 0
        player1_rolls()
        player2_rolls()
        compare_results()
#final scores and comparison
if player2_var == True:
    compare_results()
elif player2_var == False and dice_rolls > 1:
    print(f'{player1_name} has rolled a total of {dice_sum_p1}')