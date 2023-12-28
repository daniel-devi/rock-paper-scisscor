import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    if user == 'r':
        print('You Chose Rock')
    elif user == 'p':
        print('You Chose Paper') 
    elif user == 's':
        print('You Chose Scissors') 
    
    computer = random.choice(['r', 'p', 's'])
    if computer == 'r':
            print('Computer Choose Rock')
    elif computer == 'p':
            print('Computer Choose Paper') 
    else:
        print('Computer Choose Scissors')
        
    if user == computer:
        print('It\'s a tie')
        return play()
    
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    
    
    print('You lost!')
    return play()

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
