from tkinter import *
from tictactoe import *
import tkinter.messagebox
import random
import copy



## Skeleton implementation of player class, want to get rid of global state but I might
## Be stuck with building a "GlobalStateContainer" class for the board, players, and current player.
## Which isn't necessarily better
class Player:
    def __init__(self, mark, player):
        self._mark = mark
        self._player = player
## Global board state, player state, and scores - this is a target for refactoring. 
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


##Creates the main window object.
window.title("Tic Tac Toe")
window.geometry("400x200")

v = StringVar()
Label(window, textvariable=v,pady=10).pack()
v.set("Tic Tac Toe")

btn=[]

class FirstPlayerDialog:
    def __init__(self, parent):
        
        ## Displays a new top-level window.
        top = self.top = Toplevel(parent)

        ##Draws the text entry label. "Packs" it to top (first argument)
        Label(top, text="Pick a number between 1 and 100 to see who goes first").pack()
        b = Button(top, text ="OK", command=self.ok)
        b.pack(pady=5, side="bottom")
        self.e = Entry(top)
        self.e.pack(padx=5)

    ##Input validation, forces player input to be 50 if they don't submit a valid number.

    def validate_player_guess(self, guess):
        value = 0
        try:
            value = int(guess)
        except:
            value = 50
        return value

    ## Tests the player's guess against a random number 1/100. A second number 1/100 is generated for the "computer's guess"
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
    
    ##Defines our method for what happens when the user clicks the ok button.
    def ok(self):

        player_guess = self.validate_player_guess(self.e.get())
        self.determine_first_player(player_guess)
        self.top.destroy()

class BoardButton():
    ##Creates a board button in a given position. Cleverly here - it appends to the global btn array to determine it's own position.
    def __init__(self,row_frame,b):
        global btn
        self.position= len(btn)
        btn.append(Button(row_frame, text=b, relief=GROOVE, width=2,command=lambda: self.callPlayMove()))
        btn[self.position].pack(side="left")

    ##Just a wrapper for the play move function.

    def callPlayMove(self):
        global scores
        PlayMove(self.position)

##Draws the Score Board. Originally intended as a class implementation.

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

    ##Creates a new BoardButton for every cell in BoardValue, creates a new Frame whenever we've added 3 buttons

    for i, b in enumerate(BoardValue):
        global btn
        if i%3 == 0:
            row_frame = Frame(window)
            row_frame.pack(side="top")
        BoardButton(row_frame,b)
    ScoreFrame(window)

    ## ai_move() call here in case the ai goes first
    
    if ai_on:
        ai_move()
        #btn.append(Button(row_frame, text=b, relief=GROOVE, width=2))
        #btn[i].pack(side="left")
def compatibility_flip_player(cur_play, player1, player2):
    internal_player1 = copy.deepcopy(player1)
    internal_player2 = copy.deepcopy(player2)
    internal_cur_play = copy.deepcopy(cur_play)
    returned_player = {}

    pass_cur_play = (internal_cur_play['mark'], internal_cur_play['player'])
    pass_player1 = (internal_player1['mark'], internal_player1['player'])
    pass_player2 = (internal_player2['mark'], internal_player2['player'])

    new_play = flip_player(pass_cur_play, pass_player1, pass_player2)
    returned_player['mark'] = new_play[0]
    returned_player['player'] = new_play[1]

    return returned_player

##Turns the player dictionaries into tuples. Going to be needed behavior in a more class
##Based version
def compatibility_playerdicts_to_tuples(cur_play, player1, player2):
    internal_player1 = copy.deepcopy(player1)
    internal_player2 = copy.deepcopy(player2)
    internal_cur_play = copy.deepcopy(cur_play)
    cur_play_tuple = (internal_cur_play["mark"], internal_cur_play['player'])
    player1_tuple = (internal_player1['mark'], internal_player1['player'])
    player2_tuple = (internal_player2['mark'], internal_player2['player'])
    return { "cur_play": cur_play_tuple, "player1": player1_tuple, "player2": player2_tuple}


def ai_move():
    global cur_play
    global player1
    global player2
    global BoardValue

    ##Ensures that it's the AI's turn, this is important because it lets you call ai_move() from wherever you want
    ##in the event loop, without giving the AI extra turns.
    if cur_play['player']== "cpu":
        print("AI MOVING")
        ##Calls the minimax optimizer from tictactoe.py and makes a move. (Modifies board state)
        compatibility_players = compatibility_playerdicts_to_tuples(cur_play, player1, player2)
        BoardValue[minimax(BoardValue, compatibility_players["cur_play"], compatibility_players["player1"], compatibility_players["player2"])[1]] = cur_play['mark']

        ##Flips the player giving control back to the player.

        cur_play = compatibility_flip_player(cur_play, player1, player2)
        print("END AI MOVE")
    else:
        return

##For every button in array, set the button text to the board state value.
def UpdateBoard():
    for i, b in enumerate(BoardValue):
        global btn
        btn[i].config(text=b)
    ##Updating the board automatically updates variable displays. (The scoreboard)
    window.update_idletasks

def PlayMove(position_clicked):
    ##Lots of global state here, global state bad.
    global BoardValue
    global cur_play
    global player1
    global player2
    global ai_on
    global x_score
    global o_score
    global scores


    if BoardValue[position_clicked] == '-':
        print("PLAYER BLOCK")
        ##Makes the move by updating board state
        BoardValue[position_clicked] = cur_play['mark']

        ##Flips current player between player 1 and player 2
        cur_play = compatibility_flip_player(cur_play, player1, player2)

        if ai_on and not check_for_winner(BoardValue) and not check_if_tie(BoardValue):
            ai_move()
            UpdateBoard()
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Move Already Played")

    ##Checks for our winner, updates score human/cpu, and asks if the player would like to play again.

    winner = check_for_winner(BoardValue)
    tie = check_if_tie(BoardValue)
    if winner:
        if player1['mark'] == winner:
            scores[player1['player']] += 1
        else:
            scores[player2['player']] += 1
        x_score.set(str(scores[player1['player']]))
        o_score.set(str(scores[player2['player']]))

        ##Creates a dialog box asking if the user would like to play again
        retry = tkinter.messagebox.askquestion("Tic Tac Toe", winner + " Wins! Play again?")
        if retry == 'yes':
            BoardValue = ["-","-","-","-","-","-","-","-","-"]
            dialog = FirstPlayerDialog(window)

            #Wait_window disrupts the main event loop until the created window is destroyed.
            window.wait_window(dialog.top)
            ai_move()
            UpdateBoard()
            window.update()

        else:
            #Closes the application
            window.destroy()
    elif tie:
        ##Same thing as win condition, except without updating the score. 

        retry = tkinter.messagebox.askquestion("Tic Tac Toe", "Tie Game, play again?")
        if retry == 'yes':
            BoardValue = ["-","-","-","-","-","-","-","-","-"]
            dialog = FirstPlayerDialog(window)
            window.wait_window(dialog.top)
            ai_move()
            UpdateBoard()
        else:
            window.destroy()
        print("END PLAYER BLOCK")
dialog = FirstPlayerDialog(window)
window.lift()
window.attributes()
window.wait_window(dialog.top)
DrawBoard()
window.mainloop()
