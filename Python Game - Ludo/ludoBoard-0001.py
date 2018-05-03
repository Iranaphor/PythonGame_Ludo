import time
import random

ln01 = "              ╔══╦═══╦══╗               "
ln02 = "    ╔══╦══╗   ║  │   │  ║   ╔══╦══╗     "
ln03 = "    ║  ║  ║   ╠──╬───╬──╣   ║  ║  ║     "
ln04 = "    ╠══╬══╣   ║  ║   ║* ║   ╠══╬══╣     "
ln05 = "    ║  ║  ║   ╠──╬───╬──╣   ║  ║  ║     "
ln06 = "    ╚══╩══╝   ║  ║   ║  ║   ╚══╩══╝     "
ln07 = "              ╠──╬───╬──╣               "
ln08 = "              ║  ║   ║  ║               "
ln09 = "  ╔══╦══╦══╦══╩──╬───╣  ╠══╦══╦══╦══╗   "
ln10 = "  ║  │* │  │     ║   ║  │  │  │  │  ║   "
ln11 = "  ╠──╬══╬══╬══╦══╝   ╚══╬══╬══╬══╬──╣   "
ln12 = "  ║  │  │  │  │    D    │  │  │  │  ║   "
ln13 = "  ║  │  │  │  │         │  │  │  │  ║   "
ln14 = "  ╠──╬══╬══╬══╬══╗   ╔══╩══╬══╬══╬──╣   "
ln15 = "  ║  │  │  │  │  ║   ║     │  │* │  ║   "
ln16 = "  ╚══╩══╩══╩══╣  ╠───╬──╦══╩══╩══╩══╝   "
ln17 = "              ║  ║   ║  ║               "
ln18 = "              ╠──╬───╬──╣               "
ln19 = "    ╔══╦══╗   ║  ║   ║  ║   ╔══╦══╗     "
ln20 = "    ║  ║  ║   ╠──╬───╬──╣   ║  ║  ║     "
ln21 = "    ╠══╬══╣   ║* ║   ║  ║   ╠══╬══╣     "
ln22 = "    ║  ║  ║   ╠──╬───╬──╣   ║  ║  ║     "
ln23 = "    ╚══╩══╝   ║  │   │  ║   ╚══╩══╝     "
ln24 = "              ╚══╩═══╩══╝               "

BX1 = 5
BX2 = 8
BX3 = 5
BX4 = 8
BY1 = 2
BY2 = 2
BY3 = 4
BY4 = 4

GX1 = 29
GX2 = 32
GX3 = 29
GX4 = 32
GY1 = 19
GY2 = 19
GY3 = 21
GY4 = 21






listy = (ln01, ln02, ln03, ln04, ln05, ln06, ln07, ln08, ln09, ln10, ln11, ln12, ln13, ln14, ln15, ln16, ln17, ln18, ln19, ln20, ln21, ln22, ln23, ln24)

i = 0
while(i < len(listy)):
    print(listy[i])
    i+=1

def mapReload():
    l01 = []
    l02 = []
    l03 = []
    l04 = []
    l05 = []
    l06 = []
    l07 = []
    l08 = []
    l09 = []
    l10 = []
    l11 = []
    l12 = []
    l13 = []
    l14 = []
    l15 = []
    l16 = []
    l17 = []
    l18 = []
    l19 = []
    l20 = []
    l21 = []
    l22 = []
    l23 = []
    l24 = []
    i = 0
    while(i < len(ln01)):
        l01 = l01 + [ln01[i]]
        l02 = l02 + [ln02[i]]
        l03 = l03 + [ln03[i]]
        l04 = l04 + [ln04[i]]
        l05 = l05 + [ln05[i]]
        l06 = l06 + [ln06[i]]
        l07 = l07 + [ln07[i]]
        l08 = l08 + [ln08[i]]
        l09 = l09 + [ln09[i]]
        l10 = l10 + [ln10[i]]
        l11 = l11 + [ln11[i]]
        l12 = l12 + [ln12[i]]
        l13 = l13 + [ln13[i]]
        l14 = l14 + [ln14[i]]
        l15 = l15 + [ln15[i]]
        l16 = l16 + [ln16[i]]
        l17 = l17 + [ln17[i]]
        l18 = l18 + [ln18[i]]
        l19 = l19 + [ln19[i]]
        l20 = l20 + [ln20[i]]
        l21 = l21 + [ln21[i]]
        l22 = l22 + [ln22[i]]
        l23 = l23 + [ln23[i]]
        l24 = l24 + [ln24[i]]
        i+=1
    listy2 = (l01, l02, l03, l04, l05, l06, l07, l08, l09, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21, l22, l23, l24)
    (listy2[BY1])[BX1] = "B"
    (listy2[BY2])[BX2] = "B"
    (listy2[BY3])[BX3] = "B"
    (listy2[BY4])[BX4] = "B"
    (listy2[GY1])[GX1] = "G"
    (listy2[GY2])[GX2] = "G"
    (listy2[GY3])[GX3] = "G"
    (listy2[GY4])[GX4] = "G"
    i = 0
    while(i < len(listy2)):
        print(''.join(map(str, listy2[i])))
        i+=1


diceRoll1 = 0
diceRoll2 = 0
def diceRoll():
    global diceRoll1
    global diceRoll2
    diceRoll1 = random.randint(1,6)
    diceRoll2 = random.randint(1,6)
    print()
    print("You rolled a", diceRoll1, "and", diceRoll2)


def pieceMove(X1, Y1, X2, Y2, X3, Y3, X4, Y4):

    if (X1 == 5) and (X2 == 8) and (X3 == 5) and (X4 == 8) and (Y1 == 2) and (Y2 == 2) and (Y3 == 4) and (Y4 == 4):
        if (diceRoll1 == diceRoll2):
            print("You move a piece onto the board.")
            if(X1 == 5) and (Y1 == 2):
                X1 = 
        else:
            print("You need doubles to move onto the board.")
            turn = False
    
    while (diceRollSum > 0):
        if(turn == True):
            print()
    
    



winner = 0
while (winner == 0):
    playerNum = input("Number of Players [2 ~ 4]: ")
    if (playerNum == "1"):
        print("You cannot play with yourself...")
    elif (playerNum == "2"):
        
        diceRoll()
        pieceMove()
        print()
    else:
        print("You can only play 2 player games.")

    mapReload()

    
##when it is your turn
##    diceRoll()
##    is there a piece on the board?
##      no
##        have you got doubles?
##          yes
##            place piece on board
##          no
##            skip go
##      yes
##        have you got more then one piece on board?
##          no
##            move piece the sum of the roll
##          yes
##            choose piece to move
##            move piece the sum of the roll




















        
