#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 21:28:47 2018

@author: paulo
"""
import numpy as np

#Test func
A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0., 3., -1., 8.]])

b = np.array([6., 25., -11., 15.])

#Solution: [ 1.  2. -1.  1.]

def gauss(A,b,max_interacao = 1000,covergencia = 1e-18):


    # matriz temporaria
    A = np.array(A)

    #b = np.array([6., 25., -11., 15.])
    b = np.array(b)





    x = np.zeros_like(b)

    for it_count in range(max_interacao):
        x_last = np.zeros_like(x)
        for i in range(A.shape[0]):

            u1 = np.dot(A[i, :i], x_last[:i])
            u2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_last[i] = (b[i] - u1 - u2) / A[i, i]

        if np.allclose(x, x_last, rtol=covergencia):
            break
        x = x_last

    print("solução: {0}".format(x))

    return x

gauss(A,b)
def jacobe(A,b,max_interacao = 1000,covergencia = 1e-18):


    # matriz temporaria
    A = np.array(A)

    #b = np.array([6., 25., -11., 15.])
    b = np.array(b)



    x = np.zeros_like(b)

    for it_count in range(max_interacao):
        x_last = np.zeros_like(x)
        for i in range(A.shape[0]):

            u1 = np.dot(A[i, :i], x[:i])
            u2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_last[i] = (b[i] - u1 - u2) / A[i, i]

        if np.allclose(x, x_last, rtol=covergencia):
            break
        x = x_last

    print("solução: {0}".format(x))
    return x

jacobe(A,b)
