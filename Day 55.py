import random

listComputer = [-1, 0, 1]

gameStatus = True
while gameStatus:
    inputUser = input("Press S,W or G: ")
    chosedValue = random.choice(listComputer)
    if inputUser == "s" and chosedValue == -1:
        print("It's a draw")
    elif inputUser == "s" and chosedValue == 0:
        print("Hurray You Won!!!!!")
    elif inputUser == "s" and chosedValue == 1:
        print("Bad Luck You Lost..")
    elif inputUser == "w" and chosedValue == -1:
        print("Bad Luck You Lost..")
    elif inputUser == "w" and chosedValue == 0:
        print("It's a draw")
    elif inputUser == "w" and chosedValue == 1:
        print("Hurray You Won!!!!!")
    elif inputUser == "g" and chosedValue == 1:
        print("It's a draw")
    elif inputUser == "g" and chosedValue == 0:
        print("Bad Luck You Lost..")
    elif inputUser == "g" and chosedValue == -1:
        print("Hurray You Won!!!!!")
    elif inputUser == "q":
        print("Game exited")
        gameStatus = False


