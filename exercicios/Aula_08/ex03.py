lista = [5, 7, 2, 9, 4, 1, 3] 
print(f"""
    - o tamanho da lista é = {len(lista)}
    - o maior valor na lista é = {max(lista)}
    - o menor valor na lista é = {min(lista)}
    - a soma de todos os elemento é = {sum(lista)}
    - a lista em ordem crescente é = {sorted(lista)}
    - a lista em ordem decrescente é = {sorted(lista,reverse=True)}
""")
