"""
Connect Four game clone by Matthew Warren
Inspired by: http://inventwithpython.com/chapter10.html
Thought I would try to tackle the next level of game complexity
Last updated Oct 21, 2014
"""

import random
import time


def print_board(board):
    """
    Draw the game board and all pieces currently in play.
    Board is a list containing either blank spaces (unicode empty circles) or,
    red or yellow solid circles. 43 entries. The first entry, 0, is not used
    and is only there to simplfy things (making the visible pieces' indices
    correspond 1 to 1 with their positions on the board.

    Keyword arguments:
    board -- list of pieces (strings)

    Returns: None
    """
    # the board
    top = u'\u2554' + (u'\u2550\u2550\u2550\u2564' * 6) +\
    u'\u2550\u2550\u2550\u2557'

    bottom = u'\u2569' + (u'\u2550\u2550\u2550\u2567' * 6) +\
    u'\u2550\u2550\u2550\u2569'

    upright = ' ' + u'\u2502' + ' '

    row_six = u'\u2551 ' + board[36] + upright + board[37] + upright + \
    board[38] + upright + board[39] + upright + board[40] + upright + \
    board[41] + upright + board[42] + u' \u2551'

    row_five = u'\u2551 ' + board[29] + upright + board[30] + upright + \
    board[31] + upright + board[32] + upright + board[33] + upright + \
    board[34] + upright + board[35] + u' \u2551'

    row_four = u'\u2551 ' + board[22] + upright + board[23] + upright + \
    board[24] + upright + board[25] + upright + board[26] + upright + \
    board[27] + upright + board[28] + u' \u2551'

    row_three = u'\u2551 ' + board[15] + upright + board[16] + upright + \
    board[17] + upright + board[18] + upright + board[19] + upright + \
    board[20] + upright + board[21] + u' \u2551'

    row_two = u'\u2551 ' + board[8] + upright + board[9] + upright + \
    board[10] + upright + board[11] + upright + board[12] + upright + \
    board[13] + upright + board[14] + u' \u2551'

    row_one = u'\u2551 ' + board[1] + upright + board[2] + upright + \
    board[3] + upright + board[4] + upright + board[5] + upright + \
    board[6] + upright + board[7] + u' \u2551'

    row_divider = u'\u255f' + (u'\u2500\u2500\u2500\u253c' * 6) +\
    u'\u2500\u2500\u2500\u2562'

    # banner is colored red and yellow by letter
    banner = chr(27) + '[31m' + 'C ' + chr(27) + '[33m' + 'O ' + \
    chr(27) + '[31m' + 'N ' + chr(27) + '[33m' + 'N ' + \
    chr(27) + '[31m' + 'E ' + chr(27) + '[33m' + 'C ' + \
    chr(27) + '[31m' + 'T' + '   ' + chr(27) + '[33m' + 'F ' + \
    chr(27) + '[31m' + 'O ' + chr(27) + '[33m' + 'U ' + \
    chr(27) + '[31m' + 'R ' + chr(27) + '[0m'

    print '     ' + banner
    print ""
    print "    1   2   3   4   5   6   7"
    print chr(27) + '[34m' + '  ' + top
    print '  ' + row_six
    print '  ' + row_divider
    print '  ' + row_five
    print '  ' + row_divider
    print '  ' + row_four
    print '  ' + row_divider
    print '  ' + row_three
    print '  ' + row_divider
    print '  ' + row_two
    print '  ' + row_divider
    print '  ' + row_one
    print ' ' + u'\u2550' + bottom + u'\u2550' + chr(27) + '[0m'
    print ""


def blank_and_draw():
    # blank screen and re-draw board
    # returns: None
    print chr(27) + "[2J"
    print_board(board)


def choose_color():
    # ask player which color they want to be
    # return player_color
    color = ""
    while color == "":
        blank_and_draw()
        print ""
        print "Which color do you want to be? (red or yellow)"
        color = raw_input("> ")
        if color.lower().startswith('r'):
            return 'red'
        elif color.lower().startswith('y'):
            return 'yellow'
        else:
            color = ""


def goes_first():
    # essentialy flip a coin to determine who gets the first move
    # returns: string
    if random.randint(0, 1) == 0:
        return 'player'
    else:
        return 'computer'


