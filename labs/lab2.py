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
