import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch as t
import tensorflow as tf
import sys


counties_shp = gpd.read_file("/home/theWizard_m/Desktop/Datathon2024/data/AgChange/shapefiles/US_counties_2012_geoid.shp")
usda_data = pd.read_csv("/home/theWizard_m/Desktop/Datathon2024/data/USDA_PDP_AnalyticalResults.csv")



#counties_shp_no_geometry = counties_shp.drop(columns='geometry')

# Export to CSV
counties_shp.to_csv("/home/theWizard_m/Desktop/Datathon2024/data/AgChange/shapefiles/US_counties_2012_geoid.csv", index=False)

print("Shapefile attributes successfully exported to CSV!")

print(counties_shp)
#counties_shp.plot()
#plt.show()	
