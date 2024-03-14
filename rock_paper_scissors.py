import random #Provides functions that perform random operations.

def play(): 
    user = input("Whats your choice? \n 'r' for rock, 'p' for paper, 's' for scissors \n") #propmt the user to inout their choice 
    computer = random.choice(['r', 'p', 's']) #used to ramdomly select the computer's choice
    
    if user == computer:
        return 'It\'s a tie'
    if is_win(user, computer): #if it is not tie, the is_win function will be called 
        return f'You won! The computer choice was {computer}'

    return f'You lost!The computer choice was {computer}'      

def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r' ):
        return True 
    
print(play()) #the play function is called 
    
    