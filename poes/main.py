#%% Import Python Libraries

from poes.model.poes import Poes
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm, lognorm, expon, triang, uniform

#%% Call the function to test it with single values

area = 200 #ft2
h = 30 #ft
poro = 0.30
swi = 0.45
boi = 1.15

poes = Poes(area, h, poro, swi, boi)

print(f"POES is: {poes:.2f} stb")


#%% Test function for array of values

area_array = np.array([200, 250, 300, 400, 156])
h_array = np.array([30, 25, 32, 31, 40])
poro_array = np.array([0.30, 0.31, 0.26, 0.18, 0.27])
swi_array = np.array([0.45, 0.30, 0.70, 0.55, 0.62])
boi_array = np.array([1.15, 1.20, 1.30, 1.40, 1.50])

poes_array = Poes(area_array, h_array, poro_array, swi_array, boi_array)
print(poes_array)


#%% Generate random values for porosity
# Random values using normal distribution
porosity_norm = norm.rvs(loc=0.4, scale=0.5, size=1000)

# Define minimun values
porosity_norm = np.where(porosity_norm < 0, 0, porosity_norm)

# Define maximum value
porosity_norm = np.where(porosity_norm > 0.4, 0.4, porosity_norm)


# Random values using lognormal distribution
porosity_lognorm = lognorm.rvs(s=0.1, loc=0, scale=0.05, size=1000)

porosity_lognorm = np.where(porosity_lognorm < 0, 0, porosity_lognorm)

porosity_lognorm = np.where(porosity_lognorm > 0.4, 0.4, porosity_lognorm)


# Random values using Exponential distribution
porosity_expon = expon.rvs(loc=0, scale=0.05, size=1000)

porosity_expon = np.where(porosity_expon < 0, 0, porosity_expon)

porosity_expon = np.where(porosity_expon > 0.4, 0.4, porosity_expon)


# Random values using Triangular distribution
porosity_tri = triang.rvs(c=0.3, loc=0, scale= 0.4, size=1000)


# Random values using uniform distribution
porosity_uni = uniform.rvs(loc=0, scale=0.4, size=1000)


print(porosity_expon)


#%% Visualize distributions
plt.hist(porosity_lognorm, bins=100)
plt.show()