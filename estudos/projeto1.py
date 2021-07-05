print("""
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                               ./+-                                                                   
                                     +NNNNNNmmho.                             `MMMM:                `-:/                                              
                                     mMMMyyydMMMM+                             /ss/                /MMMs                                              
                                    /MMMh    oMMMm  :+++.`/o+    -+oso+:`     /+++`    ./ooo+:`  /+mMMMs++`   ./oooo/`                                
                                    dMMM:   `hMMMh  mMMMoNMMs `sNMMMMMMMN+   .MMMm  `omMMmdNMMN--MMMMMMMMd  +mMMMMMMMMy`                              
                                   -MMMMysshNMMMh` -MMMMd/::`.NMMN+` .mMMM-  oMMMo .mMMd.  /MMMo  yMMM:    hMMMs. `yMMMs                              
                                   yMMMMMMNNmy+.   yMMMs     dMMM:    yMMM/ `mMMN` hMMMdhhmMMmo` `NMMm    +MMMy    :MMMy                              
                                  `MMMN`          `NMMm`    `NMMN`   .NMMN` /MMMy `NMMNo++/-`    oMMM+    yMMM:    hMMM/                              
                         :ss`     oMMMs           oMMMo      yMMMy//sNMMN-  dMMM-  hMMMs---:o+   dMMMs//  /MMMm/:+mMMMo                               
               oyyyo/.  ohhh     `mMMM.           mMMN.      `omMMMMMMd+`  -MMMd   `smMMMMMMm-   +NMMMMy   /dMMMMMMms.                                
               -shhhddhsmNmo++/:.`....            ....          `---.      hMMM:      `---.       `---`      `.--.`                                   
                  -+hddmysyhhhhyddhs/`                                 -:/hMMMo                                                                       
                 `+hhddhysyyhyoooydhhdy+`                              mMMMMh:                                                                        
                /hyymdssohhhhyyhhhyhhsosds.                            .--.                                                                           
              `yhyyddhosyyh+++oohhyyssyhyhmo`                  `/ydmNmh+`     .-/+oyhd.                                                               
              hhyyhmyydyyyyyssyhhhsoooosdhyhd-                /NMMNhhNMMm.   .MMMMMMMh                                                                
            `ydyyyhdoodyysoohhyyhyhhyhhhyhsood/              sMMMy`  /MMMo   .:-`hMMM:                                                                
            ymhyyyddyhhyooosyhssoooohyyyhhdhyhmsoooooo++:.  +MMMh    /MMMs      .MMMm                                                                 
           :hdyyyydmyyhhhhhyyhsoosyyhdddhhhhyyyyyyyyyyyyhddyNMMN.    yMMM/      oMMM+                                                                 
           yhmyyyyhNysoohyyhhhdhhhyyyyyyyyyyyyyyyyyyhhhddhysMMMh    -MMMm`     `NMMN`                                                                 
           mhmyyyyymhoosydhhyyyyyyyyhhhhhhdddmmmdhhyo+:-`  /MMMo   `dMMM:      /MMMs                                                                  
           mhhsssyyhNdNNmmddhsooooo++++/::-:-.`            `NMMm:-/mMMN:       dMMM.                                                                  
           yyhhyhdmNMNmmmho-                                -hMMMMMMNs`       -MMMh                                                                   
           :mhNNNmmddmdo.                                     `://:.          .:::.                                                                   
         `+mmddddddms-                                                                          `:/:                                                  
        :dmdddddmh/`          sNNNNNNmdhs/`                     `-:-                   `.:/     dMMMo                                                 
      .ymddddmds-            `NMMMdddmMMMMMs`                  yMMM:                  /MMMy     :syo`                                                 
     :mdddmmy:`              oMMMs    `:mMMMh      -/+o+/.  `++MMMN++/    ./+oo+:   /+dMMMs++` -+++.  :+++`    -+++:    -/+o+/.                       
    -Ndmmh+`                `mMMM-      :MMMM`  .sNMMddMMMh`oMMMMMMMMo `+mMMmdNMMN--MMMMMMMMm  mMMM.  oMMM:   :MMMd` .yNMNddMMMh                      
    `++:`                   /MMMh       :MMMM` :NMMs`  yMMM- `NMMN``` `dMMd.  /MMMo `yMMM/``  :MMMh   :MMM+  :NMMh` /MMMo`  hMMM`                     
                            dMMM:       hMMMy `NMMMyyhNMMm/  /MMMs    hMMMhyhmMMNs` `NMMm     hMMM:   `NMMs -NMMs  .MMMNyyhNMMd/                      
                           -MMMm      :dMMMd` :MMMdo++/-`    dMMM.    NMMNoo+/:.    +MMMo    .MMMm     hMMh-NMM+   +MMMdo++/-`                        
                           yMMMdsssshNMMMNo   .NMMN/..-/o-  `MMMM/::  hMMMo-..:++   dMMMs:/  +MMMd::   oMMNNMN/    .MMMm/..-/s.                       
                          `NMMMMMMMMMNds:`     -hMMMMMMMd    hMMMMM/  `sNMMMMMMm-   +MMMMMy  -mMMMMs   -MMMMN-      -hMMMMMMNh                        
                          `........``            `.-:-.       .-:-`      .-:--`      `-:-.     -:--`    ....`         `-::-.                          
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      

""")
#realizando perguntas e somando quantidade de respostas
quantidade = 0
####################
#primeira pergunta #
####################
r = input("""responda as perguntas utilizando 's' p/sim ou 'n' para não: \n
  • Você telefonou para a vítima? \n""").lower().strip()
