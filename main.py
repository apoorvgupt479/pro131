# Import pandas
import pandas as pd
import math

GRAVITATIONAL_CONSTANT = 6.67e-11

# converting to dataframe
data =  pd.read_csv("final_data.csv")

print("***********************************************************************")
print(data.head())
print("***********************************************************************")
print(data.columns)

print("***********************************************************************")
print(data.dtypes)
print("***********************************************************************")

data["Radius"] = pd.to_numeric(data.Radius,errors='coerce')
data["Radius"] = data["Radius"]*6.957e+8

data["Mass"] = pd.to_numeric(data.Mass,errors='coerce')
data["Mass"] = data["Mass"]*1.989e+30

data["Distance"] = pd.to_numeric(data.Distance,errors='coerce')



print(data.head())

gravity = []

print(data.shape)

#gravity = (G*M)/r^2
for mass in data["Mass"]:
    for radius in data["Radius"]:
        gravity.append(GRAVITATIONAL_CONSTANT * mass / math.pow(radius,2))
        break

data["Gravity"] = gravity

data = data.dropna()
data.drop(labels=['Unnamed: 0.1', 'Unnamed: 0'],axis=1,inplace=True)

print(data.shape)
print(data.dtypes)

data.to_csv("gravity_data.csv")