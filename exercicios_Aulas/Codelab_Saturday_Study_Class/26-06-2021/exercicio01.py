#01 - Crie um programa que gerencie o aproveitamento de um jogador de futebol.O
# programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato.

#create the player dict
player=dict({
            'name' : '',
            'numberofgames': 0,
            'goalsbygame' : dict(),
            'goals':0
            })
#create the players dict
players = dict()
#entry function
def main():
    count = 0
    while True:
        #get the values from player
        player['player'] = input("Enter with the name of this player: ")
        player['numberofgames'] = int(input("Enter with the number of games this player play: "))
        #get the number of goals by game
        goals = 0
        for i in range(player['numberofgames']):
            goals = player['goalsbygame']['game'+str(i+1)] = int(input(f"Enter with the number of goals you maked in the {i+1}º game: "))
        #Add the dictionary from player in another dictionary
        player['goals'] = goals
        players['player'+str(count)] = player
        count+=1
        #Ask if the user has another value
        if input("Are You have other player to Enter ?(Y|N): ").lower().strip(" ").startswith('n'):
            break

#Show function
def showResults():
    
    for f in players.keys():
        temp = players[f]
        print(f"""
            The name of player: {temp['player']}
            in games this player maked this points:
    """)
    #show number of goals by game
        for i in range(temp['numberofgames']):
            print(f"game{i} = {str(temp['goalsbygame']['game'+str(i+1)])}".rjust(50))
    #show number of all goals
        print("The sum of all goals are: ".rjust(50),temp['goals'])
            

#call the functions
main()
showResults()