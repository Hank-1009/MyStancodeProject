"""
File: interactive.py
Name: Hank Chou
------------------------
This file uses the function interactivePrompt
from util.py to predict the reviews input by 
users on Console. Remember to read the weights
and build a Dict[str: float]
"""
from util import *
import submission


def main():
    featureExtractor = submission.extractWordFeatures
    weights = {}
    with open('weights', 'r', encoding='UTF-8') as f:
        for line in f:
            weight_lst = line.split()
            weights[weight_lst[0]] = float(weight_lst[1])
    interactivePrompt(featureExtractor, weights)


if __name__ == '__main__':
    main()
