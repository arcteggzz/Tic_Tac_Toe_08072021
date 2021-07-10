"""
"""

from typing import SupportsIndex


def main():
    one = " - "
    two = " - "
    three = " - "
    four = " - "
    five = " - "
    six =" - "
    seven = " - "
    eight = " - "
    nine = " - "
    print_board(one, two, three, four, five, six, seven, eight, nine)
    turn = 0
    turns_one = 0
    turns_two = 0
    while True:
        if turn == 0:
            turn = turn + 1
            turns_one = turns_one + 1
            player_one_move = get_player_one_move(turns_one)
            one, two, three, four, five, six, seven, eight, nine = update_board_one(one, two, three, four, five, six, seven, eight, nine, player_one_move)
            print_board(one, two, three, four, five, six, seven, eight, nine)
            if turns_one > 2:
                check_if_winner_1(one, two, three, four, five, six, seven, eight, nine)
                

        else:
            turn = turn - 1
            turns_two = turns_two + 1
            player_two_move = get_player_two_move(turns_two)
            one, two, three, four, five, six, seven, eight, nine = update_board_two(one, two, three, four, five, six, seven, eight, nine, player_two_move)
            print_board(one, two, three, four, five, six, seven, eight, nine)
            if turns_two > 2:
                check_if_winner_2(one, two, three, four, five, six, seven, eight, nine)
                break
    print ('The game is Over')

def check_if_winner_1(one, two, three, four, five, six, seven, eight, nine):
    #1
    if one == ' X ' and two == ' X ' and three == ' X ':
        print ("Player 1 is the winner")
        break
    #2
    if one == ' X ' and five == ' X ' and nine == ' X ':
        print ("Player 1 is the winner")
    #3
    if one == ' X ' and four == ' X ' and seven == ' X ':
        print ("Player 1 is the winner")
    #4
    if two == ' X ' and five == ' X ' and eight == ' X ':
        print ("Player 1 is the winner")
    #5
    if three == ' X ' and six == ' X ' and nine == ' X ':
        print ("Player 1 is the winner")
    #6
    if three == ' X ' and five == ' X ' and seven == ' X ':
        print ("Player 1 is the winner")
    #7
    if four == ' X ' and five == ' X ' and six == ' X ':
        print ("Player 1 is the winner")
    #8
    if seven == ' X ' and eight == ' X ' and nine == ' X ':
        print ("Player 1 is the winner")

def check_if_winner_2(one, two, three, four, five, six, seven, eight, nine):
    #1
    if one == ' O ' and two == ' O ' and three == ' O ':
        print ("Player 2 is the winner")
    #2
    if one == ' O ' and five == ' O ' and nine == ' O ':
        print ("Player 2 is the winner")
    #3
    if one == ' O ' and four == ' O ' and seven == ' O ':
        print ("Player 2 is the winner")
    #4
    if two == ' O ' and five == ' O ' and eight == ' O ':
        print ("Player 2 is the winner")
    #5
    if three == ' O ' and six == ' O ' and nine == ' O ':
        print ("Player 2 is the winner")
    #6
    if three == ' O ' and five == ' O ' and seven == ' O ':
        print ("Player 2 is the winner")
    #7
    if four == ' O ' and five == ' O ' and six == ' O ':
        print ("Player 2 is the winner")
    #8
    if seven == ' O ' and eight == ' O ' and nine == ' O ':
        print ("Player 2 is the winner")


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

def get_player_one_move(turns_one):
    while True:
        turns_one = str(turns_one)
        player_one_move = int(input("Player one, Enter your " + (turns_one) + " move: "))
        if is_valid_move_1(player_one_move):
            return player_one_move
        print ("Enter a valid move")

def is_valid_move_1(player_one_move):
    if 0 < player_one_move < 10:
        return player_one_move

def get_player_two_move(turns_two):
    while True:
        turns_two = str(turns_two)
        player_two_move = int(input("Player two, Enter your " + (turns_two) + " move: "))
        if is_valid_move_2(player_two_move):
            return player_two_move
        print ("Enter a valid move")

def is_valid_move_2(player_two_move):
    if 0 < player_two_move < 10:
        return player_two_move     

def print_board(one, two, three, four, five, six, seven, eight, nine):
    print (one + two + three)
    print (four + five + six)
    print (seven + eight + nine)

if __name__ == '__main__':
    main()