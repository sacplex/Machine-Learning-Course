# Simple Linear Regression

# Importing the libraries
import numpy # A mathematical library
import matplotlib.pyplot as plot # To plot the data charts
import pandas # Import and manage the data sets

# Importing the data set
dataset = pandas.read_csv('simple_linear_regression.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predicting the test set results
y_prediction = regressor.predict(X_test)

# Visualising the Training set results
plot.scatter(X_train, Y_train, color = 'red')
plot.plot(X_train, regressor.predict(X_train), color = "green")
plot.title("Salary vs. Years of Experience (Training Set)")
plot.xlabel("Years of Experience")
plot.ylabel("Salary")
plot.show()

# Visualising the Testing set results
plot.scatter(X_test, Y_test, color = 'blue')
plot.plot(X_train, regressor.predict(X_train), color = "green")
plot.title("Salary vs. Years of Experience (Test Set)")
plot.xlabel("Years of Experience")
plot.ylabel("Salary")
plot.show()