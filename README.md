Rock-Paper-Scissors Game:::
This project is a Python-based implementation of the Rock-Paper-Scissors game, enhanced with ASCII art to represent each option.
The user competes against the computer, and the game determines the winner based on classic rules.
It's a fun and simple way to engage with Python programming concepts such as conditional statements, user input, and randomness.
Features::::
User Input Handling::
The user enters a number corresponding to their choice: 0 for Rock, 1 for Paper, and 2 for Scissors.
The code checks for valid input and provides feedback if the input is out of range.
Random Computer Choice::
The computer selects a random option using Python’s random.randint() function.
Visual Feedback::
Each choice (Rock, Paper, Scissors) is represented using ASCII art, adding a creative touch to the gameplay.
Outcome Evaluation::
Implements game logic to decide if the user wins, loses, or ties with the computer.
Accounts for all possible outcomes based on the rules of Rock-Paper-Scissors.
Draw Condition::
If both user and computer select the same option, the game declares it a draw.
Error Handling::
Ensures user input is within the expected range (0, 1, or 2) and provides a fallback message for invalid inputs.

How It Works:::
The program displays the available choices:
Rock (0)
Paper (1)
Scissors (2)
The user inputs their choice as an integer.
The computer generates its choice randomly.
Both the user’s and the computer’s choices are displayed using ASCII art.
The game logic compares the choices and announces the result:
Win: The user’s choice beats the computer’s choice.
Lose: The computer’s choice beats the user’s choice.
Draw: Both choices are the same.
If the user inputs an invalid number, the program displays a "Number not found" mess

Example code Behaviour:::
--->CASE-1( User Wins)

Enter 3 numbers i.e is 0-Rock,1-Paper,2-Scissors: 2
                H^H^H^H^H^
                H^H^H^H^H^
                H^H^H^H^H^
_Computer input is 0
                @@@@@@@
                @@@@@@@        
output--You Win

--->CASE-2(Draw)
Enter 3 numbers i.e is 0-Rock,1-Paper,2-Scissors: 1
                $$$$$$$
                $$$$$$$
                $$$$$$$
                $$$$$$$
_Computer input is 1
                $$$$$$$
                $$$$$$$
                $$$$$$$
                $$$$$$$
output--withdraw

--->CASE-3(INVALID INPUT)
Enter 3 numbers i.e is 0-Rock,1-Paper,2-Scissors: 5
output--Number not found


Key Concepts Demonstrated::
This project highlights several important programming concepts:

Conditionals: Uses if-elif-else statements to handle game logic and outcomes.
Randomization: Demonstrates the use of the random module for unpredictable computer choices.
Input Validation: Ensures user-provided data is within acceptable bounds.
ASCII Art: Enhances user engagement with simple yet effective visual feedback.
