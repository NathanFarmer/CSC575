# J. Nathan Farmer, Rohit Kothari, Sachinder Katoch
#
# Step 2: Run this file to create the document index on your local machine.

import os

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

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

    for file_name in docs:
        print('Indexing', file_name[0])
        with open(file_name[0] + '\\' + file_name[1]) as f:
            for line in f:
                porters_words = []
                ps = PorterStemmer()
                for word in line.split():
                    # Stem the words using Porters Stemming
                    porters_words.append(ps.stem(word))
                for pw in porters_words:
                    # Add the word to the dict if not there 
                    ind[pw] = file_name[1][-5]

    return ind

if __name__ == '__main__':
    # Make sure all documents names are unique to be used for document_ids
    document_list = check_unique_document_ids()

    # Crawl the documents and add each term to the inverted index
    index = crawl_and_index(document_list)