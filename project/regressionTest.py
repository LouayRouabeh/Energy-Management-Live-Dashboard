import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_excel('EleConsumption.xlsx', sheet_name='RegGround')

df.plot(kind='scatter', x='HDD 18(667)', y='consumption(666)')
plt.show()

# change to dataframe
HDD = pd.DataFrame(df['HDD 18(666)'])
consumption = pd.DataFrame(df['consumption(666)'])

# build linear regression model
lm = linear_model.LinearRegression()
model = lm.fit(HDD, consumption)

model.score(HDD, consumption)

HDD_new = np.array([140])
HDD_new = HDD_new.reshape(-1, 1)
consumption_predict = model.predict(HDD_new)
consumption_predict

X = ([60, 100, 200])
X = pd.DataFrame(X)
Y = model.predict(X)
Y = pd.DataFrame(Y)
df = pd.concat([X, Y], axis=1, keys=['HDD_new_c', 'consumption_predict_kwh'])

df = pd.read_excel('EleConsumption.xlsx', sheet_name='RegGround')

df.plot(kind='scatter', x='HDD 18(666)', y='consumption(666)')
# plotting the regression line
plt.plot(HDD, model.predict(HDD), color='red', linewidth=2)

# plotting the predict value
plt.scatter(HDD_new, consumption_predict, color='yellow')
plt.show()
