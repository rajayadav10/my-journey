🎯 Number Guessing Game
Python 3.x | Status: Active | Level: Beginner | License: MIT
🧩 Overview
A fun and simple Python command-line game where you try to guess a randomly selected number between 1 and 9. You only have 3 chances to guess it right — can you beat the odds? 🎲

This project helps you understand Python basics such as loops, conditionals, user input, and the random module.
💡 Features
•	✅ Random number generation
•	✅ Limited number of guessing attempts (3 chances)
•	✅ User-friendly prompts and messages
•	✅ Beginner-friendly — no external libraries required
🧠 How the Game Works
1.	1. The program picks a secret number between 1 and 9.
2.	2. You enter your guess.
3.	3. If your guess matches the secret number — you win! 🎉
4.	4. If not, you get another try until your 3 chances run out.
5.	5. If all chances are used, the game reveals the correct number.
🧾 Code Example
import random

numbers = range(1, 10)
chances = 3
chance_count = 0
correct_guess = random.choice(numbers)

while chance_count < chances:
    guess = int(input("Guess the number (1–9): "))
    chance_count += 1

    if guess == correct_guess:
        print("🎉 You guessed it!")
        break
    else:
        print("❌ Wrong guess! Try again.")

if chance_count == chances and guess != correct_guess:
    print(f"Out of chances! The correct number was {correct_guess}.")

⚙️ Requirements
• Python 3.x
• No external dependencies required
🚀 How to Run
6.	1. Clone or download this repository.
7.	2. Open your terminal or command prompt.
8.	3. Navigate to the project folder: cd number-guessing-game
9.	4. Run the script: python number_guessing_game.py
🖥️ Example Gameplay
Guess the number (1–9): 4
❌ Wrong guess! Try again.
Guess the number (1–9): 7
🎉 You guessed it!

🔮 Future Improvements
•	✨ Add 'Too High' or 'Too Low' hints
•	✨ Allow the user to choose a custom number range
•	✨ Add a scoring system or multiple rounds
•	✨ Create a GUI version using tkinter
🧑‍💻 Author
Raja Yadav
