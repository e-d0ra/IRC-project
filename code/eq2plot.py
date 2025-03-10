import numpy as np
from scipy.integrate import dblquad
from scipy.ndimage import gaussian_filter1d
import matplotlib.pyplot as plt

def integrate_point_source_modified(x2):
    """
    Computes the count rate integral for a point source using SciPy's dblquad.
    
    Parameters:
    L : float
        Activity of the point source (Bq).
    x2 : float
        Distance between the point source and the detector.
    detector_size : float
        Half-length of the square detector (i.e., detector extends from -detector_size to +detector_size in y3 and z3).
    
    Returns:
    --------
    integral_value : float
        Computed integral value for the count rate.
    """
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
    
errors = np.sqrt(y)

plt.plot(x2, y, color = "blue")
plt.xlabel("Distance between point source and detector (m)")
plt.ylabel("Expected count rate (Bq)")
plt.title("Equation 2")
plt.xlim(0, 0.1)
plt.ylim(0, 400000)
plt.grid()

upper = gaussian_filter1d(y + errors, sigma = 3)
lower = gaussian_filter1d(y - errors, sigma = 3)
plt.fill_between(x2, upper, lower, color = "pink", alpha = 0.2)

plt.savefig('../code/diagrams/eq2.png')
plt.show()
