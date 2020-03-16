# J. Nathan Farmer, Sachinder Katoch, Rohit Kothari
#
# This script performs the information retrieval tasks.

import json, re, os
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def retrieve_documents(q):
    # Identifies a topic to use to query
    if q in topics['QUERY'].values:
        # If a topic was chosen from autocomplete use that
        topic_id = topics['TOPICID'][topics['QUERY'] == q].values[0]
        topic = q
    else:
        # If something else was entered try to match it to one of the topics
        topic_id = 200
        best_topic = 'What serum [PROTEINS] change expression in association with high disease activity in lupus?'
        similarity_score = 0.3
        if similarity_score > 0.49:
            topic = best_topic
        else:
            topic = 'The custom query was not relevant to any of the topic queries.'
            return {'topic':topic, 'docs':''}

        
    # Searches for that topic in the documents using the index
    topic_clean = re.sub(r'[^\w\s]','', topic)
    topic_words = topic_clean.split()
    ps = PorterStemmer()
    porters_words = []
    for word in topic_words:
        if (word not in stop_words) and (word != 'what') and (len(word) > 1):
            # Stem the words using Porters Stemming
            porters_words.append(ps.stem(word))

    # Find query tokens in index
    query_list = [index[x] for x in porters_words]
    query_index = {}
    # Sum token counts for a single document
    for d in query_list:
        for key, value in d.items():
            if key in query_index:
                query_index[key] += value
            else:
                query_index[key] = value

    sorted_query_index = {k: v for k, v in sorted(query_index.items(), key=lambda item: item[1], reverse=True)}
    
    # Find out if the document was listed as relevant for this topic
    topic_docs = gold_standard[gold_standard['TOPICID'] == topic_id]
    rank = 0
    ranked_query_index = {}
    for key, value in sorted_query_index.items():
        rank += 1
        if key in topic_docs['PUBMEDID'].values:
            ranked_query_index[rank] = {'document_id':int(key), 'link':links[int(key)], 'relevance':'Relevant', 'precision':0.5, 'recall':0.5}
        else:
            ranked_query_index[rank] = {'document_id':int(key), 'link':links[int(key)], 'relevance':'Not Relevant', 'precision':0.5, 'recall':0.5}

    # Calculate precision and recall for each ranked document
    rel_doc_count = len(topic_docs)
    precision_recall = []
    i = 0
    relevant = 0
    for rank, info in ranked_query_index.items():
        i += 1 
        if info['relevance'] == 'Relevant':
            relevant += 1
        precision = relevant / i
        recall = relevant / rel_doc_count

        precision_recall.append([rank, precision, recall])
    
    # Add formatted values to ranked_query_index
    for doc in precision_recall:
        if doc[1] == 0:
            ranked_query_index[doc[0]]['precision'] = '0.00'
        else:
            ranked_query_index[doc[0]]['precision'] = str(round(doc[1],2))
        if doc[2] == 0:
            ranked_query_index[doc[0]]['recall'] = '0.00'
        else:
            ranked_query_index[doc[0]]['recall'] = str(round(doc[2],2))

    return {'topic':topic, 'docs':ranked_query_index}

def load_links():
    # Loads the link for each document_id
    # Set working dir to location of this file
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    os.chdir(dir_name)
    # Search for all .html file names
    file_list = {}
    dir_name = dir_name + '\\data\\'
    for root, _, files in os.walk(dir_name):
        for f in files:
            if f.endswith('.html'):
                folder = root.split('\\data\\')
                link = '\\data\\' + folder[1] + '\\' + f
                doc_id = int(f[:-5])
                file_list[doc_id] = link

    return file_list

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
    links = load_links()

if __name__ == '__main__':
    # If we are running this file as a standalone we can use this block for
    # debugging with print statements
    print(index['john'])