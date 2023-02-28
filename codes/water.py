import numpy as np
from fun import *


# class that computes water density and viscosity from a given temperature (T) in °C.
class WaterParameters:
    def __init__(self, temperature):
        self.T = temperature  # water temperature (°C)
        self.p = np.nan  # water density (kg/m3)
        self.v = np.nan  # water viscosity (m2/s)
        self.water_density()
        self.water_viscosity()

    def water_density(self):
        try:
            self.p = 1000 * (1 - (self.T + 288.941) * pow(self.T - 3.986, 2) / (508929.2 * (self.T + 68.13)))
        except TypeError:
            logging.warning("Temperature (T) is a non-numeric data. Returning p=NaN.")
            return np.nan

    def water_viscosity(self):
        try:
            self.v = (1.14 - 0.031 * (self.T - 15) + 0.00068 * (self.T - 15) ** 2) * 10 ** -6
        except TypeError:
            logging.warning("Temperature (T) is a non-numeric data. Returning v=NaN.")
            return np.nan
