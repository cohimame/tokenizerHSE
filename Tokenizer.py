import re
import string
import MaxEntClassifier
import FeatureExtractor

maxent = MaxEntClassifier.load_classifier()
pos = 'pos'
neg = 'neg'

pnkt = set(string.punctuation)
pnkt.remove("-")

paragraph = [FeatureExtractor.PARAGRAPH]
wrap   = lambda text: paragraph + text + paragraph
xtract = lambda prv,nxt: FeatureExtractor.extract_features(prv,nxt)

def split(text):
    result = text
    for p in pnkt:
        result = result.replace(p, " {} ".format(p))
    return result.split() 

def tokenize(text):
    result = []
    stuff = wrap(split(text))
    for i in range(1,len(stuff)-1):
        
        if stuff[i] == '.':
            features = xtract(stuff[i-1],stuff[i+1])
            pred_label = maxent.classify(features)           
            if pred_label == neg:
                result.append(result.pop()+".")    
            else:
                result.append(stuff[i])
        else:
            result.append(stuff[i])
    return result

sentence =  "Кто-нибудь позвоните-ж. т.е.  \"Ёжи-сан\"   зачем-либо. Щекотно-с, кому-то!\n Вам-то легко рассуждать"

print(sentence)
print(split(sentence))

print(tokenize(sentence))

