class Team():

    elo = 0

    def __init__(self, player_1, player_2, team_name):
        self.player_1 = player_1
        self.player_2 = player_2
        self.team_name = team_name
        self.elo = (player_1.elo + player_2.elo)/2


    def __eq__(self, other):
        return self.elo == other.elo and self.elo == other.elo

    def __lt__(self, other):
        return self.elo < other.elo

    #Prints all teams currently in the database, showing the team name and the first name of both players
    def print_teams(list):
        for l in list:
            print(l.team_name + ": " + l.player_1.full_name + " and " + l.player_2.full_name)

    #Show teams ranking from team database
    def team_ranking(list):
        print("---------------------------------------------------")
        print("         ROUNDNET PICK-UP RANKINGS - TEAMS")
        print("---------------------------------------------------")
        n = 1
        for t in list:
            print(str(n) + ". " + t.team_name + "(" + t.player_1.full.name + ", " + t.player_2.full.name + ") " + "Elo: " + str(int(t.elo)))
            n += 1
        print("---------------------------------------------------")

    #Returns a team from the database given the team_name
    def find_team_name(teamValue,list):
        team = None
        for t in list:
            if t.team_name == teamValue:
                team = t
        return team

    #Function called when Game is chosen in Main
    def game_team(list):
        print("What is the name of the wining team? - Chose from team list:  ")
        Team.print_teams(list)
        winner = input().capitalize().strip()
        print("What is the name of the losing team? - Chose from team list:  ")
        Team.print_teams(list)
        loser = input().capitalize().strip()
        if winner == loser:
            print("Sorry can't compute game between the same player")
        else:
            Team.update_ranking_team(Team.find_team_name(winner, list), Team.find_team_name(loser, list))

    #Used to update the rankings according to a team game
    def update_ranking_team(winner, loser, k=32):
        try:
            expected_win_probability = 1 / (1 + 10 ** ((loser.elo - winner.elo) / 400))
            winner.player_1.elo = winner.player_1.elo + k * (1 - expected_win_probability)
            winner.player_2.elo = winner.player_2.elo + k * (1 - expected_win_probability)
            loser.player_1.elo = loser.player_1.elo + k * (expected_win_probability - 1)
            loser.player_2.elo = loser.player_2.elo + k * (expected_win_probability - 1)
            print(
                "The new rankingpoints of " + winner.player_1.full_name + " is: " + str(
                    int(winner.player_1.elo)))
            print(
                "The new rankingpoints of " + winner.player_2.full_name + " is: " + str(
                    int(winner.player_2.elo)))
            print(
                "The new rankingpoints of " + loser.player_1.full_name + " is: " + str(
                    int(loser.player_1.elo)))
            print(
                "The new rankingpoints of " + loser.player_2.full_name + " is: " + str(
                    int(loser.player_2.elo)))
            winner = None
            loser = None
        except AttributeError:
            print("The teams was not found in our databse, please try again.")