from flask import Flask,jsonify, request
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

# adding POST method

@app.route('/sum_function', methods=["POST"])
def sum_function():
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]
    z = x+y
    retjson = {
        "z" : z
    }
    return jsonify(retjson), 200

@app.route('/bye')

def bye():
    dict_1 = {
        "field1" : 'hello there again',
        "field2" : 'bye now'
    }
    return jsonify(dict_1)
    
if __name__== "__main__":
    app.run(debug=True)
