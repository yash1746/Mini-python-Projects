import random
game_start=input("enter 'YES' for start the game:")
if(game_start=="yes"):
    print("How to play: Enter the amount of BET\n             Guess the number between 1,6 \n             If you guess the number correct your Bet amount got double ")
bet_amount=int(input("enter your Beting amount(In $ ):"))
guessed_number=int(input("enter the number for betting:"))
if random.random() < 0.2:
    random_number = guessed_number
else:
    random_number = random.randint(1,6)
if(guessed_number<=6):
    print("Randomly generated number:",random_number)
    if(guessed_number==random_number):
        print("$",bet_amount*2)
    else:
        print("Better Luck next time")
else:
    print("Restart the game again AND only enter number between 1,6")


