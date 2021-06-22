# The user gives the values
# O usuário fornece os valores
note1 = float(input("Enter with the first note: "))
note2 = float(input("Enter with the second note: "))
note3 = float(input("Enter with the third note: "))
note4 = float(input("Enter with the fourth note: "))
# Apply the values in the formula
# aplica os valores na formula
middlenote = (note1 + note2 + note3 + note4)/4
# Show the result for the middle notes
# Mostra o resultado para a média
print(f"The middle note is: {middlenote:.1f}")