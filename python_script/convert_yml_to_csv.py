import pandas as pd
import yaml
import numpy as np

filepath = '../_data/data_papers_vygo.csv'


header = 'papers:\n \n'



with open(filepath) as fp:
    df = pd.read_csv(fp)



dict_yml = {'papers': []}
for ind, paper in df.iterrows():
    dict_paper = {}
    dict_paper['title'] = paper['Title']
    dict_paper['authors'] = paper['Author'].split(',')
    dict_paper['year'] = int(paper['Publication year'])
    dict_paper['tags'] = paper['Tags'].split(',')
    if not pd.isna(paper['Pdfurl']):
        dict_paper['pdfurl'] = paper['Pdfurl']
    if not pd.isna(paper['codeurl']):
        dict_paper['codeurl'] = paper['codeurl']
    if not pd.isna(paper['websiteurl']):
        dict_paper['webpageurl'] = paper['websiteurl']
    if not pd.isna(paper['abstract']):
        dict_paper['abstract'] = paper['abstract']
    if not pd.isna(paper['Bibtex']):
        dict_paper['bibtex'] = paper['Bibtex']
    dict_yml['papers'].append(dict_paper)


with open('data_test.yml', 'w') as outfile:
    yaml.dump(dict_yml, outfile, default_flow_style=False)







