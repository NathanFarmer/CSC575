# J. Nathan Farmer, Rohit Kothari, Sachinder Katoch
#
# This file is called and run when a query is submitted for document retrieval.

import json
import sys

def euclidean_distance(query):
    return query

if __name__ == '__main__':
    # Reads AJAX request via standard input
    request = json.load(sys.stdin)
    # Retreives documents using function method
    response = euclidean_distance(request)
    print("Content-Type: application/json", end="\n\n")
    # Returns response vis standard output
    json.dump(response, sys.stdout, indent=2)