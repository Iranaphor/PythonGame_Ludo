import time
import random
import os

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

def mapReload():
    uselessVariable = os.system("cls")
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

def diceIMG():
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
    dIMG1 = ("", "", "")
    if (diceRoll1 == 1):
        dIMG1 = ("│     │    ", "│  ■  │    ", "│     │    ")
    elif (diceRoll1 == 2):
        dIMG1 = ("│ ■   │    ", "│     │    ", "│   ■ │    ")
    elif (diceRoll1 == 3):
        dIMG1 = ("│ ■   │    ", "│  ■  │    ", "│   ■ │    ")
    elif (diceRoll1 == 4):
        dIMG1 = ("│ ■ ■ │    ", "│     │    ", "│ ■ ■ │    ")
    elif (diceRoll1 == 5):
        dIMG1 = ("│ ■ ■ │    ", "│  ■  │    ", "│ ■ ■ │    ")
    elif (diceRoll1 == 6):
        dIMG1 = ("│ ■ ■ │    ", "│ ■ ■ │    ", "│ ■ ■ │    ")
    if (diceRoll2 == 1):
        dIMG2 = ("│     │", "│  ■  │", "│     │")
    elif (diceRoll2 == 2):
        dIMG2 = ("│ ■   │", "│     │", "│   ■ │")
    elif (diceRoll2 == 3):
        dIMG2 = ("│ ■   │", "│  ■  │", "│   ■ │")
    elif (diceRoll2 == 4):
        dIMG2 = ("│ ■ ■ │", "│     │", "│ ■ ■ │")
    elif (diceRoll2 == 5):
        dIMG2 = ("│ ■ ■ │", "│  ■  │", "│ ■ ■ │")
    elif (diceRoll2 == 6):
        dIMG2 = ("│ ■ ■ │", "│ ■ ■ │", "│ ■ ■ │")


    print(''.join(map(str, listy2[0])))
    print(''.join(map(str, listy2[1])), "Player: ", turn)
    print(''.join(map(str, listy2[2])), "┌─────┐     ┌─────┐")
    print(''.join(map(str, listy2[3])), dIMG1[0], dIMG2[0])
    print(''.join(map(str, listy2[4])), dIMG1[1], dIMG2[1])
    print(''.join(map(str, listy2[5])), dIMG1[2], dIMG2[2])
    print(''.join(map(str, listy2[6])), "└─────┘     └─────┘")
    
    i = 7
    while(i < len(listy2)):
        print(''.join(map(str, listy2[i])))
        i+=1  

diceRoll1 = 0
diceRoll2 = 0
def diceRoll():
    global diceRoll1
    global diceRoll2
    diceRoll1 = random.randint(1,4)
    diceRoll2 = random.randint(1,4)
    diceIMG()


