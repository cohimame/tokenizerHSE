from xml.etree import ElementTree as ET

# чтение происходит параграфами, предложений не существует.

isdigit = lambda t: t.isdigit()
title   = lambda t: t.istitle()


# на вход три токена: [ prev, '.' ,nxt]
# крайний вариант:    [ prev, '.' ,'</paragraph>']
def extract_features(prev,this,nxt):
    features = {}
    
    if prev != "<paragraph>":
        features['left_neighbor_len']    = "%s" % len(left)
        features['left_neighbor_digit']  = "%s" % isdigit(left)
        features['left_neighbor_title']  = "%s" % title(left)
    else:
        features['left_neighbor_len']    = "0"
        features['left_neighbor_digit']  = "False"
        features['left_neighbor_title']  = "False"

    if nxt != "</paragraph>":
        features['right_neighbor_len']    = "%s" % len(right)
        features['right_neighbor_digit']  = "%s" % isdigit(right)
        features['right_neighbor_title']  = "%s" % title(right)
        features['paragraph_end']        = "False"
    else:
        features['right_neighbor_len']   = "0"
        features['right_neighbor_digit'] = "False"
        features['right_neighbor_title'] = "False"
        features['paragraph_end']        = "True"
    
    return features
