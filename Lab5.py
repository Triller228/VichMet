import math
import matplotlib.pyplot as plt
from matplotlib import mlab
import pandas as pd

 
 
# начальные условия
x0 = 0
y0 = 1 / float(math.exp(3))
xn = 2


 
 
f = lambda x, y: 2*x*y
for k in range(10000):
    flag = True
    N = 1
    N +=k
    h = (xn - x0) / float(N)
    ilist = mlab.frange(0, N, 1)
    xlist = [(x0+h*i) for i in ilist]
    ylist = []
 
 

 
      
    ylist1 = []
    for x in xlist:
        func = (1 / float(math.exp(3))) * math.exp(x**2)
        ylist1.append(func)
 
    prev = y0
    i=1
    for x in xlist:
        y = (prev) + (h*((f(x,ylist1[i-1]))+f(x+h, prev+h*f(x,ylist1[i-1])))/2)
        prev = y
        ylist.append(prev)
        i+=1
    
    flag = True
    raz = [] 
    for i in range(len(xlist)):
        raz.append(math.fabs(ylist[i]-ylist1[i]))
        if raz[i] > 0.01:
            flag = False
            break

    if (k < 25) or (k>2150):
        print (N)
        plt.rc('font',**{'family':'verdana'})
        plt.xlabel("ось абцисс")
        plt.ylabel("ось ординат")
        plt.plot(xlist, ylist, "b-", label="точное решение")
        plt.plot(xlist, ylist1, "r-", label="метод Рунге-Кутта")
        plt.legend()
        plt.grid()
        plt.show() 
    
    if flag:
        
        table1 = {"x": xlist, "f(x)": ylist1, "f(x')": ylist, "raz":raz }
        df1 = pd.DataFrame(data=table1)
        df1 = df1.round({"x": 5, "f(x)": 5, "f(x')":5, "raz":5})
        print('\n', df1)
        break
    