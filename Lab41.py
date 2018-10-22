import math
import matplotlib.pyplot as plt
from matplotlib import mlab
import pandas as pd

 
 
# начальные условия
x0 = 0
y0 = 1
# шаг
h = 0.01
# отрезок [x0, xn], где x0 = 0, xn = 1
xn = 1
 
 
f = lambda x, y: y * math.cos(x)

ilist = mlab.frange(0, 10, 1)
xlist = [(x0+h*i) for i in ilist]
ylist = []
 
 
prev = y0
for x in xlist:
    y = prev + h*f(x,y0)
    prev = y
    ylist.append(prev)
 
      
lst = []
for x in xlist:
    func = math.e ** math.sin(x)
    lst.append(func)
 
 
 


raz = [] 
for i in range(len(xlist)):
    raz.append(math.fabs(ylist[i]-lst[i]))

table1 = {"x": xlist, "f(x)": lst, "f(x')": ylist, "raz":raz }
df1 = pd.DataFrame(data=table1)
df1 = df1.round({"x": 5, "f(x)": 5, "f(x')":5, "raz":5})
print('\n', df1)

