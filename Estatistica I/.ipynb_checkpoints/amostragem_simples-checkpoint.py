# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:37:32 2019

@author: victor.bertoldo
"""
# Importação das bibliotecas
import pandas as pd
import numpy as np


#Import do arquivo csv de mesmo diretorio
base = pd.read_csv('iris.csv')
# Lendo o dataset
base
#retorna o tamanho do dataset
base.shape

#Impede de mudar o valor randomico a cada execução
np.random.seed(2345)
#Faz a escolha randomica -- o a gera os valores (flag), size é o tamanho do dataset, replace = false ele impede q o valor seja usado 
# novamente, p é a problabilidade o seu somatorio tem q ser igual a 1
amostra = np.random.choice(a = [0,1], size = 150, replace = True,
                            p=[0.5, 0.5])
len(amostra)
len(amostra[amostra == 1])
len(amostra[amostra == 0])