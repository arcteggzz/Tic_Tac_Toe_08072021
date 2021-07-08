"""
This code asks the user for a number and a required base.
And converts the number to the required base. 
"""

def main():
    one = " - "
    two = " - "
    three = " - "
    print_empty_board(one, two, three)
    player_one_move = get_player_one_move()
    print (player_one_move)

def get_player_one_move():
    while True:
        player_one_move = int(input("Enter your first move: "))
        try:
            val = int(player_one_move)
            break;
        except ValueError:
            print("This is not a number(move). Please enter a valid number(move")

        if is_valid_move(player_one_move):
            return player_one_move
        print ("Enter a valid move")

def is_valid_move(player_one_move):
    if 0 < player_one_move < 10:
        return player_one_move


def print_empty_board(one, two, three):
    print (one + two + three)

if __name__ == '__main__':
    main()