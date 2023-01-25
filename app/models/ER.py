from paddlenlp import Taskflow
import pandas as pd

class ER():
    def __init__(self, text, e_option, r_option) -> None:
        task = Taskflow("ner", entity_only=True)
        ner = task(text)
        e_option = [type[0:2] for type in e_option]
        self.Entities = [e[0] for e in ner if e[1][0:2] in e_option]
        total_count = {}

        if r_option == 'option1':
            for line in text:
                for word in self.Entities:
                    if word in line:
                        try:
                            total_count[word] += 1
                        except KeyError:
                            total_count[word] = 1
            task = Taskflow("knowledge_mining", with_ie=True)
            km = task(text)
            self.Relations = [(r['HEAD_ROLE']['item'], tail['item'], r['GROUP']) for r in km[1][0] for tail in r['TAIL_ROLE']] \
            + [(r['HEAD_ROLE']['item'], sup['item'], r['GROUP']) for r in km[1][0] if ('SUPPORT' in r) for sup in r['SUPPORT']]
            
        if r_option == 'option2':
            para_count = []
            for line in text:
                para_count.append({})
                for word in self.Entities:
                    if word in line:
                        try:
                            total_count[word] += 1
                        except KeyError:
                            total_count[word] = 1
                        try:
                            para_count[-1][word] += 1
                        except KeyError:
                            para_count[-1][word] = 1
            self.Relations = {}
            for line in para_count:
                for name1 in line:
                    for name2 in line:
                        if name1 == name2:
                            continue
                        if (name1,name2) in self.Relations:
                            self.Relations[(name1,name2)] += 1
                        else:
                            self.Relations[(name1,name2)] = 1
            self.Relations = [(r[0],r[1],self.Relations[r]) for r in self.Relations]
        
        self.r_DataFrame = pd.DataFrame(self.Relations, columns=['head','tail','mark'])
        self.Entities = [i for i in self.Entities if i not in self.r_DataFrame['mark']]
        self.Entities = [(e,total_count[e]) for e in self.Entities]
        self.e_DataFrame = pd.DataFrame(self.Entities, columns=['entity','mark'])
        self.DataFrame = pd.concat([self.e_DataFrame,self.r_DataFrame])
        
    def __str__(self):
        return self
    
    def to_csv(self, path):
        return self.DataFrame.to_csv(path)
    
    def to_html(self, path):
        return self.DataFrame.to_html(path)