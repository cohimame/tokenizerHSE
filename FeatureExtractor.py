from xml.etree import ElementTree as ET
from nltk import MaxentClassifier
from nltk import classify

TEST_CORP = "train_corp_tesing.xml"
PARAGRAPH = "_paragraph_"
isdigit = lambda t: t.isdigit()
title   = lambda t: t.istitle()

def read_xml(xml):
    with open(xml, encoding='utf-8') as infile:
        tree = ET.parse(infile)
    return tree

# работа происходит параграфами, предложений "не существует".
def collect_classified_data(tree):
    labeled_data = []
    paragraphs = tree.findall('.//parag')
    for paragraph_node in paragraphs:
        token_nodes = paragraph_node.findall('.//t')
        ld = extract_labeled_data(token_nodes)
        labeled_data += ld
    return labeled_data

# на вход: ['_paragraph_'  ...  '.' ... '_paragraph_']        
def extract_labeled_data(token_nodes):
    labeled_data = []
    for i in range(1,len(token_nodes)-1):    
        label = token_nodes[i].get('class')
        if label:
            prev = token_nodes[i-1].text
            this = token_nodes[i].text
            nxt  = token_nodes[i+1].text
            features = extract_features(prev,nxt)
            labeled_data.append((features,label))
    return labeled_data      
            

# на вход два крайних токена: [prev '.' nxt]
# крайний вариант:  [prev '.' '_paragraph_']
#             или:  ['_paragraph_' '.' nxt]
def extract_features(prev,nxt): 
    features = {}
    
    if prev != PARAGRAPH:
        features['left_neighbor_len']    = "%s" % len(prev)
        features['left_neighbor_digit']  = "%s" % isdigit(prev)
        features['left_neighbor_title']  = "%s" % title(prev)
    else:
        features['left_neighbor_len']    = "0"
        features['left_neighbor_digit']  = "False"
        features['left_neighbor_title']  = "False"

    if nxt != PARAGRAPH:
        features['right_neighbor_len']    = "%s" % len(nxt)
        features['right_neighbor_digit']  = "%s" % isdigit(nxt)
        features['right_neighbor_title']  = "%s" % title(nxt)
        features['paragraph_end']        = "False"
    else:
        features['right_neighbor_len']   = "0"
        features['right_neighbor_digit'] = "False"
        features['right_neighbor_title'] = "False"
        features['paragraph_end']        = "True"
    
    return features


tree = read_xml(TEST_CORP)        
data = collect_classified_data(tree)
#print(data)

train_set, test_set = data, data

me_classifier = MaxentClassifier.train(train_set)

test_ex = test_set[0][0]
print(test_ex)


print(me_classifier.classify(test_ex))
