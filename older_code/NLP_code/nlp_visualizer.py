import spacy
from spacy import displacy
# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_md")



#doc = nlp("Monsters")
doc = nlp("To be considered relevant, u1 must be clearly at the office with the PC parts on the table.")
#doc = nlp("Moments when u1 was at home, looking at an old clock, with flowers visible, with a lamp and perhaps two small monsters watching u1 are considered relevant.")
displacy.serve(doc, style="dep")