import numpy as np
import matplotlib.pyplot as plt

def calculate_flux(r):
    """Calculate the flux F given radius r."""
    L = 1000000  # Luminosity
    if np.any (r == 0):
        raise ValueError("Radius r cannot be zero to avoid division by zero.")
    return L / (4 * np.pi * r**2)

# Generate values for r (radius)
r_values = np.linspace(0.01, 5, 1000)  # Example: radius values from 1 to 100
flux_values = calculate_flux(r_values)

# Plotting the graph
plt.figure(dpi=400)
plt.plot(r_values, flux_values, color='blue')
plt.xlabel('Distance between point source and detector (m)')  # Label for x-axis
plt.ylabel('Expected count rate (Bq)')    # Label for y-axis
plt.title('Equation 1')  # subject to change
plt.grid(True)  # Adding grid for better visualization
plt.xlim(0, 5)
plt.ylim(0, 500000)
plt.tight_layout()
plt.savefig('../code/diagrams/eq1.png', dpi=400)
plt.show()

