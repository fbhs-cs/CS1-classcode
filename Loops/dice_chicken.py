from random import randint

def play_round():
    roll_number = 1
    total = 0
    while True:
        d1 = randint(1,6)
        d2 = randint(1,6)
        if d1 != d2:
            total += d1 + d2
            print('Roll #{}: {} and {}'.format(roll_number,d1,d2))
            print('Score: {}'.format(total))
        else:
            print('Aww, you rolled doubles: {} and {}!'.format(d1,d2))
            print('You lose everything!')
            print('Game Over!')
            total = 0
            break
        
        again = input('Roll again? (y/n): ')
        if again == 'n':
            print('You made it {} rolls and scored {} points.'.format(roll_number,total))
            break
        roll_number += 1
        print()
    return total


def main():
    print('Welcome to Dice Chicken!\n')
    high_score = 0
    while True:
        print('Current high score: {}\n'.format(high_score))
        score = play_round()
        if score > high_score:
            high_score = score
        while True:
            again = input('Play again? y/n: ')
            if again == 'y' or again == 'Y':
                again = 'Y'
                break
            elif again == 'n' or again == 'N':
                print()
                print('Your high score was',high_score,', thanks for playing!')
                print
                again = 'N'
                break
            else:
                print('Invalid option.')
        if again == 'Y':
            print()
            continue
        else:
            break
        
        
        
        
if __name__ == '__main__':
    main()