"""
Flood fill type game by Matthew Warren
Made for recursion practice.
Last updated Oct 24, 2014
"""

import sys
import random
import time


def randomize():
    """
    Fill each block in the board with a random color from the color list.
    """
    for x in range(0, 18):
        for y in range(0, 18):
            board[x][y] = random.choice(fill_colors)


def draw_board():
    """
    Draw the game board to the screen.
    """
    print chr(27) + "[2J"
    print "Try changing the color in the upper left."
    print "See how many turns it takes to get to a single color!"
    print "turns: %d" % turns
    count = 1
    for x in board:
        for y in x:
            if count % 18 == 0:
                sys.stdout.write(y)
                sys.stdout.write('\n')
            else:
                sys.stdout.write(y)
            
            count += 1


def flood_fill(row, column, color):
    """
    Flood fill selected block(s) with designated color. If block is already the 
    same color as target color, do nothing. Otherwise, fill selected block plus
    recursively fill bordering blocks until finished.
    """
    current_color = board[row][column]
    if current_color == color:
        return
    
    board[row][column] = color

    #check left
    if column > 0:
        if board[row][(column - 1)] == current_color:
            flood_fill(row, (column - 1), color)
            
    # check right
    if column < 17:
        if board[row][(column + 1)] == current_color:
            flood_fill(row, (column + 1), color)
            
    # check up
    if row > 0:
        if board[(row - 1)][column] == current_color:
            flood_fill((row - 1), column, color)
            
    # check down
    if row < 17:
        if board[(row + 1)][column] == current_color:
            flood_fill((row + 1), column, color)


"""
# left over code, lets player choose block to change
def get_row():
    while True:
        draw_board()
        print ""
        print "Pick a row. (1-18, top row is 1)"
        row = int(raw_input("row: "))
        if row not in valid_nums:
            draw_board()
            print ""
            print ""
            print "Please pick a row within range."
            time.sleep(1.5)
            continue
        else:
            return (row - 1)
    
def get_column():
    while True:
        draw_board()
        print ""
        print "Pick a column (1-18, left column is 1)"
        column = int(raw_input("column: "))
        if column not in valid_nums:
            draw_board()
            print ""
            print ""
            print "Please pick a row within range."
            time.sleep(1.5)
            continue
        else:
            return (column - 1)
"""


def get_color():
    """
    Ask player what color they wish to fill with.
    Returns: Integer
    """
    while True:
        draw_board()
        print "Pick a color (by number). Valid colors are (0)black, (1)red,"
        print "(2)green, (3)yellow, (4)blue, (5)magenta, (6)cyan, and (7)white."
        color = raw_input("color: ")
        if color not in ['0', '1', '2', '3', '4', '5', '6', '7']:
            print chr(27) + "[2J"
            draw_board()
            print ""
            print "Please pick a valid color."
            time.sleep(1.5)
            continue
        else:
            return int(color)


def play_again():
    """
    Ask player if they wish to play again or not.
    Returns: Boolean
    """
    while True:
        draw_board()
        print ""
        print "Play again? (yes or no)"
        play = raw_input("> ")
        if play.lower().startswith('y'):
            return True
        else:
            return False
        
        
def check_win():
    """
    Check for winning condition. If all blocks are the same color, return
    True.
    Returns: Boolean
    """
    color = board[0][0] # color of block 0, 0
    count = 0
    for x in range(0, 18):
        for y in range(0, 18):
            if board[x][y] == color:
                count += 1
    
    if count == 324: # 18 x 18
        return True
    else:
        return False

    
# constants

black = chr(27) + '[30m' + u'\u2588\u2588' + chr(27) + '[0m'
red = chr(27) + '[31m' + u'\u2588\u2588' + chr(27) + '[0m'
green = chr(27) + '[32m' + u'\u2588\u2588' + chr(27) + '[0m'
yellow = chr(27) + '[33m' + u'\u2588\u2588' + chr(27) + '[0m'
blue = chr(27) + '[34m' + u'\u2588\u2588' + chr(27) + '[0m'
magenta = chr(27) + '[35m' + u'\u2588\u2588' + chr(27) + '[0m'
cyan = chr(27) + '[36m' + u'\u2588\u2588' + chr(27) + '[0m'
white = chr(27) + '[37m' + u'\u2588\u2588' + chr(27) + '[0m'

fill_colors = [black, red, green, yellow, blue, magenta, cyan, white]

"""    
valid_nums = []

for x in range(1, (len(board) + 1)):
    valid_nums.append(x)
"""

# main game loop
while True:
    board = [[black] * 18 for x in range(18)] # initialize 18x18 grid
    
    randomize() # randomly colorize grid
    turns = 0
    
    while True:
        #row = get_row()
        #column = get_column()
        color = get_color()
    
        flood_fill(0, 0, fill_colors[color]) # flood fill with player color
        turns += 1
        
        if check_win(): # check for win
            break

    draw_board()
    print ""
    print "Congratulations! You Win!"
    time.sleep(3.5)
    
    if play_again():
        continue
    else:
        break
    
print chr(27) + "[2J"
print ""
print "Thanks for playing!"
print ""
