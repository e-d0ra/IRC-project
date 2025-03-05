import numpy as np
from scipy.integrate import dblquad

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
    L=0.0028
    detector_size=0.005
    def integrand(y3, z3):
        return x2 / ((x2**2 + y3**2 + z3**2) ** (3 / 2))
    
    integral_value, _ = dblquad(
        integrand, 
        -detector_size, detector_size,  # Limits for z3 (outer integral)
        lambda z3: -detector_size, lambda z3: detector_size  # Limits for y3 (inner integral)
    )
    
    return (L / (4 * np.pi)) * integral_value

#comment
