# -*- coding: utf-8 -*-

#import numpy as np

file = open('TermoSol.txt', 'r')

COORDINATES = [] # case 1
ELEMENT_GROUPS = [] # case 2
INCIDENCES = [] # case 3
MATERIALS = [] # case 4
GEOMETRIC_PROPERTIES = [] # case 5
BCNODES = [] # case 6
LOADS = [] # case 7

case = 0
temp = [] #talvez necesario

def what_case():
    


for line in file:
    line = line.rstrip() # remove o /n escondido da linha
    print(line)
    
    if line == "*COORDINATES":
        case = 1
    if line == "*ELEMENT_GROUPS":
        case = 2
    if line == "*INCIDENCES":
        case = 3
    if line == "*MATERIALS":
        case = 4
    if line == "*GEOMETRIC_PROPERTIES":
        case = 5
    if line == "*BCNODES":
        case = 6
    if line == "*LOADS":
        case = 7
        
    else:
        for number in line:
            try:                                                                        
                temp.append(float(number)) # try to convert line to integer
                
            except ValueError:  # if conversion to integer fails display a warning         
                print ("Warning: cannot convert to number string '%s'" % number)       
                continue # skip to next line on error
        
    
file.close()