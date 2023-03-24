'''
Name: Sahil S. Naik
Date: 13/02/2023
Designation: Classified
Source: Disclosed
Net: #1556B-B2-A51
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Iris.csv")

print("Displaying Dataset")
print(df)

print("\n---------------------------------------------------\n")
print("Dataset shape: {}".format(df.shape))

print("\n---------------------------------------------------\n")
print("Dataset info:")
print(df.info())

print("\n---------------------------------------------------\n")
print("Missing values:\n{}".format(df.isnull().sum()))

print("\n---------------------------------------------------\n")
print("Mean Sepal Length:\t{} cm".format(round(df['SepalLengthCm'].mean(),2)))
print("Mean Sepal Width:\t{} cm".format(round(df['SepalWidthCm'].mean(),2)))
print("Mean Petal Length:\t{} cm".format(round(df['PetalLengthCm'].mean(),2)))
print("Mean Petal Width:\t{} cm".format(round(df['PetalWidthCm'].mean(),2)))

print("\n---------------------------------------------------\n")
spc = df['Species'].unique()
print("Unique Species of Flowers are: ")
for i in spc:
	print(i)
	
print("\n---------------------------------------------------\n")
print("Count of Each Species:\n{}".format(df['Species'].value_counts()))

print("\n---------------------------------------------------\n")
print(">>>Visualizations\n1. Sepal Length vs Sepal Width")

x1 = df['SepalLengthCm']
y1 = df['SepalWidthCm']

plt.scatter(x1 ,y1)
plt.xlabel('Sepal Length (CM)')
plt.ylabel('Sepal Width (CM)')
plt.show()

print("\n---------------------------------------------------\n")
print("2. Petal Length vs Petal Width")
x2 = df['PetalLengthCm']
y2 = df['PetalWidthCm']

plt.scatter(x2 ,y2)
plt.xlabel('Petal Length (CM)')
plt.ylabel('Petal Width (CM)')
plt.show()
