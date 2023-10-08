from random import randint
from copy import deepcopy


class AiEnemy:
    POWER_FACTOR = 2
    MULTIPLY_FACTOR = 2

    def __init__(self, board_obj):
        self.original_board_matrix = []
        self.board = board_obj
        self.number_of_simulations = 0

    def ai_choose_location(self, player, players_list):

        # Scan for all free cells and add them as tuples in list
        free_cells = self.scan_for_free_cells()

        # Calculate the number of games that will be played in the background. (x^y) * z
        self.number_of_simulations = (len(free_cells) ** self.POWER_FACTOR) * self.MULTIPLY_FACTOR

        # dictionary collecting all unique locations, later scored for best one from the played games
        best_move_dict = {(tuple(location)): 0 for location in free_cells}

        # Loop n times , re-creating new game.
        for game in range(self.number_of_simulations):

            # Give the index in the players list of the Current player
            current_player_index = players_list.index(player)

            # Making new copy of both matrix and list, the originals must stay unchanged
            free_cells_copy = free_cells.copy()

            # Make copy of the original board
            self.board.board = deepcopy(self.original_board_matrix)

            # Variable to store the location of first move made
            first_move_row_col = ''
            while True:

                # Take the symbol of the current player based on player_index
                current_player = players_list[current_player_index % len(players_list)]

                # Randomly choose one of the free cells and return her row and col from the matrix
                row, col = free_cells_copy.pop(randint(0, len(free_cells_copy) - 1))

                # If variable is empty, save the first move location
                if not first_move_row_col:
                    first_move_row_col = (row, col)

                # Placing the token on board
                self.board.board[row][col] = current_player

                # Check for wins in the current game
                if self.board.winner_check():

                    # if the AI-Player on turn win the round reward it is based on the opponents number
                    if current_player == player:
                        best_move_dict[first_move_row_col] += len(players_list) - 1
                    else:
                        best_move_dict[first_move_row_col] -= 1
                    break

                # Check for draw condition and equivalently for no more space
                elif len(free_cells_copy) == 0:
                    # The best move reward is set to 0
                    best_move_dict[first_move_row_col] += 0
                    break

                # Move the index +1 for the next player in the list
                current_player_index += 1

        # Return the first result of sorted best_move_dict. Key is Reward Value of the location
        return sorted(best_move_dict.items(), key=lambda k: -k[1])[0][0]

    # Set up the AI board and Size for future use of the methods from gaming_board
    def update(self, new_board, grid_size):
        self.original_board_matrix = deepcopy(new_board)
        self.board.size_of_grid = grid_size

    # Return list of all locations of free cells as tuples in list
    def scan_for_free_cells(self):
        result = [[row, column]
                  for row in range(self.board.size_of_grid)
                  for column in range(self.board.size_of_grid) if self.original_board_matrix[row][column] == '']
        return result
