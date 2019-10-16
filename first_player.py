##Author Marvin G.
##Name: first_player.py
##Date: 15 OCT 2019
##Description 

#Need to choose who plays first, that person will be X. Second player will be 0. Need to set the global
#state to show that there is no player one yet.

##----------------------------Imported Modules?---------------------------------##
#need to import random function in order to allow for the computer and the magic number to roll
import random
#the math function is needed to evaluate the absolute value
import math


##---------------------------Global variable delcarations-------------------------##
#On initialization there is no first player chosen, so the value is set to false
first_player_chosen= False
#on init the CPU does not have a value, therefore it is set to 0
cpu_number = 0
#on init player has no value, set to zero
player_number = 0
#on init magic number set to 0
magic_number = 0
#the absolute value of the difference between the playeer number and the magic number
player_comparitor = abs( player_number - magic_number )
#the absolute value of the differece between the cpu number and themagic number
cpu_comparitor = abs( cpu_number - magic_number)

player_goes_first = False

##-----------------------------Function Definitions--------------------------------##

def player_choice():
    #access to the players inputted value
    global player_number
    #access to the difference between the magic number and the players input
    global player_comparitor
    #player choses a number between 1 and 10
    player_number = int(input("Choose a number between 1 and 10: "))
    valid = False
    while not valid:
        if player_number not in range(1,10):
            player_number = int(input("Invalid input. Choose a number between 1 and 10: "))
        else:
            valid = True
        
    else:
        valid = False

    #player comparitor is the absolute value of the difference between the player number and magic number
    
    player_comparitor = abs(player_number - magic_number)
    return

def cpu_choice():
    #allow access to the CPU comparitor
    global cpu_comparitor
    #allow to change CPU number globally
    global cpu_number
    #randomly rolls between 1 and 10 for cpu
    cpu_number = random.randint(1,10)
    cpu_comparitor = abs(cpu_number - magic_number) 
    #print("The CPU has rolled " + cpu_number)
    return

def magic_numberfier():
    #initialie the global variable
    global magic_number
    #roll for the random number 
    magic_number = (random.randint(1,10))
    #print("The magic number is: " + magic_number)
    return

def the_result():
    #these global variables are being use to evaluate who is closer

    #this is the absolute value of the  player number and the magic number
    global player_comparitor
    #this is the absolute value of the cpu number and the magic number
    global cpu_comparitor
    #the boolean that controls the loop, if the playe hasnt been chosen yet 
    global first_player_chosen
    #Need to have access to the value that the player goes first
    global player_goes_first

    #If the absolute value of the player comparitor is less than the aboslute value of the CPU comparitor
    #that means the player is closer to the magic number, thus the player goes first, X.
    if (player_comparitor < cpu_comparitor):  #and (player_comparitor != cpu_comparitor)
            print("The magic number was", magic_number, "You rolled" , player_number , "CPU Rolled" , cpu_number , "You go first, X")
            first_player_chosen = True
            #now set the first player to x
            player_goes_first = True
    #If the players comparitor is greater than the cpu's comparitor value that means the player is further away from the magic number, thus 
    # the player goes second.       
    elif player_comparitor > cpu_comparitor:
            print("The magic number was", magic_number, "You rolled" , player_number , "CPU Rolled" , cpu_number , "You go second, O")
            first_player_chosen = True
            #set the player to O
            player_goes_first = False
    else: 
            print("Looks like we had a tie! Do it again!!!")
    return 

def who_is_first():
    #controls the loop
    global first_player_chosen
    while first_player_chosen == False:
    #the magic number is chosen
        magic_numberfier() 

    #the player choses a number in the range
        player_choice()

    #cpu chooses a number in the range()
        cpu_choice()

    #computer generates a number
   

    #winner is evaluated
        the_result()



##--------------Run the program--------------------------##
who_is_first()


##---------------Test Statements-------------------------##
print("First player chosen: ", first_player_chosen)

##
##
##