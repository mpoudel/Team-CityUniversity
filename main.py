#-----Global Variables -------#

#Game Board

#if game is still going

#who won? or tie?

#who's turn is it

import copy
import random

# Shows the board
def display_board(cur_board):
    print(cur_board[0] + " | " + cur_board[1] + "  |  " + cur_board[2] + "  |  ")
    print(cur_board[3] + " | " + cur_board[4] + "  |  " + cur_board[5] + "  |  ")
    print(cur_board[6] + " | " + cur_board[7] + "  |  " + cur_board[8] + "  |  ")
#Play a game of tic tac toe
def play_game(cur_board, cur_play, play1, play2):
    #driving function
    #display initial board state
    display_board(cur_board)

    #while the game is still going
    while True: 

        #handle a single turn of an arbitrary player
        play1_copy = copy.deepcopy(play1)
        play2_copy = copy.deepcopy(play2)
        cur_board = handle_turn(cur_play, cur_board, play1_copy, play2_copy)

        display_board(cur_board)
        print("\n===============================================\n")
        print(empty_cells(cur_board))
        #check if the game has ended
        gameover = check_if_game_over(cur_board)
        if gameover:
            if gameover != "Tie":
                print("The winner is: " + gameover)
            else:
                print("The game was a tie")
            break

        
        #Flip to other player
        cur_play = flip_player(cur_play, play1, play2)


#Handle a single turn of an arbitrary player
def handle_turn(current_player, cur_board, player1, player2):
    new_board = copy.deepcopy(cur_board)
    # Warns the player if it enters number not between 1-9
    if current_player[1] == "human":
        position = input("Choose a position from 1 to 9: ")
        while (position not in ['1' , '2' , '3', '4', '5', '6', '7', '8', '9']) or new_board[int(position) - 1] != "-":
                print("Enter a Valid Number between 1 to 9 that doesn't already have a move made. Try again")
                position = input("Choose a position from 1 to 9: ")
        position = int(position) - 1
    else:
        position = ai_turn(cur_board, current_player, player1, player2)

    new_board[position] = current_player[0]
    return new_board


#see if hte game is over
def check_if_game_over(cur_board):
    winner = check_for_winner(cur_board)
    tie = check_if_tie(cur_board)
    if winner:
        return winner
    elif tie:
        return tie
    else:
        return False


def check_for_winner(cur_board):
    #set up global variable

    #check rows
    row_winner = check_rows(cur_board)
    #check columns
    column_winner = check_columns(cur_board)
    #check diagonals
    diagonal_winner = check_diagonals(cur_board)

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else: #there was no win
        winner = False
    return winner




def check_rows(cur_board):
    #set global
    #check if any of the rows have the same value and is not empty
    row_1 = cur_board[0] == cur_board[1] == cur_board[2] !="-"
    row_2 = cur_board[3] == cur_board[4] == cur_board[5] !="-"
    row_3 = cur_board[6] == cur_board[7] == cur_board[8] !="-"
    # if any row has a match flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return cur_board[0]
    elif row_2:
        return cur_board[3]
    elif row_3:
        return cur_board[6]
    return

def check_columns(cur_board):
 #set global
    #check if any of the rows have the same value and is not empty
    column_1 = cur_board[0] == cur_board[3] == cur_board[6] !="-"
    column_2 = cur_board[1] == cur_board[4] == cur_board[7] !="-"
    column_3 = cur_board[2] == cur_board[5] == cur_board[8] !="-"
    # if any row has a match flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    #return winner (X or O)
    if column_1:
        return cur_board[0]
    elif column_2:
        return cur_board[1]
    elif column_3:
        return cur_board[2]
    return

def check_diagonals(cur_board):
     #set global
    #check if any of the diagonals_have the same value and is not empty
    diagonals_1 = cur_board[0] == cur_board[4] == cur_board[8] !="-"
    diagonals_2 = cur_board[6] == cur_board[4] == cur_board[2] !="-"
    # if any diagonals_ has a match flag that there is a win
    if diagonals_1 or diagonals_2:
        game_still_going = False
    #return winner (X or O)
    if diagonals_1:
        return cur_board[0]
    elif diagonals_2:
        return cur_board[6]
    return


def check_if_tie(cur_board):
    if (not check_for_winner(cur_board)) and set(cur_board) == set({"X", "O"}):
        return "Tie"
    else:
        return False
def flip_player(current_player, player1, player2):
    if current_player == player1:
        return player2
    else:
        return player1
    return player2


def empty_cells(cur_board):
    empty_cells = []
    for i in range(len(cur_board)):
        if cur_board[i] == "-":
            empty_cells.append(i)
    return empty_cells

def ai_turn(cur_board, cur_play, play1, play2):
    print("AI TURN")
    play1_copy = copy.deepcopy(play1)
    play2_copy = copy.deepcopy(play2)
    return minimax(cur_board, cur_play, play1_copy, play2_copy)[1]
    
def minimax(cur_board, cur_play, player1, player2):
    potential_win = check_for_winner(cur_board)
    if potential_win:
        if potential_win == cur_play[0]:
            return (1, None)
        else:
            return (-1, None)

    move = -1
    score = -1
    available_moves = empty_cells(cur_board)
    for i in range(len(available_moves)):
        board_with_new_move = copy.deepcopy(cur_board)
        board_with_new_move[available_moves[i]] = cur_play[0]
        score_for_the_move = -minimax(board_with_new_move, flip_player(cur_play, player1, player2), player1, player2)[0]
        if score_for_the_move > score:
            score = score_for_the_move
            move = available_moves[i]
    if move == -1:
        return (0,0)
    return (score, move)

    





player1 = ("X", "human")
player2 = ("O", "cpu")
first_player = player1




board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

play_game(board, first_player, player1, player2)




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

