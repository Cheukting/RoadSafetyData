# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:03:05 2017

@author: Ting
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
#matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

from ggplot import *

data = pd.read_csv('dftRoadSafety_Accidents_2016.csv')

data.describe()
#.round(decimals=0
data['latitude'] = data.Latitude.round(decimals=1)
data['longitude'] = data.Longitude.round(decimals=1)

data2 = data[data['Local_Authority_(District)']==1].filter(['Police_Force','Accident_Severity','Number_of_Vehicles','Number_of_Casualties','Longitude','Latitude']).groupby(["Longitude","Latitude"]).sum().reset_index()
data2.describe()
data2.head()
data2["Accident_measure"] = data2.Accident_Severity * 1000 + data2.Number_of_Vehicles *10 + data2.Number_of_Casualties *100

ggplot(aes(y='Latitude', x='Longitude', color='Accident_measure'), data=data2) +\
    geom_point() +\
    scale_color_gradient(low='green', high='red')

