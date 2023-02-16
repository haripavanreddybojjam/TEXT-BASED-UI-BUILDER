import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json

nlp=spacy.blank("en")
db=DocBin()
f=open('.json')
TRAIN_DATA=json.load(f)

for text,annot in tqdm(TRAIN_DATA["annotations"]):
    doc=nlp.make_doc(text)
    ents=[]
    for start,end,label in annot["entities"]:
        span=doc.char_span(start,end,label=label,alignment_mode="contract")
        if span is None :
            print("Skip")
        else:
            ents.append(span)
    doc.ents = ents
    db.add(doc)

db.to_disk("./training.spacy")

#python -m spacy init fill-config base_config.cfg config.cfg
#python -m spacy train config.cfg  --paths.train ./train.spacy --paths.dev ./train.spacy