###############################################################################################
X = 0
Y = 0
def pieceMove():
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
    global GX1
    global GX2
    global GX3
    global GX4
    global GY1
    global GY2
    global GY3
    global GY4
    global p1Colour
    global p2Colour
    global colour
    global move
    global turn

    if (turn == "1"):
        colour = p1Colour
        print("label: colour1")
    elif (turn == "2"):
        colour = p2Colour
        print("label: colour2")
    print(colour)
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
    elif (colour == "Green"):
        if (piece == "1"):
            X = GX1
            Y = GY1
        elif (piece == "2"):
            X = GX2
            Y = GY2
        elif (piece == "3"):
            X = GX3
            Y = GY3
        elif (piece == "4"):
            X = GX4
            Y = GY4

    print("Colour: ", colour)
    move = True
    if (colour == "Blue"):
        print("label: 1")
        if (piece == "1") and ((X == 5) and (Y == 2)):
            if (diceRoll1 == diceRoll2):
                X = 6
                Y = 9
                print("You move onto the board.")
                move = False
            else:
                print("You need to roll doubles to join the board.")
                move = False
        elif (piece == "2") and ((X == 8) and (Y == 2)):
            print("label: 2")
            if (diceRoll1 == diceRoll2):
                X = 6
                Y = 9
                print("You move onto the board.")
                print("label: 3")
                move = False
            else:
                print("label: 4")
                print("You need to roll doubles to join the board.")
                move = False
        elif (piece == "3") and ((X == 5) and (Y == 4)):
            if (diceRoll1 == diceRoll2):
                X = 6
                Y = 9
                print("You move onto the board.")
                move = False
            else:
                print("You need to roll doubles to join the board.")
                move = False
        elif (piece == "4") and ((X == 8) and (Y == 4)):
            if (diceRoll1 == diceRoll2):
                X = 6
                Y = 9
                print("You move onto the board.")
                move = False
            else:
                print("You need to roll doubles to join the board.")
                move = False        
        print("label: 5")
    if (colour == "Green"):
        if (piece == "1") and ((X == 29) and (Y == 19)):
            if (diceRoll1 == diceRoll2):
                X = 31
                Y = 14
                print("You move onto the board.")
                move = False
            else:
                print("You need to roll doubles to join the board.")
                move = False
        elif (piece == "2") and ((X == 32) and (Y == 19)):
            if (diceRoll1 == diceRoll2):
                X = 31
                Y = 14
                print("You move onto the board.")
                move = False
            else:
                print("You need to roll doubles to join the board.")
                move = False
        elif (piece == "3") and ((X == 29) and (Y ==21)):
            if (diceRoll1 == diceRoll2):
                X = 31
                Y = 14
                print("You move onto the board.")
                move = False
            else:
                print("You need to roll doubles to join the board.")
                move = False
        elif (piece == "4") and ((X == 32) and (Y == 21)):
            if (diceRoll1 == diceRoll2):
                X = 31
                Y = 14
                print("You move onto the board.")
                move = False
            else:
                print("You need to roll doubles to join the board.")
                move = False

    #Movement
    print("label: 6")
    if (move == True):
        print("label: 7")
        while (diceRoll > 0):
            print("label: 8")
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
                Y = 9
            elif (X == 3) and (Y == 9):
                X = 6

        if (colour == "Blue"):
            if (X == GX1) and (Y == GY1):
                GX1 = 29
                GY1 = 19
            elif (X == GX2) and (Y == GY2):
                GX2 = 32
                GY2 = 19
            elif (X == GX3) and (Y == GY3):
                GX3 = 29
                GY3 = 21
            elif (X == GX4) and (Y == GY4):
                GX4 = 32
                GY4 = 21
        elif (colour == "Green"):
            if (X == BX1) and (Y == BY1):
                BX1 = 5
                BY1 = 2
            elif (X == BX2) and (Y == BY2):
                BX2 = 8
                BY2 = 2
            elif (X == BX3) and (Y == BY3):
                BX3 = 5
                BY3 = 4
            elif (X == BX4) and (Y == BY4):
                BX4 = 8
                BY4 = 4
        
 
        move = False
    print("label: 9")
    if (colour == "Blue"):
        if (piece == "1"):
            BX1 = X
            BY1 = Y
        elif (piece == "2"):
            print("label: 10")
            BX2 = X
            BY2 = Y
        elif (piece == "3"):
            BX3 = X
            BY3 = Y
        elif (piece == "4"):
            BX4 = X
            BY4 = Y
    elif (colour == "Green"):
        if (piece == "1"):
            GX1 = X
            GY1 = Y
        elif (piece == "2"):
            GX2 = X
            GY2 = Y
        elif (piece == "3"):
            GX3 = X
            GY3 = Y
        elif (piece == "4"):
            GX4 = X
            GY4 = Y
    print("label: 11")
    diceIMG()
###############################################################################################

winner = 0
colour = ""
while (winner == 0):
    playerNum = input("Number of Players [2 ~ 4]: ")
    if (playerNum == "1"):
        print("You cannot play with yourself...")
    elif (playerNum == "2"):
        winner = 1
        turn = input("Would you like to go first or second? [1 ~ 2]: ")
        p1Colour = input("P1 Colour? [Blue ~ Green]: ")
        if (p1Colour == "Blue"):
            p2Colour = "Green"
            print("Player 1 is Blue")
            print("Player 2 is Green")
        elif (p1Colour == "Green"):
            p2Colour = "Blue"
            print("Player 1 is Green")
            print("Player 2 is Blue")


        winner1 = 0
        while (winner1 == 0):
            if (turn == "1"):
                colour = p1Colour
                print("label: colour1")
            elif (turn == "2"):
                colour = p2Colour
                print("label: colour2")

            diceRoll()
            if (colour == "Blue"):
                if (BY1 == 2) and (BY2 == 2) and (BY3 == 4) and (BY4 == 4):
                    if (diceRoll1 == diceRoll2):
                        piece = input("What piece would you like to move? [1 ~ 4]: ")
                        pieceMove()
                else:
                    piece = input("What piece would you like to move? [1 ~ 4]: ")
                    pieceMove()
            elif (colour == "Green"):
                if (GY1 == 19) and (GY2 == 19) and (GY3 == 21) and (GY4 == 21):
                    if (diceRoll1 == diceRoll2):
                        piece = input("What piece would you like to move? [1 ~ 4]: ")
                        pieceMove()
                else:
                    piece = input("What piece would you like to move? [1 ~ 4]: ")
                    pieceMove()
            time.sleep(1)
            if (turn == "1"):
                turn = "2"
                move = True
            elif (turn == "2"):
                turn = "1"
                move = True
    elif (playerNum == "3"):
        print("Unavailable.")
    elif (playerNum == "4"):
        print("Unavailable.")
    else:
        print("Unavailable.")

    diceIMG()


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





















