# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data['board']
    except (FileNotFoundError, json.JSONDecodeError):
        return blank_board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    with open(filename, 'w') as file:
        json.dump({"board": board}, file)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    for row in range(3):
        print(f" {board[row * 3]} | {board[row * 3 + 1]} | {board[row * 3 + 2]} ")
        if row < 2:
            print("---+---+---")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    x_count = board.count(X)
    o_count = board.count(O)
    return x_count == o_count

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    while not game_done(board, True):
        display_board(board)
        turn = X if is_x_turn(board) else O
        move = input(f"Player {turn}, choose a position (1-9) or 'q' to quit: ")
        if move.lower() == 'q':
            print("Game saved.")
            return True
        if move.isdigit():
            pos = int(move) - 1
            if 0 <= pos < 9 and board[pos] == BLANK:
                board[pos] = turn
                save_board('tic_tac_toe.json', board)
            else:
                print("Invalid move. Try again.")
        else:
            print("Invalid input. Try again.")
    print("Game over.")
    return False

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# The file read code, game loop code, and file close code goes here.
if __name__ == "__main__":
    filename = 'tic_tac_toe.json'
    current_board = read_board(filename)
    while True:
        if not play_game(current_board):
            current_board = blank_board['board']  # Reset for a new game
            save_board(filename, current_board)