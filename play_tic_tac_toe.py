"""
Project: Tic-Tac-Toe OOP Training
File: play_tic_tac_toe.py - main
Author: Ivaylo Stoyanov - Devihem

This is a basic project in python for the game Tic-Tac-Toe.
The idea of this the project is to be done with OOP methods.There are some additional
options added like custom board size , custom players size , gaming board visualisation in terminal and option for new
game. For better experience all inputs are handled to stay repetitive until a proper input is received.

Players take turns placing their tokens on the board by selecting coordinates in format Row:Col .
If a player has a row, column, or diagonal filled with his symbol the player wins.
If no player wins and the board is full, the game is considered a draw.

"""

import random
from players import Players


class PlayTicTacToe:
    SIZE_OF_GRID = 0
    NUMBER_OF_PLAYERS = 0
    NUMBER_OF_AI = 0

    def __init__(self):
        self.players = None  # obj
        self.board = []

    @staticmethod
    def welcome_text():
        print("\n\n"
              "\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
              "\n*\033[32m   ______    ____   ______         ______    ___      ______         ______   ____     ______  \33[0m*"
              "\n*\033[32m  /_  __/   /  _/  / ____/        /_  __/   /   |    / ____/        /_  __/  / __ \\   / ____/  \33[0m*"
              "\n*\033[32m   / /      / /   / /              / /     / /| |   / /              / /    / / / /  / __/     \33[0m*"
              "\n*\033[32m  / /     _/ /   / /___           / /     / ___ |  / /___           / /    / /_/ /  / /___     \33[0m*"
              "\n*\033[32m /_/     /___/   \\____/          /_/     /_/  |_|  \\____/          /_/     \\____/  /_____/     \33[0m*"
              "\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
              "\n\n")

    # Staticmethod used for all user integer input values.  Receive min/max values and correspondent texts.
    # Return Int Value in the needed parameters
    @staticmethod
    def user_int_input_selecting(input_text, error_text, min_num=0, max_num=float("inf")):

        while True:
            try:
                value_size = int(input(input_text))

                if value_size < min_num:
                    raise ValueError

                if value_size > max_num:
                    raise ValueError

                return value_size

            except ValueError:
                print(error_text)
                continue

    # Main method for going through the game phase.
    def playing_phase(self):

        # If there is no more free blocks for next move the game is considerate as draw !
        max_moves = self.SIZE_OF_GRID ** 2
        made_moves = 0

        # The list of all players ( Human and Ai ) is randomly shuffled. The players turn is based on the list order.
        all_players = self.players.human_players + self.players.ai_players
        random.shuffle(all_players)

        while True:

            # Players are picked one after another in the random all players list.
            for player in all_players:

                # Printing the gaming board in the terminal
                self.board_print()

                # Future option for AI turns ! Temporary the decision is randomized somewhere on free spot !
                if player in self.players.ai_players:
                    row, col = self.ai_choose_location()
                else:
                    row, col = self.human_choose_location(player)

                # Placing the player token on the board
                self.board[row][col] = player

                # Increasing the made moves
                made_moves += 1

                # Winner condition check
                if self.winner_check():
                    print(f"\n\n--------- We have a winner !---------\n"
                          f"     Player with symbol " + "\033[32m" + f"{player}" + "\033[0m" + " WIN !\n\n")
                    return

                # Draw condition check
                elif max_moves == made_moves:
                    print("\n\nNo more moves.\nGame is DRAW !\n\n")

                    return

    # Using ASCII symbols and the grid size for different elements to represent the board in the terminal.
    def board_print(self):
        list_with_indexes_top = ['']

        for numb in range(self.SIZE_OF_GRID):
            str_numb = str(numb + 1)
            str_numb = ' ' * (4 - len(str_numb)) + str_numb

            list_with_indexes_top.append(str_numb)

        # Top frame
        print('┌──' + '──┬──' * self.SIZE_OF_GRID + '──┐')

        # Index Top
        print('│    ' + '│'.join(list_with_indexes_top) + '│')

        # Mid Rows
        counter = 0
        for row in self.board:
            counter += 1
            str_counter = str(counter)
            str_counter = ' ' * (4 - len(str_counter)) + str_counter
            print_row = [' ' * (4 - len(el)) + el for el in row]
            print('├──' + '──┼──' * self.SIZE_OF_GRID + '──┤')
            print('│' + '│'.join([str_counter] + print_row) + '│')

        # Bottom frame
        print('└──' + '──┴──' * self.SIZE_OF_GRID + '──┘\n')

    # Ai - Location choosing
    def ai_choose_location(self):
        while True:
            row = random.randint(0, self.SIZE_OF_GRID - 1)
            col = random.randint(0, self.SIZE_OF_GRID - 1)
            if self.board[row][col] == "":
                return row, col

    # Human - Location choosing with try/expect loop for filtering the incorrect inputs.
    def human_choose_location(self, player):

        while True:

            try:
                player_pick_location = input(
                    f"Select where you want to place your Token "
                    f"[" + "\033[32m" + f"{player}" + "\033[0m" + "] in format Row:Col !\n -> ").split(":")

                # Four checks for proper input , if the input is incorrect raise ValueError and Continue to the loop
                # Check-1 , If there is more than two values after the split
                if len(player_pick_location) != 2:
                    raise ValueError

                # Check-2 , if all elements are integers
                for loc in player_pick_location:
                    for el in loc:
                        if not el.isdigit():
                            raise ValueError

                row = int(player_pick_location[0])
                col = int(player_pick_location[1])

                # Check-3, if all numbers are in the range of the board
                if 0 < row <= self.SIZE_OF_GRID and 0 < col <= self.SIZE_OF_GRID:
                    row = row - 1
                    col = col - 1
                else:
                    raise ValueError

                # Check-4, if the token is placed on free place
                if self.board[row][col] != "":
                    raise ValueError

                # Return the row and col locations if all checks are passed
                return row, col

            except ValueError:
                print("Incorrect input! [Expected valid coordinates in format Row:Col where the block is free !]\n\n")
                continue

    # The method check for winner on the board.
    def winner_check(self):

        # Rows - Check
        for row in self.board:
            if row[0] != '' and all([True if el == row[0] else False for el in row[1:]]):
                return True

        # Columns - Check
        for col in range(self.SIZE_OF_GRID):
            if self.board[0][col] != '' and all(
                    [True if self.board[0][col] == row[col] else False for row in self.board[1:]]):
                return True

        # Primer diagonal - Check
        if self.board[0][0] != '' and all(
                [True if self.board[0][0] == self.board[row][row] else False for row in range(self.SIZE_OF_GRID)]):
            return True

        # Secondary diagonal - Check
        if (self.board[0][self.SIZE_OF_GRID - 1] != ''
                and all([True if self.board[0][self.SIZE_OF_GRID - 1] == self.board[row][
                    self.SIZE_OF_GRID - 1 - row] else False
                         for row in range(self.SIZE_OF_GRID)])):
            return True

    @staticmethod
    def another_game_select():
        while True:
            try:
                new_game = input("\n\nDo you want to play another game ? [Y/N]:\n -> ")

                if new_game.upper() not in ['Y', 'N']:
                    raise ValueError

                if new_game.upper() == 'Y':
                    return True
                return False

            except ValueError:
                print("Incorrect input! [Expected Y or N]\n\n")
                continue

    def run(self):
        self.welcome_text()

        self.SIZE_OF_GRID = self.user_int_input_selecting(
            input_text="Please select the gaming board size [ 3 - More ]:\n-> : ",
            error_text="Incorrect input! [Expected integer with value 3 or bigger]\n\n",
            min_num=3)

        self.NUMBER_OF_PLAYERS = self.user_int_input_selecting(
            input_text="Please select how many total players will participate [ 2 - More ]:\n-> : ",
            error_text="Incorrect input! [Expected integer with value 2 or bigger]\n\n",
            min_num=2)

        self.NUMBER_OF_AI = self.user_int_input_selecting(
            input_text=f"Please select how many AI opponents will participate [ 0 - {self.NUMBER_OF_PLAYERS} ]:\n-> : ",
            error_text="Incorrect input! [Expected integer between 0 and total players!]\n\n",
            max_num=self.NUMBER_OF_PLAYERS)

        self.players = Players(self.NUMBER_OF_PLAYERS, self.NUMBER_OF_AI)

        while True:

            self.board = [['' for _ in range(self.SIZE_OF_GRID)] for __ in range(self.SIZE_OF_GRID)]

            self.playing_phase()

            if not self.another_game_select():
                break

        print("Thank you for playing !")


if __name__ == "__main__":
    PlayTicTacToe().run()
