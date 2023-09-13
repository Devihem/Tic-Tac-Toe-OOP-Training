class Players:
    def __init__(self, players_count: int):
        self.players_tuple = ()
        self.players_ai_tuple = ()
        self.create_and_set_player_list(players_count)

    def create_and_set_player_list(self, players_count):
        players_list = []
        ai_list = []

        for player_numb in range(players_count):

            while True:
                try:
                    player_symbol = input(f"Player {player_numb + 1}, please select your symbol:\n-> ")

                    if player_symbol in players_list or len(player_symbol) != 1:
                        raise ValueError

                    players_list.append(player_symbol)

                    break

                except ValueError:
                    print(
                        "Incorrect input! [Expected single Symbol that is not already in use from another player]\n\n")
                    continue

            self.players_tuple = tuple(players_list)
            self.players_ai_tuple = tuple(ai_list)
