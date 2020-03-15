# J. Nathan Farmer, Sachinder Katoch, Rohit Kothari
#
# This script performs the information retrieval tasks.

import json
import pandas as pd

def retrieve_documents(q):
    # Uses the index to retrieve relevant documents
    if q:
        return {10901322:'data/ajepidem/10901322.html', 10901323:'data/ajepidem/10901323.html'}

def load_relevance():
    # Loads the predefined relevance information

    # Gold standard file
    gold_standard = pd.read_csv('data/trecgen2007.gold.standard.tsv.txt', sep="\t", header=None, encoding='ISO-8859-1')
    gs_columns = ['TOPICID', 'PUBMEDID', 'OFFSET', 'LENGTH', 'MESH_ASPECTS']
    gold_standard.columns = gs_columns
    print(gold_standard.head())

    # Topics file
    topics = gold_standard = pd.read_csv('data/2007topics.txt', sep=">", header=None, encoding='ISO-8859-1')
    topics_columns = ['TOPICID', 'QUERY']
    topics.columns = topics_columns
    # Get rid of opening <
    topics['TOPICID'] = pd.to_numeric(topics['TOPICID'].str[1:])
    print(topics.head())

    return None

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
    relevance = load_relevance()

if __name__ == '__main__':
    # If we are running this file as a standalone we can use this block for
    # debugging with print statements
    print(index['john'])