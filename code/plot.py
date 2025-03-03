import numpy as np
import matplotlib.pyplot as plt

N=1000000 # Number of simulated particles for Monte Carlo method
# Limits of the integrals, dimensions in SI units
r1=0.02343/2
L=0.0028
y3b=0.005
y3a=-0.005
z3b=0.005
z3a=-0.005
y3=np.random.uniform(y3a, y3b, N)
z3=np.random.uniform(z3a, z3b, N)
x1b=0
x1a=-L
x1=np.random.uniform(x1a, x1b, N)
y1b=r1
y1a=-r1
y1=np.random.uniform(y1a, y1b, N)
z1b=np.sqrt(r1**2-y1**2)
z1a=-np.sqrt(r1**2-y1**2)
z1=np.random.uniform(z1a, z1b, N)
C=1000000 # Activity of source set as 1M Bq
# Computing the integral
def equation3(x2):
    def integral(z3, y3, z1, y1, x1):
        I=C/(np.pi*r1**2*L)
        theta2=(x2+x1)/((x2+x1)**2+(y3-y1)**2+(z3-z1)**2)**1.5/(4*np.pi)
        P=I*theta2
        return P
    y=integral(z3, y3, z1, y1, x1)   
    y_mean=(y.sum())/len(y)
    domain=0.01**2*np.pi*r1**2*L
    integ=domain*y_mean    
    return integ

x2 = np.linspace(0, 0.1, num=1000, endpoint = True)
errors = 

plt.plot(x2, equation3(x2))
xlabel("Distance from point source to detector")
ylabel("Count rate")
title("")

upper = gaussian_filter1d(equation3(x2) + errors, sigma = 3)
lower = gaussian_filter1d(equation3(x2) - errors, sigma = 3)
fill_between(x2, upper, lower, color = "blue", alpha = 0.2)

plt.show()
