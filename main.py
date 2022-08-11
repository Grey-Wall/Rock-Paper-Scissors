import random as random

moves = ["Rock", "Paper", "Scissors"]
RockPaperScissors = ["Rock", "Paper", "Scissors"]
choice = input("Choose Rock, Paper, or Scissors \n")

print("chioce is:" + choice)

print(random.choice(moves))

if choice == "Rock" and moves == "Paper" :
    print("You loose")
else :
    print("You win")

Rock=1
Paper=2
Scissors=3

