import random

while True:

    choice = input("Choose between Rock, Paper, Scissor: ")
    choice = choice.lower()

    if choice == 'quit':
        break

    if choice != 'rock' and choice != 'paper' and choice != 'scissor':
        print("choose correct choice")
        continue

    computer = random.choice(["rock","paper","scissor"])
    print("Computer chose ", computer)
    if computer == choice:
        print("It was a tie")
        break
    elif computer == 'rock' and choice == 'paper':
        print("You won")
        break
    elif computer == 'paper' and choice == 'scissor':
        print("You won")
        break
    elif computer == 'scissor' and choice == 'rock':
        print("You won")
        break
    else:
        print("Try again")
        continue

