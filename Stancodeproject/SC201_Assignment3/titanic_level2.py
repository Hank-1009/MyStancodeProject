"""
File: titanic_level2.py
Name: 
----------------------------------
This file builds a machine learning algorithm by pandas and sklearn libraries.
We'll be using pandas to read in dataset, store data into a DataFrame,
standardize the data by sklearn, and finally train the model and
test it on kaggle. Hyperparameters are hidden by the library!
This abstraction makes it easy to use but less flexible.
You should find a good model that surpasses 77% test accuracy on kaggle.
"""

import math
import pandas as pd
from sklearn import preprocessing, linear_model
TRAIN_FILE = 'titanic_data/train.csv'
TEST_FILE = 'titanic_data/test.csv'


def data_preprocess(filename, mode='Train', training_data=None):
	"""
	:param filename: str, the filename to be read into pandas
	:param mode: str, indicating the mode we are using (either Train or Test)
	:param training_data: DataFrame, a 2D data structure that looks like an excel worksheet
						  (You will only use this when mode == 'Test')
	:return: Tuple(data, labels), if the mode is 'Train'
			 data, if the mode is 'Test'
	"""
	data = pd.read_csv(filename)
	features = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
	features_test = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

	if mode == 'Train':
		data = data[features]
		# Missing data 處理
		data = data.dropna()
		labels = data.pop('Survived')
		# Changing 'male' to 1, 'female' to 0
		data.loc[data.Sex == 'male', 'Sex'] = 1
		data.loc[data.Sex == 'female', 'Sex'] = 0
		# Changing 'S' to 0, 'C' to 1, 'Q' to 2
		data.loc[data.Embarked == 'S', 'Embarked'] = 0
		data.loc[data.Embarked == 'C', 'Embarked'] = 1
		data.loc[data.Embarked == 'Q', 'Embarked'] = 2
		return data, labels
	elif mode == 'Test':
		data = data[features_test]
		# Missing data 處理
		# Age
		data['Age'].fillna(round(training_data['Age'].mean(), 3), inplace=True)
		# Fare
		data['Fare'].fillna(round(training_data['Fare'].mean(), 3), inplace=True)
		# Changing 'male' to 1, 'female' to 0
		data.loc[data.Sex == 'male', 'Sex'] = 1
		data.loc[data.Sex == 'female', 'Sex'] = 0
		# Changing 'S' to 0, 'C' to 1, 'Q' to 2
		data.loc[data.Embarked == 'S', 'Embarked'] = 0
		data.loc[data.Embarked == 'C', 'Embarked'] = 1
		data.loc[data.Embarked == 'Q', 'Embarked'] = 2
		return data


def one_hot_encoding(data, feature):
	"""
	:param data: DataFrame, key is the column name, value is its data
	:param feature: str, the column name of interest
	:return data: DataFrame, remove the feature column and add its one-hot encoding features
	"""
	# One hot encoding for a new category Male
	if feature == 'Sex':
		data['Sex_0'] = 0
		data.loc[data['Sex'] == 0, 'Sex_0'] = 1
		# One hot encoding for a new category Female
		data['Sex_1'] = 0
		data.loc[data['Sex'] == 0, 'Sex_1'] = 1
		# No need Sex anymore!
		data.pop('Sex')
	if feature == 'Pclass':
		# One hot encoding for a new category FirstClass
		data['Pclass_0'] = 0
		data.loc[data['Pclass'] == 1, 'Pclass_0'] = 1
		# One hot encoding for a new category SecondClass
		data['Pclass_1'] = 0
		data.loc[data['Pclass'] == 2, 'Pclass_1'] = 1
		# One hot encoding for a new category ThirdClass
		data['Pclass_2'] = 0
		data.loc[data['Pclass'] == 3, 'Pclass_2'] = 1
		# No need Pclass anymore!
		data.pop('Pclass')
	if feature == 'Embarked':
		data['Embarked_0'] = 0
		data.loc[data['Embarked'] == 0, 'Embarked_0'] = 1
		data['Embarked_1'] = 0
		data.loc[data['Embarked'] == 1, 'Embarked_1'] = 1
		data['Embarked_2'] = 0
		data.loc[data['Embarked'] == 2, 'Embarked_2'] = 1
		data.pop('Embarked')
	return data


def standardization(data, mode='Train'):
	"""
	:param data: DataFrame, key is the column name, value is its data
	:param mode: str, indicating the mode we are using (either Train or Test)
	:return data: DataFrame, standardized features
	"""
	# 不會受stack frame 影響
	standardizer = preprocessing.StandardScaler()
	if mode == 'Train':
		data = standardizer.fit_transform(data)
	elif mode == 'Test':
		data = standardizer.transform(data)

	return data


def main():
	"""
	You should call data_preprocess(), one_hot_encoding(), and
	standardization() on your training data. You should see ~80% accuracy
	on degree1; ~83% on degree2; ~87% on degree3.
	Please write down the accuracy for degree1, 2, and 3 respectively below
	(rounding accuracies to 8 decimals)
	TODO: real accuracy on degree1 -> 0.80196629
	TODO: real accuracy on degree2 -> 0.83707865
	TODO: real accuracy on degree3 -> 0.87640449
	"""
	# Data cleaning
	train_data, Y = data_preprocess(TRAIN_FILE, mode='Train')
	test_data = data_preprocess(TEST_FILE, mode='Test', training_data=train_data)
	# one hot encoding
	train = one_hot_encoding(train_data, 'Sex')
	train = one_hot_encoding(train, 'Pclass')
	train = one_hot_encoding(train, 'Embarked')
	test = one_hot_encoding(test_data, 'Sex')
	test = one_hot_encoding(test, 'Pclass')
	test = one_hot_encoding(test, 'Embarked')
	# Normalization / Standardization
	standardizer = preprocessing.StandardScaler()
	X_train = standardizer.fit_transform(train)
	#############################
	# Degree 1 Polynomial Model #
	#############################
	# h在fit的時候會被改變
	h = linear_model.LogisticRegression(max_iter=10000)
	d1_classifier = h.fit(X_train, Y)
	acc1 = d1_classifier.score(X_train, Y)
	print('Degree 1 Training Accuracy: ', acc1)
	# X_test = standardizer.transform(test)
	# predictions_d1 = d1_classifier.predict(X_test)
	#############################
	# Degree 2 Polynomial Model #
	#############################
	poly = preprocessing.PolynomialFeatures(degree=2)
	X_train_poly = poly.fit_transform(X_train)
	d2_classifier = h.fit(X_train_poly, Y)
	acc2 = d2_classifier.score(X_train_poly, Y)
	print('Degree 2 Training Accuracy: ', acc2)
	#############################
	# Degree 3 Polynomial Model #
	#############################
	cubic = preprocessing.PolynomialFeatures(degree=3)
	X_train_cubic = cubic.fit_transform(X_train)
	d3_classifier = h.fit(X_train_cubic, Y)
	acc3 = d3_classifier.score(X_train_cubic, Y)
	print('Degree 3 Training Accuracy: ', acc3)




if __name__ == '__main__':
	main()
