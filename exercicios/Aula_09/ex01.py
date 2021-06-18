valores = list()
para = True
while para:
    user_value = input("digite um valor:")
    if user_value not in valores:
        valores.append(user_value)
    para = (input("continuar? sim | não : ").strip().lower().startswith('s'))
print(f"os numeros em ordem crescente são: {sorted(valores)}")
