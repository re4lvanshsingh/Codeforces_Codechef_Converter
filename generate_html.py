import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Read data from Excel file
data = pd.read_excel('CFCC_data.xlsx')

# Extract feature and response variable
x = data['CF'].values
y = data['CC'].values

# Reshape the input array to 2D
x = x.reshape(-1, 1)

# Transform input features to polynomial features
poly_features = PolynomialFeatures(degree=3)
x_poly = poly_features.fit_transform(x)

# Fit the quadratic regression model
model = LinearRegression()
model.fit(x_poly, y)

# Extract the coefficients
coefficients = model.coef_

# Print the coefficients
print("Coefficients:", coefficients)

# Generate points on x-axis for plotting
x_axis = np.linspace(x.min(), x.max(), 100)
x_axis = x_axis.reshape(-1, 1)

# Transform the x-axis points to polynomial features
x_axis_poly = poly_features.transform(x_axis)

# Predict the y-axis values
y_pred = model.predict(x_axis_poly)

# Plotting the data points and regression curve
plt.scatter(x, y, label='Data')
plt.plot(x_axis, y_pred, color='r', label='Cubic Regression')
plt.xlabel('Codeforces')
plt.ylabel('Codechef')
plt.title('Codeforces to Codechef Graph')
plt.legend()

# Convert the plot to an HTML-compatible representation using mpld3
html_plot = mpld3.fig_to_html(plt.gcf())

# Display the HTML plot
print(html_plot)
