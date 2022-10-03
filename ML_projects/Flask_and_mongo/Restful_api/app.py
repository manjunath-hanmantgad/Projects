from importlib.resources import Resource
from flask import Flask, jsonify , request
from flask_restful import Api
app = Flask(__name__)
api = Api(app) # api is the constructor and takes input as our app.

# define the resources (what is api trying to solve/achieve here)

# defining the function outside so that it can be called everywhere in the code.

def posted_data_validity(postedData, functionName):
    if (functionName == "add" or functionName == "subtract" or functionName == "multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301 # returns 301 error code 
        else:
            return 200
    elif (functionName == "divide"):
        if "x"  not in postedData or "y" not in postedData:
            return 301 
        elif int(postedData["y"]) == 0:
            return 302  
        else:
            return 200

class Add(Resource):
    def post(self):
        # request is received by GET method
        # get posted data 
        postedData = request.get_json() 

        # to handle error of input 
        status_code = posted_data_validity(postedData, "add")
        if (status_code != 200):
            retJson = {
                "Message" : "an error occurred",
                "Status Code" : 301
            }

        x = postedData["x"]
        y = postedData["y"]
        x = int(x) # ensuring x and y are integers
        y = int(y)

        # what is achieved here
        ret = x+y
        retMap = {
            'Sum':ret , 
            'Status Code' : 200
        }
        return jsonify(retMap)

    # def get(self):

    
    #def put(self):

    #def delete(self):
#pass

class Subtract(Resource):
    def post(self):
        # request is received by GET method
        # get posted data 
        postedData = request.get_json() 

        # to handle error of input 
        status_code = posted_data_validity(postedData, "subtract")
        if (status_code != 200):
            retJson = {
                "Message" : "an error occurred",
                "Status Code" : 301
            }

        x = postedData["x"]
        y = postedData["y"]
        x = int(x) # ensuring x and y are integers
        y = int(y)

        # what is achieved here
        ret = x-y
        retMap = {
            'Sum':ret , 
            'Status Code' : 200
        }
        return jsonify(retMap) 

class Divide(Resource):
    def post(self):
        # request is received by GET method
        # get posted data 
        postedData = request.get_json() 

        # to handle error of input 
        status_code = posted_data_validity(postedData, "divide")
        if (status_code != 200):
            retJson = {
                "Message" : "an error occurred",
                "Status Code" : 301
            }

        x = postedData["x"]
        y = postedData["y"]
        x = int(x) # ensuring x and y are integers
        y = int(y)

        # what is achieved here
        ret = x/y
        retMap = {
            'Sum':ret , 
            'Status Code' : 200
        }
        return jsonify(retMap)  

class Multiply(Resource):
    def post(self):
        # request is received by GET method
        # get posted data 
        postedData = request.get_json() 

        # to handle error of input 
        status_code = posted_data_validity(postedData, "multiply")
        if (status_code != 200):
            retJson = {
                "Message" : "an error occurred",
                "Status Code" : 301
            }

        x = postedData["x"]
        y = postedData["y"]
        x = int(x) # ensuring x and y are integers
        y = int(y)

        # what is achieved here
        ret = x*y
        retMap = {
            'Sum':ret , 
            'Status Code' : 200
        }
        return jsonify(retMap)  


# mapping the methods 

api.add_resource(Add, "/add") # adding the add method here
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)