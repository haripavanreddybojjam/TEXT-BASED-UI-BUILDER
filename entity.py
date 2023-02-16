import spacy
import json

nlp_ner = spacy.load("model-best")
doc=nlp_ner("I want a red background. I want the screen size to be 100x200  . "
            "i  want 7 buttons and 2 labels, add 3 checkbuttons and 1 scale")

with open('main_details.json') as f:
   datas = json.load(f)

root_path=datas['Root_path']

for_basic={}
others={}
try:
    print(doc.ents)
    for i in doc.ents:
        if i.label_=="BG" :
            for_basic['bg']=i
        if i.label_=="SCREEN_RESOL":
            a=str(i).split('x')
            for_basic['width']=int(a[0])
            for_basic['height']=int(a[1])
        else:
            others[i.label_]=i
    with open(root_path + '/basic_details.json', 'w') as f:
        json.dump(str(for_basic), f)
        print(for_basic)
    with open(root_path + '/wid_from.json', 'w') as f:
        print(others)
        json.dump(str(others), f)
except UserWarning:
     print("NO INPUT")



