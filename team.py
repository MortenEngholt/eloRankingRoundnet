class Team():

    elo = 0

    def __init__(self, player1, player2, teamName):
        self.player1 = player1
        self.player2 = player2
        self.teamName = teamName
        self.elo = (player1.elo + player2.elo)/2


    def __eq__(self, other):
        return self.elo == other.elo and self.elo == other.elo

    def __lt__(self, other):
        return self.elo < other.elo

    #Prints all teams currently in the database, showing the team name and the first name of both players
    def print_teams(list):
        for l in list:
            print(l.teamName + ": " + l.player1.fullName + " and " + l.player2.fullName)

    #Show teams ranking from team database
    def team_ranking(list):
        print("---------------------------------------------------")
        print("         ROUNDNET PICK-UP RANKINGS - TEAMS")
        print("---------------------------------------------------")
        n = 1
        for t in list:
            print(str(n) + ". " + t.teamName + "(" + t.player1.full.name + ", " + t.player2.full.name + ") " + "Elo: " + str(int(t.elo)))
            n += 1
        print("---------------------------------------------------")

    #Returns a team from the database given the teamName
    def find_teamName(teamValue,list):
        team = None
        for t in list:
            if t.teamName == teamValue:
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
            Team.update_ranking_team(Team.find_teamName(winner, list), Team.find_teamName(loser, list))

    #Used to update the rankings according to a team game
    def update_ranking_team(winner, loser, k=32):
        try:
            expected_win_probability = 1 / (1 + 10 ** ((loser.elo - winner.elo) / 400))
            winner.player1.elo = winner.player1.elo + k * (1 - expected_win_probability)
            winner.player2.elo = winner.player2.elo + k * (1 - expected_win_probability)
            loser.player1.elo = loser.player1.elo + k * (expected_win_probability - 1)
            loser.player2.elo = loser.player2.elo + k * (expected_win_probability - 1)
            print(
                "The new rankingpoints of " + winner.player1.fullName + " is: " + str(
                    int(winner.player1.elo)))
            print(
                "The new rankingpoints of " + winner.player2.fullName + " is: " + str(
                    int(winner.player2.elo)))
            print(
                "The new rankingpoints of " + loser.player1.fullName + " is: " + str(
                    int(loser.player1.elo)))
            print(
                "The new rankingpoints of " + loser.player2.fullName + " is: " + str(
                    int(loser.player2.elo)))
            winner = None
            loser = None
        except AttributeError:
            print("The teams was not found in our databse, please try again.")