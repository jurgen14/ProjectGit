# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

e = 5
print(e)

#VECTOR
y = np.array([-4, 8, 5])
print(y)

#MATRIZ
m = np.array([[1, 8, -9], [3, -6, 7]])
print(m)
print(type(m))
print(m.shape)
print(".............")

print(y.reshape(1,3))
print(y.reshape(3,1))

#SUMA DE MATRICES
m1 = np.array([[5, 12, 6], [-3, 0, 14]])
m2 = np.array([[2, 8, 3], [-1, 0, 0]])

print(m1 + m2)
print(".............")
print(m1)
print(m1.T)
print(".............")
y_reshape = y.reshape(1, 3)
print(y_reshape.T)
print(".............")
print(m1 * 10)
print(".............")
n1 = np.array([2, 8, -4])
n2 = np.array([1, -7, 3])
print(np.dot(n1, n2))
print(".............")
print(np.dot(m1, m2.T))











