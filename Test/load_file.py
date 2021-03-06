# -*- coding: utf-8 -*-

#import numpy as np

def load(file):

    file = open(file, 'r')

    COORDINATES = [] # case 1
    ELEMENT_GROUPS = [] # case 2
    INCIDENCES = [] # case 3
    MATERIALS = [] # case 4
    GEOMETRIC_PROPERTIES = [] # case 5
    BCNODES = [] # case 6
    LOADS = [] # case 7
    
    case = 0
    temp = []
    palavra = ""
    
    
        
    for line in file:
        temp = []
        line = line.rstrip() # remove o /n escondido da linha
        line += " "
        #print(line)
        
        if line == "*COORDINATES ":
            case = 1
        elif line == "*ELEMENT_GROUPS ":
            case = 2
        elif line == "*INCIDENCES ":
            case = 3
        elif line == "*MATERIALS ":
            case = 4
        elif line == "*GEOMETRIC_PROPERTIES ":
            case = 5
        elif line == "*BCNODES ":
            case = 6
        elif line == "*LOADS ":
            case = 7
            
        else:
            for number in line:
                print(number)
                if number != " " : #start of something
                    palavra += number
                else:
                    try:                                                                        
                        temp.append(float(palavra)) # try to convert line to float
                        palavra = ""
                        
                    except ValueError:  # if conversion to integer fails display a warning         
                        print ("Warning: cannot convert to number string '%s'" % palavra)
                        temp.append((palavra))
                        palavra = ""
                        continue # skip to next line on error
                        
        if case == 1 and len(temp) != 0:
            COORDINATES.append(temp)  # case 1            
        if case == 2 and len(temp) != 0:
            ELEMENT_GROUPS.append(temp) # case 2
        if case == 3 and len(temp) != 0:
            INCIDENCES.append(temp) # case 3
        if case == 4 and len(temp) != 0:
            MATERIALS.append(temp) # case 4
        if case == 5 and len(temp) != 0:
            GEOMETRIC_PROPERTIES.append(temp) # case 5
        if case == 6 and len(temp) != 0:
            BCNODES.append(temp) # case 6
        if case == 7 and len(temp) != 0:
            LOADS.append(temp) # case 7
                
        
    file.close()
    
    print(COORDINATES,ELEMENT_GROUPS,INCIDENCES,GEOMETRIC_PROPERTIES,BCNODES,LOADS)
    
    return(COORDINATES,ELEMENT_GROUPS,INCIDENCES,GEOMETRIC_PROPERTIES,BCNODES,LOADS)
    
load("TermoSol.txt")