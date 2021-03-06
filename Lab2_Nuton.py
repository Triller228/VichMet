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


#Пункт3
def product( val, n ):
	mul = 1
	for i in range(n):
		if i: mul *= val - X[i-1]
		yield mul
C=[] # список коэффициентов полинома

# вычисляем коэффициенты
for n in range(len(x)):
	p = product(X[n],n+1 )
	C.append( (Y[n]-sum(C[k]*next(p) for k in range(n)) )/next(p))

def f(v):
    """ Значение полинома в точке v """
    return sum(C[k]*p for k, p in enumerate(product(v, len(C)) ) )


for i in range(len(X)):
    lagr1.append((f(X[i])))

table1 = {"x'": X, "f(x')": Y, "L(x')":lagr1}
df1 = pd.DataFrame(data=table1)
df1.round({"x'": 1, "f(x')": 2, "L(x')":3})
print('\n', df1)


  
