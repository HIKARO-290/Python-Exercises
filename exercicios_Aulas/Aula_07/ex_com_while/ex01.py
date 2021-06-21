opcao = 0
while opcao != 5:
    valor01 = float(input("digite o primeiro valor para a operação \n"))
    valor02 = float(input("digite o segundo valor para a operação \n"))
    print('''
        Operações:
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
        \n
        ''')
    opcao = int(input("Digite o numero da operação que deseja: \n"))
    if opcao == 1:
        print(f"o resultado da soma será de:{valor01 + valor02}\n")
    elif opcao == 2:
        print(f"o resultado da multiplicação será de:{valor01 + valor02}\n")
    elif opcao == 3:
        if valor01>valor02:
            print(f"o maior valor é:{valor01}\n")
        else:
            print(f"o maior valor é:{valor02}\n")      
    elif opcao == 5:
        print("saindo")
        opcao = 5
    elif opcao != 4:
        print("numero incorreto!")
   
