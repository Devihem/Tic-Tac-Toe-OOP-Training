from random import randint
from copy import deepcopy
from gaming_board import GamingBoard


class AiEnemy:
    def __init__(self, board_obj):
        self.board = board_obj
        self.number_of_simulations = 100

    def ai_choose_location(self, player, players_list):

        # Number of game played ( AI-LOOP )
        game_counts = self.number_of_simulations

        # Scan for all free block and add them in list
        free_cells = [[row, column]
                      for row in range(self.board.size_of_grid)
                      for column in range(self.board.size_of_grid) if self.board.board[row][column] == '']

        # dictionary collecting all unique locations, later scored for best one from the played games
        best_move_dict = {(tuple(location)): 0 for location in free_cells}

        # Loop n times , re-creating new game.
        for game in range(game_counts):

            # Give the index in the players list of the Current player
            current_player_index = players_list.index(player)

            # making new copy of both matrix and list, the originals must stay unchanged
            free_cells_copy = free_cells.copy()
            matrix = deepcopy(self.board.board)

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

                    #  QUESTION - if the unique move is created last it will give wrong data !
                    # if first_move_row_col not in best_move_dict:
                    #     best_move_dict[first_move_row_col] = 0

                # Placing the token on board
                matrix[row][col] = current_player

                # Check for wins in the current game
                print('SELF BOARD INFO',self.board.size_of_grid ,self.board.board)
                if self.board.winner_check():
                    print(game)
                    print(best_move_dict)
                    print(first_move_row_col)
                    # if the AI-Player on turn win the reward is based on the opponents number
                    if current_player == player:
                        best_move_dict[first_move_row_col] += len(players_list) - 1
                    else:
                        best_move_dict[first_move_row_col] -= 1
                    break

                # Check for draw condition and equivalently for no more space
                elif self.board.draw_check():
                    # The best move reward is set to 0
                    best_move_dict[first_move_row_col] += 0
                    break

                if not free_cells_copy:
                    break
                # Move the index +1 for the next player in the list
                current_player_index += 1

        return sorted(best_move_dict.items(), key=lambda k: -k[1])[0][0]

    def update_board(self, new_board, grid_size):
        self.board.board = new_board
        self.board.SIZE_OF_GRID = grid_size


