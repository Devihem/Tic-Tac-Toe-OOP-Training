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
from gaming_board import GamingBoard


class PlayTicTacToe:
    SIZE_OF_GRID = 0
    NUMBER_OF_PLAYERS = 0
    NUMBER_OF_AI = 0

    def __init__(self):
        self.players = None  # obj
        self.board = GamingBoard()  # obj

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

        # The list of all players ( Human and Ai ) is randomly shuffled. The players turn is based on the list order.
        all_players = self.players.human_players + self.players.ai_players
        random.shuffle(all_players)

        while True:

            # Players are picked one after another in the random all players list.
            for player in all_players:

                # Printing the gaming board in the terminal
                self.board.terminal_print()

                # Future option for AI turns ! Temporary the decision is randomized somewhere on free spot !
                if player in self.players.ai_players:
                    row, col = self.ai_choose_location()
                else:
                    row, col = self.human_choose_location(player)

                # Placing the player token on the board
                self.board.place_token(row, col, player)

                # decrease the value of total free cells
                self.board.free_cells -= 1

                # The method check for winner on the board.
                if self.board.winner_check():
                    print(f"\n\n--------- We have a winner !---------\n"
                          f"     Player with symbol " + "\033[32m" + f"{player}" + "\033[0m" + " WIN !\n\n")
                    return

                # If there is no more free cells for next move the game is considerate as draw !
                elif 0 == self.board.free_cells:
                    print("\n\nNo more moves.\nGame is DRAW !\n\n")
                    return

    # Ai - Location choosing
    def ai_choose_location(self):
        while True:
            row = random.randint(0, self.SIZE_OF_GRID - 1)
            col = random.randint(0, self.SIZE_OF_GRID - 1)

            if self.board.board[row][col] == "":
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
                if self.board.board[row][col] != "":
                    raise ValueError

                # Return the row and col locations if all checks are passed
                return row, col

            except ValueError:
                print("Incorrect input! [Expected valid coordinates in format Row:Col where the block is free !]\n\n")
                continue

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

            # Resize the board based on the Grid Size input ( Create new clear board )
            self.board.create_empty_board_grid(self.SIZE_OF_GRID)

            self.playing_phase()

            if not self.another_game_select():
                break

        print("Thank you for playing !")


if __name__ == "__main__":
    PlayTicTacToe().run()
