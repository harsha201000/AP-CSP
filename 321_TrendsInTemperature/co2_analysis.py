# Import Required Libraries
import matplotlib.pyplot as plt
import pandas as pd
import math

"""
Dataset Information:
# The average CO2 is expressed as parts per million (ppm)			
# which is the number of molecules of CO2 in every one million			
# molecules of dried air (water vapor removed).  			
# Missing months are denoted by -99.99.			
# -1 means no data on the number of days			
"""

# Load carbon dioxide dataset
co2_data = pd.read_csv("co2_data.csv", header=0)
print(co2_data)
# Replace average column in carbon dioxide dataset
co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)
print(co2_data)
# Plot Carbon Dioxide Data
plt.plot(co2_data['Year'],co2_data['Average'], color='gray')
plt.ylabel('CO2 Levels in ppm')
plt.xlabel('Years')
plt.title('Change in Carbon Dioxide')
plt.show()
# Dropna row 3 and 7
co2_data.dropna(subset=['Average'], inplace=True)
print(co2_data)
