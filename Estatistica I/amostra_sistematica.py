# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:50:00 2019

@author: victor.bertoldo
"""

import numpy as np
import pandas as pd
from math import ceil

populacao = 150
amostra = 14
k = ceil(populacao /  amostra)

r = np.random.randint(low=1,high = k+1, size = 1)

acumulador = r[0]
sorteados = []
for i in range(amostra):
    #print(acumulador)
    sorteados.append(acumulador)
    acumulador += k

base = pd.read_csv('iris.csv')
base_final = base.loc[sorteados]    