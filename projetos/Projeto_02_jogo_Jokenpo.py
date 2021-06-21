#importa biblioteca random
from random import randint
#gera lista de opções
lista = ["pedra","papel","tesoura"]
#gera lista de imagens
iten = ["""
                  _________                                   
                 /%%%%%%%%/|
                /%%%%%%%%/@|
               /________/@@|
               |########|@@|
               |########|@/
               |________|/
                  Pedra

        """,
        """                                                  
              @@@@@@@@@@@@@@@
               @.............@
               @@@@@@@@@@@@@@@
              @.............@
              @@@@@@@@@@@@@@@
               @.............@
               @@@@@@@@@@@@@@@
              @.............@
              @@@@@@@@@@@@@@@ 
                    Papel """,
        """                                               
                       @
                      !@!
                      !@!
                      !@!
                    !@! !@!
                   @  @ @  @
                   @  @ @  @                                  
                    !@! !@!
                    Tesoura           
                                                  """]
#atribui verdadeiro para loop
jogar = True
#inicia loop
while jogar:
    maquina = randint(0,2)
#recebe valor de jogada
    jogador_str = str(input("digite sua opção pedra, papel ou tesoura: \n")).lower()
#verifica se opção existe   
    if jogador_str not in lista:
      print("opção inválida tente novamente")
      continue
#pega index da escolha do jogador
    jogador = lista.index(jogador_str)
#verifica quem venceu a jogada e apresenta o que foi jogado
    if maquina == jogador :
        print(f""""
              você:{iten[jogador]}

              maquina: {iten[maquina]}
              \n você empatou!""")
    elif maquina == 1 and jogador==0 or maquina==2 and jogador==1 or maquina == 0 and jogador == 2:
        print(f""""
                você:{iten[jogador]}  

                maquina:{iten[maquina]}
        você perdeu!""")
    else:
        print(f""""
                você:{iten[jogador]}

                maquina: {iten[maquina]}
        você ganhou!""")
        
#pergunta se deseja jogar novamente
    jogar = input("continuar jogando? sim | não : ").strip().lower().startswith('s')