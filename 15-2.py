#Kata 15-2 Andres Venegas Pelayo
import numpy as np
import math
import matplotlib.pyplot as plt

n = 10
a = 1
b = 1.5
h = 0.05
#x = np.linspace(a,b,n)
y0 = 1
x=[1,1.05,1.10,1.15,1.20,1.25,1.30,1.35,1.40,1.45,1.50]

def fprima(x,y):
    return 2*(x)*(y)

def euler(h,x,y0):
    y = []
    y.append(y0)
    for i in range(1,len(x)):
        y.append(y[i-1] + h*fprima(x[(i)-1],y[i-1]))
    return y

y = euler(h,x,y0)

plt.plot(x,y,'b')
plt.grid()

print(y[10])
