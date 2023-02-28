import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from grains import *
from fun import *


# class that calculates the characteristic grain sizes, coefficient of uniformity
# and finally plots the gradation curve.
class GradationParameters(GrainsReader):
    # GradationParameters inherits global variables and methods from GrainsReader
    def __init__(self, show_plot=True):
        # initialize parent classes
        GrainsReader.__init__(self)
        # assign parameters from arguments
        self.show_plot = show_plot  # kwargs to show the gradation curve plot, default True (bool)
        self.D = [10, 30, 50, 60, 84, 90]  # percentage smaller of a sediment mixture (%)
        self.D_char = pd.DataFrame  # characteristic grain sizes (mm)
        self.U = np.nan  # coefficient of uniformity (-)
        self.condition = ""  # variable that states if the mixture is well or poorly graded (string)
        self.g = 9.81  # gravity (m/s2)
        self.s = 2.68  # specific gravity or relative density (-)
        self.ws = pd.DataFrame  # settling velocity (m/s)
        self.characteristic_diameters()
        self.uniformity_coefficient()
        self.gradation_plotting()

    def characteristic_diameters(self):
        try:
            self.D_char = self.grain_sizes.reindex(self.grain_sizes.index.union(self.D)).sort_index(
                ascending=True).interpolate(method='index').loc[self.D].sort_index(ascending=True)
        except TypeError:
            logging.warning("The grains.csv file has non-numeric data.")
            return np.nan

    def uniformity_coefficient(self):
        try:
            self.U = self.D_char["Size (mm)"][60] / self.D_char["Size (mm)"][10]
            if self.U > 5:
                self.condition = 'Well graded sediment mixture'
            else:
                self.condition = 'Poorly graded sediment mixture'
        except TypeError:
            logging.warning("The grains.csv file has non-numeric data.")
            return np.nan

    def gradation_plotting(self):
        logging.disable(logging.WARNING)
        try:
            if self.show_plot:
                grain_index = self.grain_sizes.reset_index()
                grain_index.plot(x="Size (mm)", y="% finer", kind='line', color='DarkBlue', grid=True,
                                 title="Gradation Curve", logx=True)
                plt.show()
        finally:
            logging.disable(logging.NOTSET)
