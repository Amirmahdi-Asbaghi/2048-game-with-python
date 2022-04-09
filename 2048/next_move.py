# some functions for generate the nex table by user input
import copy
import random


def left_move(state_table):
    """Calculates the next state when the numbers should go to the left"""
    table = copy.deepcopy(state_table)
    for row in table:
        for i in range(2, -1, -1):
            if row[i] == 0:
                row[i] = row[i + 1]
                row[i + 1] = 0
        for i in range(0, 3):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] += row[i + 1]
                row[i + 1] = 0
        for i in range(2, -1, -1):
            if row[i] == 0:
                row[i] = row[i + 1]
                row[i + 1] = 0
    return table


def right_move(state_table):
    """Calculates the next state when the numbers should go to the right"""
    table = copy.deepcopy(state_table)
    for row in table:
        for i in range(1, 4):
            if row[i] == 0:
                row[i] = row[i - 1]
                row[i - 1] = 0
        for i in range(3, 0, -1):
            if row[i] == row[i - 1] and row[i] != 0:
                row[i] += row[i - 1]
                row[i - 1] = 0
        for i in range(1, 4):
            if row[i] == 0:
                row[i] = row[i - 1]
                row[i - 1] = 0
    return table


def convert_vertical_to_horizontal(state_table):
    """convert list from vertical mood to horizontal"""
    table = copy.deepcopy(state_table)
    return_list = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for j in range(4):
        for i in range(4):
            return_list[j][i] = table[i][j]
    return return_list


def up_move(state_table):
    """Calculates the next state when the numbers should go to the right"""
    table = copy.deepcopy(state_table)
    temp_table = copy.deepcopy(convert_vertical_to_horizontal(table))
    return convert_vertical_to_horizontal(left_move(temp_table))


def down_move(state_table):
    """Calculates the next state when the numbers should go to the right"""
    table = copy.deepcopy(state_table)
    temp_table = copy.deepcopy(convert_vertical_to_horizontal(table))
    return convert_vertical_to_horizontal(right_move(temp_table))


def add_number(state_table):
    table = copy.deepcopy(state_table)
    zero_cords = []

    def two_or_four(probability_of_tails):
        if random.random() < probability_of_tails:
            return 2
        else:
            return 4

    for i in range(4):
        for j in range(4):
            if table[i][j] == 0:
                zero_cords.append((i, j))
    if len(zero_cords) == 1:
        table[zero_cords[0][0]][zero_cords[0][1]] = two_or_four(.9)
        return table
    elif len(zero_cords) == 0:
        return -1
    else:
        zero_cord = zero_cords[random.randint(0, len(zero_cords) - 1)]
        table[zero_cord[0]][zero_cord[1]] = two_or_four(.9)
        return table


def first_table():
    table = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    table = add_number(table)
    table = add_number(table)
    return table


def print_table(state_table):
    for i in range(4):
        for j in range(4):
            print(f"{state_table[i][j]}  ",end="")
        print(" ")

def game_over(state_table):
    """check if user lose or not"""
    table = copy.deepcopy(state_table)
    for i in range(0, 4):
        for j in range(0, 4):
            if table[i][j] == 0:
                return False
    for row in table:
        for i in range(0, 3):
            if row[i] == row[i + 1]:
                return False
    for i in range(0, 3):
        for j in range(0, 3):
            if table[j][i] == table[j + 1][i]:
                return False
    return True