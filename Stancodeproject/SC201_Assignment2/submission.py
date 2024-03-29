#!/usr/bin/python

import math
import random
from collections import defaultdict
from util import *
from typing import Any, Dict, Tuple, List, Callable

FeatureVector = Dict[str, int]
WeightVector = Dict[str, float]
Example = Tuple[FeatureVector, int]


############################################################
# Milestone 3a: feature extraction

def extractWordFeatures(x: str) -> FeatureVector:
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x: movie review
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    d = defaultdict(int)
    # split() 可以處理換行字元
    for word in x.split():
        d[word] += 1
    return d
    # END_YOUR_CODE


############################################################
# Milestone 4: Sentiment Classification

def learnPredictor(trainExamples: List[Tuple[Any, int]], validationExamples: List[Tuple[Any, int]],
                   featureExtractor: Callable[[str], FeatureVector], numEpochs: int, alpha: float) -> WeightVector:
    """
    Given |trainExamples| and |validationExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of epochs to
    train |numEpochs|, the step size |eta|, return the weight vector (sparse
    feature vector) learned.

    You should implement gradient descent.
    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and validationExamples
    to see how you're doing as you learn after each epoch. Note also that the 
    identity function may be used as the featureExtractor function during testing.
    """
    weights = {}  # feature => weight

    # BEGIN_YOUR_CODE (our solution is 12 lines of code, but don't worry if you deviate from this)
    # feature extractor
    # train = []
    # validation = []

    def predictor(data):
        # data: 是像trainExamples裡的tuple中 第一項的正常影評
        # 所以還得用featureExtractor去得出feature vector，再跟weights內積
        return 1 if dotProduct(featureExtractor(data), weights) > 0 else -1
    # Train/ validation set
    # trainExamples: [("hi bye", 1),.......]
    # (1) 利用feature extractor 找出 feature vector (2) 把評價為-1變為0
    # for i in range(len(trainExamples)):
    #     train.append((featureExtractor(trainExamples[i][0]), 0)) if trainExamples[i][1] == -1 else \
    #         train.append((featureExtractor(trainExamples[i][0]), trainExamples[i][1]))
    # for i in range(len(validationExamples)):
    #     validation.append((featureExtractor(validationExamples[i][0]), 0))if validationExamples[i][1] == -1 else \
    #         validation.append((featureExtractor(validationExamples[i][0]), validationExamples[i][1]))
    for epoch in range(numEpochs):
        for x, y in trainExamples:
            # get feature vector
            d2 = featureExtractor(x)
            # modify y value
            y = 0 if y < 0 else 1
            h = sigmoid(dotProduct(weights, d2))
            # Gradient descent with increment function
            increment(weights, -alpha * (h - y), d2)
        trainError = evaluatePredictor(trainExamples, predictor)
        validationError = evaluatePredictor(validationExamples, predictor)
        print("Training error: (" + str(epoch)+' epoch): '+str(trainError))
        print("Validation error: (" + str(epoch) + ' epoch): ' + str(validationError))
    # END_YOUR_CODE
    return weights


############################################################
# Milestone 5a: generate test case

def generateDataset(numExamples: int, weights: WeightVector) -> List[Example]:
    """
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    """
    random.seed(42)

    def generateExample() -> Tuple[Dict[str, int], int]:
        """
        Return a single example (phi(x), y).
        phi(x) should be a dict whose keys are a subset of the keys in weights
        and values are their word occurrance.
        y should be 1 or -1 as classified by the weight vector.
        Note that the weight vector can be arbitrary during testing.
        """
        # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
        phi = defaultdict(int)
        sample_list = random.sample(weights.keys(), random.randint(1, len(weights)))
        for word in sample_list:
            phi[word] += 1
        y = 1 if dotProduct(weights, phi) >= 0 else -1
        # END_YOUR_CODE
        return phi, y

    return [generateExample() for _ in range(numExamples)]


############################################################
# Milestone 5b: character features

def extractCharacterFeatures(n: int) -> Callable[[str], FeatureVector]:
    """
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces mapped to their n-gram counts.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    """

    def extract(x: str) -> Dict[str, int]:
        # BEGIN_YOUR_CODE (our solution is 5 lines of code, but don't worry if you deviate from this)
        # 先把空格處理掉
        # new_phi : 一次一則影評
        new_phi = defaultdict(int)
        x = x.replace(' ', '')
        for i in range(len(x.replace(u'\x85', ''))-n+1):
            new_phi[x.replace(u'\x85', '')[i:i+n]] += 1
        return new_phi
        # END_YOUR_CODE

    return extract


############################################################
# Problem 3f: 
def testValuesOfN(n: int):
    """
    Use this code to test different values of n for extractCharacterFeatures
    This code is exclusively for testing.
    Your full written solution for this problem must be in sentiment.pdf.
    """
    trainExamples = readExamples('polarity.train')
    validationExamples = readExamples('polarity.dev')
    featureExtractor = extractCharacterFeatures(n)
    weights = learnPredictor(trainExamples, validationExamples, featureExtractor, numEpochs=20, alpha=0.01)
    outputWeights(weights, 'weights')
    outputErrorAnalysis(validationExamples, featureExtractor, weights, 'error-analysis')  # Use this to debug
    trainError = evaluatePredictor(trainExamples,
                                   lambda x: (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
    validationError = evaluatePredictor(validationExamples,
                                        lambda x: (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
    print(("Official: train error = %s, validation error = %s" % (trainError, validationError)))


#### 自己手刻的部分
def sigmoid(k):
    """
    :param k: float, linear function value
    :return: float, probability of the linear function value
    """
    return 1 / (1 + math.exp(-k))


