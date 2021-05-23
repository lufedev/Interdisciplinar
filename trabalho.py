import pandas as pd

viagens = pd.read_csv('viagens2.csv', sep=';')
del viagens['Unnamed: 5']

def correlacao(c1,c2):
    nome = viagens.columns[c1]
    nome2 = viagens.columns[c2]

    print("\nValor de correlação: ",viagens[nome].corr(viagens[nome2]))




for col in range(1,len(viagens.columns)):
    print(col,".",viagens.columns[col])

c1 = int(input("\nInsira o número da coluna 1: "))
c2 = int(input("Insira o número da coluna 2: "))
correlacao(c1,c2)

