from math import sin
import math


def work(f, a, b, n):
    print("\nТекущее число разбиений: ", n)
    h = (b-a)/float(n)
    print("Текущий шаг:", h)
    total = sum([f((a + (k*h))) for k in range(0, n)])
    result = h * total
    print("Текущий результат: ", result)
    return result


def f(x):
    return sin(x)*math.fabs(x)

print("Используем формулу левых прямоугольников")
print("Интегрируемая функция: f(x) = sin(x) / x")
print("Точность: 0.001")

n = 2
a1 = work(f, -1, 1, n)
n *= 2
a2 = work(f, -1, 1, n)

while n < 100:
    n *= 2
    a1 = work(f, -1, 1, n)
    n *= 2
    a2 = work(f, -1, 1, n)

print("\nОтвет:", a2, "\nКоличество разбиений:", n)