"""
File: titanic_level1.py
Name: 
----------------------------------
This file builds a machine learning algorithm from scratch 
by Python codes. We'll be using 'with open' to read in dataset,
store data into a Python dict, and finally train the model and 
test it on kaggle. This model is the most flexible one among all
levels. You should do hyperparameter tuning and find the best model.
"""

import math

TRAIN_FILE = 'titanic_data/train.csv'
TEST_FILE = 'titanic_data/test.csv'


def data_preprocess(filename: str, data: dict, mode='Train', training_data=None):
    """
    :param filename: str, the filename to be processed
    :param data: an empty Python dictionary
    :param mode: str, indicating the mode we are using
    :param training_data: dict[str: list], key is the column name, value is its data
                          (You will only use this when mode == 'Test')
    :return data: dict[str: list], key is the column name, value is its data
    """
    with open(filename, 'r') as f:
        first = True
        for line in f:
            if first:
                feature_names = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
                first = False
                if mode == 'Train':
                    for feature in feature_names:
                        data[feature] = []
                elif mode == 'Test':  # Test Mode
                    feature_names = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
                    for feature in feature_names:
                        data[feature] = []
                # [Survived, Pclass, Sex, Age, SibSp, Parch, Fare, Embarked] , survived要看是否為train data
            else:
                line = line.strip()
                if mode == 'Train':
                    # 每筆資料的特徵向量(若為Train mode，first column為Y_label)
                    feature_vector = feature_extractor(line, mode)
                    for i in range(len(feature_names)):
                        if 'NAN' not in feature_vector:
                            data[feature_names[i]].append(feature_vector[i])
                elif mode == 'Test':  # Test Mode
                    feature_vector = feature_extractor(line, mode)
                    for i in range(len(feature_names)):
                        if feature_vector[i] == 'mean':  # Test Data的missing value 我們利用training_data的平均值來補
                            value = sum(training_data[feature_names[i]]) / len(training_data[feature_names[i]])
                            data[feature_names[i]].append(round(value, 3))
                        else:
                            data[feature_names[i]].append(feature_vector[i])
    return data


def one_hot_encoding(data: dict, feature: str):
    """
    :param data: dict[str, list], key is the column name, value is its data
    :param feature: str, the column name of interest
    :return data: dict[str, list], remove the feature column and add its one-hot encoding features
    """
    if feature == 'Sex':
        data['Sex_0'] = []
        data['Sex_1'] = []
        for i in range(len(data[feature])):
            if data[feature][i] == 1:
                data['Sex_1'].append(1)
                data['Sex_0'].append(0)
            else:
                data['Sex_1'].append(0)
                data['Sex_0'].append(1)
        # Delete key
        del data['Sex']
    elif feature == 'Pclass':
        data['Pclass_0'] = []
        data['Pclass_1'] = []
        data['Pclass_2'] = []
        for i in range(len(data[feature])):
            if data[feature][i] == 1:
                data['Pclass_0'].append(1)
                data['Pclass_1'].append(0)
                data['Pclass_2'].append(0)
            elif data[feature][i] == 2:
                data['Pclass_0'].append(0)
                data['Pclass_1'].append(1)
                data['Pclass_2'].append(0)
            elif data[feature][i] == 3:
                data['Pclass_0'].append(0)
                data['Pclass_1'].append(0)
                data['Pclass_2'].append(1)
        # Delete key
        del data['Pclass']
    elif feature == 'Embarked':
        data['Embarked_0'] = []
        data['Embarked_1'] = []
        data['Embarked_2'] = []
        for i in range(len(data[feature])):
            if data[feature][i] == 0:
                data['Embarked_0'].append(1)
                data['Embarked_1'].append(0)
                data['Embarked_2'].append(0)
            elif data[feature][i] == 1:
                data['Embarked_0'].append(0)
                data['Embarked_1'].append(1)
                data['Embarked_2'].append(0)
            else:
                data['Embarked_0'].append(0)
                data['Embarked_1'].append(0)
                data['Embarked_2'].append(1)
        # Delete key
        del data['Embarked']
    return data


def normalize(data: dict):
    """
    :param data: dict[str, list], key is the column name, value is its data
    :return data: dict[str, list], key is the column name, value is its normalized data
    """
    for key in data:
        # loop over list
        min_ = min(data[key])
        max_ = max(data[key])
        for i in range(len(data[key])):
            data[key][i] = (data[key][i] - min_) / (max_ - min_)
    return data


