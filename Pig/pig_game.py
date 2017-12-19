from random import randint
import os

class bcolors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def play_round():
    
    round_score=0
    holding = False
    while not holding:
        #print('\n'*20)
        dice1=randint(1,6)
        dice2=randint(1,6)
        print('You rolled \033[95m{} \033[0mand \033[95m{}\033[0m'.format(dice1,dice2))
        if (dice1==1 and dice2!=1) or (dice1!=1 and dice2==1):
            round_score = 0
            print('\033[91mYou rolled a 1.\033[0m')
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
            print('Would you like to \033[1m(r)\033[0moll or \033[1m(h)\033[0mold?')
            ask=input('> ')
            if ask.upper() == 'H':
               holding = True
               break
            elif ask.upper() == 'R':
                break
            else:
                print('\033[91mNot a valid option!\033[0m')
    
    return round_score

def main():
    os.system('cls')
    score = 0
    round_count = 0
    print('Welcome to \033[95mPig!\033[0m')
    while True:
        print('Press \033[1menter\033[0m when it is your turn\nor enter \033[1mq\033[0m to quit...')
        keypress = input('> ')
        if keypress.upper() == 'Q':
            break
        
        round_count+=1
        os.system('cls')
        print('\033[1mBegin Round #{}\033[0m'.format(round_count))
        round_score = play_round()
        score += round_score
        print('Round \033[1m#{}\033[0m score: \033[93m{}\033[0m'.format(round_count,round_score))
        print('Total score: \033[92m{}\033[0m'.format(score))
        print()
        
    print('Your final score was: \033[92m{}\033[0m'.format(score))
    print('You played \033[92m{}\033[0m rounds'.format(round_count))


if __name__ == '__main__':
    main()
