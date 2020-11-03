import pandas as pd
from sklearn import linear_model

df = pd.read_csv('fuel.csv')
regr = linear_model.LinearRegression()
X = df[['Weight', 'Volume']]
y = df['CO2']

regr.fit(X, y)

predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)
