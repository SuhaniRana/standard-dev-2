import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
list = df["numbers"].to_list()
std_deviation = statistics.stdev(list)
print(std_deviation)