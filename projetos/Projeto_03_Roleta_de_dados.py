from random import randint
#create a dictionary to save all gamers
gamers = dict()
#get the name of gamers
for count in range(4):
    gamers[input(f"Enter with the name of the {count+1}º gamer: ")] = dict()
numberofgames = int(input("Enter with the number of matches you will play"))
#create a dictionary to save all matches results
matches = dict()
#save all matches
for count in range(numberofgames):
    matcheslist = list()
    for gamer in gamers.keys():
#roll the dices
        gamers[gamer]['dice01'] = randint(1,6)
        gamers[gamer]['dice02'] = randint(1,6)
        print(f"The first dice give  the {gamers[gamer]['dice01']} side")
        print(f"The first dice give  the {gamers[gamer]['dice02']} side")
#perform the sum of dices
        gamers[gamer]['sumdices'] = gamers[gamer]['dice01'] + gamers[gamer]['dice02']
        print(f"The result value in this matche is: {gamers[gamer]['sumdices']}")
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
for matche in matches.items():
    print(f"""        {"".center(27).replace(" ","_")}
        |{("matche "+str(int(matche[0])+1)).center(25)}|
        |{"".center(25).replace(" ","_")}|""")
    
    
    for gamer in temp.items():
        temp = gamer[1]
        print(f"""        |{str(gamer[0]).center(12)}|{str(temp['sumdices']).center(12)}|""")
    print(f"""        {"".center(27).replace(" ","-")}""")