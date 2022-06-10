import pandas as pd
import yaml

filepath = '../_data/data_papers_vygo.csv'


header = 'papers:\n \n'

def qtfy(str):
    if pd.isna(str):
        return ''
    else:
        return '''"''' + str + ''' "'''

with open(filepath) as fp:
    df = pd.read_csv(fp)

dict_yml = {'papers': []}
for ind, paper in df.iterrows():
    dict_paper = {}
    dict_paper['title'] = paper['Title']
    dict_paper['authors'] = paper['Author'].split(',')
    dict_paper['year'] = int(paper['Publication year'])
    dict_paper['tags'] = paper['Tags'].split(',')
    dict_paper['pdfurl'] = paper['Pdfurl']
    dict_paper['codeurl'] = paper['codeurl']
    dict_paper['webpageurl'] = paper['websiteurl']
    dict_paper['abstract'] = paper['abstract']
    dict_paper['bibtex'] = paper['Bibtex']
    dict_yml['papers'].append(dict_paper)
    stop = 0


with open('data_test.yml', 'w') as outfile:
    yaml.dump(dict_yml, outfile, default_flow_style=False)







