import math
import pandas as pd
import numpy as np
a = 0
b = 2
print ("Input N")
N = int(input())
step = float((b-a)/N)
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

from math import exp
f = lambda x: exp(-x**2)
def LeftRect(f, a, b, n):
    print ("Прямоугольники: ")
    print
    print("\nТекущее число разбиений: ", n)
    h = (b-a)/float(n)
    print("Текущий шаг:", h)
    integral = sum([f((a + (i*h))) for i in range(0, n)])
    result = h * integral
    return result

def Trapez(f,a,b,n):
    print ("Трапеция: ")
    print("\nТекущее число разбиений: ", n)
    h = (b-a)/float(n)
    print("Текущий шаг:", h)
    integral = sum([f(x[i]) for i in range(1,N)])
    integral += 0.5*(f(a)+f(b))
    integral *= h
    return integral

def Simpson(f,a,b,n):
    print ("Трапеция: ")
    print("\nТекущее число разбиений: ", n)
    h = (b-a)/float(n)
    print("Текущий шаг:", h)
    h = (b-a)/float(n)
    part1 = f(x[0])
    part2 = 4 * sum(f(x[i]) for i in range(1,n,2))
    part3 = 2 * sum(f(x[i]) for i in range(2,n-1,2))
    part4 = f(x[n])
    return (h/3*(part1+part2+part3+part4))

print("LeftRect = ", LeftRect(f,a,b,N))
print()
print("Trapez = ", Trapez(f,a,b,N))
print()
print("Simpson = ", Simpson(f,a,b,N))
print()
