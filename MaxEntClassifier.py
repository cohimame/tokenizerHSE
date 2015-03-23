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


tokens = ['comp','.','lingu','.']


featuresets = [(gender_features(name), gender) for (name, gender) in names]


train_set, test_set = featuresets[500:], featuresets[:500]


#me_classifier = MaxentClassifier.train(train_set)




#print(nb_classifier.classify(gender_features('Gary')))

#print(me_classifier.classify(gender_features('Grace')))
