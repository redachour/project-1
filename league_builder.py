import csv

# Open CSV file and return a list of dictionaries of players
def get_players(file, category):
    with open(file, category) as csvfile:
        return list(csv.DictReader(csvfile))

# Sort players by experience
def experience(players):
    no = []
    yes = []
    for player in players:
        if player['Soccer Experience'] == 'YES':
            yes.append(player)
        else:
            no.append(player)
    return yes, no

# Add a team to each player
def add_team(teams, players):
    index = 0
    soccer_players = []
    for exp in experience(players):
        for player in exp:
            player['Team'] = list(teams.keys())[index]
            soccer_players.append(player)
            if index < len(teams) - 1:
                index += 1
            else:
                index = 0
    return soccer_players

# Write the teams file
def print_teams(teams, players):
    # append players to teams dictionary
    for player in add_team(teams, players):
        teams[player['Team']].append(player)
    # open and write teams.txt
    file = open('teams.txt', 'a')
    for team, players in teams.items():
        file.write(team + '\n')
        for player in players:
            file.write(', '.join([player['Name'],
                            player['Soccer Experience'],
                            player['Guardian Name(s)']]) + '\n')
        file.write("\n")

# write guardian letter files
def print_letters(teams, players):
    for player in add_team(teams, players):
        # the file name
        name = '_'.join(player['Name'].lower().split()) + '.txt'
        file = open(name, 'a')
        file.write('Dear {},\n\n'
                   '{}, has been added to the {} team.\n'
                   'Training starts November 29th at 9am.\n'
                   'Thank you.\n'.format(player['Guardian Name(s)'],
                                         player['Name'],
                                         player['Team']))

if __name__ == "__main__":
    # create a dictionary with team name as keys and an ampty list as values
    teams = {'Sharks': [], 'Dragons': [], 'Raptors': []}
    # getting a list of all players
    players = get_players('soccer_players.csv', 'r')
    # write teams.txt file
    print_teams(teams, players)
    # write all guardian letter files
    print_letters(teams, players)