def learnPredictor(inputs: dict, labels: list, degree: int, num_epochs: int, alpha: float):
    """
    :param inputs: dict[str, list], key is the column name, value is its data
    :param labels: list[int], indicating the true label for each data
    :param degree: int, degree of polynomial features
    :param num_epochs: int, the number of epochs for training
    :param alpha: float, known as step size or learning rate
    :return weights: dict[str, float], feature name and its weight
    """
    # Step 1 : Initialize weights
    weights = {}  # feature => weight
    keys = list(inputs.keys())
    length = len(inputs[keys[1]])
    if degree == 1:
        for i in range(len(keys)):
            weights[keys[i]] = 0
    elif degree == 2:
        for i in range(len(keys)):
            weights[keys[i]] = 0
        for i in range(len(keys)):
            for j in range(i, len(keys)):
                weights[keys[i] + keys[j]] = 0
    # Step 2 : Start training

    for epoch in range(num_epochs):
        for i in range(length):  # 每個i代表一筆data
            each_data = {}
            if degree == 1:
                for key in weights:  # 這個迴圈把每筆資料弄成一個list vector
                    # Step 3 : Feature Extract
                    each_data[key] = inputs[key][i]
                h = sigmoid(dotProduct(weights, each_data))
                # Step 4 : Update weights
                increment(weights, -alpha * (h - labels[i]), each_data)
            elif degree == 2:
                # 記得先放一次項!!!!!!!!!
                for key in keys:  # 這個迴圈把每筆資料弄成一個list vector
                    # Step 3 : Feature Extract
                    each_data[key] = inputs[key][i]
                # 再放二次項!!!
                for k in range(len(keys)):
                    for t in range(k, len(keys)):
                        each_data[keys[k] + keys[t]] = inputs[keys[k]][i]*inputs[keys[t]][i]
                h = sigmoid(dotProduct(weights, each_data))
                # Step 4 : Update weights
                increment(weights, -alpha * (h - labels[i]), each_data)
    return weights


### 自己手刻
def feature_extractor(line, mode):
    """
    : param line: str, the line of data extracted from the training set
    : return: Tuple(list, label), the feature vector and the true label
    """
    data_lst = line.split(',')
    # [Id, Surv, Pclass, F_Name, L_Name, Sex5, Age, SibSp, ParCh, Ticket, Fare10, Cabin, Embarked]
    ans = []
    if mode == 'Train':
        ans.append(int(data_lst[1]))
        start = 2
    else:
        start = 1
    for i in range(len(data_lst)):
        if i == start:
            # Pclass
            ans.append(int(data_lst[i]))
        elif i == start + 3:
            # Sex
            if data_lst[i] == 'male':
                ans.append(1)
            else:
                ans.append(0)
        elif i == start + 4:
            # Age
            if data_lst[i]:
                ans.append(float(data_lst[i]))
            elif mode == 'Train':
                ans.append('NAN')
            elif mode == 'Test':
                ans.append('mean')
        elif i == start + 5:
            # SibSp
            ans.append(int(data_lst[i]))
        elif i == start + 6:
            # Parch
            ans.append(int(data_lst[i]))
        elif i == start + 8:
            # Fare
            if data_lst[i]:
                ans.append(float(data_lst[i]))
            elif mode == 'Train':
                ans.append('NAN')
            elif mode == 'Test':
                ans.append('mean')
        elif i == start + 10:
            # Embarked
            if data_lst[i] == 'S':
                ans.append(0)
            elif data_lst[i] == 'C':
                ans.append(1)
            elif data_lst[i] == 'Q':
                ans.append(2)
            elif mode == 'Train':
                ans.append('NAN')
            elif mode == 'Test':
                ans.append('mean')
    return ans


def dotProduct(d1, d2):
    """
    @param dict d1: a feature vector represented by a mapping from a feature (string) to a weight (float).
    @param dict d2: same as d1
    @return float: the dot product between d1 and d2
    """
    if len(d1) < len(d2):  # 一開始 d1 長度短
        return dotProduct(d2, d1)  # recursion中d2變成短的 ，d1是長的
    else:
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        return sum(d1.get(key, 0) * d2[key] for key in d2)
        # END_YOUR_CODE


def sigmoid(k):
    """
    :param k: float, linear function value
    :return: float, probability of the linear function value
    """
    return 1 / (1 + math.exp(-k))


def increment(d1, scale, d2):
    """
    Implements d1 += scale * d2 for sparse vectors.
    @param dict d1: the feature vector which is mutated.
    @param scale float
    @param dict d2: a feature vector.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    for word in d2:
        d1[word] = d1.get(word, 0) + scale * d2[word]
    # END_YOUR_CODE
