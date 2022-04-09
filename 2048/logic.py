# This file is for the main logic of the program
from next_move import *


def logic():
    table = first_table()
    counter = 0
    while True:

        print("please enter your move")
        print("'r' for right")
        print("'l' for left")
        print("'u' for up")
        print("'d' for down")
        print(f"count of moves = {counter}")
        print_table(table)
        if not game_over(table):
            user_move = input("")
            if user_move == 'u':
                next_table = up_move(table)
                if table == next_table:
                    pass
                else:
                    table = add_number(next_table)
            elif user_move == 'd':
                next_table = down_move(table)
                if table == next_table:
                    pass
                else:
                    table = add_number(next_table)
            elif user_move == 'r':
                next_table = right_move(table)
                if table == next_table:
                    pass
                else:
                    table = add_number(next_table)
            elif user_move == 'l':
                next_table = left_move(table)
                if table == next_table:
                    pass
                else:
                    table = add_number(next_table)
            elif user_move == 'e':
                break
            else:
                print("bad input, try again")
            counter += 1
        else:
            print("Game Over")
            break
