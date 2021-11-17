print('\t _______________________________________________________________')
print('\t|                                                               |')
print('\t|       This is a program to play "Rock Paper Scissors".        |')
print('\t|_______________________________________________________________|\n')
import random
user_score, ai_score = 0, 0
j = 0 # number of rounds
n = int(input('\tHow many times do you like to play? \t'))
while j<n:  
    choices = ['r', 'p', 's']
    ai_choice = random.choice(choices)
    choices_dict = {'r' : 'Rock', 'p' : 'Paper', 's' : 'Scissors'}
    user_choice = input('\nEnter r for Rock, s for Scissors, or p for Paper : \t')
    
    try:
        print(f'\n\tYour choice is {choices_dict[user_choice]} and machine\'s choice is {choices_dict[ai_choice]}.')
    except KeyError:
        print('\tInvalid input; Play again!\n')
    else:
        if (user_choice == 'r' and ai_choice == 's') or (user_choice == 'p' and ai_choice == 'r') \
            or (user_choice == 's' and ai_choice == 'p'):
            print('\tYou won!')
            user_score += 1
        elif user_choice == ai_choice:
            print('\tTie')
        else:
            print('\tMachine won!')
            ai_score +=1
        j += 1
        print(f'\t\tyou = {user_score}, machine = {ai_score} ')
        print('____________________________________________________________________')
        
print(f'\n\tAfter {j} rounds, your score is {user_score}, and machine\'s score is {ai_score}.')
score = max(user_score, ai_score)
if user_score > ai_score:
    result = 'You won'
elif user_score < ai_score:
    result = 'Machine won'
else:
    result = 'Tie'
print(f'\n-------------------------{result} with {score} score(s)-------------------------\n')