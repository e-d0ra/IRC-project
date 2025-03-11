# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 21:15:10 2025

@author: wuhei
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad

def integrate_point_source_modified(x2):
    

    L=1e6
    detector_size=0.005
    def integrand(y3, z3):
        return x2 / ((x2**2 + y3**2 + z3**2) ** (3 / 2))
    
    integral_value, _ = dblquad(
        integrand, 
        -detector_size, detector_size,  # Limits for z3 (outer integral)
        lambda z3: -detector_size, lambda z3: detector_size  # Limits for y3 (inner integral)
    )
    
    return (L / (4 * np.pi)) * integral_value

x2 = np.linspace(0.001, 0.1, num=1000, endpoint = True)
y=np.array([])
for n in range (0, len(x2)):
    y=np.append(y, integrate_point_source_modified(x2[n]))


# Plotting the graph
plt.figure(dpi=400)
plt.plot(x2, y, label='Equation 2')

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
x1b=L
x1a=0
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

y=np.array([])
for n in range (0, len(x2)):
    y=np.append(y, equation3(x2[n]))
plt.plot(x2, y, label='Equation 3')

plt.xlabel('Distance between source and detector (m)')  # Label for x-axis
plt.ylabel('Expected count rate (Bq)')    # Label for y-axis
plt.title('Combined plot')  # subject to change
plt.grid(True)  # Adding grid for better visualization
plt.xlim(0, 0.1)
plt.ylim(0, 75000)
plt.legend()
plt.tight_layout()
plt.savefig('../code/diagrams/combined.png', dpi=400)
plt.show()