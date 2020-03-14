# J. Nathan Farmer, Rohit Kothari, Sachinder Katoch
#
# Step 3: Run this file to launch the web server and point your browser to localhost:5000.

from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__, static_url_path='')

def retrieve_documents(q):
    if q:
        return {1:'data/ajepidem/10901322.html', 2:'data/ajepidem/10901323.html'}

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return(str(e))

@app.route('/get_query')
def get_query():
    try:
        query = request.args.get('query')
        # Retrieve documents using function
        rel_docs = retrieve_documents(query)
        return jsonify(result=rel_docs)
    except Exception as e:
        return(str(e))

@app.route('/data/<path:path>')
def send_js(path):
    return send_from_directory('data', path)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')