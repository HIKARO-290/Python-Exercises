from random import randint
from time import sleep
import os
#create a dictionary to save all gamers
gamers = dict()
dices = {
    'dice01':{
    '1' : """
            ____________  #
           /          /|  #
          /     0    / |  #
         /          / 0|  #
        /__________/  0|  #
        |          |00 /  #
        |   0  0   |0 /   #
        |   0  0   | /    #
        |__________|/     #
    """,
    '2' : """
            ___________   #
           /          /|  #
          /  0   0   / |  #
         /          / 0|  #
        /__________/ 0 |  #
        |          |0  /  #
        |    0     |  /   #
        |          | /    #
        |__________|/     #
    """,
    '3' : """         
             ___________  #
            /          /| #
           /  0  0  0 / | #
          /          / 0| #
         /__________/  0| #
         |          |0  / #
         |   0  0   |0 /  #
         |          | /   #
         |__________|/    #
    """,
    '4' : """
            ___________   #
           /          /|  #
          /  0   0   / |  #  
         /  0   0   / 0|  #
        /__________/   |  #
        |  0   0   | 0 /  #
        |  0   0   |  /   #
        |  0   0   |0/    #
        |__________|/     #
    """,
    '5' : """
            ___________   #
           /  0   0   /|  #
          /    0     / |  #
         /  0   0   / 0|  #
        /__________/  0|  #
        | 0        |0  /  #
        |    0     |0 /   #
        |       0  | /    #
        |__________|/     #
    """,
    '6' : """
            ___________   #
           / 0     0  /|  #
          / 0     0  / |  #
         / 0     0  / 0|  #
        /__________/  0|  #
        |  0   0   |0  /  #
        |    0     |0 /   #
        |  0   0   | /    #
        |__________|/     #
    """},
    'dice02':{'1' : """    ____________  
    |\          \    
    | \     0    \  
    |  \          \  
    |0  \__________\
    \ 0 |          |
     \  |   0  0   |
      \ |   0  0   |
       \|__________|
       
       """,
    '2' : """    ____________  
    |\          \    
    | \   0  0   \  
    |  \          \  
    | 0 \__________\
    \   |          |
     \  |   0  0   |
      \ |   0  0   |
       \|__________|
       
       """,
    '3' : """    ____________  
    |\ 0        \    
    | \    0     \  
    |  \       0  \  
    | 0 \__________\
    \   |          |
     \  |   0  0   |
      \ |   0  0   |
       \|__________|
       
       """,
    '4' : """    ____________  
    |\          \    
    | \ 0     0  \  
    |  \  0    0  \  
    | 0 \__________\
    \   |          |
     \  |   0  0   |
      \ |   0  0   |
       \|__________|
       
       """,
    '5' : """    ____________  
    |\   0    0 \    
    | \      0   \  
    |  \    0   0 \  
    | 0 \__________\
    \   |          |
     \  |   0  0   |
      \ |   0  0   |
       \|__________|
       
       """,
    '6' : """    ____________  
    |\  0    0  \    
    | \  0    0  \  
    |  \  0    0  \  
    | 0 \__________\
    \   |          |
     \  |   0  0   |
      \ |   0  0   |
       \|__________|
       
       """}}

#get the name of gamers
os.system('cls' if os.name == 'nt' else 'clear')
winners = list()
for count in range(4):
    gamers[input(f"Enter with the name of the {count+1}º gamer: ")+str(count+1)] = dict({'winner' : 0})
    
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
    for gamer in temp.keys():
        print("The player:",gamer,"play:")
        part1 = dices['dice01'][str(temp[gamer]['dice01'])].split("#")
        part2 = dices['dice02'][str(temp[gamer]['dice02'])].split("\n")
        full=""
        for i in range(len(part1)):
            full += part1[i]+part2[i]
            full +=" \n "
        print(full)
        sleep(3)
        #clear all inputs prints
        os.system('cls' if os.name == 'nt' else 'clear')

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