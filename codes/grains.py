import os
import pandas as pd


# class that uses the read_csv method from Pandas to read the grain size distribution from grains.csv.
class GrainsReader:
    def __init__(self, csv_file_name=os.path.abspath("..") + "\\grains.csv", delimiter=","):
        self.sep = delimiter
        self.grain_sizes = pd.DataFrame
        self.grain_data(csv_file_name)

    def grain_data(self, csv_file_name):
        self.grain_sizes = pd.read_csv(csv_file_name,
                                       names=["% finer", "Size (mm)"],
                                       skiprows=[0],
                                       sep=self.sep,
                                       index_col=["% finer"])

    def __call__(self, csv_file_name, *args, **kwargs):
        print("grains")
