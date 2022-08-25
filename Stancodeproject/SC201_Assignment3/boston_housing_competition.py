"""
File: boston_housing_competition.py
Name: Hank Chou
--------------------------------
This file demonstrates how to analyze boston
housing dataset. Students will upload their 
results to kaggle.com and compete with people
in class!

You are allowed to use pandas, sklearn, or build the
model from scratch! Go data scientist!
"""

import pandas as pd
from sklearn import linear_model, preprocessing, tree, ensemble, model_selection, metrics

TRAIN_FILE = 'boston_housing/train.csv'
TEST_FILE = 'boston_housing/test.csv'


def main():
    # Data cleaning
    data = data_preprocess(TRAIN_FILE)
    train_data, val_data = model_selection.train_test_split(data, test_size=0.5)

    # Extract true labels
    Y_train = train_data.medv
    Y_val = val_data.medv

    # Extract features
    feature_names = ['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'black', 'lstat']
    x_train = train_data[feature_names]
    x_val = val_data[feature_names]
    # # Normalization / Standardization
    standardizer = preprocessing.StandardScaler()
    x_train = standardizer.fit_transform(x_train)
    x_val = standardizer.transform(x_val)
    # Test data
    test_data = data_preprocess(TEST_FILE)
    x_test = test_data[feature_names]
    x_test = standardizer.transform(x_test)

    # Degree 1 Linear regression
    h = linear_model.LinearRegression()
    l_f = preprocessing.PolynomialFeatures(degree=1)
    X_train = l_f.fit_transform(x_train)
    classifier = h.fit(X_train, Y_train)
    acc_train = classifier.score(X_train, Y_train)
    # R square
    print('Degree 1 Training accuracy:', acc_train)
    X_val = l_f.transform(x_val)
    acc_val = classifier.score(X_val, Y_val)
    print('Degree 1 Validation accuracy:', acc_val)
    # RMSE
    predictions_train = classifier.predict(X_train)
    print('Degree 1  Train RMSE:', metrics.mean_squared_error(predictions_train, Y_train)**0.5)
    predictions_val = classifier.predict(X_val)
    print('Degree 1  Validation RMSE:', metrics.mean_squared_error(predictions_val, Y_val) ** 0.5)


    # # Degree 2 Linear regression
    # h = linear_model.LinearRegression()
    # p_f = preprocessing.PolynomialFeatures(degree=2)
    # X_train = p_f.fit_transform(x_train)
    # classifier_2 = h.fit(X_train, Y_train)
    # acc_train = classifier_2.score(X_train, Y_train)
    # print('Degree 2 Training accuracy:', acc_train)
    # X_val = p_f.transform(x_val)
    # acc_val = classifier_2.score(X_val, Y_val)
    # print('Degree 2 Validation accuracy:', acc_val)
    X_test = l_f.transform(x_test)
    predictions = classifier.predict(X_test)
    out_file(predictions, test_data, 'degree1_standardize.csv')


def data_preprocess(filename):
    """
    : param filename: str, the csv file to be read into by pd
    : param mode: str, the indicator of training mode or testing mode
    -----------------------------------------------
    This function reads in data by pd, changing string data to float,
    and finally tackling missing data showing as NaN on pandas
    """
    # Read in data as a column based DataFrame
    data = pd.read_csv(filename)

    return data


def out_file(predictions, test_data, filename):
    """
    : param predictions: numpy.array, a list-like data structure that stores 0's and 1's
    : param filename: str, the filename you would like to write the results to
    """
    print('\n===============================================')
    print(f'Writing predictions to --> {filename}')
    with open(filename, 'w') as out:
        out.write('ID,medv\n')
        for i in range(len(predictions)):
            out.write(str(test_data['ID'][i]) + ',' + str(predictions[i]) + '\n')
    print('===============================================')



if __name__ == '__main__':
    main()
