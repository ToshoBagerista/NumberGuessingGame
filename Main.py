import random

if __name__ == '__main__':
    global chances
    choice = int(input(f'Welcome to the Number Gessing Game!\nI\'m thinking of a number between 1 and 100.\n\nPlease selct the difficulty level:\n[1] Easy (10 chances)\n[2] Medium (5 chances)\n[3] Hard (3 chances)\n\nEnter your choice: '))
    match choice:
        case 1:
            chances = 10
            print(f'Great! You have selected the Easy difficulty level. You have 10 chances to guess the number!')
        case 2:
            chances = 5
            print(f'Great! You have selected the Medium difficulty level. You have 5 chances to guess the number!')
        case 3:
            chances = 3
            print(f'Great! You have selected the Hard difficulty level. You have 3 chances to guess the number!')
    print('Let\'s start the game!')

    num = random.randint(1, 100)

    for i in range(chances):
        guess = int(input('Enter your guess: '))
        if guess == num:
            print(f'Congratulations! You guessed the correct number in {i} attempts.')
            break
        elif guess < num: print(f'Incorrect! The number is greater than {guess}.')
        elif guess > num: print(f'Incorrect! The number is less than {guess}.')