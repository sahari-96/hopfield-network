# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 20:07:32 2021

@author: Asus
"""

import matplotlib.pyplot as plt
import numpy as np


def hardlims(x):
    if x<0:
        return -1
    else:
        return 1

np.random.seed(1000)

number_of_patterns = 3
x1 = 5
x2 = 5 
number_of_iteration = 20


P = np.zeros((number_of_patterns, x1 * x2 ))

P[0] = [-1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1]
P[1] = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
P[2] = [-1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1]


W = np.zeros((x1 * x2 , x1 * x2))

for i in range(x1 * x2):
    for j in range(x1 * x2):
        if i == j :
             W[i, j] = 0
        else:
            
            w = 0
        
            for n in range(number_of_patterns):
                w += P[n, i] * P[n, j]
            
            W[i, j] = w / P.shape[0]
            W[j, i] = W[i, j]
        

x_test = np.array([-1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1])


Y = np.empty([1, 25], dtype=int)
for _ in range(number_of_iteration ):
    X_Test = x_test
    y = X_Test.dot( W ) 
    Y = np.array([hardlims(y[i]) for y[i] in y])
    X_test = Y
    
    
fig, ax = plt.subplots(1, number_of_patterns, figsize=(10, 5))

for i in range(number_of_patterns):
    ax[i].matshow(P[i].reshape((x1, x2)), cmap='gray')
    ax[i].set_xticks([])
    ax[i].set_yticks([])
    
plt.show()
              
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].matshow(x_test.reshape(x1, x2), cmap='gray')
ax[0].set_title('Corrupted pattern')
ax[0].set_xticks([])
ax[0].set_yticks([])

ax[1].matshow(X_test.reshape(x1, x2), cmap='gray')
ax[1].set_title('Recovered pattern')
ax[1].set_xticks([])
ax[1].set_yticks([])

plt.show()