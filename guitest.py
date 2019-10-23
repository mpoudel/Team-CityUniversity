from tkinter import *
from tictactoe import *
import tkinter.messagebox
import random

BoardValue = ["-","-","-","-","-","-","-","-","-"]
player1 = ("X", "human")
player2 = ("O", "cpu")
ai_on = True
cur_play = player1
scores = { "X": 0, "O": 0 }

window = Tk()
x_score = tkinter.StringVar()
o_score = tkinter.StringVar()
x_score = 0
o_score = 0
window.title("Tic Tac Toe")
window.geometry("400x200")

v = StringVar()
Label(window, textvariable=v,pady=10).pack()
v.set("Tic Tac Toe")

btn=[]
scores = {}
class FirstPlayerDialog:
    def __init__(self, parent):

        top = self.top = Toplevel(parent)
        Label(top, text="Pick a number between 1 and 100 to see who goes first").pack()
        b = Button(top, text ="OK", command=self.ok)
        b.pack(pady=5, side="bottom")
        self.e = Entry(top)
        self.e.pack(padx=5)
    def validate_player_guess(self, guess):
        value = 0
        try:
            value = int(guess)
        except:
            value = 50
        return value
    def determine_first_player(self, player_guess):
        global cur_play
        global player1
        global player2
        test_against = random.randint(0,100)
        computer_guess = random.randint(0,100)
        computer_guess = test_against - computer_guess
        player_guess = test_against - player_guess
        if abs(computer_guess) < abs(player_guess):
            temp = player2
            player2 = player1
            player1 = temp
            cur_play = player1
            print("CPU is first player")
            return
        else:
            print("Human is first player")
            return
    def ok(self):

        player_guess = self.validate_player_guess(self.e.get())
        self.determine_first_player(player_guess)
        self.top.destroy()

class BoardButton():
    def __init__(self,row_frame,b):
        global btn
        self.position= len(btn)
        btn.append(Button(row_frame, text=b, relief=GROOVE, width=2,command=lambda: self.callPlayMove()))
        btn[self.position].pack(side="left")

    def callPlayMove(self):
        PlayMove(self.position)

def ScoreFrame(parent):
    global x_score
    global o_score
    frame = Frame(parent)
    frame.pack(side="bottom")
    x_label = Label(frame, text="X score: ").pack(side="top")
    o_label = Label(frame, text="O score: ").pack(side="bottom")
    x_score_value = Label(x_label, textvariable=x_score).pack(side="right")
    o_score_value = Label(frame, textvariable=o_score).pack(side="right")


def DrawBoard():
    global BoardValue
    global cur_play
    global player1
    global player2
    global x_score
    global o_score
    if ai_on:
        ai_move()
    for i, b in enumerate(BoardValue):
        global btn
        if i%3 == 0:
            row_frame = Frame(window)
            row_frame.pack(side="top")
        BoardButton(row_frame,b)
    ScoreFrame(window)
        #btn.append(Button(row_frame, text=b, relief=GROOVE, width=2))
        #btn[i].pack(side="left")

def ai_move():
    global cur_play
    global player1
    global player2
    global BoardValue
    if cur_play[1] == "cpu":
        BoardValue[minimax(BoardValue, cur_play, player1, player2)[1]] = cur_play[0]
        cur_play = flip_player(cur_play, player1, player2)
    else:
        return
def UpdateBoard():
    for i, b in enumerate(BoardValue):
        global btn
        btn[i].config(text=b)
    window.update_idletasks

def PlayMove(positionClicked):
    global BoardValue
    global cur_play
    global player1
    global player2
    global ai_on
    global scores
    global x_score
    global o_score
    if BoardValue[positionClicked] == '-':
        BoardValue[positionClicked] = cur_play[0]
        cur_play = flip_player(cur_play, player1, player2)
        if ai_on and not check_for_winner(BoardValue) and not check_if_tie(BoardValue):
            ai_move()
            UpdateBoard()
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Tie", "Move Already Played")
    winner = check_for_winner(BoardValue)
    tie = check_if_tie(BoardValue)
    if winner:
        retry = tkinter.messagebox.askquestion("Tic Tac Toe", winner + " Wins! Play again?")
        if retry == 'yes':
            scores[winner] += 1
            x_score = scores["X"]
            o_score = scores["O"]
            BoardValue = ["-","-","-","-","-","-","-","-","-"]
            cur_play = player1
            ##cur_play = flip_player(cur_play, player1, player2)
            ai_move()
            UpdateBoard()

        else:
            window.destroy()
    elif tie:
        retry = tkinter.messagebox.askquestion("Tic Tac Toe", "Tie Game, play again?")
        if retry == 'yes':
            BoardValue = ["-","-","-","-","-","-","-","-","-"]
            ##cur_play = flip_player(cur_play, player1, player2)
            cur_play = player1
            ai_move()
            UpdateBoard()
        else:
            window.destroy()
dialog = FirstPlayerDialog(window)
window.lift()
window.attributes("-topmost", True)
window.wait_window(dialog.top)
DrawBoard()
window.mainloop()
