import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from pathlib import Path

lstViagens = pd.read_csv('a.csv', sep=';')
del lstViagens['Unnamed: 5']


def correlacao(column1, column2):
    column1_name = lstViagens.columns[column1]
    column2_name = lstViagens.columns[column2]

    correlation = lstViagens[column1_name].corr(lstViagens[column2_name],method='pearson')

    print(f"\nValor de correlação: { correlation }")

    
    plt.figure(figsize = (16,8))
    plt.scatter(
        lstViagens[column1_name], 
        lstViagens[column2_name], 
        c='red')
    plt.xlabel(column1_name)
    plt.ylabel(column2_name)
    plt.show()




def regressao(columnsX, columnY):
    lstColumnsX = columnsX.split(",")
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

    #print(intercept, coeficientRegression, score)

    predictionColumns = []
    print("\n=============Valores para predição=============\n")

    tem_arquivo = input('Você possui um arquivo (S/N): ')

    while (tem_arquivo not in ['S','N']):
        tem_arquivo = input('Caractere inválido, escreva novamente!! (S/N): ')

    while(tem_arquivo == 'S'): #Voce possui um arquivo (S/N):
        
        nome_arq = input('Digite o nome do arquivo (Sem o ".csv"): ')+'.csv'

        #Se você tem o arquivo ele existe?
        #Se sim:
        if Path(nome_arq).is_file():

            lstvalores = pd.read_csv(nome_arq, sep=',', header=None)
            for i in range(0,3):
                predictionColumns.append(float(lstvalores[i]))
            break        
            #Se não:

        tem_arquivo = input('Arquivo não encontrado, deseja tentar de novo? (S/N): ')
        while (tem_arquivo not in ['S','N']):
            tem_arquivo = input('Caractere inválido, escreva novamente!! (S/N): ')
        
            

    #Se não
    if tem_arquivo == 'N' :
        print("Digite os valores manualmente: ")
        for columnName in lstColumnNamesX:
            predictionColumns.append(float(input(columnName + ": ")))    
                
            
  


   
   
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
        columns = columnNames()
        [print("{}. {}".format(column, columns[column])) for column in columns]

        column1 = int(input("\nInsira o número da coluna 1: "))
        column2 = int(input("Insira o número da coluna 2: "))
        correlacao(column1, column2)

        if int(input("\n1. Voltar ao menu\n0. Sair\n")) == 1:
            menu()

    if option == 2:
        cls()
        flag = False
        columns = columnNames()
       
        [print("{}. {}".format(column, columns[column])) for column in columns]

        columnsX = input("\nEscolha as colunas para x separadas por virgula: ")

        
        while (flag == False):

            if (len(columnsX.split(",")) > 3 or len(columnsX.split(",")) < 2):
                print("Quantidade de colunas invalidas, minimo de 2 colunas maximo de 3")
                flag = False

            else:
                flag = True
            
            if flag == True:
                for column in columnsX.split(","):
                    if int(column) not in [1,2,3,4]:
                        flag = False
                        print("Coluna com valor invalido, digite novamente!")
                        break
                    flag = True

            if flag == False:
                columnsX = input("\nEscolha novamente as colunas para x separadas por virgula: ")
                
           
           
        for column in columnsX.split(","):
            del columns[int(column)]
    

        if(len(columnsX.split(",")) == 3):
            regressao(columnsX, list(columns.values())[0])
        else:
            [print("{}. {}".format(column, columns[column])) for column in columns]
            
            columnY = int(input("\nEscolha a coluna para y: "))
            
    

            regressao(columnsX, columns[columnY])

        if int(input("\n1. Voltar ao menu\n0. Sair\n")) == 1:
            menu()


menu()