# [Subject]
Mini project Python

## Key terminology
randint  (Random integer)  
While loop


## Exercise

* Number Guessing:
Generate a random number between 1 and 100 (or any other range).
The player guesses a number. For every wrong answer the player receives a clue.
When the player guesses the right number, display a score.

* Rock Paper Scissors:
The player plays against a computer opponent typing either a letter (rps) or an entire word (rock paper scissors) to play their move.
Create a function that checks whether the move is valid or not.
Create another function to create a computer move.
Create another function to check who wins the round.
Finally, create a function that keeps track of the score.
The game should be played in a predetermined number of rounds.

* Tic-Tac-Toe:
Generate a 3x3 board on the command line.
This is a 2-player game, where one player inputs “X” and the other player inputs “O”.
Bonus: create a single-player version that you can play against the computer.

### Sources

https://www.geeksforgeeks.org/number-guessing-game-in-python/  

https://realpython.com/python-rock-paper-scissors/  



### Overcome challenges
I had to study a lot of Python guides on how to create small games like these. First I had no clear direction of how I would proceed after setting up the basics. After studying those guides I came to a better understanding of how to tackle some of these problems and come up with possible ways to mimick very basic computer input.

### Results
I created the Rock Paper Scissors game by implementing "randint", which uses a random integer for the computer to pick one of the options.  

```
from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:

    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("You're trying to use an unauthorized weapon!")

    player = False
    computer = t[randint(0,2)]
```
