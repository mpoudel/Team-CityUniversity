from tkinter import *
from tictactoe import *
import tkinter.messagebox
import random
import copy

BoardValue = ["-","-","-","-","-","-","-","-","-"]
player1 = {"mark": "X", "player":"human"}
player2 = {"mark": "O", "player": "cpu"}
ai_on = True
cur_play = copy.deepcopy(player1)
scores = dict()
scores["cpu"] = 0
scores["human"] = 0
window = Tk()

x_score = tkinter.StringVar()
o_score = tkinter.StringVar()
x_score.set(str(0))
o_score.set(str(0))
window.title("Tic Tac Toe")
window.geometry("400x200")

v = StringVar()
Label(window, textvariable=v,pady=10).pack()
v.set("Tic Tac Toe")

btn=[]
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
            player1 = { 'mark': "O", 'player': "human"}
            player2 = { 'mark': "X", 'player': "cpu"}
            cur_play = copy.deepcopy(player2)
            print("CPU is first player")
            return
        else:
            player1 = {'mark': "X", 'player': "human"}
            player2 = {'mark': "O", 'player': "cpu"}
            cur_play = copy.deepcopy(player1)
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
        global scores
        PlayMove(self.position)

def ScoreFrame(parent):
    global x_score
    global o_score
    xframe = Frame(parent)
    oframe = Frame(parent)
    xframe.pack(side="bottom")
    oframe.pack(side="bottom")
    x_label = Label(xframe, text="Your  score: ").pack(side="left")
    o_label = Label(oframe, text="CPU score: ").pack(side="left")
    x_score_value = Label(xframe, textvariable=x_score).pack(side="right")
    o_score_value = Label(oframe, textvariable=o_score).pack(side="right")


def DrawBoard():
    global BoardValue
    global cur_play
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
    internal_player1 = copy.deepcopy(player1)
    internal_player2 = copy.deepcopy(player2)
    pass_cur_play = (cur_play['mark'], cur_play['player'])
    pass_player1 = (internal_player1['mark'], internal_player1['player'])
    pass_player2 = (internal_player2['mark'], internal_player2['player'])
    if cur_play['player']== "cpu":
        print("AI MOVING")
        BoardValue[minimax(BoardValue, pass_cur_play, pass_player1, pass_player2)[1]] = cur_play['mark']
        new_play = flip_player(pass_cur_play, pass_player1, pass_player2)
        cur_play['mark'] = new_play[0]
        cur_play['player'] = new_play[1]
        print("END AI MOVE")
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
    global x_score
    global o_score
    global scores
    internal_player1 = copy.deepcopy(player1)
    internal_player2 = copy.deepcopy(player2)
    if BoardValue[positionClicked] == '-':
        print("PLAYER BLOCK")
        BoardValue[positionClicked] = cur_play['mark']
        pass_cur_play = (cur_play['mark'], cur_play['player'])
        pass_player1 = (internal_player1['mark'], internal_player1['player'])
        pass_player2 = (internal_player2['mark'], internal_player2['player'])
        new_play = flip_player(pass_cur_play, pass_player1, pass_player2)
        cur_play['mark'] = new_play[0]
        cur_play['player'] = new_play[1]
        if ai_on and not check_for_winner(BoardValue) and not check_if_tie(BoardValue):
            ai_move()
            UpdateBoard()
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Move Already Played")
    winner = check_for_winner(BoardValue)
    tie = check_if_tie(BoardValue)
    if winner:
        if player1['mark'] == winner:
            scores[player1['player']] += 1
        else:
            scores[player2['player']] += 1
        x_score.set(str(scores[player1['player']]))
        o_score.set(str(scores[player2['player']]))
        retry = tkinter.messagebox.askquestion("Tic Tac Toe", winner + " Wins! Play again?")
        if retry == 'yes':
            BoardValue = ["-","-","-","-","-","-","-","-","-"]
            dialog = FirstPlayerDialog(window)
            window.wait_window(dialog.top)
            ##cur_play = flip_player(cur_play, player1, player2)
            ai_move()
            UpdateBoard()
            window.update()

        else:
            window.destroy()
    elif tie:
        retry = tkinter.messagebox.askquestion("Tic Tac Toe", "Tie Game, play again?")
        if retry == 'yes':
            BoardValue = ["-","-","-","-","-","-","-","-","-"]
            ##cur_play = flip_player(cur_play, player1, player2)
            dialog = FirstPlayerDialog(window)
            window.wait_window(dialog.top)
            ai_move()
            UpdateBoard()
        else:
            window.destroy()
        print("END PLAYER BLOCK")
dialog = FirstPlayerDialog(window)
window.lift()
window.attributes("-topmost", True)
window.wait_window(dialog.top)
DrawBoard()
window.mainloop()
