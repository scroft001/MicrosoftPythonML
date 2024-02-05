import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

ufos = pd.read_csv('ufos.csv')
#print(ufos.head())

ufos = pd.DataFrame({'Seconds': ufos['duration (seconds)'], 'Country': ufos['country'],'Latitude': ufos['latitude'],'Longitude': ufos['longitude']})

ufos.Country.unique()
#print(ufos)

ufos.dropna(inplace=True)
ufos = ufos[(ufos['Seconds'] >= 1) & (ufos['Seconds'] <= 60)]
#ufos.info()

ufos['Country'] = LabelEncoder().fit_transform(ufos['Country'])
print(ufos.head())