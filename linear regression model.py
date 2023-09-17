# Import necessary libraries
# pip install scikit-learn matplotlib
# create a basic linear regression model to predict house prices based on the number of bedrooms.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate some sample data
np.random.seed(0)
X = np.random.rand(100, 1) * 5  # Number of bedrooms
y = 2 * X + 1 + np.random.randn(100, 1)  # House prices with some noise

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error (MSE) to evaluate the model
mse = mean_squared_error(y_test, y_pred)

# Plot the data and the regression line
plt.scatter(X_test, y_test, label='Actual Data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('Number of Bedrooms')
plt.ylabel('House Price')
plt.title(f'Linear Regression (MSE: {mse:.2f})')
plt.legend()
plt.show()

# Predict the price of a house with 3 bedrooms
bedrooms = np.array([[3.0]])
predicted_price = model.predict(bedrooms)
print(f'Predicted price for a 3-bedroom house: ${predicted_price[0][0]:.2f}')
