#Пункт1
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
a = -1
b = 1
print ("Input N")
N = int(input())
print ("Input M")
M = int(input())
step = float((b-a) / N)
x = []
y = []
x.append(a)
i = 1
while i <= N:
    x.append(x[i-1] + step)
    i += 1

#Пункт2
i=0
while i<=N:
    y.append(math.fabs(x[i])*math.sin(x[i]))
    i+=1

#Пункт3
def lagranz(x,y,const):
         lagr=0
         for i in range(len(y)):
             chisl=1; znam=1
             for j in range(len(x)):
                 if i==j:
                     continue   
                 else: 
                     chisl=chisl*(const-x[j])
                     znam=znam*(x[j]-x[i])
             lagr=lagr+y[i]*chisl/znam
         return lagr

lagr= [] # Интерполяционный полином точкаx x(0)...x(n)
for i in range(len(x)):
    lagr.append(lagranz(x,y,x[i]))



#Пункт4
X = []
step = float((b-a)/M)
X.append(a)
i=1
while i <= M:
    X.append(X[i-1] + step)
    i += 1

#Пункт5
Y = []
i=0
while i<=M:
    Y.append(math.fabs(X[i])*math.sin(X[i]))
    i+=1

lagr1 = [] # Интерполяционный полином точкаx x'(0)...x'(n)
for i in range(len(X)):
    lagr1.append(lagranz(x,y,X[i]))


def _poly_newton_coefficient(x,y):
    x = np.array(x, dtype=np.float32)
    y = np.array(y, dtype=np.float32)
    m = len(x)

    a = np.copy(y)
    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(x[k:m] - x[k-1])
    return a

def newton_polynomial(x_data, y_data, x):
    
    """
    x_data: data points at x
    y_data: data points at y
    x: evaluation point(s)
    """
    a = _poly_newton_coefficient(x_data, y_data)
    n = len(x_data) - 1 # Degree of polynomial
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x -x_data[n-k])*p
    return p


Nut = []
for i in range(len(X)):
    Nut.append(newton_polynomial(x,y, X[i]))

raz = [] # Интерполяционный полином точкаx x'(0)...x'(n)
for i in range(len(X)):
    raz.append(Y[i]-Nut[i])

table = {"x": x, "f(x)": y, "L(x)":lagr}
df = pd.DataFrame(data=table)
df.round({'x': 2, 'f(x)': 1, 'L(x)':2})
print(df)

table1 = {"x'": X, "f(x')": Y, "L(x')":lagr1,"N(x')":Nut,"raz":raz }
df1 = pd.DataFrame(data=table1)
df1 = df1.round({"x'": 7, "f(x')": 7, "L(x')":7,"N(x')":7, "raz":5})
print('\n', df1)    

