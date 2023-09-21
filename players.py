from random import shuffle


class Players:
    def __init__(self):
        self.players_count = 0
        self.ai_count = 0
        self.human_players = ()
        self.ai_players = ()

    def create_players_list(self, number_of_players, number_of_ai):
        self.players_count = number_of_players
        self.ai_count = number_of_ai
        self.add_human_players()
        self.add_ai_players()

    def add_human_players(self):
        self.human_players = self.set_players(players_count=self.players_count - self.ai_count, print_name="Player")

    def add_ai_players(self):
        self.ai_players = self.set_players(players_count=self.ai_count, print_name="AI")

    def set_players(self, players_count, print_name):
        players_list = []

        for player_numb in range(players_count):

            while True:
                try:
                    player_symbol = input(f"Please select symbol for {print_name} {player_numb + 1}\n-> ")

                    if player_symbol in players_list or player_symbol in self.human_players or len(player_symbol) != 1:
                        raise ValueError

                    players_list.append(player_symbol)

                    break

                except ValueError:
                    print(
                        "Incorrect input! [Expected single Symbol that is not already in use from another player]\n\n")
                    continue

        return players_list

    # The list of all players ( Human and Ai ) is randomly shuffled. The players turn is based on the list order.

    def all_players_shuffle(self):
        self.__all_players = list(self.human_players + self.ai_players)
        shuffle(self.__all_players)

    def __iter__(self):
        self.__counter = -1
        return self

    def __next__(self):
        self.__counter += 1

        if self.__counter == len(self.__all_players):
            raise StopIteration

        return self.__all_players[self.__counter]
