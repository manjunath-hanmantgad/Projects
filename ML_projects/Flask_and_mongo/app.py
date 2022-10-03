from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/bye')

def bye():
    dict_1 = {
        "field1" : 'hello there again',
        "field2" : 'bye now'
    }
    return jsonify(dict_1)
    
if __name__== "__main__":
    app.run(debug=True)
