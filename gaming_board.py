class GamingBoard:
    def __init__(self):
        self.size_of_grid = 0
        self.free_cells = 0
        self.board = []

    # Create new empty board based on the given grid size, the board is square !
    def create_empty_board_grid(self, size_of_grid):
        self.size_of_grid = size_of_grid
        self.free_cells = size_of_grid * size_of_grid
        self.board = [['' for _ in range(self.size_of_grid)] for __ in range(self.size_of_grid)]

    def place_token(self, row, col, symbol):
        self.board[row][col] = symbol

    # The method check for winner on the board.
    def winner_check(self):

        # Rows - Check
        for row in self.board:
            if row[0] != '' and all([True if el == row[0] else False for el in row[1:]]):
                return True

        # Columns - Check
        for col in range(self.size_of_grid):
            if self.board[0][col] != '' and all(
                    [True if self.board[0][col] == row[col] else False for row in self.board[1:]]):
                return True

        # Primer diagonal - Check
        if self.board[0][0] != '' and all(
                [True if self.board[0][0] == self.board[row][row] else False for row in
                 range(self.size_of_grid)]):
            return True

        # Secondary diagonal - Check
        if (self.board[0][self.size_of_grid - 1] != ''
                and all([True if self.board[0][self.size_of_grid - 1] == self.board[row][
                    self.size_of_grid - 1 - row] else False
                         for row in range(self.size_of_grid)])):
            return True

    def draw_check(self):
        if self.free_cells == 0:
            return True

        # TODO
        # return not self.free_cells
        # коплиране ?

    def check_if_coordinates_are_valid(self, player_pick_location):

        try:
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
            if 0 < row <= self.size_of_grid and 0 < col <= self.size_of_grid:
                row = row - 1
                col = col - 1
            else:
                raise ValueError

            # Check-4, if the token is placed on free place
            if self.board[row][col] != "":
                raise ValueError

            return True

        except ValueError:
            print("Incorrect input! [Expected valid coordinates in format Row:Col where the block is free !]\n\n")
            return False

    # Using ASCII symbols and the grid size for different elements to represent the board in the terminal.
    def terminal_print(self):
        list_with_indexes_top = ['']

        for numb in range(self.size_of_grid):
            str_numb = str(numb + 1)
            str_numb = ' ' * (4 - len(str_numb)) + str_numb

            list_with_indexes_top.append(str_numb)

        # Top frame
        print('┌──' + '──┬──' * self.size_of_grid + '──┐')

        # Index Top
        print('│    ' + '│'.join(list_with_indexes_top) + '│')

        # Mid Rows
        counter = 0
        for row in self.board:
            counter += 1
            str_counter = str(counter)
            str_counter = ' ' * (4 - len(str_counter)) + str_counter
            print_row = [' ' * (4 - len(el)) + el for el in row]
            print('├──' + '──┼──' * self.size_of_grid + '──┤')
            print('│' + '│'.join([str_counter] + print_row) + '│')

        # Bottom frame
        print('└──' + '──┴──' * self.size_of_grid + '──┘\n')
