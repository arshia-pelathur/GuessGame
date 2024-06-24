import random

print('******Guess the Number Game******')
print('I am thinking of a number between 1 and 30. Can you guess it in less than 5 attempts??')

random_number = random.randint(1,30)
guess_limit = 5
guess_counter = 1
while guess_counter <=guess_limit:
    guess = int(input('\nEnter your guess: '))
    if guess not in range(1,30):
        print('Value entered is not in range. Enter correct value.')
        print('GAME OVER!!! Try Again')
        break
    elif guess<random_number:
        print('Too low!. Guess higher')
    else:
        print('Too high!. Guess lower')
    guess_counter+=1

if guess == random_number:
    print('Congratulations! You guessed correctly!')
else:
    print(f'Sorry. The number was {random_number}. Try again next time :( ')


