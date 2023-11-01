import math
import matplotlib.pyplot as plt

def prostoe(a):
    k = 0
    for i in range(2,a):
        if (a % i == 0):
            k = k + 1
    if (k <= 0):
        ot= 1
    else:
        ot=0
    return ot

def task1():
    print("Введите число")
    a=int(input())
    if prostoe(a)==1:
        print('Простое')
    else:
        print('Не простое')
    task1()

 def function(x):
    if math.cos(x)<=0:
        if math.e ** x>0:
            return math.cos(x), math.e ** x
def task2():
     a=2
     b=15
     for x in range(a,b):
        f(x)
     plt.plot(f(x))
     plt.show()
    task2()
