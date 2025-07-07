import random

randomNo = random.randint(1,3)

print(randomNo)


if randomNo ==1:
    comp = "s"
elif randomNo ==2:
    comp = "w"
elif randomNo ==3:
    comp ='g'

player = input('Enter your option: Snack (s) , water (w) , Gun (g)')

def game(comp, player):

    if comp == "s":
        if player =="w":
            return False
        elif player =="g":
            return True
        
    elif comp == "g":
        if player =="w":
            return True
        elif player =="g":
            return False

    elif comp == "w":
        if player == "s":
            return True
        elif player =="g":
            return False

a = game(comp, player)

if a == None:
    print('Game is tie!')
elif a == True:
    print('You have won !')
elif a == False:
    print('You have lost !')        