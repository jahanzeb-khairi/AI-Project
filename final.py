import tkinter as tk
from PIL import ImageTk, Image
import random
from gtts import gTTS
from playsound import playsound
import os


def Speak(Text):
    obj = gTTS(text=Text, lang='en', slow=False)
    obj.save('Text.mp3')
    playsound('Text.mp3')
    os.remove("Text.mp3")

def start_game():
    global im
    global b1, b2
    b1.place(x=1300, y=400)
    b2.place(x=1300, y=550)

    im = Image.open("images/roll.png")
    im = im.resize((65, 65))
    im = ImageTk.PhotoImage(im)
    b = tk.Button(root, image=im, height=80, width=80)
    b.place(x=1350, y=200)

    b = tk.Button(root, text="Click Here to End Game", height=3, width=20, fg="red", bg="yellow", font=('cursive', 14, 'bold'), activebackground='red', command=root.destroy)
    b.place(x=1300, y=20)

def reset_coins():
    global player_1, player_2
    global pos1, pos2
    player_1.place(x=0, y=800)
    player_2.place(x=60, y=800)
    pos1 = 0
    pos2 = 0

def load_dice_images():
    global Dice
    names = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]
    for nam in names:
        im = Image.open("images/" + nam)
        im = im.resize((65, 65))
        im = ImageTk.PhotoImage(im)
        Dice.append(im)

def check_Ladder(Turn):
    global pos1, pos2
    f = 0
    if Turn == 1:
        if pos1 in Ladder:
            Speak("Ladder at " + str(pos1) + " Moving Up to " + str(Ladder[pos1]))
            pos1 = Ladder[pos1]
            f = 1
    else:
        if pos2 in Ladder:
            Speak("Ladder at " + str(pos2) + " Moving Up to " + str(Ladder[pos2]))
            pos2 = Ladder[pos2]
            f = 1
    return f

def check_snake(Turn):
    global pos1, pos2
    global player1_shield, player2_shield

    if Turn == 1:
        if pos1 in Snake:
            if player1_shield:
                Speak("Shield saved Player 1 from snake!")
                player1_shield = False
            else:
                Speak("Snake at " + str(pos1) + " Going down to " + str(Snake[pos1]))
                pos1 = Snake[pos1]
    else:
        if pos2 in Snake:
            if player2_shield:
                Speak("Shield saved Player 2 from snake!")
                player2_shield = False
            else:
                Speak("Snake at " + str(pos2) + " Going down to " + str(Snake[pos2]))
                pos2 = Snake[pos2]

def check_powerups(Turn):
    global pos1, pos2
    global player1_shield, player2_shield
    global player1_trap, player2_trap

    boost_activated = False

    current_pos = pos1 if Turn == 1 else pos2

    if current_pos in Shield:
        Speak("Shield activated! Protection from snakes.")
        if Turn == 1:
            player1_shield = True
        else:
            player2_shield = True

    if current_pos in Boost:
        Speak("Boost activated! Extra dice roll")
        boost_activated = True

    if current_pos in Trap:
        Speak("Trap activated! Opponent will skip next turn")
        if Turn == 1:
            player2_trap = True
        else:
            player1_trap = True

    return boost_activated


def roll_dice():
    global Dice
    global turn
    global pos1, pos2
    global b1, b2
    global player1_shield, player2_shield
    global player1_trap, player2_trap

    if (turn == 1 and player1_trap) or (turn == 2 and player2_trap):
        Speak("Player " + str(turn) + " turn is skipped due to trap!")
        if turn == 1:
            player1_trap = False
            turn = 2
            b1.configure(state='disabled')
            b2.configure(state='normal')
        else:
            player2_trap = False
            turn = 1
            b1.configure(state='normal')
            b2.configure(state='disabled')
        return

    r = random.randint(1, 6)
    b3 = tk.Button(root, image=Dice[r-1], height=80, width=80)
    b3.place(x=1350, y=200)

    Speak(str(r))

    Lad = 0
    if turn == 1:
        if (pos1 + r) <= 100:
            pos1 += r
        Lad = check_Ladder(turn)
        check_snake(turn)
        boost = check_powerups(turn)
        move_coin(turn, pos1)
    else:
        if (pos2 + r) <= 100:
            pos2 += r
        Lad = check_Ladder(turn)
        check_snake(turn)
        boost = check_powerups(turn)
        move_coin(turn, pos2)

    is_winner()

    if boost:
        Speak("Rolling again due to Boost!")
        root.after(500, roll_dice)
        return

    if r != 6:
        if turn == 1:
            turn = 2
            b1.configure(state='disabled')
            b2.configure(state='normal')
        else:
            turn = 1
            b1.configure(state='normal')
            b2.configure(state='disabled')

    Speak("Player - " + str(turn) + " turn")

