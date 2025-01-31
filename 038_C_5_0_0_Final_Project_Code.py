#!/usr/bin/env python3
#Madeline Garner

#Final Project: Tic-Tac-Toe Game

import random #Random is for the computer to generate a random number for X moves
import sys #Sys is so sys.exit() can be used to quit program smoothly

user_wins = 0
computer_wins = 0   #Initializing variables of win and tie records
ties = 0

def beginning_options(): #Function to greet user and give options to begin game, search files, or quit
    print("\nWelcome to a game of Tic Tac Toe!")
    print("\nYour moves will be marked by O and the computer's moves will be marked by X.")
    print("\nWould you like to:")
    print("1. Begin a new game")
    print("2. Search existing player files")
    print("3. Quit")

    while True:
        choice = input("\nPlease enter 1, 2, or 3: ")
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

def player_name(): #Function to enter player name, also used for searching files
    player_1 = input("\nPlease enter your name: ")
    player_2 = "Computer AI"
    print("Player 1:", player_1)
    print("Player 2:", player_2)
    return player_1, player_2

def game_board(board): #Function to create Tic Tac Toe board
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

def available_spaces(board): #Function to check for available spaces in the board
    available = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                available.append((row, col)) #adds open space to available list
    return available

def winner_check(board, player_mark): #Function checks for a winner
    '''
    This first checks each row to see if all 3 spaces have "O"s for the user to win,
    or if all 3 spaces have "X"s for the computer to win. Then it does the same for
    the columns. Then it checks from diagonal top left to bottom right, then lastly
    it checks diagonal from top right to bottom left.
    '''
    for row in range(3):
        if board[row][0] == player_mark and board[row][1] == player_mark and board[row][2] == player_mark:
            return True
    for col in range(3):
        if board[0][col] == player_mark and board[1][col] == player_mark and board[2][col] == player_mark:
            return True
    if board[0][0] == player_mark and board[1][1] == player_mark and board[2][2] == player_mark:
        return True
    if board[0][2] == player_mark and board[1][1] == player_mark and board[2][0] == player_mark:
        return True
    return False

def save_record(player_1, player_2, outcome, wins): #Function to save game outcome to text file
    with open(f"{player_1}_vs_{player_2}_record.txt", "a") as file:
        #the f in front of the string adds the names of the players.
        #opens file in append mode, opens file so it can be added to or creates it
        #if it doesn't exist
        file.write(f"{outcome}: {wins}\n") #adds this string to the end of file

def load_record(player_1, player_2): #Function to search previous player files
    try:
        #tries to open a file with the entered player name
        with open(f"{player_1}_vs_{player_2}_record.txt", "r") as file:
            #opens file in reading mode
            record_lines = file.readlines() #reads all lines in file and stores the list of strings to record_lines variable

            '''
            adds total of user wins, computer wins, and ties based on the strings
            read in the file. For example when the file reads the lines and then
            stores them in record_lines, then the following 3 lines of code count
            how many times each outcome appears in the file.
            '''
            user_wins = sum("User wins" in line for line in record_lines)
            computer_wins = sum("Computer wins" in line for line in record_lines)
            ties = sum("Tie" in line for line in record_lines)
            
            #prints out records of wins and ties for that file
            print("\nRecord:")
            print(f"\nUser wins: {user_wins}")
            print(f"Computer wins: {computer_wins}")
            print(f"Ties: {ties}")
    except FileNotFoundError:
        #if the file does not exist it will print that it was not found
        print("\nNo record found.")

def enter_move(board): #Function for user to enter their moves
    while True:
        move = input("\nEnter your move (1-9 or 'quit' to exit): ")
        if move.lower() == 'quit':
            print("\nThanks for playing. Goodbye!")
            sys.exit()
        elif move.isdigit() and len(move) == 1 and 1 <= int(move) <= 9:
            #checks if move is a single digit and is within 1-9
            move = int(move) - 1 #subtracts 1 since board indexes start with 0
            row = move // 3
            col = move % 3
            '''
            If the user enters 9 as their move then 1 would be subracted (now 8).
            The row is determined using floor division by 3 (number of rows).
            8 // 3 is row 2
            (there are rows 0, 1, and 2 so this move is in the bottom most row)

            Then the column is move modulo 3 (number of columns).
            8 % 3 is col 2 (the columns also go from 0, 1, and 2,
            so this move would be in the farthest right column).

            This means the user move is in the bottom right corner, which is
            marked as space 9.
            '''
            if board[row][col] not in ['X', 'O']:
                #checks if space is not taken
                return row, col
            else:
                print("\nThat position is already taken. Try again.")
        else:
            print("\nInvalid input. Please enter a number from 1 to 9 or 'quit' to exit.")

def tic_tac_toe_game(player_1, player_2): #Function to run game moves, updating board, and winner checking
    global user_wins, computer_wins, ties
    #makes win variables adjustable inside functions and can be accessed out of it
    
    while True:
        board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        computer_row, computer_col = 1, 1
        board[computer_row][computer_col] = 'X'
        #numbers rows and columns, places first computer move X at middle (5)
        game_board(board)

        available = available_spaces(board)
        
        while len(available): #while there are available spaces, user can enter a move
            row, col = enter_move(board)
            board[row][col] = 'O' #user moves are marked with O
            game_board(board)

            if winner_check(board, 'O'):
                print("\nYou win!")
                user_wins += 1
                save_record(player_1, player_2, "\nUser wins", user_wins)
                #uses winner_check function and determines user wins
                #adds 1 to user win count
                #uses save record function to save player names and adds user win to a file
                break
            
            available = available_spaces(board)
            if not available: #checks for tie
                print("\nIt's a tie!")
                ties += 1
                save_record(player_1, player_2, "\nTie", ties)
                break
            
            computer_row, computer_col = random.choice(available)
            board[computer_row][computer_col] = 'X'
            #Computer plays random move
            game_board(board)

            if winner_check(board, 'X'): #determines if computer won
                print("\nComputer wins!")
                computer_wins += 1
                save_record(player_1, player_2, "\nComputer wins", computer_wins)
                break

            available.remove((computer_row, computer_col))
            #removes computer move from available spaces

        if not available: #Tie if no available spaces and if user hasn't won
            print("\nIt's a tie!")
            ties += 1
            save_record(player_1, player_2, "Tie", ties)

        while True:
            play_again = input("\nDo you want to play again? (y/n): ")
            if play_again.lower().startswith('y'):
                break #if user plays again this will start game loop over again
            elif play_again.lower().startswith('n'):
                print("\nThanks for playing!")
                sys.exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


# Main game loop
while True:
    choice = beginning_options() #calls beginning_options function
    if choice == '1':
        player_1, player_2 = player_name()
        tic_tac_toe_game(player_1, player_2)
        '''
        if user chooses to play, player names are added to the new game and
        the game tic_tac_toe_game function is played using them, which will
        add those names and the outcomes to a file.
        '''
    elif choice == '2':
        player_1, player_2 = player_name()
        load_record(player_1, player_2)
        '''
        if user chooses to search previous file records, they will enter the
        player name and then the load_record function will search and display
        information about that game file if it exists.
        '''
    elif choice == '3': #option to quit before starting
        print("\nThanks for playing. Goodbye!")
        sys.exit()
