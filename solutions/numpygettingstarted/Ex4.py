import numpy as np
import pandas as pd

# Read a csv file, get a Pandas DataFrame back.
dataframe = pd.read_csv('BergenWeather2019.csv')
print('Dataframe shape', dataframe.shape)

# Get the 'Precipitation' column as 32-bit floats.
precipitation = np.array(dataframe['Precipitation'], dtype=np.float32)
print('precipitation shape', precipitation.shape)
print(precipitation)

# Create a view of the first 364 values and reshape as a 2D array of shape (52, 7).
weeks = precipitation[:364].reshape((52,7))
print('\nweeks shape', weeks.shape)
print(weeks)

print('\nPrecipitation in first week:\n', weeks[0])
print('\nPrecipitation in final week:\n', weeks[-1])
print('\nPrecipitation on first weekend:\n', weeks[0][5:])
print('\nPrecipitation on final week:\n', weeks[-1][:5])