def is_winner():
    global pos1, pos2

    if pos1 == 100:
        msg = "Player - 1 is the Winner"
        Speak(msg)
        Lab = tk.Label(root, text=msg, height=2, width=20, bg='red', font=('Cursive', 30, 'bold'))
        Lab.place(x=300, y=300)
        reset_coins()
    elif pos2 == 100:
        msg = "Player - 2 is the Winner"
        Speak(msg)
        Lab = tk.Label(root, text=msg, height=2, width=20, bg='red', font=('Cursive', 30, 'bold'))
        Lab.place(x=300, y=300)
        reset_coins()

def move_coin(Turn, r):
    if Turn == 1:
        player_1.place(x=Index[r][0], y=Index[r][1])
        Speak("You are at " + str(pos1))
    else:
        player_2.place(x=Index[r][0], y=Index[r][1])
        Speak("You are at " + str(pos2))

def get_index():
    Num = [100,99,98,97,96,95,94,93,92,91,81,82,83,84,85,86,87,88,89,90,80,79,78,77,76,75,74,73,72,71,61,62,63,64,65,66,67,68,69,70,60,59,58,57,56,55,54,53,52,51,41,42,43,44,45,46,47,48,49,50,40,39,38,37,36,35,34,33,32,31,21,22,23,24,25,26,27,28,29,30,20,19,18,17,16,15,14,13,12,11,1,2,3,4,5,6,7,8,9,10]
    row = 30
    i = 0
    for x in range(1, 11):
        col = 80
        for y in range(1, 11):
            Index[Num[i]] = (col, row)
            col += 111
            i += 1
        row += 78

#Game Initialization ---
Dice = []
Index = {}
pos1 = None
pos2 = None

Ladder = {9:27, 18:37, 25:54, 28:51, 56:64, 68:88, 76:97, 79:100}
Snake = {99:77, 95:75, 93:69, 87:24, 67:30, 63:19, 59:17, 16:7}

Shield = [2, 35, 68]
Boost = [13, 46, 79]
Trap = [24, 57, 95]

player1_shield = False
player2_shield = False
player1_trap = False
player2_trap = False

root = tk.Tk()
root.geometry("1600x1000")
root.title("Snake and Ladder Game with Power-Ups")

F1 = tk.Canvas(root, width=1200, height=800)
F1.place(x=0, y=0)

img1 = ImageTk.PhotoImage(Image.open("images/final_cover.png"))
F1.create_image(0, 0, anchor='nw', image=img1)

shield_img = ImageTk.PhotoImage(Image.open("images/shield.png").resize((30,30)))
boost_img = ImageTk.PhotoImage(Image.open("images/boost.png").resize((30,30)))
trap_img = ImageTk.PhotoImage(Image.open("images/trap.png").resize((30,30)))

get_index()

for sq in Shield:
    F1.create_image(Index[sq][0]+10, Index[sq][1]+10, anchor='nw', image=shield_img)
for sq in Boost:
    F1.create_image(Index[sq][0]+10, Index[sq][1]+10, anchor='nw', image=boost_img)
for sq in Trap:
    F1.create_image(Index[sq][0]+10, Index[sq][1]+10, anchor='nw', image=trap_img)

b1 = tk.Button(root, text="Player - 1", height=3, width=20, fg="red", bg="cyan", font=('cursive', 14, 'bold'), activebackground='blue', command=roll_dice)
b1.place(x=1300, y=400)

b2 = tk.Button(root, text="Player - 2", height=3, width=20, fg="red", bg="orange", font=('cursive', 14, 'bold'), activebackground='red', command=roll_dice)
b2.place(x=1300, y=550)

player_1 = tk.Canvas(root, width=40, height=40)
player_1.create_oval(10, 10, 40, 40, fill='blue')

player_2 = tk.Canvas(root, width=40, height=40)
player_2.create_oval(10, 10, 40, 40, fill='red')

turn = 1

reset_coins()
load_dice_images()

Speak("Welcome to Snake and Ladder Game with Power-Ups! Start with Player 1")
start_game()

root.mainloop()
