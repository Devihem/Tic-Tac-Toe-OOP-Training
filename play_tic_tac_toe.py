from players import Players


class PlayTicTacToe:
    SIZE_OF_GRID = 0
    NUMBER_OF_PLAYERS = 0

    # NUMBER_OF_AI = 0

    def __init__(self):
        self.players = ()
        self.board = []

    def playing_phase(self):
        max_moves = self.SIZE_OF_GRID ** 2
        made_moves = 0

        while True:

            for player in self.players.players_tuple:

                self.board_print()

                row, col = self.user_token_loc_selecting(player)

                self.board[row][col] = player

                made_moves += 1

                if self.winner_check():
                    print(f"\n\n--------- We have a winner !---------\n"
                          f"     Player with symbol " + "\033[32m" + f"{player}" + "\033[0m" + " WIN !\n\n")

                elif max_moves == made_moves:
                    print("\n\nNo more moves.\nGame is DRAW !\n\n")

    def user_token_loc_selecting(self, player):

        while True:

            try:
                player_pick_location = input(
                    f"Select where you want to place your Token "
                    f"[" + "\033[32m" + f"{player}" + "\033[0m" + "] in format Row:Col !\n -> ").split(":")

                if len(player_pick_location) != 2:
                    raise ValueError

                for loc in player_pick_location:
                    for el in loc:
                        if not el.isdigit():
                            raise ValueError

                row = int(player_pick_location[0])
                col = int(player_pick_location[1])

                if 0 < row <= self.SIZE_OF_GRID and 0 < col <= self.SIZE_OF_GRID:
                    row = row - 1
                    col = col - 1
                else:
                    raise ValueError

                if self.board[row][col] != "":
                    raise ValueError

                return row, col

            except ValueError:
                print("Incorrect input! [Expected valid coordinates in format Row:Col where the block is free !]\n\n")
                continue

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
    def user_int_input_selecting(input_text, error_text, minimum_value):
        while True:
            try:
                value_size = int(input(input_text))

                if value_size < minimum_value:
                    raise ValueError

                return value_size

            except ValueError:
                print(error_text)
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

    @staticmethod
    def welcome_text():
        print("\n\n"
              "\n---------------------------------Welcome-to-my-mini-project----------------------------------"
              "\n   ______    ____   ______         ______    ___      ______         ______   ____     ______"
              "\n  /_  __/   /  _/  / ____/        /_  __/   /   |    / ____/        /_  __/  / __ \\   / ____/"
              "\n   / /      / /   / /              / /     / /| |   / /              / /    / / / /  / __/   "
              "\n  / /     _/ /   / /___           / /     / ___ |  / /___           / /    / /_/ /  / /___   "
              "\n /_/     /___/   \\____/          /_/     /_/  |_|  \\____/          /_/     \\____/  /_____/  "
              "\n----------------------------------------------------------------------------------------------"
              "\n\n")

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

    def run(self):
        self.welcome_text()

        self.SIZE_OF_GRID = self.user_int_input_selecting(
            input_text="Please select Grid Size:\n-> ",
            error_text="Incorrect input! [Expected integer with value 3 or bigger]\n\n",
            minimum_value=3)

        self.NUMBER_OF_PLAYERS = self.user_int_input_selecting(
            input_text="Please select how many players will participate:\n-> ",
            error_text="Incorrect input! [Expected integer with value 2 or bigger]\n\n",
            minimum_value=2)

        self.players = Players(self.NUMBER_OF_PLAYERS)

        while True:

            self.board = [['' for _ in range(self.SIZE_OF_GRID)] for __ in range(self.SIZE_OF_GRID)]

            self.playing_phase()

            if not self.another_game_select():
                break

        print("Thank you for playing !")


PlayTicTacToe().run()
