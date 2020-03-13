from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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
        res_str = 'The query is: ' + query
        return jsonify(result=res_str)
    except Exception as e:
        return(str(e))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')