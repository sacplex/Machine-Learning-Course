# Importing the libraries
import numpy # A mathematical library
import matplotlib.pyplot as plot # To plot the data charts
import pandas # Import and manage the data sets

# Importing the data set
dataset = pandas.read_csv('multiple_linear_regression.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,4].values
                
# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X = LabelEncoder()
X[:, 3] = labelEncoder_X.fit_transform(X[:, 3])
 
oneHotEncoder = OneHotEncoder(categorical_features = [3])
X = oneHotEncoder.fit_transform(X).toarray()  

# Avoiding the dummy variable trap
X = X[:, 1:]
                
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

#Predicting the Test set results
y_pred = regressor.predict(X_test)

# Building the optimal model using Backward Elimination
import statsmodels.formula.api as statsmodels
X = numpy.append(arr = numpy.ones((50,1)).astype(int), values = X,axis = 1)

# Select all the independent variables
X_opt = X[:, [0,1,2,3,4,5]] 

# Fit the full model with all possible predictors
regressor_OLS = statsmodels.OLS(endog = Y, exog = X_opt).fit()
regressor_OLS.summary()

# Select all the independent variables except 2
X_opt = X[:, [0,1,3,4,5]] 

# Fit the full model with all possible predictors
regressor_OLS = statsmodels.OLS(endog = Y, exog = X_opt).fit()
regressor_OLS.summary()

# Select all the independent variables except 1 and 2
X_opt = X[:, [0,3,4,5]] 

# Fit the full model with all possible predictors
regressor_OLS = statsmodels.OLS(endog = Y, exog = X_opt).fit()
regressor_OLS.summary()