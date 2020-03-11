# J. Nathan Farmer, Rohit Kothari, Sachinder Katoch
#
# Step 2: Run this file to create the document index on your local machine.

import os

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

if __name__ == '__main__':
    # Set working dir to location of this file
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    os.chdir(dir_name)

    # Find out if all current document_ids are unique
    file_list = []
    dir_name = dir_name + '\\data\\'
    for root, dirs, files in os.walk(dir_name):
        for f in files:
            if f.endswith('.html'):
                file_list.append(f)
    
    file_count = len(file_list)
    unique_file_count = len(set(file_list))
    print('File Count:', file_count)
    print('Unique File Name Count:', unique_file_count)
    if file_count == unique_file_count: print('All file names are unique! The file names will become our document_ids.')
    else: print('Something went wrong when you downloaded the documents. You seem to have duplicate document names. Please delete the "data" directory and run download_documents.py again.')

    # Crawl the documents and add each term to the inverted index
    
    ps = PorterStemmer()