def is_space_open(board, column):
    """
    Check where, exactly, in a column a piece will end up if dropped there.
    Returns that index as an integer.
    Returns 'full' if no moves left in that column.

    Keyword arguments:
    board -- list, reflects current positions of all game pieces
    column -- integer, which column (1-7) we are trying to put a piece into

    Returns:
    Integer, when a move is available in that column
    String, when no moves are left in that column
    """
    index = column # bottom row indices are the same as the column num.
    while True:
        if index > (column + 35): # now higher than top row of places
            return 'full'

        if board[index] == u'\u25ef': # if that position is empty
            return index
        else: # position is full, move to the one just above it
            index += 7
            continue # and check that one


def get_player_move():
    """
    Ask the player where he wants to put his game piece.
    Check if it is a valid move (1-7), and use is_space_open() to check
    whether it is free, and the final index the piece ends up in.

    Returns: Integer, index in list 'board' where piece was placed
    """
    while True:
        blank_and_draw()
        print ""
        print ""
        print "Select a column to drop into. (1-7)"
        column = raw_input("> ")
        if column not in "1 2 3 4 5 6 7".split(): # check if 1-7
            blank_and_draw()
            print ""
            print ""
            print "Please enter a number between 1 and 7."
            time.sleep(1.5)
            continue
        else:
            if is_space_open(board, int(column)) == 'full': # if column full
                blank_and_draw()
                print ""
                print ""
                print "Column full! Pick another."
                column = 'x' # so 'column' is no longer 1-7
                time.sleep(1.5)
                continue
            else:
                break

    # get index of where piece will end up if dropped there,
    return is_space_open(board, int(column)) # then return index of move


# various checks for a win condition.
# checking to the left or down is redundant

def check_up(each, positions):
    # check if position + 3 above it make a win
    # each -- int index of place we're checking
    # positions -- list of places where a player's pieces are (ints)
    # returns: Boolean
    if (each + 7) in positions and (each + 14) in positions and \
    (each + 21) in positions:
        #print "won upwards of %d" % each # debug
        return True
    else:
        return False


def check_right(each, positions):
    # check if position + 3 to its right make a win
    # each -- int index of place we're checking
    # positions -- list of places where a player's pieces are (ints)
    # returns: Boolean
    if (each + 1) in positions and (each + 2) in positions and \
    (each + 3) in positions:
        #print "won to the right of %d" % each # debug
        return True
    else:
        return False


def check_up_right(each, positions):
    # returns: Boolean
    # check if position + 3 up and to its right make a win
    # each -- int index of place we're checking
    # positions -- list of places where a player's pieces are (ints)
    if (each + 8) in positions and (each + 16) in positions and \
    (each + 24) in positions:
        #print "won up and to the right of %d" % each # debug
        return True
    else:
        return False


def check_up_left(each, positions):
    # returns: Boolean
    # check if position + 3 up and to its left make a win
    # each -- int index of place we're checking
    # positions -- list of places where a player's pieces are (ints)
    if (each + 6) in positions and (each + 12) in positions and \
    (each + 18) in positions:
        #print "won up and to the left of %d" % each # debug
        return True
    else:
        return False


def see_if_won(board, player_color):
    """
    Check all of a player's pieces for possible win conditions.
    Return True if a win is found.

    Keyword arguments:
    board -- list, contains all pieces in play, as well as empty spaces
    player_color -- color of player whom we are checking for

    Returns: Boolean
    """
    index = 0

    positions = [] # list of ints, indices of player's pieces
    for space in board:
        if space == player_color:
            positions.append(index)
            index += 1 # move to next index
        else:
            index += 1

    for each in positions: # each: integer index of piece
        for way in possible_wins[each]: # check in dictionary for all the
            if way == 'above':                      # ways in which one can win from that
                if check_up(each, positions): # particular index
                    return True
            elif way == 'right':
                if check_right(each, positions):
                    return True
            elif way == 'up_right':
                if check_up_right(each, positions):
                    return True
            elif way == 'up_left':
                if check_up_left(each, positions):
                    return True
            else:
                continue

    return False # when no wins are found


def play_again():
    # Ask player whether or not they would like to play again
    # returns: Boolean
    while True:
        blank_and_draw()
        print ""
        print "Do you wish to play again? (yes or no)"
        again = raw_input("> ")
        if again.lower().startswith('y'):
            return True
        elif again.lower().startswith('n'):
            return False
        else:
            continue


