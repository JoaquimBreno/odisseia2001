import pandas
import numpy as np


class Grafo():

    def __init__(self):
        self.matrizAdj = {}
        """
        {[usuario] = {
                       [segue] = peso 
                       }
         }
        """

        self.userData = {}
        """
        [usuario] = {[nome] = nome
                       [seguindo] = usuario segue x pessoas
                       [seguidores] = y pessoas seguem usuario
                     }
        
         }
         """

    def iniciaGrafo(self):
        df = pandas.read_csv("usuarios.csv", header=None)
        df = df.T
        for i in df:
            name = df[i][0]
            username = df[i][1]
            self.matrizAdj[username] = {}
            self.userData[username] = {}
            self.userData[username]["nome"] = name
            self.userData[username]["seguindo"] = 0
            self.userData[username]["seguidores"] = 0

        df = pandas.read_csv("conexoes.csv", header=None)
        df = df.T
        for i in df:
            saida = df[i][0]
            chegada = df[i][1]
            peso = df[i][2]
            self.matrizAdj[saida][chegada] = peso
            self.userData[saida]["seguindo"] += 1
            self.userData[chegada]["seguidores"] += 1

        self._ordenaGrafo()
        
    def _ordenaGrafo(self):
        self.userData = dict(sorted(self.userData.items()))
        self.matrizAdj = dict(sorted(self.matrizAdj.items()))
        for usuario in self.matrizAdj:
            self.matrizAdj[usuario] = dict(sorted(self.matrizAdj[usuario].items()))
            self.matrizAdj[usuario] = dict(sorted(self.matrizAdj[usuario].items(), reverse = True, key= lambda x: x[1]))

    def exibeSeguidos(self, usuario):
        print(f"Usuario {usuario} segue {(self.userData[usuario]['seguindo'])} pessoas. \n")

    def exibeSeguidores(self, usuario):
        print(f"Usuario {usuario} é seguido(a) por {(self.userData[usuario]['seguidores'])} pessoas. \n")

    def exibirStories(self, usuario):
        print("Visualizar story de: ") 
        for key in self.matrizAdj[usuario]:
            print(key)

    def _topK(self, k):
        mais_seguidos = self.userData = dict(sorted(self.userData.items(), reverse=True, key = lambda x: x[1]["seguidores"] ))
        top = []
        for pessoa in mais_seguidos.keys():
            top.append(pessoa)
        return top[:k]

    def topK(self, k):
        i = 1
        for user in self._topK(k):
            print(i, "-", user, "possui ", self.userData[user]["seguidores"], "seguidores")
            i += 1

    def buscaGrafo(self, usuario1, usuario2):
        pass


odisseia = Grafo()
odisseia.iniciaGrafo()
print("exibir topK: ")
odisseia.topK(5)
print()
print("exibir seguidores:")
odisseia.exibeSeguidores("helena42")
print()
print("exibir seguidos:")
odisseia.exibeSeguidos("helena42")
print()
odisseia.exibirStories("helena42")