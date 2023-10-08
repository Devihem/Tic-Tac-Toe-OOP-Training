"""
Project: Tic-Tac-Toe OOP Training
File: play_tic_tac_toe.py - main
Author: Ivaylo Stoyanov - Devihem

This is a basic project in python for the game Tic-Tac-Toe.
The idea of this the project is to be done with OOP construction.There are some additional
options added like custom board size , custom players size , gaming board visualisation in terminal and option for new
game. For better experience all inputs are handled to stay repetitive until a proper input is received.

Players take turns placing their tokens on the board by selecting coordinates in format Row:Col .
If a player has a row, column, or diagonal filled with his symbol the player wins.
If no player wins and the board is full, the game is considered a draw.

"""

import random
from players import Players
from gaming_board import GamingBoard
from ai_enemy import AiEnemy


class PlayTicTacToe:
    SIZE_OF_GRID = 0
    NUMBER_OF_PLAYERS = 0
    NUMBER_OF_AI = 0

    def __init__(self):
        self.players = Players()  # obj
        self.board = GamingBoard()  # obj
        self.AI_enemy = AiEnemy(GamingBoard())  # obj

    # The method set all class constants and parameters based on user input and give the option for repeat the game.
    def run(self):

        # ASCII Welcome text printed in terminal
        self.welcome_text()

        # Set the GRID_SIZE , HUMAN and AI players count. ( Using user input )
        self.set_constants()

        # UPDATE PLAYERS . Create and fill the players list
        self.players.create_players_list(self.NUMBER_OF_PLAYERS, self.NUMBER_OF_AI)

        while True:

            #  UPDATE BOARD . Resize the board based on the Grid Size input ( Create new empty board )
            self.board.create_empty_board_grid(self.SIZE_OF_GRID)

            #  Shuffle the player order before any new game
            self.players.all_players_shuffle()

            # PLAYING PHASE
            self.playing_phase()

            # Giving prompt for new game
            if not self.another_game_select():
                break

        print("Thank you for playing !")

    # Main method for going through the game logic.
    def playing_phase(self):

        while True:

            # Players are picked one after another in from list with all players ( shuffled before any new game ).
            for player in self.players:

                # Printing the gaming board in the terminal
                self.board.terminal_print()

                # Future option for AI turns ! Temporary the decision is randomized somewhere on free spot !
                if player in self.players.ai_players:

                    # TODO fix the player listy

                    # self.AI_enemy.update_board(self.board.board, self.SIZE_OF_GRID)
                    self.AI_enemy.update( self.board.board, self.SIZE_OF_GRID)
                    row, col = self.AI_enemy.ai_choose_location(player,
                                                                self.players.human_players + self.players.ai_players)

                else:
                    row, col = [int(i) - 1 for i in self.human_choose_location(player)]

                # Placing the player token on the board
                self.board.place_token(row, col, player)

                # decrease the value of total free cells
                self.board.free_cells -= 1

                # The method check for winner.
                if self.board.winner_check():
                    print(f"\n\n* * * * We Have A Winner  * * * * *\n"
                          f"*  \033[32m Congratulations Player: {player} !\33[0m   *\n"
                          f"* * * * * * * * * * * * * * * * * * \n\n")

                    return

                # The method check if the game is DRAW.
                elif self.board.draw_check():
                    print(f"\n\n* * * * * No More Moves * * * * *\n"
                          f"*    \033[34m This round is DRAW\33[0m        *\n"
                          f"* * * * * * * * * * * * * * * * * \n\n")
                    return

    def set_constants(self):

        # FOR TEST ONLY
        # self.SIZE_OF_GRID = 4
        # self.NUMBER_OF_PLAYERS = 2
        # self.NUMBER_OF_AI = 2

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
            player_pick_location = input(
                f"Select where you want to place your Token "
                f"[" + "\033[32m" + f"{player}" + "\033[0m" + "] in format Row:Col !\n -> ").split(":")

            # TODO - board must check only for coordinates. Other checks stay here !

            # Four checks for proper input , if the input is incorrect raise ValueError and Continue to the loop
            if self.board.check_if_coordinates_are_valid(player_pick_location):
                # Return the row and col locations if all checks are passed
                return player_pick_location

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


if __name__ == "__main__":
    PlayTicTacToe().run()
