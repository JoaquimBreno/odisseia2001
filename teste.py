import pandas
df = pandas.read_csv("conexoes.csv", header=None)
df = df.T
for i in df:
    saida = df[i][0]
    chegada = df[i][1]
    peso = df[i][2]
print(df[i])

df = pandas.read_csv("usuarios.csv", header=None)
df = df.T
for i in df:
    name = df[i][0]
    username = df[i][1]
print(df[i])