if r.startswith('s'):
  quantidade +=1
  print("você está se complicando \n")
r = ""
r = input("  • Você esteve no local do crime? \n").lower().strip()
####################
# segunda pergunta #
####################
if r.startswith('s'):
  quantidade +=1
  if quantidade == 1:
    print("você está se complicando! \n")
    
  else:
    print("Você está se complicando cada vez mais! \n")
r = ""
#####################
# terceira pergunta #
#####################
r = input("  • Você mora perto da vítima? \n").lower().strip()
if r.startswith('s'):
  quantidade +=1
  if quantidade == 1:
    print("você está se complicando! \n")
  elif quantidade == 2:
    print("Você está se complicando cada vez mais! \n")
  else:
    print("Veja bem não tenho tempo a perder. Caso seja o culpado! CONFESSE LOGO!!! \n")    
r = ""
###################
# quarta pergunta #
###################
r = input("  • Você devia para a vítima? \n").lower().strip()
if r.startswith('s'):
  quantidade +=1
  if quantidade == 1:
    print("você está se complicando! \n")
  elif quantidade == 2:
    print("Você está se complicando cada vez mais! \n")
  elif quantidade ==3:
    print("Veja bem não tenho tempo a perder. Caso seja o culpado! CONFESSE LOGO!!! \n")
  else:
    print("você já está a meio passo da prisão... \n")    
r = ""
###################
# quinta pergunta #
###################
r = input("  • Você já trabalhou com a vítima? \n").lower().strip()
if r.startswith('s'):
  quantidade +=1
  if quantidade == 1:
    print("você está se complicando! \n")
  elif quantidade == 2:
    print("Você está se complicando cada vez mais! \n")
  elif quantidade ==3:
    print("Veja bem não tenho tempo a perder. Caso seja o culpado! CONFESSE LOGO!!! \n")
  elif quantidade == 4:
    print("você já está a meio passo da prisão... \n")
#####################################
# imprimindo resultado da acariação #
#####################################
if quantidade == 2:
  print("Você é considerado suspeito(a), e continuará sendo investigado.")
elif 3<=quantidade<=4:
  print("VOCÊ É CONSIDERADO CÚMPLICE, Agora diga quem é o arquitedo deste crime!")
elif quantidade == 5:
  print("VOCÊ É O ASSASSINO, SERÁ PRESO E TRANCAFIADO NA CADEIA...")
else:
  print("Logo quando pensei que seria você o culpado. hahahah.pode ir você é Inocente! ")