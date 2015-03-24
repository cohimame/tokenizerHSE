from nltk import MaxentClassifier
from nltk import classify
import random

import CorporaExtractor
import FeatureExtractor

if __name__ == "__main__":
    """    
        CorporaExtractor.form_train_corpora() # train.xml
        CorporaExtractor.form_test_corpora()  # test.xml

    """

    trdata = FeatureExtractor.collect_classified_data("train.xml")
    random.shuffle(data)


    half = round(len(data)/2)
    train_set, test_set = data[:half], data[half:]

    
    me_classifier = MaxentClassifier.train(train_set)

    test_ex = test_set[0][0]
    print(test_ex)
    print(me_classifier.classify(test_ex))

    classify.accuracy(me_classifier, test_set)


   
