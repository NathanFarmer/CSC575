# CSC 575 Final Project

### J. Nathan Farmer, Rohit Kothari, Sachinder Katoch

An internet connection is requried to download the data and use the UI.

### Step 1: Run download_documents.py.
The full dataset was too large to upload here. It should be downloaded by running download_documents.py. On your local machine, the documents will be extracted to a folder called "data". The .gitignore file tells git to ingore anything in that folder so it does not sync to this repository.

### Step 2: Run index_documents.py.
Once the documents are downloaded, we need to build the inverted index. This is done by running index_documents.py. The script will crawl through each of the previously extracted documents and dump the indexed results to a file called index.json in the data folder.

### Step 3: Open the UI.
Once the index is built, you can open the UI in your browser by running "Search Engine UI.exe". This will launch Mongoose web server and open your broswer to index.html. Once you are finished using the UI, you will want to close Mongoose or else it will allow a new instance to run on your machine every time you open it. Mongoose stays open as a "hidden icon" on Windows machines. Right click the blue diamond icon and select exit to close the web server.