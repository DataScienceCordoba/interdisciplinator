#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from collections import OrderedDict

df = pd.read_csv('formulario.csv')

counts = {c: sum(df[c] == 'Principiante') for c in df.columns}

l = counts.items()

s = sorted(l, key=lambda x: x[1])

#Inicializacion del arreglo de expertos e indice de columnas:
experts = [[]] * 8
index = {0 : 'Aprendizaje Automático (Machine Learning)', 
         1 : 'Conocimiento de Dominio(s) de Aplicación', 
		 2 : 'Visualización de Datos', 
		 3 : 'Comunicación y Presentación de ideas', 
		 4 : 'Estadística', 
		 5 : 'Matemática', 
		 6 : 'Programación', 
		 7 : 'Ciencias de la Computación'}

#experts[i] contiene los expertos y avanzados de cada conjunto de mayor a menor:
for i in range(0, 8):
	aux_ex = df[df[index[i]] == 'Avanzado']
	aux_ex_2= df[df[index[i]] == 'Expert@']
	l = aux_ex['Apellido']
	l.append(aux_ex_2['Apellido'])
	experts[i] = l
	
#Hacemos grupos sin repeticiones ni personas en comun:
exp_grupo = [[]] * 8
s = set([])
exp_grupo[0] = set(experts[0])
#print exp_grupo[0]
#t = len(exp_grupo[0])
for i in range (1, 8):
	s = s.union(set(exp_grupo[i-1]))
	exp_grupo[i] = set(experts[i]).difference(s)
	#t = t + len(exp_grupo[i])
	#print exp_grupo[i]
	#print t

all_exp = set(experts[0])
for i in range (1, 8):
	all_exp = all_exp.union(set(experts[i]))

t = len(all_exp)
#Repartimos parejo entre los grupos:
