import numpy as np

x = np.array([-1, -0.6666666666666667,-0.3333333333333334, -1.1102230246251565e-16, 0.3333333333333332, 0.6666666666666665, 0.9999999999999998])
y = np.array([-0.8414709848078965, -0.41224653537982475, -0.1090648989320508,-1.232595164407831e-32, 0.10906489893205065, 0.4122465353798245,0.8414709848078962])

def coef(x, y): 
    '''x : array of data points 
     y : array of f(x) ''' 
    x.astype(float) 
    y.astype(float) 
    n = len(x) 
    a = [] 
    for i in range(n):
        a.append(y[i])
        
    for j in range(1, n): 
        for i in range(n-1, j-1, -1): 
            a[i] = float(a[i]-a[i-1])/float(x[i]-x[i-j])
            yield a[i]


K = list(coef(x,y))
  
n = len(x)
def Nuton(n, x_mas, coef, x_znach):
    s = coef[0]
    p = float(1)
    for i in range(1, n):
        p *= (x_znach-x[i-1])
        s += coef[i]*p
    return s

for i in range(len(x)):
    print ("X = ", x[i], end = " ")
    print ("Y = ", y[i], end = " ")
    print ("Nuton = ",Nuton(n,x,K,x[i]), end = " ")
    print()
    
    