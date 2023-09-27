import math

def task1():
  x = 3
  y = 5
  z = 2
  a= (math.log(abs(x-1))-math.sqrt(abs(y)))/((x ** (1. / 3.))+math.sqrt(abs(y)))
  b= (math.log(x))+z ** (x+y)
  print('1. ',a,b)
task1()
def task2():
  a=1
  b=-5
  c=4
  x=2
  f= ((2*x+b) ** (1. / 3.))+(c*x ** (1. / 3.))/(x+c)
  print('2. ',f)
task2()

def task3():
  x=5
  f=(math.cos(math.sin(1/(x ** (1/3)))) ** 3)
  print('3. ',f )
task3()
def task4():
  Vch=1000
  Sside=500
  Sbase=250
  r=(Vch/Sside)*2
  l=2*r
  h=Sside/l
  Vpr=(Sbase*h*(1/3))
  print('4. ', Vpr)
task4()
def task5():
  v = 1000
  hor = 5
  ras=9*hor*4
  ot= v/ras
  print('5. ',ot )
task5()
def task6():
  v=30
  h=5
  r=math.sqrt((v/h)*(4/3))
  l=math.sqrt(r*r+h*h)
  print('6. ',l )
task6()

def task9():
  cost=2000000
  mon=30000
  mo=cost/mon

  print('9. ',mo )
task9()
def task8():
  u0=60
  u1=80
  s=15000
  u2=((u1*u1)-(u0*u0))
  a=(s/u2)/2
  print('8. ',a )
task8()
def task7():
  A1=3
  B1=5
  C1=7
  A2=2
  B2=6
  C2=4
  D=A1*B2-A2*B1
  X=(C1*B2-C2*B1)/D
  Y=(A1*C2-A2*C1)/D
  if A1*X+B1*Y == C1 and A2*X+B2*Y == C2:
    print('7.',A1, B1, C1, A2, B2, C2)
    print('7,',Y)

task7()






