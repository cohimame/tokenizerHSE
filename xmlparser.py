from xml.etree import ElementTree as ET

TEST = "try.xml"

wrap         = lambda tag, text: "<{0}>{1}</{0}>".format(tag,text)
parag_wrap   = lambda parag: wrap("parag",parag)
sent_wrap    = lambda sent:  wrap("sentence",sent)
text_wrap    = lambda text:  wrap("text",text)
token_wrap   = lambda token: wrap("token",token)
pos_dot_wrap = lambda token: "<token class=\"pos\">{}</token>".format(token)
neg_dot_wrap = lambda token: "<token class=\"neg\">{}</token>".format(token)


def read_xml(xml):
    with open(xml, encoding='utf-8') as infile:
        tree = ET.parse(infile)
    return tree

def extract_texts(root):
    return root.findall('.//text')

def extract_sentences(text):
    result = []
    paragraphs = text.findall('.//paragraph')   
    for paragraph in paragraphs:         
        sentences =  paragraph.findall('./sentence')
        for sentence in sentences:
            result.append(sentence.findall('./source')[0].text) 
    return result

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
    result = ["<sentence>"]
    for i in range(1,len(tokens)):
        wrapped = decide(aug[i-1],aug[i],aug[i+1])
        result.append(wrapped)
    result.append("</sentence>")   
    return result

def decide(prev,this,nxt):
    if this == u'.':
        if nxt != "</sent>":
            if prev.isdigit() or len(prev) == 1:
                return pos_dot_wrap(this)
            else:
                return neg_dot_wrap(this)
        else:
            return pos_dot_wrap(this)          
    else:
        return token_wrap(this)


def decorate(text):
    txt = []
    for paragraph in text:
        par = []
        for sentence in paragraph:
            sent = ''.join(sentence)
            par.append(sent)    
        par = parag_wrap(''.join(par))
        txt.append(par)
    result = text_wrap('\n'.join(txt))    
    return result


def form_corpora(dest, texts):
    with open(dest, mode = "w" ,encoding='utf-8') as outfile:
        for text in texts:
            parsed_struct = extract_tokenized_sentences(text)
            decorated = decorate(parsed_struct)
            outfile.write(decorated)


tree = read_xml("test10.xml")
texts = extract_texts(tree)
form_corpora("output", texts)

s = ['1','.','пункт','диплома','т','.','т','.']

print(prepare_sentence(s))
            
