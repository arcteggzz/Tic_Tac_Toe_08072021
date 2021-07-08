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
    print_empty_board(one, two, three, four, five, six, seven, eight, nine)
    player_one_move = get_player_one_move()
    updated_board = update_board(one, two, three, four, five, six, seven, eight, nine, player_one_move)
    print (player_one_move)
    print (two)
    # print_empty_board(one, two, three, four, five, six, seven, eight, nine)

def update_board(one, two, three, four, five, six, seven, eight, nine, player_one_move):
    if player_one_move == 1:
        one = ' X '
        return one
    if player_one_move == 2:
        two = ' X '
        print (two)
        return two
    if player_one_move == 3:
        three = ' X '
        return three
    if player_one_move == 4:
        four = ' X '
        return four
    if player_one_move == 5:
        five = ' X '
        return five
    if player_one_move == 6:
        six = ' X '
        return six
    if player_one_move == 7:
        seven = ' X '
        return seven
    if player_one_move == 8:
        eight = ' X '
        return eight
    if player_one_move == 9:
        nine = ' X '
        return nine

def get_player_one_move():
    while True:
        player_one_move = int(input("Enter your first move: "))
        if is_valid_move(player_one_move):
            return player_one_move
        print ("Enter a valid move")

def is_valid_move(player_one_move):
    if 0 < player_one_move < 10:
        return player_one_move

def print_empty_board(one, two, three, four, five, six, seven, eight, nine):
    print (one + two + three)
    print (four + five + six)
    print (seven + eight + nine)

if __name__ == '__main__':
    main()