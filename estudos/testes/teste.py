from random import randint  
partidas = dict() 
jogadores = dict()  
quantPartidas = int(input('Quantas partidas quer realizar? '))  
for contadorPartidas in range(quantPartidas):
    lista = list()      
    for partida in range(4):         
        lista.append(randint(1,6))         
        print('frase')     
    partidas['partida'+ str(contadorPartidas+1)] = lista  
for jog in range(1,5):
    jogadores['jogador'+str(jog)] = list()  
conta = 0
for key in partidas.keys():     
    temp = list(partidas[key])     
    temp = sorted(temp)      
    for ordenando in range(4):
        jogadores['jogador'+str(ordenando+1)].append(temp.index(partidas[key][ordenando])+1)
        for i in range(ordenando):
            if i!=0:
                if jogadores['jogador'+str(ordenando+1)][conta] == jogadores['jogador'+str(i)][conta]:
                    jogadores['jogador'+str(ordenando+1)][conta] +=1 
                    conta+=1
                else:
                    conta+=1
                    pass
            else:
                conta+=1
vitorias = list() 
print(jogadores)
for key in jogadores.keys():     
    vitorias.append(jogadores[key].count(1)) 
print(f'O jogador{vitorias.index(max(vitorias))+1} é o grande campeão.')
