from xml.etree import ElementTree as ET

TEST = "try.xml"
TEST_OUT = "try_train.xml"

TRAIN_CORP_SOURCE = "first500.xml"
TRAIN_CORP = "train.xml"
TEST_CORP_SOURCE = "other700.xml"
TEST_CORP = "test.xml"
PARAGRAPH = "_paragraph_"

wrap         = lambda tag, text: "<{0}>{1}</{0}>".format(tag,text)
parag_wrap   = lambda parag: "\n  " + wrap("parag",parag)
sent_wrap    = lambda sent:  wrap("sentence",sent)
text_wrap    = lambda text:  wrap("text",text)
token_wrap   = lambda token: wrap("t",token)
pos_dot_wrap = lambda token: "<t class=\"pos\">{}</t>".format(token)
neg_dot_wrap = lambda token: "<t class=\"neg\">{}</t>".format(token)

def form_train_corpora():
    tree = read_xml(TRAIN_CORP_SOURCE)
    texts = extract_texts(tree)
    form_corpora(TRAIN_CORP, texts)

def form_test_corpora():
    tree = read_xml(TEST_CORP_SOURCE)
    texts = extract_texts(tree)
    form_corpora(TEST_CORP, texts)

def form_corpora(dest, texts):
    with open(dest, mode = "w" ,encoding='utf-8') as outfile:
        outfile.write("""<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n""")
        for text in texts:
            parsed_struct = extract_tokenized_sentences(text)
            decorated = decorate(parsed_struct)
            outfile.write(decorated)

def decorate(text):
    txt = []
    for paragraph in text:
        pw  = ['\n    ' + token_wrap(PARAGRAPH)]
        par = ['    ' + '\n    '.join(sentence) for sentence in paragraph]   
        par = pw + par + ['    ' + token_wrap(PARAGRAPH) + '\n  ']
        
        par = parag_wrap('\n'.join(par))
        txt.append(par)
    result = text_wrap('\n'.join(txt))    
    return result            

def read_xml(xml):
    with open(xml, encoding='utf-8') as infile:
        tree = ET.parse(infile)
    return tree

def extract_texts(root):
    return root.findall('.//text')

def extract_tokenized_sentences(text):
    result = []
    paragraphs = text.findall('.//paragraph')   
    for paragraph in paragraphs:
        par = []    
        sentences =  paragraph.findall('./sentence')
        for sentence_node in sentences:
            token_nodes = sentence_node.findall('.//token')
            ts = [token.get('text') for token in token_nodes]
            sentence = prepare_sentence(ts)
            par.append(sentence)  
        result.append(par)     
    return result

def prepare_sentence(tokens):
    aug = ["<sentence>"] + tokens + ["</sentence>"]
    result = []
    for i in range(1,len(tokens)+1):
        wrapped = decide(aug[i-1],aug[i],aug[i+1])
        result.append(wrapped)  
    return result

def decide(prev,this,nxt):
    if this == u'.':
        if nxt != "</sentence>":
            if prev.isdigit():
                return neg_dot_wrap(this)
            elif prev.isalpha() and len(prev) < 5:
                return neg_dot_wrap(this)     
            else:
                return pos_dot_wrap(this)
        else:
            return pos_dot_wrap(this)          
    else:
        return token_wrap(this)

if __name__ == "__main__":
    tree = read_xml(TEST)
    texts = extract_texts(tree)
    form_corpora(TEST_OUT, texts)

    s = ['1','.','пункт','диплома','т','.',')','.']
    print(prepare_sentence(s))

    
            
