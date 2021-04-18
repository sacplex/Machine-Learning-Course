# Importing the libraries
import numpy # A mathematical library
import matplotlib.pyplot as plot # To plot the data charts
import pandas # Import and manage the data sets

# Importing the data set
dataset = pandas.read_csv('multiple_linear_regression.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,4].values
                
# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])
 
# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X = LabelEncoder()
X[:, 0] = labelEncoder_X.fit_transform(X[:, 0])
 
oneHotEncoder = OneHotEncoder(categorical_features = [0])
X = oneHotEncoder.fit_transform(X).toarray()  

labelEncoder_Y = LabelEncoder()
Y = labelEncoder_Y.fit_transform(Y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5, random_state = 0)