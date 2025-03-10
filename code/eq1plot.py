import numpy as np
import matplotlib.pyplot as plt

def calculate_flux(r):
    """Calculate the flux F given radius r."""
    L = 1_000_000  # Luminosity
    if np.any (r == 0):
        raise ValueError("Radius r cannot be zero to avoid division by zero.")
    return L / (4 * np.pi * r**2)

# Generate values for r (radius)
r_values = np.linspace(1, 100, 100)  # Example: radius values from 1 to 100
flux_values = calculate_flux(r_values)

# Plotting the graph
plt.plot(r_values, flux_values, color='blue')
plt.xlabel('Distance between point source and detector (m)')  # Label for x-axis
plt.ylabel('Expected count rate (Bq)')    # Label for y-axis
plt.title('Equation 1')  # subject to change
plt.grid(True)  # Adding grid for better visualization
plt.xlabel(0, 0.1)
plt.ylabel(0, 80000)
plt.savefig('../code/diagrams/eq1.png', dpi=400)
plt.show()

