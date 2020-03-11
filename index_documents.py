# J. Nathan Farmer, Rohit Kothari, Sachinder Katoch
#
# Step 2: Run this file to create the document index on your local machine.

import os

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

if __name__ == '__main__':
    # Crawl the documents and add each term to the inverted index

    ps = PorterStemmer()

