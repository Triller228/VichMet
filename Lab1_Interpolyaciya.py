#Пункт1
import math
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
step = float((b-a) / M)
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

lagr1= [] # Интерполяционный полином точкаx x'(0)...x'(n)
for i in range(len(X)):
    lagr1.append(lagranz(X,Y,X[i]))

table = {"x": x, "f(x)": y, "L(x)":lagr}
df = pd.DataFrame(data=table)
df.round({'x': 2, 'f(x)': 1, 'L(x)':2})
print(df)

table1 = {"x'": X, "f(x')": Y, "L(x')":lagr1}
df1 = pd.DataFrame(data=table1)
df1.round({"x'": 1, "f(x')": 2, "L(x')":3})
print('\n', df1)    
