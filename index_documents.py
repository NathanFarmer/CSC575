# J. Nathan Farmer, Sachinder Katoch, Rohit Kothari
#
# Step 2: Run this file to create the document index on your local machine.

import os
import json
import re
from html.parser import HTMLParser

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from bs4 import BeautifulSoup
import string
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def check_unique_document_ids():
    # Set working dir to location of this file
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    os.chdir(dir_name)

    # Search for all .html file names
    file_list = []
    dir_name = dir_name + '\\data\\'
    for root, _, files in os.walk(dir_name):
        for f in files:
            if f.endswith('.html'):
                file_list.append([root, f])
    
    # Check if those file names are all unique
    just_files = []
    for tup in file_list:
        just_files.append(tup[1])
    file_count = len(just_files)
    unique_file_count = len(set(just_files))
    print('File Count:', file_count)
    print('Unique File Name Count:', unique_file_count)
    if file_count == unique_file_count: print('All file names are unique! The file names will become our document_ids.')
    else: print('Something went wrong when you downloaded the documents. You seem to have duplicate document names. Please delete the "data" directory and run download_documents.py again.')

    return file_list

def crawl_and_index(docs):
    ind = {}
    # For each file in the list
    for file_name in docs:
        print('Indexing', file_name[1])
        porters_words = []
        with open(file_name[0] + '\\' + file_name[1]) as f:
            doc_id = int(file_name[1][:-5])
            for line in f:
                # Remove HTML
                no_html_tags = BeautifulSoup(line, 'lxml').text
                no_html_tags = no_html_tags.translate(str.maketrans('', '', string.punctuation))
                # Split on special characters and numbers
                all_words = re.split(' |,|/|-|\n|\u0096|\u0097|\u00a0|\u00fc', no_html_tags)
                ps = PorterStemmer()
                for word in all_words:
                    # Remove numbers
                    word = re.sub(r'[0-9]+', '', word)
                    if word not in stop_words and len(word) > 1:
                        # Stem the words using Porters Stemming
                        porters_words.append(ps.stem(word))

            for pw in porters_words:
                if pw not in ind:
                    # Add the word to the dict if not there 
                    ind[pw] = {doc_id:1}
                elif doc_id not in ind[pw]:
                    # If the word is in the dict but the doc_id is not
                    ind[pw] = {doc_id:1}
                else:
                    # If the word is in the dict and so is the doc_id                        
                    freq = ind[pw][doc_id] + 1
                    ind[pw] = {doc_id:freq}

    return ind

if __name__ == '__main__':
    # Make sure all documents names are unique to be used for document_ids
    document_list = check_unique_document_ids()

    # Crawl the documents and add each term to the inverted index
    index = crawl_and_index(document_list)

    # Set working dir to location of this file again
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    os.chdir(dir_name)

    # Dump the index to a json file
    with open('data/index.json', 'w') as f:
        json.dump(index, f)
