class Player():

    player_id = 1

    def __init__(self, firstName, lastName,elo):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = firstName + " " + lastName
        self.elo = elo
        self.id = firstName + " " + lastName + ": Player_id " + str(Player.player_id)

        Player.player_id += 1

    def __eq__(self, other):
        return self.elo == other.elo and self.elo == other.elo

    def __lt__(self, other):
        return self.elo < other.elo

    # Prints the names of all players currently in the database
    def print_players(list):
        for l in list:
            print(l.fullName)

    #Show player ranking
    def player_ranking(list):
        print("---------------------------------------------------")
        print("        ROUNDNET PICK-UP RANKINGS - PLAYERS")
        print("---------------------------------------------------")
        n = 1
        for p in list:
            print(str(n) + ". " + p.id + " Elo: " + str(int(p.elo)))
            n += 1
        print("---------------------------------------------------")

    # Find  a player object given the firstName value and a database list
    def find_player_name(playerValue, list):
        player = None
        for x in list:
            if x.fullName == playerValue:
                player = x
        return player

    # Function called when Game is chosen in Main
    def game_players(list):
        print("What is the first name of the winner? - Chose from player list:  ")
        Player.print_players(list)
        winner = input().capitalize().strip()
        print("What is the first name of the loser? - Chose from player list:  ")
        Player.print_players(list)
        loser = input().capitalize().strip()
        if winner == loser:
            print("Sorry can't compute game between the same player")
        else:
            Player.update_ranking_player(Player.find_player_name(winner, list),
                                         Player.find_player_name(loser, list))

    # Used to update the rankings according to a game between two players
    def update_ranking_player(winner, loser, k=32):
        try:
            expected_win_probability = 1 / (1 + 10 ** ((loser.elo - winner.elo) / 400))
            winner.elo = winner.elo + k * (1 - expected_win_probability)
            loser.elo = loser.elo + k * (expected_win_probability - 1)
            print("The new rankingpoints of " + winner.fullName + " is: " + str(
                int(winner.elo)))
            print(
                "The new rankingpoints of " + loser.fullName + " is: " + str(int(loser.elo)))
            winner = None
            loser = None
        except AttributeError:
            print("The player was not found in our databse, please try again.")

    def game_players(list):
        print("What is the first name of the winner? - Chose from player list:  ")
        Player.print_players(list)
        winner = input().capitalize().strip()
        print("What is the first name of the loser? - Chose from player list:  ")
        Player.print_players(list)
        loser = input().capitalize().strip()
        if winner == loser:
            print("Sorry can't compute game between the same player")
        else:
            Player.update_ranking_player(Player.find_player_name(winner, list),
                                         Player.find_player_name(loser, list))