import os
import shutil
import argparse

# pip install -U spacy
# python -m spacy download en_core_web_sm
# python -m spacy download fr_core_news_sm
#import spacy

def preprocess_token(content):
    content = content.replace('&', '&amp;')
    content = content.replace('<', '&lt')
    content = content.replace('>', '&gt')
    content = content.replace(',', '\\,')
    return content


def preprocess_lemma(content):
    content = content.replace('.', '')
    content = content.replace(',', '')
    content = content.replace('&', '')
    content = content.replace('@card@', '')
    content = content.replace('"', '')
    content = content.replace("'", '')
    return content


def spacy2unitex(doc):
    content = ''
    for token in doc:
        lemma = preprocess_lemma(token.lemma_)
        form = preprocess_token(token.text)
        content += '{' 
        content += form
        content += ','
        content += lemma
        content += '.'
        content += token.pos_
        content += '} '
    return content


def stanza2unitex():
    pass


def treetagger2unitex():
    pass


if __name__ == '__main__':
    pass