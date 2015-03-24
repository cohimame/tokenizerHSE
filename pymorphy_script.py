# -*- coding: utf-8 -*-
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def lemmatize_word(w):
    return morph.parse(w)[0].normal_form


def lemmatize(tokens):
    return [lemmatize_word(t) for t in tokens]
    

if __name__ == "__main__":
  
  text = u"Кто-нибудь позвоните Ёжи зачем-либо щекотно-с кому-то"

  tokens = text.split()
  
  print("pymorphy output: %s" % lemmatize(tokens))

