# The user gives the values
# O usuário fornece os valores
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
nota4 = float(input("digite a quarta nota: "))
# Apply the values in the formula
# aplica os valores na formula
media = (nota1 + nota2 + nota3 + nota4)/4
# Show the result for the middle notes
# Mostra o resultado para a média
print(f"a média das notas é de:{media:.1f}")