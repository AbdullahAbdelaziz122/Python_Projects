from tkinter import *
import random


def next_turn(row,col):
    global player
    if game_btns[row][col]['text']=="" and check_winner() == False:
        if player==players[0]:

            game_btns[row][col]['text'] = player
            if check_winner() == False:
                player = players[1]
                #switch player
                label.config(text=(players[1]+ " turn"))

            elif check_winner() == True:
                label.config(text=(players[0]+" Wins!"))

            elif check_winner() == 'tie':
                label.config(text=("No winner"))

        elif player == players[1]:

            game_btns[row][col]['text'] = player

            if check_winner() == False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner() == True:
                label.config(text=(players[1] + " wins!"))

            elif check_winner() == 'tie':
                label.config(text=("no winner"))


def check_winner():

    for row in range(3):
        if game_btns[row][0]['text']==game_btns[row][1]['text']==game_btns[row][2]['text']!="":
            return True

    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            return True

    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
            return True
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
            return True

        #if there are no impty spaces left
    if check_emptyspaces() == False:
            for row in range(3):
                for col in range(3):
                    game_btns[row][col].config(bg='red')

            return 'tie'

    else:
            return False

def check_emptyspaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text']!="":
                spaces-=1

    if spaces == 0:
        return False
    else:
        return True


def start_newgame():
    global player
    player = random.choice(players)

    label.config(text=(player +"turn"))

    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="",bg="white")


frame = Tk()
frame.title("Tic-Tac-Toe Game")

players = ["x","o"]
player = random.choice(players)

game_btns =[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
label= Label(frame,text=(player + " turn"),bg="blue",fg="white",font=('consolas',40))
label.pack(side="top")

restart_button= Button(frame,text="restart" ,font=('consolas',20),command=start_newgame)
restart_button.pack()


btns_frame = Frame(frame)
btns_frame.pack()

for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btns_frame,text="",font=('consolas',50),width=4,height=1,
                                      command=lambda row=row , col=col: next_turn(row,col))
        game_btns[row][col].grid(row=row,column=col)

frame.mainloop()