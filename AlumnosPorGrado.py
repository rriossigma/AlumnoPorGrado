import plistlib
from tkinter import Y
import matplotlib.pyplot as plt
import pandas as pd
import csv

df = pd.read_csv('cleanstudentscomplete.csv')

#students = df.value_counts("grade")

year = df[["grade"]]
#print(year)
dummies = pd.get_dummies(year[["grade"]])
#print(dummies)

concat = pd.concat([year, dummies ] , axis = 1)
#print(concat)
agrupado = concat.groupby(["grade"]).sum()
print(agrupado)

agrupado["Totals"] = agrupado["grade_10th"] + agrupado["grade_11th"] + agrupado["grade_12th"] + agrupado["grade_9th"]

etiquetas = df["grade"].value_counts().keys()

pie = agrupado["Totals"].plot.pie(figsize=(10,10) ,labels=etiquetas,autopct="%0.5f")

#pieChart = plt.figure(figsize=(7,8))
plt.pie(agrupado["Totals"])
plt.show()
