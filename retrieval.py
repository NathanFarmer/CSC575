import json

def retrieve_documents(q):
    if q:
        return {1:'data/ajepidem/10901322.html', 2:'data/ajepidem/10901323.html'}

def load_index():
    with open('data/index.json', 'r') as read_file:
        idx = json.load(read_file)
    return idx