#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from collections import OrderedDict
import random

df = pd.read_csv('mergedData.csv')
f = open('grupos', 'w')

columns= ['Aprendizaje Automático (Machine Learning)', 'Conocimiento de Dominio(s) de Aplicación', 
'Visualización de Datos','Comunicación y Presentación de ideas', 'Estadística', 'Programación', 'Ciencias de la Computación']
counts = {c: sum(df[c] == 'Principiante') for c in columns}

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
    l = aux_ex['Name']
    l.append(aux_ex_2['Name'])
    experts[i] = l
    
#Hacemos grupos sin repeticiones ni personas en comun:
exp_grupo = [[]] * 8
s = set([])
exp_grupo[0] = set(experts[0])
print ('--------------' + index[0] + '--------------')
print (pd.Series(list(exp_grupo[0])))
#t = len(exp_grupo[0])
for i in range (1, 8):
    s = s.union(set(exp_grupo[i-1]))
    exp_grupo[i] = set(experts[i]).difference(s)
    #t = t + len(exp_grupo[i])
    print ('--------------' + index[i] + '--------------')
    print (pd.Series(list(exp_grupo[i])))
    #print t

#all_exp = set(experts[0])
all_exp_list = list(experts[0])
for i in range (1, 8):
    #all_exp = all_exp.union(set(experts[i]))
    all_exp_list = all_exp_list + list(experts[i])

#print type (all_exp_list)
random.shuffle(all_exp_list,  random.random)
exp_grupo = set(all_exp_list)

''' 
print 'set'
print all_exp
print 'list'
print all_exp_list
'''
t = len(exp_grupo)

#Repartimos parejo entre los grupos:
members = set(df['Name'])
cant_members = len(members)
f.write( '\n=============================')
f.write( "Cantidad de miembros:" + str(cant_members))

g=5

cant_grupos = int(cant_members/g)
f.write( '\n=============================')
f.write( "Cantidad de grupos:" + str(cant_grupos))

'''
resto = cant_members - cant_grupos * g
print '\n============================='
print "Personas sin grupo:" + str(resto)
'''

f.write( '\n=============================')
f.write( '\n===========Grupos:=============')
f.write( '\n=============================')

not_exp_members = set(members).difference(exp_grupo)
lst = list(exp_grupo)
not_exp_list = list(not_exp_members)

exps = [ lst[i::cant_grupos] for i in range(0, cant_grupos) ]
not_exp = [ not_exp_list[i::cant_grupos] for i in range(0, cant_grupos) ]
not_exp.reverse()

map_grupos = {}
grupos = [[]] * cant_grupos
for i in range(0, cant_grupos):
    grupos[i] = exps[i] + not_exp[i]
    f.write( '\nGrupo' + str(i))
    f.write( str(grupos[i]))
    for apellido in grupos[i]:
        map_grupos[apellido] = i

f.write( '\n=============================')
f.write ('\n=============================')
f.write( '\n=============================')


df['Grupo'] = df.Name.apply(lambda x: map_grupos[x])
df[['Name', 'Grupo']].to_csv('lista_grupos.csv', index=False)

'''

print '\n============================='
print len(not_exp_list)
print len(exp_grupo)
print 'not experts'
print not_exp_list
print 'grupos'
a = 2
grupos = [not_exp_list[i:i+a] for i  in range(0, len(not_exp_list), a)]
'''