def flip_anim():
    # shows "progress" for a couple of seconds
    # returns: None
    for x in range(1, 4): # loop 3 times, add a period every time
        blank_and_draw()
        print ""
        print ""
        print "Flipping a coin to see who goes first" + ('.' * x)
        time.sleep(0.8)
    return


############# AI routine below ################

def get_computer_move():
    # fallback function for AI, if no other moves can be made
    # picks a random column to drop
    # returns: Integer, index in list 'board' where computer's piece went
    while True:
        move = random.randint(1, 7)
        if is_space_open(board, move) == 'full':
            continue
        else:
            return is_space_open(board, move)


def go_for_win(board, computer_color):
    """
    Highest priority move. If a move this turn will cause a win condition,
    take it. Test on a copy of the board whether or not a move in each slot
    will cause a win.

    Keyword arguments:
    board -- list, contains positions of all game pieces
    computer_color -- string, computer's color

    Returns: Integer. Index of placed piece, if possible
                     Boolean, for when no wins are possible
    """
    for slot in range(1, 8): # columns 1-7
        test_board = []
        test_board = test_board + board # duplicate the board

        if is_space_open(test_board, slot) == 'full':
            continue
        else:
            move = is_space_open(test_board, slot)
            test_board[move] = computer_color

        # now test if it's a win:
        if see_if_won(test_board, computer_color):
            return move
        else:
            continue

    # no winning moves found
    return False


def block_player(board, player_color):
    """
    Essentially play as the player, testing every move to see if it will lead
    to a win. If it does, put own piece there, blocking the player's win.

    Keyword arguments:
    board -- list, contains state of all spaces on the board
    player_color -- string, which color the player is

    Returns: Integer, index where computer's piece ends up
                     Boolean, if no moves are found
    """
    for slot in range(1, 8): # columns 1-7
        test_board = []                                 # duplicate the board
        test_board = test_board + board # so original is unaltered

        if is_space_open(test_board, slot) == 'full':
            continue
        else:
            move = is_space_open(test_board, slot)
            test_board[move] = player_color

        # now test if it's a win:
        if see_if_won(test_board, player_color):
            return move # if so, block it
        else:
            continue

    # no blocking moves found
    return False


def dont_screw_it(board, player_color, computer_color):
    """
    Avoid throwing the game by placing a piece such that the player would
    win on his next move. Go through every column, first test-placing a
    computer piece there, then placing a player piece on top of that. If that
    leads to a player win, add that index to a 'bad_moves' and avoid moving
    there, IF POSSIBLE. Originally ran into an infinite loop if the only
    remaining moves (typical late-game situation) would lead to player win.
    In that case, bite the bullet and select one at random.

    Keyword arguments:
    board -- list, contains positions of all pieces
    player_color -- string, represents player's pieces
    computer_color -- string, represents computer's pieces

    Returns: Integer, index where piece ends up finally
    """
    bad_moves = []

    # first, test drop computer pieces
    for slot in range(1, 8): # columns 1-7
        test_board = []
        test_board = test_board + board # duplicate the board so we
                                                                        # don't alter the actual board
        if is_space_open(test_board, slot) == 'full':
            continue
        else:
            comp_move = is_space_open(test_board, slot)
            test_board[comp_move] = computer_color # computer's move (index)

        # now drop player piece in the same slot
        if is_space_open(test_board, slot) == 'full':
            continue
        else:
            move = is_space_open(test_board, slot)
            test_board[move] = player_color # player's move (index)

        # now test if it's a win
        if see_if_won(test_board, player_color):
            bad_moves.append(comp_move) # add to 'bad_moves'
        else:
            continue # not a win? continue to next column

    print "bad moves: ", bad_moves
    loop_count = 1 # avoid infinite loops
    while True:
        if loop_count > 7:
            return get_computer_move() # give up and pick one at random
        else:
            new_move = random.randint(1, 7) # random move
            if is_space_open(board, new_move) in bad_moves: # not in bad_moves
                loop_count += 1
                continue
            elif is_space_open(board, new_move) == 'full':
                loop_count += 1
                continue
            else:
                return is_space_open(board, new_move) # return index of move

################################# setup #######################################

