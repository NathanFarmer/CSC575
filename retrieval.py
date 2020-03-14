import json

def retrieve_documents(q):
    # Uses the index to retrieve relevant documents
    if q:
        return {10901322:'data/ajepidem/10901322.html', 10901323:'data/ajepidem/10901323.html'}

def load_relevance():
    # Loads the predefined relevance information
    
    return None

def load_index():
    # This function loads the index from index.json
    with open('data/index.json', 'r') as read_file:
        idx = json.load(read_file)
    return idx

if __name__ == 'retrieval' or __name__ == '__main__':
    # Whether we are running this file as a standalone or importing it
    # from somewhere else we still want to go ahead and load the index
    index = load_index()
    relevance = load_relevance()

if __name__ == '__main__':
    # If we are running this file as a standalone we can use this block for
    # debugging with print statements
    print(index['john'])