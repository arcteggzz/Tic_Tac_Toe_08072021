from typing import SupportsIndex

#Remaining tasks
#4. Make computer make moves.

def main():
    #This initializes the beggining of the game.
    one = " - "
    two = " - "
    three = " - "
    four = " - "
    five = " - "
    six = " - "
    seven = " - "
    eight = " - "
    nine = " - "
    #Call the print function that prints out the empty board.
    print_board(one, two, three, four, five, six, seven, eight, nine)
    turn = 0 #Variable that helps swith the players turns from player 1 back to player 2 continously.
    turns_one = 0 #tracks how many times player 1 has played
    turns_two = 0 #tracks how many times player 2 has played
    #Call the check winner function
    """
    This checks if there is a winner of the game.
    It takes in the 1-9 variables and checks if they are filled with the correct data to determine a winner.
    It then returns a variable(over).
    Over is a boolean variable.
    """
    over = check_if_winner_1(one, two, three, four, five, six, seven, eight, nine)
    while over:
        print (over)#I use this to check the state of Over  (true or false)
        # The If statement below is the draw checker.
        #If all squares are filled, game is a draw and you immediately break out of the while loop.
        if one != " - " and two != " - " and three != " - " and four != " - " and five != " - " and six != " - " and seven != " - " and eight != " - " and nine != " - ":
            print ('Game is a draw')
            break
        if turn == 0:
            turn = turn + 1
            turns_one = turns_one + 1
            if turns_one == 1:
                #run a special checker for move 1
                player_one_move = get_player1_first_move(turns_one)
            else:
                #run the other checker for moves 2 and above
                player_one_move = get_player1_other_moves(turns_one, one, two, three, four, five, six, seven, eight, nine)
            one, two, three, four, five, six, seven, eight, nine = update_board_one(one, two, three, four, five, six, seven, eight, nine, player_one_move)
            print_board(one, two, three, four, five, six, seven, eight, nine)
            over = check_if_winner_1(one, two, three, four, five, six, seven, eight, nine)
                
        else:
            turn = turn - 1
            turns_two = turns_two + 1
            if turns_two == 1:
                #run a special checker for move 1
                player_two_move = get_player2_first_move(turns_two)
            else:
                #run the other checker for moves 2 and above
                player_two_move = get_player2_other_moves(turns_two, one, two, three, four, five, six, seven, eight, nine)
            one, two, three, four, five, six, seven, eight, nine = update_board_two(one, two, three, four, five, six, seven, eight, nine, player_two_move)
            print_board(one, two, three, four, five, six, seven, eight, nine)
            over = check_if_winner_2(one, two, three, four, five, six, seven, eight, nine)
    print ('The game is Over') 
        
def check_if_winner_1(one, two, three, four, five, six, seven, eight, nine):
    over = True
    #1
    if one == ' X ' and two == ' X ' and three == ' X ':
        print ("Player 1 is the winner")
        over = False
        return over
    #2
    if one == ' X ' and five == ' X ' and nine == ' X ':
        print ("Player 1 is the winner")
        over = False
        return over
    #3
    if one == ' X ' and four == ' X ' and seven == ' X ':
        print ("Player 1 is the winner")
        over = False
        return over
    #4
    if two == ' X ' and five == ' X ' and eight == ' X ':
        print ("Player 1 is the winner")
        over = False
        return over
    #5
    if three == ' X ' and six == ' X ' and nine == ' X ':
        print ("Player 1 is the winner")
        over = False
        return over
    #6
    if three == ' X ' and five == ' X ' and seven == ' X ':
        print ("Player 1 is the winner")
        over = False
        return over
    #7
    if four == ' X ' and five == ' X ' and six == ' X ':
        print ("Player 1 is the winner")
        over = False
        return over
    #8
    if seven == ' X ' and eight == ' X ' and nine == ' X ':
        print ("Player 1 is the winner")
        over = False
        return over
    else:
        return over

def check_if_winner_2(one, two, three, four, five, six, seven, eight, nine):
    over = True
    #1
    if one == ' O ' and two == ' O ' and three == ' O ':
        print ("Player 2 is the winner")
        over = False
        return over
    #2
    if one == ' O ' and five == ' O ' and nine == ' O ':
        print ("Player 2 is the winner")
        over = False
        return over
    #3
    if one == ' O ' and four == ' O ' and seven == ' O ':
        print ("Player 2 is the winner")
        over = False
        return over
    #4
    if two == ' O ' and five == ' O ' and eight == ' O ':
        print ("Player 2 is the winner")
        over = False
        return over
    #5
    if three == ' O ' and six == ' O ' and nine == ' O ':
        print ("Player 2 is the winner")
        over = False
        return over
    #6
    if three == ' O ' and five == ' O ' and seven == ' O ':
        print ("Player 2 is the winner")
        over = False
        return over
    #7
    if four == ' O ' and five == ' O ' and six == ' O ':
        print ("Player 2 is the winner")
        over = False
        return over
    #8
    if seven == ' O ' and eight == ' O ' and nine == ' O ':
        print ("Player 2 is the winner")
        over = False
        return over
    else:
        return over

