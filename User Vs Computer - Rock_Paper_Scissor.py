import random

option = ['rock','paper','scissor']

game_num = int(input('Number of Games to be Played : '))

def rules():

    
        if user_choice == 'rock' and system_choice == 'rock':
            print('Rock Hits Rock! its a Tie !!!')
        elif user_choice == 'paper' and system_choice == 'rock':
            print('Paper Captures Rock! You have Won!!')
        elif user_choice == 'scissor' and system_choice == 'rock':
            print('Rock Broke the Scissor! Computer has Won!!, Better Luck Next Time !!')
        elif user_choice == 'rock' and system_choice == 'paper':
            print('Paper Captures Rock! Computer has Won!!, Better Luck Next Time !!')
        elif user_choice == 'paper' and system_choice == 'paper':
            print('Paper and Paper !! its a Tie!!')
        elif user_choice == 'scissor' and system_choice == 'paper':
            print('Scissor Cuts Paper! , You Have Won !!!') 
        elif user_choice == 'rock' and system_choice == 'scissor':
            print('Rock Broke the Scissor! , You Have Won !!!')
        elif user_choice == 'paper' and system_choice == 'scissor':
            print('Scissor Cuts Paper!, Computer has Won!!, Better Luck Next Time !!')
        elif user_choice == 'scissor' and system_choice == 'scissor':
            print('Scissor Fights with Scissor!,  its a Tie')
        else:
            print('Wrong or Invalid Input from User !!!')

for i in range(game_num):
    user_choice = input().lower()
    system_choice = random.choice(option)
    print(f'\nUser Choice : {user_choice}')
    print(f'\nSystem Choice : {system_choice}\n')
    rules()
