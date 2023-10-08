from random import randint
from copy import deepcopy


class AiEnemy:
    def __init__(self, board_obj):
        self.original_board_matrix = []
        self.board = board_obj  # Otherwise highlight errors
        self.number_of_simulations = 100

    def ai_choose_location(self, player, players_list):
        # Making copy of the matrix and keep it for rollback, the idea is to use the methods from class gaming_board.
        self.original_board_matrix = deepcopy(self.board.board)

        # Number of game played ( AI-LOOP )
        game_counts = self.number_of_simulations

        # Scan for all free block and add them in list
        free_cells = [[row, column]
                      for row in range(self.board.size_of_grid)
                      for column in range(self.board.size_of_grid) if self.original_board_matrix[row][column] == '']

        # dictionary collecting all unique locations, later scored for best one from the played games
        best_move_dict = {(tuple(location)): 0 for location in free_cells}

        # Loop n times , re-creating new game.
        for game in range(game_counts):
            # Give the index in the players list of the Current player
            current_player_index = players_list.index(player)

            # making new copy of both matrix and list, the originals must stay unchanged
            free_cells_copy = free_cells.copy()

            # First the Original is received & copied. Then is played directly on the matrix in the board class.
            self.board.board = deepcopy(self.original_board_matrix)

            # variable to store the first move of every game
            first_move_row_col = ''
            while True:

                # Take the symbol of the current player
                current_player = players_list[current_player_index % len(players_list)]

                # PLACE TOKEN ON RANDOM FREE CELL ( Index Out of Range handled from GAME IS DRAW )
                row, col = free_cells_copy.pop(randint(0, len(free_cells_copy) - 1))

                # If value is empty, save the first move location and add it to the best_move_dictionary if is new
                if not first_move_row_col:
                    first_move_row_col = (row, col)

                # Placing the token on board
                self.board.board[row][col] = current_player

                # Check for wins in the current game

                if self.board.winner_check():

                    # if the AI-Player on turn win the reward is based on the opponents number
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

        return sorted(best_move_dict.items(), key=lambda k: -k[1])[0][0]

    def update(self, new_board, grid_size):
        self.board.board = deepcopy(new_board)
        self.board.size_of_grid = grid_size
