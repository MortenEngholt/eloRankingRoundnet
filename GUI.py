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

def list_sort(list, key):
    list.sort(key=attrgetter(key), reverse=True)

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
    #Load teams
    with open('teams', 'rb') as teams_file:
        config_dictionary = pickle.load(teams_file)
        teams.clear()
        for line in config_dictionary:
            teams.append(line)


#Main window
window = Tk()
window.geometry("420x250")
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
header.pack(side= TOP)

#buttons
mainMenu = Frame(window, padx=5, pady=5, bg="white")
createButton = Button(mainMenu,
                text = "Create team or player",
                command = lambda: open_create_player(),
                font=("Helvetica", 10),
                width=25)

gameButton = Button(mainMenu,
                text = "Submit a game",
                command =click,
                font=("Helvetica", 10),
                width=25)

rankingButton = Button(mainMenu,
                text = "Show rankings",
                command =lambda: [list_sort(players, "elo"),Player.player_ranking(players)],
                font=("Helvetica", 10),
                width=25)

showPlayersButton = Button(mainMenu,
                text = "Show players",
                command =lambda: [list_sort(players, "fullName"), Player.print_players(players)],
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

createButton.pack()
gameButton.pack()
rankingButton.pack()
showPlayersButton.pack()
showTeamsButton.pack()
saveButton.pack()
loadButton.pack()
quitButton.pack()
mainMenu.pack()


#Create player/team window
def open_create_player():
    createWindow = Toplevel()
    createWindow.geometry("300x425")
    createWindow.title("Roundnet Denmark - Create Player")
    createWindow.config(background="white")

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
                           command=lambda: [players.append(Player(entryFirstName.get(), entryLastName.get(), 1500)),
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
                                       values= [p.firstName + " " + p.lastName  for p in players])

    # Select second player
    secondPlayer = Label(createWindow, text="Second player:",
                        fg="black",
                        bg="white")

    selectSecond = tkinter.ttk.Combobox(createWindow,
                                       state="readonly",
                                       values=[p.firstName + " " + p.lastName for p in players])

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
                           command=lambda: [teams.append(Team(Player.find_player_name(selectFirst.get(), players), Player.find_player_name(selectSecond.get(), players), entryTeamName.get())),
                                            createWindow.destroy()],
                           bd=0)

    headerPlayer.pack(fill=BOTH)
    firstNameLabel.pack(anchor= W)
    entryFirstName.pack(anchor= W)
    lastNameLabel.pack(anchor= W)
    entryLastName.pack(anchor= W)
    submitButtonPlayer.pack(anchor= W,
                       pady=(20,50))
    headerTeam.pack(fill=BOTH)
    firstPlayer.pack(anchor = W)
    selectFirst.pack(anchor=W)
    secondPlayer.pack(anchor=W)
    selectSecond.pack(anchor=W)
    teamNameLabel.pack(anchor=W)
    entryTeamName.pack(anchor=W)
    submitButtonTeam.pack(anchor=W,
                          pady=(20,0))

#Open window
window.mainloop()