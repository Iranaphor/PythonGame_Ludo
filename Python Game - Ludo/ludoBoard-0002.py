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
ln09 = "  ╔══╦══╦══╦══╬──╬───╬──╬══╦══╦══╦══╗   "
ln10 = "  ║  │* │  │  │  ║   ║  │  │  │  │  ║   "
ln11 = "  ╠──╬══╬══╬══╬══╝   ╚══╬══╬══╬══╬──╣   "
ln12 = "  ║  │  │  │  │    D    │  │  │  │  ║   "
ln13 = "  ║  │  │  │  │         │  │  │  │  ║   "
ln14 = "  ╠──╬══╬══╬══╬══╗   ╔══╬══╬══╬══╬──╣   "
ln15 = "  ║  │  │  │  │  ║   ║  │  │  │* │  ║   "
ln16 = "  ╚══╩══╩══╩══╬──╬───╬──╬══╩══╩══╩══╝   "
ln17 = "              ║  ║   ║  ║               "
ln18 = "              ╠──╬───╬──╣               "
ln19 = "    ╔══╦══╗   ║  ║   ║  ║   ╔══╦══╗     "
ln20 = "    ║  ║  ║   ╠──╬───╬──╣   ║  ║  ║     "
ln21 = "    ╠══╬══╣   ║* ║   ║  ║   ╠══╬══╣     "
ln22 = "    ║  ║  ║   ╠──╬───╬──╣   ║  ║  ║     "
ln23 = "    ╚══╩══╝   ║  │   │  ║   ╚══╩══╝     "
ln24 = "              ╚══╩═══╩══╝               "

BX1 = 6
BX2 = 8
BX3 = 5
BX4 = 8
BY1 = 9
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
    (listy2[BY1])[BX1 + 1] = "1"
    (listy2[BY2])[BX2 + 1] = "2"
    (listy2[BY3])[BX3 + 1] = "3"
    (listy2[BY4])[BX4 + 1] = "4"
    (listy2[GY1])[GX1] = "G"
    (listy2[GY2])[GX2] = "G"
    (listy2[GY3])[GX3] = "G"
    (listy2[GY4])[GX4] = "G"
    (listy2[GY1])[GX1 + 1] = "1"
    (listy2[GY2])[GX2 + 1] = "2"
    (listy2[GY3])[GX3 + 1] = "3"
    (listy2[GY4])[GX4 + 1] = "4"
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
    print("You rolled a", diceRoll1, "and", diceRoll2)

