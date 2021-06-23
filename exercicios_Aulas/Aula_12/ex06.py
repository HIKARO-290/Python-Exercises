#pede ao usuário uma opção

lista = list()
cont = 0
opcao = 0
for controller in range(15):
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
#pega as notas
        student['note1'] = float(input("digite a primeira nota do aluno: "))
        student['note2'] = float(input("digite a segunda nota do aluno: "))
        student['note3'] = float(input("digite a terceira nota do aluno: "))
        student['note4'] = float(input("digite a quarta nota do aluno: "))
        student['note5'] = float(input("digite a quinta nota do aluno: "))
        student['middle'] = (student['note1']+ student['note2']+ student['note3']+ student['note4']+ student['note5'])/5
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
            for a in lista:
                print(f"""
                    _________________________________________________
                    |   Aluno   |  notas    |   status              |
                    |___________|___________|_______________________|
                    | {a['name']}                                        |
                    |_______________________________________________|
                    |   nota 01 |       {a['note1']:.1f}      |                  |
                    |   nota 02 |       {a['note2']:.1f}      |                  |
                    |   nota 03 |       {a['note3']:.1f}      |                  |   
                    |   nota 04 |       {a['note4']:.1f}      |                  |
                    |   nota 05 |       {a['note5']:.1f}      |                  |
                    |   média : |       {a['middle']:.1f}      |      {a['status']}    |
                    |___________|________________|________________|
                 """)
    elif option == 3:
#sai do sistema
        break
