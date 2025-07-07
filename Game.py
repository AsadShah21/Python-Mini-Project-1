import random   # using this import so pc selects the number randomly

# Similar Game is Rock Paper Scissor


print('computer turn: Snake(s) / Water(w) / Gun(g): \nComputer has chosen its value')

randomNO = random.randint(1,3) # pc will select number 1,2,3 randomly

if randomNO == 1:
    comp = 's'
elif randomNO == 2:
    comp ='w'
elif randomNO == 3:
    comp = 'g'    

Player = input('Choose your option now: Snake(s) , Water(w) , Gun(g): ')

# passing computer value and player value to our game function

def game(comp,Player):
    if comp == Player:   # if values are same than tie
        return None
    elif comp == 's':           # if computer selects snack and you select water will return false
        if Player == 'w':
            return False
        elif Player =='g':
            return True
    elif comp == 'w':           # if computer selects water and you select snake will return false
        if Player == 's':
            return True
        elif Player =='g':
            return False
    elif comp == 'g':           # if computer selects gun and you select snake will return false
        if Player == 's':
            return False
        elif Player =='w':
            return True   


a = game(comp, Player)

if a == None:                         # if game function returns none value the game is tie
    print(' The game is a Tie')        
elif a:                               # if game returns true you win
    print('You win !')
else:
    print('You lose !')               # if game returns false you lose