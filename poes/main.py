#%% Import Python Libraries

from poes.model.poes import Poes
import numpy as np

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