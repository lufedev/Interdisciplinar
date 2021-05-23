import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

viagens = pd.read_csv('viagens2.csv', sep=';')
del viagens['Unnamed: 5']

def correlacao(c1,c2):
    nome = viagens.columns[c1]
    nome2 = viagens.columns[c2]

    print("\nValor de correlação: ",viagens[nome].corr(viagens[nome2]))

def regressao(c1,c2):
    nome  = viagens.columns[c1]
    nome2 = viagens.columns[c2]

    # Set the features of our model, these are our potential inputs

    valores = [nome,nome2]

    # Set the variable X to be all our input columns: Temperature, Wind Speed and Pressure

    X = viagens[valores]

    # set y to be our output column: Humidity

    y = viagens['Outros Gastos']

    # plt.subplot enables us to plot mutliple graphs
    # we produce scatter plots for Humidity against each of our input variables

    plt.subplot(2,2,1)
    plt.plot(X[nome],y)
    plt.subplot(2,2,2)
    plt.plot(X[nome2],y)
    plt.show()
    
   


for col in range(1,len(viagens.columns)):
    print(col,".",viagens.columns[col])

c1 = int(input("\nInsira o número da coluna 1: "))
c2 = int(input("Insira o número da coluna 2: "))
regressao(c1,c2)

