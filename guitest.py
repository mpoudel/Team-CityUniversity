from tkinter import *
from tictactoe import *
import tkinter.messagebox

BoardValue = ["-","-","-","-","-","-","-","-","-"]
player1 = ("X", "human")
player2 = ("O", "cpu")
ai_on = True
cur_play = player1

window = Tk()
window.title("Noughts And Crosses")
window.geometry("10x200")

v = StringVar()
Label(window, textvariable=v,pady=10).pack()
v.set("Noughts And Crosses")

btn=[]
class BoardButton():
    def __init__(self,row_frame,b, cur_play, player1, player2):
        global btn
        self.position= len(btn)
        btn.append(Button(row_frame, text=b, relief=GROOVE, width=2,command=lambda: self.callPlayMove()))
        btn[self.position].pack(side="left")

    def callPlayMove(self):
        PlayMove(self.position)

def DrawBoard():
    for i, b in enumerate(BoardValue):
        global btn
        if i%3 == 0:
            row_frame = Frame(window)
            row_frame.pack(side="top")
        BoardButton(row_frame,b, cur_play, player1, player2)
        #btn.append(Button(row_frame, text=b, relief=GROOVE, width=2))
        #btn[i].pack(side="left")

def UpdateBoard():
    for i, b in enumerate(BoardValue):
        global btn
        btn[i].config(text=b)

def PlayMove(positionClicked):
    global BoardValue
    global cur_play
    global player1
    global player2
    global ai_on
    if BoardValue[positionClicked] == '-':
        BoardValue[positionClicked] = cur_play[0]
        cur_play = flip_player(cur_play, player1, player2)
        if ai_on:
            BoardValue[minimax(BoardValue, cur_play, player1, player2, {})[1]] = cur_play[0]
            cur_play = flip_player(cur_play, player1, player2)
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Tie", "Move Already Played")
        UpdateBoard()
    if check_for_winner(BoardValue):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Someone Won!")

DrawBoard()
window.mainloop()
