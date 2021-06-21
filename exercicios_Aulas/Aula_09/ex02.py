valores = list()
pares = list()
impares = list()
para = "False"
while para:
    user_value = input("digite um valor:")
    valores.append(user_value)
    para = input("continuar? sim | não : ").strip().lower().startswith('s')
    if int(user_value)%2==0:
        pares.append(user_value)
    else:
        impares.append(user_value) 

print(f"""
        Os números digitados foram: {sorted(valores)}
        OS números pares são:   {sorted(pares)}
        Os números impares são: {sorted(impares)}
""")
