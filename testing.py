import spacy
nlp_ner = spacy.load("D:\pythonProject\FInal\model-best")
doc=nlp_ner("I want a blue background with red text and font size must be 7. i want 2 buttons too and font must be in Times New roman")
