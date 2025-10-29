import random
numbers = range(1,10)
chances =3
chance_count = 0
correct_guess = random.choice(numbers)
while chance_count < chances:
    guess = int(input('guess the number from 1-10:'))
    chance_count += 1
    if guess == correct_guess:
        print(' you guessed it!')
        break
    else:
        print('keep trying')
        if chance_count == chances:
            print('out of try! try next time')