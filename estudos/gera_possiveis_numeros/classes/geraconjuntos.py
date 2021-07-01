class GeraConjuntos:
    def __init__(self,valor):
        self.maximo = valor

    def geralista(self):
        listaconjunto = list()
        for k in range(self.maximo-6):
            for i in range(k,self.maximo-6):
                listaconjunto.append(list())
                listaconjunto[i].append(k
                
                +1)
                for j in range(i+2,i+7):
                    listaconjunto[i].append(j)
        return listaconjunto
