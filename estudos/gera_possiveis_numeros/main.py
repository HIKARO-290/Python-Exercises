from classes.geraconjuntos import GeraConjuntos
resultado = GeraConjuntos(int(input("digite o numero máximo do sorteio: ")))
resultado = resultado.geralista()
for i in range(len(resultado)):
    print(resultado[i])