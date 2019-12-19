from random import randint
import os
import time

class bcolors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def play_round(player_name):
    
    round_score=0
    holding = False
    while not holding:
        #print('\n'*20)
        dice1=randint(1,6)
        dice2=randint(1,6)
        print(f"\033[95m{player_name}\033[0m rolled \033[95m{dice1} \033[0mand \033[95m{dice2}\033[0m")
        if (dice1==1 and dice2!=1) or (dice1!=1 and dice2==1):
            round_score = 0
            print(f'\033[91m{player_name} rolled a 1.\033[0m')
            break
        else:
            sum=dice1+dice2
            if dice1==dice2 and dice1!=1:
                print('\033[92mDoubles!\033[0m')
                sum=sum*2
            elif dice1 == 1:
                sum=25
            round_score += sum       
        print('Points: \033[94m{}\033[0m'.format(sum))
        print('Round Score: \033[93m{}\033[0m'.format(round_score))
        while True:
            print('\033[1m(R)\033[0moll or \033[1m(H)\033[0mold?')
            ask=input('> ')
            if ask.upper() == 'H':
               holding = True
               break
            elif ask.upper() == 'R':
                break
            else:
                print('\033[91mNot a valid option!\033[0m')
    
    return round_score

def play_game():
    os.system('clear')
    print('Welcome to \033[95mPig!\033[0m')
    num_players = 2
    while True:
        try:
            max_score = int(input("Enter score to win: "))
            if max_score > 0:
                break
        except:
            print("Please enter a positive integer.")
    
    player_scores = [0] * num_players
    round_count = 0
    player_names = []
    for i in range(num_players):
        name = input("Enter player's name: ")
        player_names.append(name)
    
    print("Choosing who goes first",end="")
    for i in range(3):
        print(".",end="",flush=True)
        time.sleep(.5)
    print()
    turn = randint(1,num_players) - 1
    while True:
        is_winner = False
        for score in player_scores:
            if score >= max_score:
                is_winner = True
        if is_winner:
            break
        print(f"Round \033[1m#{round_count//num_players + 1}\033[0m:")
        print(f"It is \033[95m{player_names[turn]}\033[0m's turn.")
        print("Press \033[1menter\033[0m when you are ready or \033[1mq\033[0m to quit...")
        keypress = input('> ')
        if keypress.upper() == 'Q':
            break
        os.system('clear')
        
        round_score = play_round(player_names[turn])
        
        player_scores[turn] += round_score
        print(f"\033[95m{player_names[turn]}\033[0m's Round \033[1m#{round_count//num_players + 1}\033[0m score: \033[93m{round_score}\033[0m")
        round_count += 1
        print()
        for i in range(num_players):
            print(f"\033[1m{player_names[i]}\033[0m's Total Score: \033[92m{player_scores[i]}\033[0m",end="\t\t\t")
        print()
        print()
        turn = (turn + 1) % num_players
    if is_winner:
        winner = player_names[player_scores.index(max(player_scores))]
        print(f"\033[1m{winner}\033[0m \033[92mwon the game!\033[0m")
    print("Final Score Summary")
    for i in range(num_players):
        print(f"{player_names[i]}'s Total Score: \033[92m{player_scores[i]}\033[0m")
    print('You played \033[92m{}\033[0m round(s)'.format((round_count-1)//num_players + 1))
    


def main():
    play_game()


if __name__ == '__main__':
    play_game()
