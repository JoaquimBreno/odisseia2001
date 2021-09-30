import pandas
import numpy as np


class Grafo():

    def __init__(self):
        self.matrizAdj = {}
        """
        {[usuario] = {
        [seguindo] = peso 
                       }
         }
        """

        self.userData = {}
        """
        [usuario] = {
        [nome] = nome
        [seguindo] = usuario segue x pessoas
        [seguidores] = y pessoas seguem usuario
                     }
        
         }
         """

    def iniciaGrafo(self):
        """
         Lê os 2 arquivos, monta o grafo, organizar os dados dos usuários e ordena o grafo.
        """
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
        """
        Primeiro organizamos o dicionário geral e depois ordenamos os dicionários internos, priorizando conexões peso 2
        """
        self.userData = dict(sorted(self.userData.items()))
        self.matrizAdj = dict(sorted(self.matrizAdj.items()))
        for usuario in self.matrizAdj:
            self.matrizAdj[usuario] = dict(sorted(self.matrizAdj[usuario].items()))
            self.matrizAdj[usuario] = dict(sorted(self.matrizAdj[usuario].items(), reverse=True, key=lambda x: x[1]))

    def exibeSeguidos(self, usuario):
        """
        Acessa self.userData e imprime quantas pessoas o usuário segue.
        """
        print(f"Usuario {usuario} segue {(self.userData[usuario]['seguindo'])} pessoas. \n")

    def exibeSeguidores(self, usuario):
        """
        Acessa self.userData e imprime quantas pessoas segue o usuário.
        """
        print(f"Usuario {usuario} é seguido(a) por {(self.userData[usuario]['seguidores'])} pessoas. \n")

    def exibirStories(self, usuario):
        """
        Imprime username de cada usuário.
        """
        print(f"Visualizar story de: {usuario}")
        for key in self.matrizAdj[usuario]:
            print(key)

    def _topK(self, k):
        """
        Reordena o userData por ordem de seguidores.
        """
        mais_seguidos = dict(sorted(self.userData.items(), reverse=True, key=lambda x: x[1]["seguidores"]))
        top = []
        for pessoa in mais_seguidos.keys():
            top.append(pessoa)
            if len(top) >= k:
                break
        return top[:k]

    def topK(self, k):
        """
        Imprime o '_topk'
        """
        i = 1
        for user in self._topK(k):
            print(i, "-", user, "possui ", self.userData[user]["seguidores"], "seguidores")
            i += 1

    def buscaGrafo(self, usuario1, usuario2):
        ordemBuscaLargura = [usuario1]
        visitados = []
        predecessor = {usuario1: None}

        while len(ordemBuscaLargura) > 0:
            primeiro_elemento = ordemBuscaLargura[0]
            ordemBuscaLargura = ordemBuscaLargura[1:]
            visitados.append(primeiro_elemento)
            for adjacente in self.matrizAdj[primeiro_elemento].keys():
                if adjacente == usuario2:
                    pred = primeiro_elemento
                    caminho_invertido = [usuario2]
                    while pred is not None:
                        caminho_invertido.append(pred)
                        pred = predecessor[pred]
                    caminho = ''
                    for no in caminho_invertido[::-1]:
                        caminho += f'{no} -> '
                    return print(f"O caminho entre os dois usuários informados é :{caminho[:-3]}")

                if adjacente not in ordemBuscaLargura and adjacente not in visitados:
                    predecessor[adjacente] = primeiro_elemento
                    ordemBuscaLargura.append(adjacente)

        return False


odisseia = Grafo()
odisseia.iniciaGrafo()
print("exibir topK: ")
odisseia.topK(5)
print()
print("exibir seguidores:")
odisseia.exibeSeguidores("sophia31")
print()
print("exibir seguidos:")
odisseia.exibeSeguidos("sophia31")
print()
odisseia.exibirStories("sophia31")
odisseia.buscaGrafo("helena42", "arthur46")