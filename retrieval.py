# J. Nathan Farmer, Sachinder Katoch, Rohit Kothari
#
# This script performs the information retrieval tasks.

import json
import pandas as pd

def retrieve_documents(q):
    # Uses the index to retrieve relevant documents
    if q:
        topic = topics['QUERY'][topics['TOPICID']==200].iloc[0]

    return {'topic':topic, 'docs':{1:{'document_id':14747618,'link':'data/rheumatolgy/14747618.html','relevance':'Relevant'}, 
                                   2:{'document_id':10662869,'link':'data/rheumatolgy/10662869.html','relevance':'Relevant'}, 
                                   3:{'document_id':10901322,'link':'data/ajepidem/10901322.html','relevance':'Not Relevant'}}}

def load_topics():
    # Loads the predefined topics file
    topics = pd.read_csv('data/2007topics.txt', sep=">", header=None, encoding='ISO-8859-1')
    topics_columns = ['TOPICID', 'QUERY']
    topics.columns = topics_columns
    # Get rid of opening <
    topics['TOPICID'] = pd.to_numeric(topics['TOPICID'].str[1:])

    return topics

def load_gold_standard():
    # Loads the predefined gold standard file
    gold_standard = pd.read_csv('data/trecgen2007.gold.standard.tsv.txt', sep="\t", header=None, encoding='ISO-8859-1')
    gs_columns = ['TOPICID', 'PUBMEDID', 'OFFSET', 'LENGTH', 'MESH_ASPECTS']
    gold_standard.columns = gs_columns
    gold_standard['MESH_ASPECTS'] = gold_standard['MESH_ASPECTS'].str.split('|')

    return gold_standard

def load_index():
    # This function loads the index from index.json
    with open('data/index.json', 'r') as read_file:
        idx = json.load(read_file)
    return idx

if __name__ == 'retrieval' or __name__ == '__main__':
    # Whether we are running this file as a standalone or importing it
    # from somewhere else we still want to go ahead and load the index
    # and relevance judgements
    index = load_index()
    topics = load_topics()
    gold_standard = load_gold_standard()

if __name__ == '__main__':
    # If we are running this file as a standalone we can use this block for
    # debugging with print statements
    print(index['john'])