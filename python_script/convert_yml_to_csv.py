import pandas as pd
import yaml
import numpy as np

filepath = '../_data/data_papers_vygo.csv'

header = 'papers:\n \n'

#key_map for papers
key_map = {'title': 'Title', 'authors': 'Author', 'year': 'Publication year', 'tags': 'Tags', 'pdfurl': 'Pdfurl',
           'codeurl': 'codeurl', 'webpageurl': 'websiteurl', 'abstract': 'abstract', 'bibtex': 'Bibtex'}

#key_map for backgroud
# key_map = {'title': 'Title', 'authors': 'Authors', 'year': 'Publication year', 'pdfurl': 'Pdfurl','abstract': 'Abstract'}

with open(filepath) as fp:
    df = pd.read_csv(fp)

dict_yml = {'papers': []}
for ind, paper in df.iterrows():
    dict_paper = {}
    for k,v in key_map.items():
        if not pd.isna(paper[v]):
            if k=="authors":
                dict_paper[k]=', '.join(paper[v].replace('\xa0','').split(','))
            else:
                dict_paper[k]=paper[v]
                if k=='year':
                    dict_paper[k]=int(paper[v])

    # dict_paper['title'] = paper['Title']
    # dict_paper['authors'] = paper['Authors'].split(',')
    # dict_paper['year'] = int(paper['Publication year'])
    #
    # dict_paper['tags'] = paper['Tags'].split(',')
    # if not pd.isna(paper['Pdfurl']):
    #     dict_paper['pdfurl'] = paper['Pdfurl']
    # if not pd.isna(paper['codeurl']):
    #     dict_paper['codeurl'] = paper['codeurl']
    # if not pd.isna(paper['websiteurl']):
    #     dict_paper['webpageurl'] = paper['websiteurl']
    # if not pd.isna(paper['abstract']):
    #     dict_paper['abstract'] = paper['abstract']
    # if not pd.isna(paper['Bibtex']):
    #     dict_paper['bibtex'] = paper['Bibtex']
    dict_yml['papers'].append(dict_paper)

with open('data_test.yml', 'w') as outfile:
    yaml.dump(dict_yml, outfile, default_flow_style=False)
