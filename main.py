import tkinter.ttk
from tkinter import *
from player import *
from team import *
from operator import attrgetter
import pickle

#Database lists to hold all player and team objects
players = []
teams = []

#Dummy player and team objects - to be deleted later on. For now just for testing
#mortenEngholt = Player("Morten", "Engholt", 1600)
#hjalteKnudsen = Player("Hjalte", "Knudsen", 1550)
#rasmineBak = Player("Rasmine", "Bak", 1430)
#askeHammar = Player("Aske", "Hammar", 1426)
#t1 = Team(mortenEngholt, hjalteKnudsen, "T1")
#t2 = Team(rasmineBak, askeHammar, "T2")
#teams.append(t1)
#teams.append(t2)
#players.append(mortenEngholt)
#players.append(hjalteKnudsen)
#players.append(rasmineBak)
#players.append(askeHammar)

count = 0

def click():
    global count
    count += 1
    print(count)

def save():
    #save players
    with open('players', 'wb') as players_file:
        pickle.dump(players, players_file)
    #Save teams
    with open('teams', 'wb') as teams_file:
        pickle.dump(teams, teams_file)

def load():
    #Load players
    with open('players', 'rb') as players_file:
        config_dictionary = pickle.load(players_file)
        players.clear()
        for line in config_dictionary:
            players.append(line)
        players_file.close()
    #Load teams
    with open('teams', 'rb') as teams_file:
        config_dictionary = pickle.load(teams_file)
        teams.clear()
        for line in config_dictionary:
            teams.append(line)
        teams_file.close()


#Main window
window = Tk()
window.geometry("375x250")
window.title("Roundnet Denmark - Ranking")
window.config(background="white")

#Icon
icon = PhotoImage(file="logo.png")
window.iconphoto(True, icon)

#Label
header = Label(window,
              text="Roundnet Denmark - Pick-Up Ranking",
              font=("Helvetica", 20, "bold"),
              bg="Red",
              padx=10)

#buttons
mainMenu = Frame(window, padx=5, pady=5, bg="white")
gameButton = Button(mainMenu,
                text = "Submit a game",
                command = lambda: open_submit_game(),
                font=("Helvetica", 10),
                width=25)

createButton = Button(mainMenu,
                text = "Create team or player",
                command = lambda: open_create_player(),
                font=("Helvetica", 10),
                width=25)

rankingButton = Button(mainMenu,
                text = "Show rankings",
                command =lambda: [players.sort(key=lambda p: p.elo, reverse=True),Player.player_ranking(players)],
                font=("Helvetica", 10),
                width=25)

showPlayersButton = Button(mainMenu,
                text = "Show players",
                command =lambda: [players.sort(key=lambda p: p.fullName), Player.print_players(players)],
                font=("Helvetica", 10),
                width=25)

showTeamsButton = Button(mainMenu,
                text = "Show teams",
                command =lambda: Team.print_teams(teams),
                font=("Helvetica", 10),
                width=25)

saveButton = Button(mainMenu,
                text = "Save",
                command = lambda: save(),
                font=("Helvetica", 10),
                width=25)

loadButton = Button(mainMenu,
                text = "Load",
                command = lambda: load(),
                font=("Helvetica", 10),
                width=25)

quitButton = Button(mainMenu,
                text = "Quit",
                command = window.destroy,
                font=("Helvetica", 10),
                width=25)

header.pack(side= TOP, fill=BOTH)
gameButton.pack()
createButton.pack()
rankingButton.pack()
showPlayersButton.pack()
showTeamsButton.pack()
saveButton.pack()
loadButton.pack()
quitButton.pack()
mainMenu.pack()

