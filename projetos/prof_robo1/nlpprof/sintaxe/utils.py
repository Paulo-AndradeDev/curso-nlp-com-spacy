import spacy
from spacy import displacy


def displacy_dep(texto):

    nlp = spacy.load("pt_core_news_lg")

    text = texto

    doc = nlp(text)

    html_displacy_dep =  displacy.render(doc, style='dep',page=True)

    return  html_displacy_dep
