from nltk import MaxentClassifier
from nltk import classify
import random
import pickle


import CorporaExtractor
import FeatureExtractor

pos = 'pos'
neg = 'neg'

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

def eval_metrics(classifier, data):
    true_pos  = 0.0
    false_pos = 0.0
    false_neg = 0.0

    for example in data:
        features   = example[0]
        label      = example[1]
        pred_label = me_classifier.classify(features)

        if pred_label == label == pos:
            true_pos  += 1
            
        elif (label == pos) and (pred_label == neg):
            false_neg += 1

        elif (label == neg) and (pred_label == pos):
            false_pos += 1
        else:
            continue

    pre = true_pos / (true_pos + false_pos)
    re  = true_pos / (true_pos + false_neg)
    
    f   = 2 * pre * re / (pre + re)

    return pre,re,f
    
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

    print("accuracy %s" % classify.accuracy(me_classifier, test_set))

    print("pre %s, re %s , f %s" % eval_metrics(me_classifier, test_set))


    #"""
   
