import random

option = ['rock','paper','scissor']

game_num = int(input('Number of Games to be Played : '))

def rules():

    
        if Computer_1 == 'rock' and Computer_2 == 'rock':
            print('Rock Hits Rock! its a Tie !!!')
        elif Computer_1 == 'paper' and Computer_2 == 'rock':
            print('Paper Captures Rock! Computer - 1 have Won!!')
        elif Computer_1 == 'scissor' and Computer_2 == 'rock':
            print('Rock Broke the Scissor! Computer - 2 has Won!!')
        elif Computer_1 == 'rock' and Computer_2 == 'paper':
            print('Paper Captures Rock! Computer - 2 has Won!!')
        elif Computer_1 == 'paper' and Computer_2 == 'paper':
            print('Paper and Paper !! its a Tie!!')
        elif Computer_1 == 'scissor' and Computer_2 == 'paper':
            print('Scissor Cuts Paper! , Computer - 1 Have Won !!!') 
        elif Computer_1 == 'rock' and Computer_2 == 'scissor':
            print('Rock Broke the Scissor! , Computer - 1 Have Won !!!')
        elif Computer_1 == 'paper' and Computer_2 == 'scissor':
            print('Scissor Cuts Paper!, Computer - 2 has Won!!')
        elif Computer_1 == 'scissor' and Computer_2 == 'scissor':
            print('Scissor Fights with Scissor!,  its a Tie')
        else:
            print('Wrong or Invalid Input from User !!!')

for i in range(game_num):
    Computer_1 = random.choice(option)
    Computer_2 = random.choice(option)
    print(f'\nComputer - 1  : {Computer_1}')
    print(f'\nComputer - 2  : {Computer_2}\n')
    rules()
