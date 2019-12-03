# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 00:32:37 2019

@author: Essam
"""

from random import randint
import random



def individual(length,min,max):
    return [randint(min,max)for x in range(length)]

def population(count,length,min,max):
    return[individual(length,min,max) for x in range(count)]
    
    
def oneBox(indivi,i):
    return indivi[i:i+3]+indivi[i+9:i+12]+indivi[i+18:i+21]
    
def box(indi):
    return [oneBox(indi,i) for i in [0, 3, 6, 27, 30, 33, 54, 57, 60]]
all=9
def make2d(indivi):
    return [indivi[i*all:(i+1)*all]for i in range(9)]

def check(indivi):
    return sum(all-len(set(row))for row in indivi) 


def compare(xs1,xs2):
    return sum(1 if x1 and x1 != x2 else 0 for x1,x2 in zip(xs1,xs2))

def solution_fitness(fsolution,problem,fpuzzle=None):
    if not fpuzzle:
        fpuzzle=problem
        
    solution=make2d(fsolution)  #???????????????????????????????????????????
    fitness=check(solution)   #row
    fitness+=check(zip(*solution))    #column
    fitness+=check(box(fsolution))      #box
    
    
    fitness+=compare(fsolution,fpuzzle)
    
    return fitness/(len(fsolution) * 1.0)

def vector_fitness(solution):
    x=[]
    for i in range(9):
        x=x+[solution[i*all:(i+1)*all]]
    
    a=[1,2,3,4,5,6,7,8,9]
    for i in range(9):
        for j in range(9):
            z=[a[w]-x[i][j] if a[w]==x[i][j]  else a[w]  for w in range(len(a))] 
            for i in range(len(z)-1):
                if z[i]==0:
                    z.pop(i)
                
      
    return len(z)

      
#while cross-over tries to converge to a specific point in landscape,
# mutation does its best to avoid convergence and explore more areas. 

x=individual(81,0,9)
dataset=[0,0,4,3,0,0,2,0,9,0,0,5,0,0,9,0,0,1,0,7,0,0,6,0,0,4,3,0,0,6,0,0,2,0,8,7,1,9,0,0,0,7,4,0,0,0,5,0,0,8,3,0,0,0,6,0,0,0,0,0,1,0,5,0,0,3,5,0,8,6,9,0,0,4,2,9,1,0,3,0,0]
#print(x)
#print(solution_fitness(x,dataset))

#y=[x[i*9:(i+1)*9]for i in range(9)]
#for i in range(9):
#    w=check(y[i])
#print(check(w))
print(vector_fitness(x))

#print(solution_fitness(x,dataset))
#print(evolve(x,dataset))


