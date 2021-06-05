import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

lstViagens = pd.read_csv('viagens.csv', sep=';')
del lstViagens['Unnamed: 5']


def correlacao(column1, column2):
    column1_name = lstViagens.columns[column1]
    column2_name = lstViagens.columns[column2]

    correlation = lstViagens[column1_name].corr(lstViagens[column2_name])

    print(f"\nValor de correlação: { correlation }")


def regressao(columnsX, columnY):
    lstColumnsX = columnsX.split(" ")
    lstColumnNamesX = []

    for column in lstColumnsX:
        lstColumnNamesX.append(lstViagens.columns[int(column)])

    x = lstViagens[lstColumnNamesX]
    y = lstViagens[columnY]

    regression = linear_model.LinearRegression()
    regression.fit(x, y)

    intercept = regression.intercept_
    coeficientRegression = regression.coef_
    score = regression.score(x, y)

    # print(intercept, coeficientRegression, score)

    predictionColumns = []
    print("\nValores para predição:\n")
    
    for columnName in lstColumnNamesX:
        predictionColumns.append(float(input(columnName + ": ")))
        
    #qual é a média pro "nome3" quando o "nome" e o "nome2" são = 1000
    prediction = regression.predict([predictionColumns])
  
  
    if len(coeficientRegression) > 2:
       print("\nNovo {} = {:.4}  + {} * {} + {} * {} + {} * {}".format(columnY, intercept, coeficientRegression[0], predictionColumns[0],coeficientRegression[1], predictionColumns[1], coeficientRegression[2], predictionColumns[2]))
    else:
       print("\nNovo {} = {:.4}  + {} * {} + {} * {}".format(columnY, intercept, coeficientRegression[0], predictionColumns[0], coeficientRegression[1], predictionColumns[1]))
    
    # print("\nNovo {} = {:.4}".format(columnY, intercept))
    print("Novo {} feito através da predição {:.4f}".format(columnY, float(prediction)))


def columnNames():
    columns = {}
        
    for col in range(1, len(lstViagens.columns)):
        columns[col] = lstViagens.columns[col]

    return columns


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    cls()
    # printColumns(lstViagens.columns)
    option = int(input("\n1. Correlação\n2. Regressão\n0. Sair\n"))

    if option == 1:
        cls()
        [print("{}. {}".format(i, columnName))
         for i, columnName in columnNames()]

        column1 = int(input("\nInsira o número da coluna 1: "))
        column2 = int(input("Insira o número da coluna 2: "))
        correlacao(column1, column2)

        if int(input("\n1. Voltar ao menu\n0. Sair\n")) == 1:
            menu()

    if option == 2:
        cls()
        
        columns = columnNames()
       
        [print("{}. {}".format(column, columns[column])) for column in columns]

        columnsX = input("\nEscolha as colunas para x: ")
       
        for column in columnsX.split(" "):
            del columns[int(column)]
    
        if(len(columnsX.split(" ")) == 3):
            regressao(columnsX, list(columns.values())[0])
        else:
            [print("{}. {}".format(column, columns[column])) for column in columns]
            
            columnY = int(input("\nEscolha a coluna para y: "))
            
    

            regressao(columnsX, columns[columnY])

        if int(input("\n1. Voltar ao menu\n0. Sair\n")) == 1:
            menu()


menu()
