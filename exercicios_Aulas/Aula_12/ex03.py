#pede ao usuário uma opção

lista = list()
cont = 0
opcao = 0
while True:
#Cria dicionário para cadastrar aluno
    student = dict()
#exibe o menu
    option = input("""
        - [1]cadastrar média e novo aluno.
        - [2]visualizar media de alunos cadastrados.
        - [3]Sair do systema.
        """)
    if option.isnumeric():
        option = int(option)
    else:
        continue
#executa opção desejada
    if option == 1:
#pega volores dos alunos
        student['name'] = input("digite o nome do aluno: ")
        student['middle'] = float(input("digite a média do aluno: "))
#define status do aluno
        if student['middle'] >= 7:
            student['status'] = "aprovado"
        elif student['middle'] >= 5:
            student['status'] = "recuperação"
        else:
            student['status'] = "reprovado"
#adiciona dicionário do aluno em uma lista
        lista.append(student)
    elif option == 2:
#imprime boletim informativo
        if not lista:
            print("não existe alunos cadastrados")
        else:
            print("""
                    _____________________________________
                    |   Aluno   |   média   |   status  |
                    |___________|___________|___________|""")
            for a in lista:
                print(f"""
                    | {a['name']} | {a['middle']} | {a['status']} |
                 """)
            print("""                    _____________________________________
             """)
    elif option == 3:
#sai do sistema
        break
    