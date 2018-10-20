import numpy as np

x = np.array([-1, -0.6666666666666667,-0.3333333333333334, -1.1102230246251565e-16, 0.3333333333333332, 0.6666666666666665, 0.9999999999999998])
y = np.array([-0.8414709848078965, -0.41224653537982475, -0.1090648989320508,-1.232595164407831e-32, 0.10906489893205065, 0.4122465353798245,0.8414709848078962])

def _poly_newton_coefficient(x,y):
    """
    x: list or np array contanining x data points
    y: list or np array contanining y data points
    """
    x.astype(float)
    y.astype(float)
    m = len(x)

    x = np.copy(x)
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

for i in range(len(x)):
    print(newton_polynomial(x,y,x[i]), end = ' ')
    
    