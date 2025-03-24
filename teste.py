from pysr import PySRRegressor
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**2 - x + 0.5*x + 10*np.cos(x-3)
    
    
x = np.linspace(-10,10,100).reshape(100,1)
y = f(x)

plt.plot(x,y)
plt.show()

reg = PySRRegressor(niterations=10000,timeout_in_seconds=60)


reg.fit(x,y)
print(reg.sympy())