from sys import displayhook
from tkinter.tix import DisplayStyle
from spacy import displacy
import spacy
nlp = spacy.load("en_core_web_sm")
piano_text = "Gus is learning piano, he also like to play drum"
piano_doc = nlp(piano_text)
for token in piano_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )
displacy.serve(piano_doc, style="dep")

'''
OutPut:


TOKEN: Gus
=====
token.tag_ = 'NNP'
token.head.text = 'learning'
token.dep_ = 'nsubj'

TOKEN: is
=====
token.tag_ = 'VBZ'
token.head.text = 'learning'
token.dep_ = 'aux'

TOKEN: learning
=====
token.tag_ = 'VBG'
token.head.text = 'like'
token.dep_ = 'ccomp'

TOKEN: piano
=====
token.tag_ = 'NN'
token.head.text = 'learning'
token.dep_ = 'dobj'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'like'
token.dep_ = 'punct'

TOKEN: he
=====
token.tag_ = 'PRP'
token.head.text = 'like'
token.dep_ = 'nsubj'

TOKEN: also
=====
token.tag_ = 'RB'
token.head.text = 'like'
token.dep_ = 'advmod'

TOKEN: like
=====
token.tag_ = 'VBP'
token.head.text = 'like'
token.dep_ = 'ROOT'

TOKEN: to
=====
token.tag_ = 'TO'
token.head.text = 'play'
token.dep_ = 'aux'

TOKEN: play
=====
token.tag_ = 'VB'
token.head.text = 'like'
token.dep_ = 'xcomp'

TOKEN: drum
=====
token.tag_ = 'NN'
token.head.text = 'play'
token.dep_ = 'dobj'

Using the 'dep' visualizer
Serving on http://0.0.0.0:5000 ...'''
    