from mat import *

A = readm('A.csv')
b = readm('b.csv')

def solve(A, b):

    import numpy as np
    a,b = np.array(A) , np.array(b)
    n = len(a[0])
    # eliminate
    for k in range(0, n-1):
        for i in range(k+1, n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k:n] = a[i, k:n] - lam*a[k,k:n]
                b[i] = b[i] - lam*b[k]
    x = np.array([0]*n)
    # Back Substitution 
    for k in range(n-1, -1, -1):
        x[k] = (b[k] - np.dot(a[k,k+1:n], x[k+1:n]))/a[k,k]
    return x.flatten()
print(solve(A,b))