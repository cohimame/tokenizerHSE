from xml.etree import ElementTree as ET

TEST = "try.xml"

wrap       = lambda tag, text: "<{0}>{1}</{0}>".format(tag,text)
sent_wrap  = lambda sent:  wrap("sentence",sent)
parag_wrap = lambda parag: wrap("parag",parag)
text_wrap  = lambda text:  wrap("text",text)


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
            sentence = [token.get('text') for token in token_nodes]
            par.append(sentence)  
        result.append(par)     
    return result

def decorate(text):
    txt = []
    for paragraph in text:
        par = []
        for sentence in paragraph:
            sent = sent_wrap(' '.join(sentence))
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
