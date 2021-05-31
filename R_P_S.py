import random
def RPS():
    moves = ["rock","paper","scissors"]

    while True:
        computer = moves[random.randint(0,2)]
        player = input("rock, paper or scissors or do you wish to end the game: ")
        player = player.lower()
        if player == "rock":
            if computer == "paper":
                print("You lose",computer, "beats", player)
            else:
                print("You win!",player, "beats", computer)
        elif player == "paper":
            if computer == "rock":
                print("You win", player, "beats", computer)
            else:
                print("You lose!",computer, "beats", player)
        elif player == "scissors":
            if computer == "paper":
                print("You win", player, "beats", computer)
            else:
                print("You lose!",computer, "beats", player)
        elif player == "end the game":
            print("Thank you for playing this game")
            break
        elif player == computer:
            print("Tie")
        else:
            print("Check your spelling and try again")
        

RPS()