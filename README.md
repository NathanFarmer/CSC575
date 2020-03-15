# CSC 575 Final Project

### J. Nathan Farmer, Sachinder Katoch, Rohit Kothari

An internet connection is requried to download the data and use the UI.

### Step 1: Run download_documents.py
The full dataset was too large to upload here. It should be downloaded by running download_documents.py. On your local machine, the documents will be extracted to a folder called "data". The .gitignore file tells git to ingore anything in that folder so it does not sync to this repository.

### Step 2: Run index_documents.py
Once the documents are downloaded, we need to build the inverted index. This is done by running index_documents.py. The script will crawl through each of the previously extracted documents and dump the indexed results to a file called index.json in the data folder.

### Step 3: Run ir_project.py
Once the index is built, you can launch the web server by running ir_project.py. Once the web server is running, open the browser of your choice and point to localhost:5000.