# {position:[ways you can connect 4 from each board position]
possible_wins = {1:['above', 'right', 'up_right'], \
2:['above', 'right', 'up_right'], 3:['above', 'right', 'up_right'], \
4:['above', 'right', 'up_left', 'up_right'], 5:['above', 'up_left'], \
6:['above', 'up_left'], 7:['above', 'up_left'], \
8:['above', 'right', 'up_right'], 9:['above', 'right', 'up_right'], \
10:['above', 'right', 'up_right'], \
11:['above', 'right', 'up_left', 'up_right'], 12:['above', 'up_left'], \
13:['above', 'up_left'], 14:['above', 'up_left'], \
15:['above', 'right', 'up_right'], 16:['above', 'right', 'up_right'], \
17:['above', 'right', 'up_right'], \
18:['above', 'right', 'up_left', 'up_right'], 19:['above', 'up_left'], \
20:['above', 'up_left'], 21:['above', 'up_left'], 22:['right'], 23:['right'], \
24:['right'], 25:['right'], 29:['right'], 30:['right'], 31:['right'], \
32:['right'], 36:['right'], 37:['right'], 38:['right'], 39:['right'], \
26:['null'], 27:['null'], 28:['null'], 33:['null'], 34:['null'], \
35:['null'], 40:['null'], 41:['null'], 42:['null'], }

# control characters and such for the two player colors
red = chr(27) + '[31m' + u'\u25cf' + chr(27) + '[34m'
yellow = chr(27) + '[33m' + u'\u25cf' + chr(27) + '[34m'

############################## main game loop #################################


while True:
    # setup part
    board = (u'\u25ef ' * 43).split() # reset board to 43 empty spaces

    print chr(27) + "[2J"
    print "        W E L C O M E  T O "
    print ""

    print_board(board)
    print ""

    time.sleep(2) # pause so player can read

    if choose_color() == 'red':
        blank_and_draw()
        print "OK. Player will be " + chr(27) + '[31m' + "red" + chr(27) + \
        '[0m' + ','
        print "and Computer will be " + chr(27) + '[33m' + "yellow" + \
        chr(27) + '[0m' + '.'
        player_color = red # assign colors
        computer_color = yellow
    else:
        blank_and_draw()
        print "OK. Player will be " + chr(27) + '[33m' + "yellow" + chr(27) + \
        '[0m' + ','
        print "and Computer will be " + chr(27) + '[31m' + "red" + chr(27) + \
        '[0m' + '.'
        player_color = yellow
        computer_color = red

    time.sleep(3)

    flip_anim() # show progress while 'coin flip' happens

    blank_and_draw()
    print ""
    print ""
    if goes_first() == 'player': # decide who has first move
        print "The Player has first move."
        next_move = 'player'
        time.sleep(2.5)
    else:
        print "The Computer has first move."
        next_move = 'computer'
        time.sleep(2.5)

    game_won = False
    turn = 1

    # play loop
    while game_won == False:
        if turn == 42: # out of moves, game over
            blank_and_draw()
            print ""
            print "No more moves! It's a draw."
            break

        if next_move == 'player':
            move = get_player_move()
            board[move] = player_color # make change to board state
            # check for win
            if see_if_won(board, player_color) == True:
                blank_and_draw()
                print ""
                print "Four in a row. You win!"
                time.sleep(3.5)
                game_won = True # break out of play loop
            else:
                next_move = 'computer' # computer goes next
                turn += 1
                continue
        else: # computer's move
            # change this to check if board[4] is empty, or not
            # idk if taking the middle after first move matters or not
            if turn == 1: # first turn
                move = 4 # take the middle position (can force a win)
            else:
                if go_for_win(board, computer_color) == False: # top priority
                    if block_player(board, player_color) == False:
                        move = dont_screw_it(board, player_color, \
                        computer_color)
                        #print "dont screw it move: ", move # debug
                    else:
                        move = block_player(board, player_color)
                        #print "block move: ", move # debug
                else:
                    move = go_for_win(board, computer_color)

            board[move] = computer_color # make change to board state
            # check for win
            if see_if_won(board, computer_color) == True:
                blank_and_draw()
                print ""
                print "Four in a row. Computer wins!"
                time.sleep(3.5)
                game_won = True
            else:
                next_move = 'player' # player goes next
                turn += 1
                continue

    # game_won = True
    if play_again():
        continue
    else:
        break

blank_and_draw() # exit message
print ""
print "Thanks for playing!"
