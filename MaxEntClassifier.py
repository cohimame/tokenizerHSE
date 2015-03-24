from nltk import MaxentClassifier
from nltk import classify
import random
import pickle


import CorporaExtractor
import FeatureExtractor

def load_classifier():
    f = open('me_classifier.pickle','rb')
    classifier = pickle.load(f)
    f.close()
    return classifier

def save_classifier(classifier):
    f = open('me_classifier.pickle', 'wb')
    pickle.dump(classifier, f)
    f.close()
    
def train_classifier(data):
    me_classifier = MaxentClassifier.train(train_set)
    return me_classifier
    
if __name__ == "__main__":
    """    
    CorporaExtractor.form_train_corpora() # train.xml
    #CorporaExtractor.form_test_corpora()  # test.xml

    """

    data = FeatureExtractor.collect_classified_data("train.xml")
    random.shuffle(data)


    half = round(len(data)/2)
    train_set, test_set = data[:half], data[half:]

    
    #me_classifier = train_classifier(data)
    #save_classifier(me_classifier)
    me_classifier = load_classifier()
    
    

    test_ex = test_set[0][0]
    print(test_ex)
    print(me_classifier.classify(test_ex))

    print(classify.accuracy(me_classifier, test_set))

    #"""
   
