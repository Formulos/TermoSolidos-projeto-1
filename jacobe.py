#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 21:28:47 2018

@author: paulo
"""
import numpy as np


def jacobe(A,b,max_interacao = 1000,covergencia = 1e-18):

    
    # matriz temporaria
    A = np.array(A)
    
    #b = np.array([6., 25., -11., 15.])
    b = np.array(b)
    
    L = np.tril(A)
    U = np.triu(A,1)
    L = np.linalg.inv(L)

    
    T = np.dot(-L,U)
    C = np.dot(L,b)
    
    x = None
    x_current = np.ones(b.shape)
    
    for i in range(max_interacao):
        # x = T * x_current + C
        x = (np.dot(T,x_current)) + C
        
        if np.allclose(x, x_current, rtol=covergencia):
            break
        
        x_current = x
        
    print("Solução: {0}".format(x))