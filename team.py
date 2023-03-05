class Team():

    elo = 0

    def __init__(self, player1, player2, teamName):
        self.player1 = player1
        self.player2 = player2
        self.teamName = teamName
        self.teamId = teamName + ": " + player1.fullName + " & " + player2.fullName
        self.elo = (player1.elo + player2.elo)/2


    def __eq__(self, other):
        return self.elo == other.elo and self.elo == other.elo

    def __lt__(self, other):
        return self.elo < other.elo

    #Prints all teams currently in the database, showing the team name and the first name of both players
    def print_teams(list):
        for l in list:
            print(l.teamId)

    #Show teams ranking from team database
    def team_ranking(list):
        print("---------------------------------------------------")
        print("         ROUNDNET PICK-UP RANKINGS - TEAMS")
        print("---------------------------------------------------")
        n = 1
        for t in list:
            print(str(n) + ". " + t.teamName + "(" + t.teamId + ") " + "Elo: " + str(int(t.elo)))
            n += 1
        print("---------------------------------------------------")

    #update team elo
    def compute_team_elo(team):
        team.elo = (team.player1.elo + team.player2.elo)/2
        return team.elo

    #Returns a team from the database given the teamName
    def find_teamName(teamValue,list):
        team = None
        for t in list:
            if t.teamId == teamValue:
                team = t
        return team

    #Used to update the rankings according to a team game
    def update_ranking_team(winner, loser, k=32):
        if winner.teamId == loser.teamId:
            print("Sorry can't compute game between the same two teams")
        else:
            expected_win_probability = 1 / (1 + 10 ** ((Team.compute_team_elo(loser) - Team.compute_team_elo(winner)) / 400))
            winner.player1.elo = winner.player1.elo + k * (1 - expected_win_probability)
            winner.player2.elo = winner.player2.elo + k * (1 - expected_win_probability)
            loser.player1.elo = loser.player1.elo + k * (expected_win_probability - 1)
            loser.player2.elo = loser.player2.elo + k * (expected_win_probability - 1)
            winner = None
            loser = None