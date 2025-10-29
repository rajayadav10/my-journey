import random

numbers = range(1, 10)
correct_guess = random.choice(numbers)
max_chance = 3
chance = 0

while chance < max_chance:
    guess = int(input('Guess the number: '))
    chance += 1

    if guess == correct_guess:
        print('🎉 Woah! You guessed it!!')
        break
    elif guess > correct_guess:
        print('⬇️ Too high!')
    elif guess < correct_guess:
        print('⬆️ Too low!')


if guess != correct_guess:
    print(f'😢 Sorry, you ran out of tries! The correct number was {correct_guess}.')
