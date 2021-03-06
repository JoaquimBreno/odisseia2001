import pandas
import numpy as np

# ----------------------------------------------------------------------------------------------
# 
#
#
#
#
# ----------------------------------------------------------------------------------------------
# usuarios = pandas.read_csv("usuarios.csv", header=None)
# print("Usuarios: ")
# print(usuarios.T)
# print()



# conexoes = pandas.read_csv("conexoes.csv", header=None )
# print("conexoes: ")
# print(conexoes.T)
# print()
# print("conexoes T [0]")
# print(conexoes.T[0])

# ----------------------------------------------------------------------------------------------
# 
#
#   
#
#
# ----------------------------------------------------------------------------------------------
class Grafo():

    def __init__(self):
        self.matrizAdj = {}

    def iniciaGrafo(self, usuario):
        self.matrizAdj[usuario]= {}
    
    def conectaGrafo(self, origem, destino, peso):
        self.matrizAdj[origem][destino] = peso

    def carregaGrafos(self, arquivo):
        df = pandas.read_csv(arquivo, header=None)
        for usernames in df[1]:
            self.iniciaGrafo(usernames)
    
    def carregaConexoes (self, arquivo):
        df = pandas.read_csv(arquivo, header=None)
        for _, linha in df.iterrows():
            self.conectaGrafo(linha[0], linha[1], linha[2])

    def exibeSeguidos (self, usuario):
        print(f"Para o(a) usuário(a) de username: '{usuario}' foram encontradas {len(self.matrizAdj[usuario].keys())} pessoas seguidas.")

odisseia = Grafo()
odisseia.carregaGrafos("usuarios.csv")
odisseia.carregaConexoes("conexoes.csv")
odisseia.exibeSeguidos("sophia31")
