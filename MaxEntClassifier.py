from nltk.corpus import names
from nltk import MaxentClassifier
from nltk import classify
import random

names = ( [(name, 'male')for name in names.words('male.txt')]
         + [(name, 'female') for name in names.words('female.txt')]
          )

random.shuffle(names)

# names is [ (u'Marthe', 'female') , (u'Alex','male'), ...]

def gender_features(word):
    return {'last_letter': word[-1], 'first_letter': word[0]}


"""
tokens = ['comp','.','ling','.']
toklen = 4
index is in [0,1,2,3]

"""

isdigit = lambda t: t.isdigit()
title   = lambda t: t.istitle()

def extract_features(tokens,n):
    features = {}

    toklen = len(tokens)

    # is it better to work with augmented tokens???
    # tokens = [<paragraph>] + tokens + [</paragraph>]

    # one more feature: "is not alfanumeric"

    if 1 < n + 1 < toklen:
        right = tokens[n+1]
        left =  tokens[n-1]      
        features['right_neighbor_len']   = "%s" % len(right)    
        features['left_neighbor_len']    = "%s" % len(left)
        features['right_neighbor_digit'] = "%s" % isdigit(right)    
        features['left_neighbor_digit']  = "%s" % isdigit(left)
        features['right_neighbor_title'] = "%s" % title(right)
        features['left_neighbor_title']  = "%s" % title(left)
        
    elif n+1 == toklen != 1:
        left =  tokens[n-1]
        features['left_neighbor_len']   =  "%s" % len(left)
        features['left_neighbor_digit']  = "%s" % isdigit(left)
        features['paragraph_end']        = "%s" % True
        
    elif n == 0 & toklen > 1:
        right = tokens[n+1]
        features['right_neighbor_len']   = "%s" % len(right)    
        features['right_neighbor_digit'] = "%s" % isdigit(right)
        
    else:
        features['dunno'] = 'lol'
        
    return features

tokens = ['comp','.','lingu','.']


featuresets = [(gender_features(name), gender) for (name, gender) in names]


train_set, test_set = featuresets[500:], featuresets[:500]


#me_classifier = MaxentClassifier.train(train_set)




#print(nb_classifier.classify(gender_features('Gary')))

#print(me_classifier.classify(gender_features('Grace')))
