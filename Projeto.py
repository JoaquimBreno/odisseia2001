import pandas

# ----------------------------------------------------------------------------------------------
# 
#
#
#
# oi
# Testando
# 
#
# ----------------------------------------------------------------------------------------------
usuarios = pandas.read_csv("usuarios.csv", header=None)
print("Usuarios: ")
print(usuarios.T)
print()



conexoes = pandas.read_csv("conexoes.csv", header=None )
print("conexoes: ")
print(conexoes.T)
print()
print("conexoes T [0]")
print(conexoes.T[0])

class Grafo():

    def __init__(self):
        self.matrizAdj = {}

    