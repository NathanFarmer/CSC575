# CSC 575 Final Project

### J. Nathan Farmer, Sachinder Katoch, Rohit Kothari

An internet connection is requried to download the data and use the UI.

### Step 1: Run download_documents.py (30-45 minutes)
The full dataset was too large to upload here. It should be downloaded by running download_documents.py. On your local machine, the documents will be extracted to a folder called "data". The .gitignore file tells git to ingore anything in that folder so it does not sync to this repository.

### Step 2: Download index.json from Google Drive and copy to "data" directory (5 minutes) OR run index_documents.py (12 hours)
Once the documents are downloaded, we need to build the inverted index. The completed index is available as a file in Google Drive [(https://drive.google.com/file/d/19VFZOHg_T4X_535X_xo4FLCNW3kqgBjr/view?usp=sharing)](https://drive.google.com/file/d/19VFZOHg_T4X_535X_xo4FLCNW3kqgBjr/view?usp=sharing) due to the length of time it takes to index the entire corpus. The fastest way to get the search tool up and running is to use this index we provided. Creating the index was done by running index_documents.py. The script crawls through each of the previously extracted documents and dumps the indexed results to a file called index.json in the data folder.

### Step 3: Run ir_project.py
Once the index is in your "data" directory, you can launch the web server by running ir_project.py. Once the web server is running, open the browser of your choice and point to localhost:5000.

### File Descriptions:
* **download_documents.py:** Downloads/unzips the documents and relevance files.
* **index_documents.py:** Parses the downloaded documents and creates an inverted index.
* **ir_project.py:** Runs a Flask web server that can accept GET and POST commands from the UI, as well as run Python scripts.
* **templates/index.html:** A Bootstrap search page that accepts user input and returns relevant documents.
* **static/js/search_and_display.js:** The JavaScript file that sends AJAX requests to the web server and modifies the search page DOM.
* **retrieval.py:** The code for matching queries to topics and topics to documents. Precison and recall are also calculated here.