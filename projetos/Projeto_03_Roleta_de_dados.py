from random import randint
import os
#create a dictionary to save all gamers
gamers = dict()
#get the name of gamers
winners = list()
for count in range(4):
    gamers[input(f"Enter with the name of the {count+1}º gamer: ")] = dict({'winner' : 0})
    
numberofgames = int(input("Enter with the number of matches you will play: "))
#clear all inputs prints
os.system('cls' if os.name == 'nt' else 'clear')
#create a dictionary to save all matches results
matches = dict()
#save all matches
for count in range(numberofgames):
    matcheslist = list()
    for gamer in gamers.keys():
#roll the dices
        gamers[gamer]['dice01'] = randint(1,6)
        gamers[gamer]['dice02'] = randint(1,6)
#perform the sum of dices
        gamers[gamer]['sumdices'] = gamers[gamer]['dice01'] + gamers[gamer]['dice02']
        gamers[gamer]['winner']+=1
        matcheslist.extend([gamers[gamer]['sumdices']])
    temp = dict()
#Sort items by winner
    matcheslist.sort(reverse = True)
    for i in range(4):
        for gamer in gamers.items():
            
            temp2=gamer[1]
            if temp2['sumdices'] == matcheslist[i]:
                temp[gamer[0]]= gamer[1]
    gamers = temp 
    matches[f'{count}'] = dict(gamers)
#Show the table with the winner by matche
bigwinner = dict({'name':'','value':0})
for matche in matches.items():
    temp = matche[1]
    print(f"""        {"".center(53).replace(" ","_")}
        |{("matche "+str(int(matche[0])+1)).center(51)}|
        |{"".center(51).replace(" ","_")}|
        |{"name".center(12)}|{"dice 01".center(12)}|{"dice 02".center(12)}|{"full result".center(12)}|
        |{"".center(12).replace(" ","_")}|{"".center(12).replace(" ","_")}|{"".center(12).replace(" ","_")}|{"".center(12).replace(" ","_")}|""")
    for gamer in temp.keys():
        print(f"""        |{str(gamer).center(12)}|{str(temp[gamer]['dice01']).center(12)}|{str(temp[gamer]['dice02']).center(12)}|{str(temp[gamer]['sumdices']).center(12)}|""")
        if temp[gamer]['winner'] > bigwinner['value']:
            bigwinner['name'] = gamer
            bigwinner['value'] = temp[gamer]['winner']

    print(f"""        {"".center(53).replace(" ","-")}""")
#Show the big winner ..
print("The big winner is:",bigwinner['name'])