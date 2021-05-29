import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

lst_viagens = pd.read_csv('viagens2.csv', sep=';')
del lst_viagens['Unnamed: 5']

def correlacao(column1, column2):
    column1_name = lst_viagens.columns[column1]
    column2_name = lst_viagens.columns[column2]

    correlation = lst_viagens[column1_name].corr(lst_viagens[column2_name])

    print(f"\nValor de correlação: { correlation }")

def regressao(column1, column2, column3):
    column1_name = lst_viagens.columns[column1]
    column2_name = lst_viagens.columns[column2]
    column3_name = lst_viagens.columns[column3]
    
    x = lst_viagens[[column1_name, column2_name]]
    y = lst_viagens[column3_name]

    regression = linear_model.LinearRegression()
    regression.fit(x, y)
    coeficientRegression = regression.coef_
    score = regression.score(x, y)
    
    #qual é a média pro "nome3" quando o "nome" e o "nome2" são = 1000
    prediction = regression.predict([[1000, 1000]])
    
    print(f"\n{ coeficientRegression }")
    print(f"\nCoeficiente de determinação R² da predição: { score }")
    print(f"\nPredição usando o modelo linear: { float(prediction) }")

def printColumns(columns):
    for col in range(1, len(columns)):
        print(col, ".", columns[col])

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def menu():
    cls()
    printColumns(lst_viagens.columns)
    option = int(input("\n1. Correlação\n2. Regressão\n0. Sair\n"))

    if option == 1:
        column1 = int(input("\nInsira o número da coluna 1: "))
        column2 = int(input("Insira o número da coluna 2: "))
        correlacao(column1, column2)
        
        if int(input("\n1. Voltar ao menu\n0. Sair\n")) == 1:
            menu()


    if option == 2:
        column1 = int(input("\nInsira o número da coluna 1: "))
        column2 = int(input("Insira o número da coluna 2: "))
        column3 = int(input("Insira o número da coluna 3: "))
        regressao(column1, column2, column3)

        if int(input("\n1. Voltar ao menu\n0. Sair\n")) == 1:
            menu()

menu()