###############################################################################################
X = 0
Y = 0
def move():
    print("YAYAYAYAY")
    global diceRoll1
    global diceRoll2
    global X
    global Y
    global BX1
    global BX2
    global BX3
    global BX4
    global BY1
    global BY2
    global BY3
    global BY4
    diceRoll = diceRoll1 + diceRoll2
    if (colour == "Blue"):
        if (piece == "1"):
            X = BX1
            Y = BY1
        elif (piece == "2"):
            X = BX2
            Y = BY2
        elif (piece == "3"):
            X = BX3
            Y = BY3
        elif (piece == "4"):
            X = BX4
            Y = BY4
        print(X)
        print(Y)

    if (piece == "1") and ((X == 5) and (Y == 2)):
        if (diceRoll1 == diceRoll2):
            X = 6
            Y = 9
            print("You move onto the board.")
        else:
            print("You need to roll doubles to join the board.")
    elif (piece == "2") and ((X == 8) and (Y == 2)):
        if (diceRoll1 == diceRoll2):
            X = 6
            Y = 9
            print("You move onto the board.")
        else:
            print("You need to roll doubles to join the board.")
    elif (piece == "3") and ((X == 5) and (Y == 4)):
        if (diceRoll1 == diceRoll2):
            X = 6
            Y = 9
            print("You move onto the board.")
        else:
            print("You need to roll doubles to join the board.")
    elif (piece == "4") and ((X == 8) and (Y == 4)):
        if (diceRoll1 == diceRoll2):
            X = 6
            Y = 9
            print("You move onto the board.")
        else:
            print("You need to roll doubles to join the board.")
    else:
        while (diceRoll > 0):
            diceRoll = diceRoll - 1
            if (X ==  6) and (Y == 9):
                X = 9
            elif (X == 9) and (Y == 9):
                X = 12
            elif (X == 12) and (Y == 9):
                X = 15
            elif (X == 15) and (Y == 9):
                Y = 7
            elif (X == 15) and (Y == 7):
                Y = 5
            elif (X == 15) and (Y == 5):
                Y = 3
            elif (X == 15) and (Y == 3):
                Y = 1
            elif (X == 15) and (Y == 1):
                X = 18
            elif (X == 18) and (Y == 1):
                X = 22
            elif (X == 22) and (Y == 1):
                Y = 3
            elif (X == 22) and (Y == 3):
                Y = 5
            elif (X == 22) and (Y == 5):
                Y = 7
            elif (X == 22) and (Y == 7):
                Y = 9
            elif (X == 22) and (Y == 9):
                X = 25
            elif (X == 25) and (Y == 9):
                X = 28
            elif (X == 28) and (Y == 9):
                X = 31
            elif (X == 31) and (Y == 9):
                X = 34
            elif (X == 34) and (Y == 9):
                Y = 11
            elif (X == 34) and (Y == 11):
                Y = 14
            elif (X == 34) and (Y == 14):
                X = 31
            elif (X == 31) and (Y == 14):
                X = 28
            elif (X == 28) and (Y == 14):
                X = 25
            elif (X == 25) and (Y == 14):
                X = 22
            elif (X == 22) and (Y == 14):
                Y = 16
            elif (X == 22) and (Y == 16):
                Y = 18
            elif (X == 22) and (Y == 18):
                Y = 20
            elif (X == 22) and (Y == 20):
                Y = 22
            elif (X == 22) and (Y == 22):
                X = 18
            elif (X == 18) and (Y == 22):
                X = 15
            elif (X == 15) and (Y == 22):
                Y = 20
            elif (X == 15) and (Y == 20):
                Y = 18
            elif (X == 15) and (Y == 18):
                Y = 16
            elif (X == 15) and (Y == 16):
                Y = 14
            elif (X == 15) and (Y == 14):
                X = 12
            elif (X == 12) and (Y == 14):
                X = 9
            elif (X == 9) and (Y == 14):
                X = 6
            elif (X == 6) and (Y == 14):
                X = 3
            elif (X == 3) and (Y == 14):
                Y = 11
            elif (X == 3) and (Y == 11):
##                if (colour == "Blue"):
##                    X = 6
##                else:
##                    Y = 9
                Y = 9
            elif (X == 3) and (Y == 9):
                X = 6
    if (colour == "Blue"):
        if (piece == "1"):
            BX1 = X
            BY1 = Y
        elif (piece == "2"):
            BX2 = X
            BY2 = Y
        elif (piece == "3"):
            BX3 = X
            BY3 = Y
        elif (piece == "4"):
            BX4 = X
            BY4 = Y
            
    mapReload()
###############################################################################################

mapReload()
winner = 0
while (winner == 0):
    playerNum = input("Number of Players [2 ~ 4]: ")
    if (playerNum == "1"):
        print("You cannot play with yourself...")
    elif (playerNum == "2"):
        winner = 1
        turn = input("Would you like to go first or second? [1 ~ 2]:")
        colour = input("What colour would you like to be? [Blue ~ Green]: ")
        winner1 = 0
        while (winner1 == 0):
            diceRoll()
            piece = input("What piece would you like to move? [1 ~ 4]: ")
            move()
##            if (turn == 1):
##                turn = 2
##            elif (turn == 2):
##                turn = 1
    elif (playerNum == "3"):
        print("Unavailable.")
    elif (playerNum == "4"):
        print("Unavailable.")
    else:
        print("Unavailable.")

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





















