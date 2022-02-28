from os import name, system
from random import randint
from time import sleep

import pyinputplus as pyip  # pip install pyinputplus


def clear_console():
    return system('cls' if name in ('nt', 'dos') else 'clear')


clear_console()

# horizontal size
hor_size = pyip.inputInt("Please insert horizontal size = ", min=1)
# vertical size
vert_size = pyip.inputInt("Please insert vertical size = ", min=1)
# size of winning line
line_size = pyip.inputInt(
    "Please insert win line size = ",
    min=1,
    max=(max(hor_size, vert_size))
    )

move_counter = 0
# Set zeros for whole field. 0 - empty, -1 - crosses (X), 1 - noughts (0)
field = [[0] * hor_size for i in range(vert_size)]
history = dict()


# Print to console current state of the game
def print_field():
    print("")
    for i in range(vert_size):
        for j in range(hor_size):
            if field[i][j] == 0:
                print("|_", end='')
            elif (field[i][j] == -1):
                print("|X", end='')
            else:
                print("|O", end='')
        print("|")


def won(row_n, col_n):
    win_counter = 0
    new_col_n = col_n
    new_row_n = row_n
    last_move = field[row_n][col_n]
    # Move left
    while new_col_n >= 0 and field[new_row_n][new_col_n] == last_move:
        win_counter += 1
        new_col_n += -1
    # Move right
    new_col_n = col_n
    while new_col_n < hor_size and field[new_row_n][new_col_n] == last_move:
        win_counter += 1
        new_col_n += 1
    # Check horizontal win
    if win_counter >= line_size + 1:
        return True
    win_counter = 0
    new_col_n = col_n
    # Move up
    while new_row_n >= 0 and field[new_row_n][new_col_n] == last_move:
        win_counter += 1
        new_row_n += -1
    new_row_n = row_n
    # Move down
    while new_row_n < vert_size and field[new_row_n][new_col_n] == last_move:
        win_counter += 1
        new_row_n += 1
    # Check vertical win
    if win_counter >= line_size+1:
        return True
    win_counter = 0
    new_row_n = row_n
    # Move diagonally up-left
    while (new_row_n >= 0 and new_col_n >= 0 and
            field[new_row_n][new_col_n] == last_move):
        win_counter += 1
        new_row_n += -1
        new_col_n += -1
    new_col_n = col_n
    new_row_n = row_n
    # Move diagonally down-right
    while (new_col_n < hor_size and new_row_n < vert_size and
            field[new_row_n][new_col_n] == last_move):
        win_counter += 1
        new_row_n += 1
        new_col_n += 1
    # Check diagonal win
    if win_counter >= line_size + 1:
        return True
    win_counter = 0
    new_col_n = col_n
    new_row_n = row_n
    # Move diagonally up-right
    while (new_col_n < hor_size and new_row_n >= 0 and
            field[new_row_n][new_col_n] == last_move):
        win_counter += 1
        new_col_n += 1
        new_row_n += -1
    new_col_n = col_n
    new_row_n = row_n
    # Move diagonally down-left
    while (new_col_n >= 0 and new_row_n < vert_size and
            field[new_row_n][new_col_n] == last_move):
        win_counter += 1
        new_col_n += -1
        new_row_n += 1
    # Check diagonal win
    if win_counter >= line_size + 1:
        return True
    return False


print_field()

sleep(0.5)

while move_counter < hor_size * vert_size:
    rand_col = randint(0, hor_size-1)
    rand_row = randint(0, vert_size-1)
    # side: 0 for X, 1 for O
    side = move_counter % 2
    # Select random cell
    while field[rand_row][rand_col] != 0:
        rand_col = randint(0, hor_size-1)
        rand_row = randint(0, vert_size-1)
    if side == 0:
        xo_sign = "X"
    else:
        xo_sign = "O"
    history[move_counter + 1] = xo_sign, rand_row + 1, rand_col + 1
    if side == 0:
        field[rand_row][rand_col] = -1
    else:
        field[rand_row][rand_col] = 1

    clear_console()

    print_field()

    if won(rand_row, rand_col):
        print("We have a winner!!!")
        if side == 0:
            print("Player 1 won with X!")
        else:
            print("Player 2 won with O!")
        break
    move_counter += 1
    sleep(0.5)

if hor_size * vert_size == move_counter:
    print("Draw! Friendship win!")

print(f"Here is history of the moves(move: (X/O, row, column)): {history}")
