from random import randint
lista = ["pedra","papel","tesoura"]
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
jogar = True
while jogar:
    maquina = randint(0,2)
    jogador_str = str(input("digite sua opção pedra, papel ou tesoura: \n")).lower()
    jogador = lista.index(jogador_str)
    if jogador_str not in lista:
      print("opção inválida tente novamente")
      pass
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
        

    jogar = input("continuar jogando? sim | não : ").strip().lower().startswith('s')