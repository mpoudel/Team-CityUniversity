#-----Global Variables -------#

#Game Board

#if game is still going
game_still_going = True

#who won? or tie?
winner = None

#who's turn is it

current_player="X"



board = ["-","-","-",
         "-","-","-",
         "-","-","-"]


# Shows the board
def display_board():
    print(board[0] + " | " + board[1] + "  |  " + board[2] + "  |  ")
    print(board[3] + " | " + board[4] + "  |  " + board[5] + "  |  ")
    print(board[6] + " | " + board[7] + "  |  " + board[8] + "  |  ")
#Play a game of tic tac toe
def play_game():
    #driving function
    #display initial board state
    display_board()

    #while the game is still going
    while game_still_going: 

        #handle a single turn of an arbitrary player
        handle_turn(current_player)


        #check if the game has ended
        check_if_game_over()
        
        #Flip to other player
        flip_player()

# The game has ended
    if winner == "X" or winner == "O": 
        print(winner + " won.")
    elif winner == None:
        print("Tie.")



#Handle a single turn of an arbitrary player
def handle_turn(current_player):
    position = input("Choose a position from 1 to 9: ")
    position = int(position) - 1 

    board[position] = current_player

    display_board()

#see if hte game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    #set up global variable
    global winner

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else: #there was no win
        winner = None
    return




def check_rows():
    #set global
    global game_still_going
    #check if any of the rows have the same value and is not empty
    row_1 = board[0] == board[1] == board[2] !="-"
    row_2 = board[3] == board[4] == board[5] !="-"
    row_3 = board[6] == board[7] == board[8] !="-"
    # if any row has a match flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
 #set global
    global game_still_going
    #check if any of the rows have the same value and is not empty
    column_1 = board[0] == board[3] == board[6] !="-"
    column_2 = board[1] == board[4] == board[7] !="-"
    column_3 = board[2] == board[5] == board[8] !="-"
    # if any row has a match flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    #return winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
     #set global
    global game_still_going
    #check if any of the diagonals_have the same value and is not empty
    diagonals_1 = board[0] == board[4] == board[8] !="-"
    diagonals_2 = board[6] == board[4] == board[2] !="-"
    # if any diagonals_ has a match flag that there is a win
    if diagonals_1 or diagonals_2:
        game_still_going = False
    #return winner (X or O)
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return


def check_if_tie():
    return

def flip_player():
    return


play_game()




# board
#display board
# play game
# create ai
#handle turn
    #check rows
    #check colmn
    #check diagonals
#check tie
#flip player

