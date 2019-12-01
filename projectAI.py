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
dim=9
def make2d(indivi):
    return [indivi[i*dim:(i+1)*dim]for i in range(dim)]

def check(indivi):
    return sum(dim-len(set(row))for row in indivi )


def compare(x1,x2):
    return sum(1 if x1 and x1 != x2 else 0 for x1,x2 in zip (x1,x2))

def sudoku_fitness(fsolution,problem,fpuzzle=None):
    if not fpuzzle:
        fpuzzle=problem
        
    solution=make2d(fsolution)
    fitness=check(solution)
    fitness+=check(zip(*solution))
    fitness+=check(box(fsolution))
    fitness+=compare(fsolution,fpuzzle)
    
    return fitness/(len(fsolution) * 1.0)


        

x=individual(81,0,9)
dataset=[0,0,4,3,0,0,2,0,9,0,0,5,0,0,9,0,0,1,0,7,0,0,6,0,0,4,3,0,0,6,0,0,2,0,8,7,1,9,0,0,0,7,4,0,0,0,5,0,0,8,3,0,0,0,6,0,0,0,0,0,1,0,5,0,0,3,5,0,8,6,9,0,0,4,2,9,1,0,3,0,0]
#print(x)
print(sudoku_fitness(x,dataset))
