#!/usr/bin/python
 # -*- coding: utf-8 -*-

# ���� ��������� f(x) = 0.6x^3+5.5x^2+10x-5

# ���������� �����
# ����� ���������, �� ������� ������� ����������
# ����� ���������, �� ������� ������� �������
# ��������� ������
# ��������� �������
# ���������� ����������, �� ������� f > 0
# ���������� ����������, �� ������� f < 0

from sympy import *
import matplotlib.pyplot as plt

print("1. ���������� �����")
x = Symbol('x')
func = 0.6*x**3 + 5.5*x**2 + 10*x - 5
y = solve(func, x)
print(f'��������� �����: X1 = {round(y[0],2)}; X2 = {round(y[1],2)}')


print("2. ����� ���������, �� ������� ������� ����������")
dif = diff(func)
print(solve(0 < dif))


print("3. ����� ���������, �� ������� ������� �������")
print(solve(0 > dif))


print("4. ��������� ������")
list_y = []
for i in range(-5, 6):
    x = i
    y = 0.6*x**3 + 5.5*x**2 + 10*x - 5
    list_y.append(y)
print(list_y)
plt.plot(range(-5, 6), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
plt.plot(range(-5, 6), list_y)
plt.show()


print("5. ��������� �������")
roots = solve(dif)
top = roots[0]
x = top
y = 0.6*x**3 + 5.5*x**2 + 10*x - 5
print(f'x = {round(float(top), 2)}, y = {round(float(y), 2)}')


print("6. ���������� ����������, �� ������� f > 0")
print(solve(0 < func))


print("7. ���������� ����������, �� ������� f < 0")
print(solve(func < 0))