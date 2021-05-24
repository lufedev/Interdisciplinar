import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

viagens = pd.read_csv('viagens2.csv', sep=';')
del viagens['Unnamed: 5']

def correlacao(c1,c2):
    nome = viagens.columns[c1]
    nome2 = viagens.columns[c2]

    print("\nValor de correlação: ",viagens[nome].corr(viagens[nome2]))

def regressao(c1,c2,c3):
    nome  = viagens.columns[c1]
    nome2 = viagens.columns[c2]
    nome3 = viagens.columns[c3]
    X = viagens[[nome,nome2]]
    Y = viagens[nome3]

    regr = linear_model.LinearRegression()
    regr.fit(X, Y)
    #qual é a média pro "nome3" quando o "nome" e o "nome2" são = 1000
    pred = regr.predict([[1000, 1000]])
    print(regr.coef_) 
    print(pred) 


for col in range(1,len(viagens.columns)):
    print(col,".",viagens.columns[col])

c1 = int(input("\nInsira o número da coluna 1: "))
c2 = int(input("Insira o número da coluna 2: "))
correlacao(c1,c2)
c1 = int(input("\nInsira o número da coluna 1: "))
c2 = int(input("Insira o número da coluna 2: "))
c3 = int(input("Insira o número da coluna 3: "))
regressao(c1,c2,c3)

