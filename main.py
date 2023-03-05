from player import *
from operator import attrgetter
from team import*

#Database lists to hold all player and team objects
players = []
teams = []

#Dummy player and team objects - to be deleted later on. For now just for testing
mortenEngholt = Player("Morten", "Engholt", 1600)
hjalteKnudsen = Player("Hjalte", "Knudsen", 1550)
rasmineBak = Player("Rasmine", "Bak", 1430)
askeHammar = Player("Aske", "Hammar", 1426)
t1 = Team(mortenEngholt, hjalteKnudsen, "T1")
t2 = Team(rasmineBak, askeHammar, "T2")
teams.append(t1)
teams.append(t2)
players.append(mortenEngholt)
players.append(hjalteKnudsen)
players.append(rasmineBak)
players.append(askeHammar)

#Function to sort rankings by a chosen value in the PLayer object
def list_sort(list, key):
    list.sort(key=attrgetter(key), reverse=True)

def option_not_availble():
    print("Option not available, you need to choose either T or P")

#Primary code to run program giving the user multiple options
while True:
    selection = input("What would you like to do? (Create/Game/Ranking/Quit) ").capitalize().strip()
    # Chosen to create a new player
    if selection == "Create":
        select = input("What would you like to create team (T) or player (P)?: ").capitalize().strip()
        if select == "T":
            print("What is the first name of the first player? ")
            Player.print_players(players)
            first_player = input().capitalize().strip()
            print("What is the first name of the second player? ")
            Player.print_players(players)
            second_player = input().capitalize().strip()
            teamName = input("What is the name of the team? ").capitalize().strip()
            teams.append(Team(Player.find_player_name(first_player, players),Player.find_player_name(second_player, players),teamName))
        elif select == "P":
            firstName = input("What is the players first name? ").capitalize().strip()
            lastName = input("What is the players last name? ").capitalize().strip()
            players.append(Player(firstName,lastName, 1500))
        else:
            option_not_availble()

    # Chosen to create a game with a winner and a loser
    elif selection == "Game":
        team_or_player = input("Would you like to submit a game with teams (T) og players (P)? ").capitalize().strip()
        if team_or_player == "T":
            Team.game_team(teams)
        elif team_or_player == "P":
            Player.game_players(players)
        else:
            option_not_availble()

    #Shows the rankings of players or teams sorted by Elo
    elif selection == "Ranking":
        team_or_player = input("Would you like to see the teams (T) og players (P) ranking? ").capitalize().strip()
        if team_or_player == "T":
            list_sort(teams, "elo")
            Team.team_ranking(teams)
        elif team_or_player == "P":
            list_sort(players, "elo")
            Player.player_ranking(players)
        else:
            option_not_availble()

    #Stops the program from running
    elif selection == "Quit":
        print("Thanks for updating the rankings!")
        break