#Create a game
def open_submit_game():
    submitGameWindow = Toplevel()
    submitGameWindow.geometry("400x500")
    submitGameWindow.title("Submit Game")
    submitGameWindow.config(background="white")

    #Header for submitting a game using teams
    headerTeam = Label(submitGameWindow,
                       font="helvetica 13 bold",
                       text="Submit a game using team names",
                       fg="white",
                       bg="black")

    # Select winning team
    winTeam = Label(submitGameWindow, text="Winning team:",
                        fg="black",
                        bg="white")

    selectWinner = tkinter.ttk.Combobox(submitGameWindow,
                                       state="readonly",
                                       values=[t.teamId for t in teams])

    #select losing team
    loseTeam = Label(submitGameWindow, text="Losing team:",
                    fg="black",
                    bg="white")

    selectLoser = tkinter.ttk.Combobox(submitGameWindow,
                                        state="readonly",
                                        values=[t.teamName + ": " + t.player1.fullName + " & " + t.player2.fullName for
                                                t in teams])

    # Submit game
    submitButtonTeam = Button(submitGameWindow,
                              text="Submit Game",
                              command=lambda: [Team.update_ranking_team(Team.find_teamName(selectWinner.get(),teams),Team.find_teamName(selectLoser.get(),teams)),
                                               submitGameWindow.destroy()],
                              bd=0)

    headerTeam.pack(fill=BOTH)
    winTeam.pack()
    selectWinner.pack(fill=BOTH)
    loseTeam.pack()
    selectLoser.pack(fill=BOTH)
    submitButtonTeam.pack()



#Create player/team window
def open_create_player():
    createWindow = Toplevel()
    createWindow.geometry("300x425")
    createWindow.title("Create Player or Team")
    createWindow.config(background="white")

    #Header for creating a player
    headerPlayer = Label(createWindow,
                   font = "helvetica 13 bold",
                   text="Create Player for the ranking database",
                   fg = "white",
                   bg = "black")

    #Entry first name
    firstNameLabel = Label(createWindow, text="First name:",
                           fg="black",
                           bg="white")
    entryFirstName = Entry(createWindow,
                           font=("Helvetica",10),
                           bd=0,
                           bg= "white",
                           fg="black")
    #Entry last name
    lastNameLabel = Label(createWindow, text="Last name:",
                          fg="black",
                          bg="white")

    entryLastName = Entry(createWindow,
                          font=("Helvetica", 10),
                          bd=0,
                          bg="white",
                          fg="black")
    #Submit button
    submitButtonPlayer = Button(createWindow,
                           text="Create Player",
                           command=lambda: [players.append(Player(entryFirstName.get().capitalize(), entryLastName.get().capitalize(), 1500)),
                                            createWindow.destroy()],
                           bd=0)

    #Create team header
    headerTeam = Label(createWindow,
                         font="helvetica 13 bold",
                         text="Create Team for the ranking database",
                         fg="white",
                         bg="black")

    # Select first player
    firstPlayer = Label(createWindow, text="First player:",
                           fg="black",
                           bg="white")

    selectFirst = tkinter.ttk.Combobox(createWindow,
                                       state= "readonly",
                                       values= [p.fullName  for p in players])

    # Select second player
    secondPlayer = Label(createWindow, text="Second player:",
                        fg="black",
                        bg="white")

    selectSecond = tkinter.ttk.Combobox(createWindow,
                                       state="readonly",
                                       values=[p.fullName for p in players])

    # Team name
    teamNameLabel = Label(createWindow, text="Team name:",
                          fg="black",
                          bg="white")

    entryTeamName = Entry(createWindow,
                          font=("Helvetica", 10),
                          bd=0,
                          bg="white",
                          fg="black")

    # Submit team
    submitButtonTeam = Button(createWindow,
                           text="Create Team",
                           command=lambda: [teams.append(Team(Player.find_player_name(selectFirst.get(), players), Player.find_player_name(selectSecond.get(), players), entryTeamName.get().capitalize())),
                                            createWindow.destroy()],
                           bd=0)

    headerPlayer.pack(fill=BOTH)
    firstNameLabel.pack()
    entryFirstName.pack(fill=BOTH)
    lastNameLabel.pack()
    entryLastName.pack(fill=BOTH)
    submitButtonPlayer.pack(pady=(20,50))
    headerTeam.pack(fill=BOTH)
    firstPlayer.pack()
    selectFirst.pack(fill=BOTH)
    secondPlayer.pack()
    selectSecond.pack(fill=BOTH)
    teamNameLabel.pack()
    entryTeamName.pack(fill=BOTH)
    submitButtonTeam.pack(pady=(20,0))

#Open window
window.mainloop()