def update_board_two(one, two, three, four, five, six, seven, eight, nine, player_two_move):
    if player_two_move == 1:
        one = ' O '
        return one, two, three, four, five, six, seven, eight, nine
    if player_two_move == 2:
        two = ' O '
        return one, two, three, four, five, six, seven, eight, nine
    if player_two_move == 3:
        three = ' O '
        return one, two, three, four, five, six, seven, eight, nine
    if player_two_move == 4:
        four = ' O '
        return one, two, three, four, five, six, seven, eight, nine
    if player_two_move == 5:
        five = ' O '
        return one, two, three, four, five, six, seven, eight, nine
    if player_two_move == 6:
        six = ' O '
        return one, two, three, four, five, six, seven, eight, nine
    if player_two_move == 7:
        seven = ' O '
        return one, two, three, four, five, six, seven, eight, nine
    if player_two_move == 8:
        eight = ' O '
        return one, two, three, four, five, six, seven, eight, nine
    if player_two_move == 9:
        nine = ' O '
        return one, two, three, four, five, six, seven, eight, nine

def update_board_one(one, two, three, four, five, six, seven, eight, nine, player_one_move):
    if player_one_move == 1:
        one = ' X '
        return one, two, three, four, five, six, seven, eight, nine
    if player_one_move == 2:
        two = ' X '
        return one, two, three, four, five, six, seven, eight, nine
    if player_one_move == 3:
        three = ' X '
        return one, two, three, four, five, six, seven, eight, nine
    if player_one_move == 4:
        four = ' X '
        return one, two, three, four, five, six, seven, eight, nine
    if player_one_move == 5:
        five = ' X '
        return one, two, three, four, five, six, seven, eight, nine
    if player_one_move == 6:
        six = ' X '
        return one, two, three, four, five, six, seven, eight, nine
    if player_one_move == 7:
        seven = ' X '
        return one, two, three, four, five, six, seven, eight, nine
    if player_one_move == 8:
        eight = ' X '
        return one, two, three, four, five, six, seven, eight, nine
    if player_one_move == 9:
        nine = ' X '
        return one, two, three, four, five, six, seven, eight, nine

#Get Players Moves
"""
01. Get Player 1 move for turn 1.
"""
def get_player1_first_move(turns_one):
    while True:
        turns_one = str(turns_one)
        player_one_move = int(input("Player one, Enter your " + (turns_one) + " move: "))
        if is_valid_move_1(player_one_move):
            return player_one_move
        print ("Enter a valid move")

"""
01 A.Get Player 1 move for turn 2, 3, 4, and 5.
"""
def get_player1_other_moves(turns_one, one, two, three, four, five, six, seven, eight, nine):
    while True:
        turns_one = str(turns_one)
        player_one_move = int(input("Player one, Enter your " + (turns_one) + " move: "))
        if is_valid_move_1(player_one_move) and non_duplicate_checker_1(player_one_move, one, two, three, four, five, six, seven, eight, nine):
            return player_one_move
        print ("Enter a valid move")

"""
01 B.Non Duplicate Checker for Player 1 for turn 2, 3, 4, and 5.
"""
def non_duplicate_checker_1(player_one_move, one, two, three, four, five, six, seven, eight, nine):
    if player_one_move == 1 and one == " - ":
        return player_one_move
    elif player_one_move == 2 and two == " - ":
        return player_one_move
    elif player_one_move == 3 and three == " - ":
        return player_one_move
    elif player_one_move == 4 and four == " - ":
        return player_one_move
    elif player_one_move == 5 and five == " - ":
        return player_one_move
    elif player_one_move == 6 and six == " - ":
        return player_one_move
    elif player_one_move == 7 and seven == " - ":
        return player_one_move
    elif player_one_move == 8 and eight == " - ":
        return player_one_move
    elif player_one_move == 9 and nine == " - ":
        return player_one_move
"""
01 C.Number clicked Checker for Player 1
"""
def is_valid_move_1(player_one_move):
    if 0 < player_one_move < 10:
        return player_one_move

"""
02. Get Player 2 move for turn 1.
"""
def get_player2_first_move(turns_two):
    while True:
        turns_two = str(turns_two)
        player_two_move = int(input("Player two, Enter your " + (turns_two) + " move: "))
        if is_valid_move_1(player_two_move):
            return player_two_move
        print ("Enter a valid move")

"""
02 A.Get Player 2 move for turn 2, 3, 4, and 5.
"""
def get_player2_other_moves(turns_two, one, two, three, four, five, six, seven, eight, nine):
    while True:
        turns_two = str(turns_two)
        player_two_move = int(input("Player two, Enter your " + (turns_two) + " move: "))
        if is_valid_move_2(player_two_move) and non_duplicate_checker_2(player_two_move, one, two, three, four, five, six, seven, eight, nine):
            return player_two_move
        print ("Enter a valid move")

"""
02 B.Non Duplicate Checker for Player 2
"""
def non_duplicate_checker_2(player_two_move, one, two, three, four, five, six, seven, eight, nine):
    if player_two_move == 1 and one == " - ":
        return player_two_move 
    elif player_two_move == 2 and two == " - ":
        return player_two_move
    elif player_two_move == 3 and three == " - ":
        return player_two_move
    elif player_two_move == 4 and four == " - ":
        return player_two_move
    elif player_two_move == 5 and five == " - ":
        return player_two_move
    elif player_two_move == 6 and six == " - ":
        return player_two_move
    elif player_two_move == 7 and seven == " - ":
        return player_two_move
    elif player_two_move == 8 and eight == " - ":
        return player_two_move
    elif player_two_move == 9 and nine == " - ":
        return player_two_move
"""
02 C.Number clicked Checker for Player 2
"""
def is_valid_move_2(player_two_move):
    if 0 < player_two_move < 10:
        return player_two_move     

"""
Print the current game state(Board)
"""
def print_board(one, two, three, four, five, six, seven, eight, nine):
    print (one + two + three)
    print (four + five + six)
    print (seven + eight + nine)

if __name__ == '__main__':
    main()