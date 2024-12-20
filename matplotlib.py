# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HauSMX33VWsDCyuB1OBqQEhl1khOcMxu
"""

import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv('/content/archive.zip')

data.head()

x_data = data["Category"].head(10)
y_data = data["Price (Rs.)"].head(10)

plt.plot(x_data,y_data,"o--g")
plt.xlabel("Category")
plt.ylabel("Price (Rs.)")
plt.title("Catogory and Price (Rs.)")
plt.show()