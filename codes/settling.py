import pandas as pd
from gradation import *
from fun import *


# class that computes the settling velocity in m/s for each characteristic grain size.
class SettlingParameters(GradationParameters):
    # SettlingParameters inherits global variables and methods from GradationParameters
    def __init__(self, viscosity):
        # initialize parent classes
        GradationParameters.__init__(self, show_plot=False)
        self.v = viscosity  # water viscosity (m2/s)
        self.temp = pd.DataFrame  # temporal data frame
        self.settling_velocity()

    def settling_velocity(self):
        try:
            self.temp = self.D_char[(self.D_char["Size (mm)"] > 0.001) & (self.D_char["Size (mm)"] <= 0.1)]
            self.ws = (self.s - 1) * self.g * (0.001 * self.temp) ** 2 / (18 * self.v)
            self.temp = self.D_char[(self.D_char["Size (mm)"] > 0.1) & (self.D_char["Size (mm)"] <= 1)]
            self.ws = pd.concat([self.ws, 10 * self.v / (0.001 * self.temp) *
                                 ((1 + 0.01 * (self.s - 1) * self.g * (0.001 * self.temp) ** 3 / self.v ** 2) ** .5 - 1)])
            self.temp = self.D_char[self.D_char["Size (mm)"] > 1]
            self.ws = pd.concat([self.ws, 1.1 * ((self.s - 1) * self.g * 0.001 * self.temp) ** .5])
            self.ws = self.ws.rename(columns={"Size (mm)": "Set_velocity (m/s)"})

        except TypeError:
            logging.warning("Could not calculate the settling velocity (ws). "
                            "Check that grains.csv and viscosity have numeric data.")
            self.ws = np.nan
