# CSC 575 Final Project

### J. Nathan Farmer, Sachinder Katoch, Rohit Kothari

An internet connection is requried to download the data and use the UI.

### Step 1: Run download_documents.py (30-45 minutes)
The full dataset was too large to upload here. It should be downloaded by running download_documents.py. On your local machine, the documents will be extracted to a folder called "data". The .gitignore file tells git to ingore anything in that folder so it does not sync to this repository.

### Step 2: Download index.json from Box and copy to "data" directory (5 minutes) OR run index_documents.py and zipf.py (12+ hours)
Once the documents are downloaded, we need to build the inverted index. The completed index is available as a file in Box [(https://app.box.com/s/kci5t0n8qg1643ijsolxt2xnfq4ve0ji)](https://app.box.com/s/kci5t0n8qg1643ijsolxt2xnfq4ve0ji) due to the length of time it takes to index the entire corpus. The fastest way to get the search tool up and running is to use this index we provided. Creating the index was done by running index_documents.py. The script crawls through each of the previously extracted documents and dumps the indexed results to a file called index.json in the data folder. Next, running zipf.py removes the most and least common words from index.json.

### Step 3: Run ir_project.py
Once the index is in your "data" directory, you can launch the web server by running ir_project.py. Once the web server is running, open the browser of your choice and point to localhost:5000. A video demonstration of using the browser UI for the IR system can be found at: [https://app.box.com/s/p07dil246jfpzrukyy0o7zqk7vh6pdl4](https://app.box.com/s/p07dil246jfpzrukyy0o7zqk7vh6pdl4)

### File Descriptions:
* **download_documents.py:** Downloads/unzips the documents and relevance files.
* **index_documents.py:** Parses the downloaded documents and creates an inverted index.
* **zipf.py:** Removes the most ane least common terms from the index for performance.
* **ir_project.py:** Runs a Flask web server that can accept GET and POST commands from the UI, as well as run Python scripts.
* **templates/index.html:** A Bootstrap search page that accepts user input and returns relevant documents.
* **static/js/search_and_display.js:** The JavaScript file that sends AJAX requests to the web server and modifies the search page DOM.
* **retrieval.py:** The code for matching queries to topics and topics to documents. Precison and recall are also calculated here.