from pydoc import describe
import pandas as pd
import math as mt

data_set_RAW = pd.read_csv("/home/laurencezhou/PycharmProjects/DATA3888_Kidney_Graft_Predictor"
                           "/Merged_data_250719_final.csv")
print(data_set_RAW.head)
print(describe(data_set_RAW))
