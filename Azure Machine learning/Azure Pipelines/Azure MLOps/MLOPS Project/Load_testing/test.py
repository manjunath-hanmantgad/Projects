#!pip install locust

import time
import json
from locust import HttpUser, task, between

# test_data variable with sample test data to infer the ML model during the load test
test_data = json.dumps({"data": [[8.75, 0.83, 70, 259, 15.82, 1016.51, 1.0]]})

# headers we will use for the API calls in our load test
headers = {'Content-Type': 'application/json'}

# MLServiceUser takes input as httpuser (HttpUser is the user agent that can visit different endpoints.)
class MLServiceUser(HttpUser):
    
    wait_time = between(1, 5) # wait time for user is 1 to 5 seconds between testing each endpoint

    @task # to start defining our task to test an endpoint of our choice using a custom function test_weather_predictions
        
    def test_weather_predictions(self):
        # make a post request to the endpoint using test_data and the headers defined previously
        self.client.post("", data=test_data, headers=headers)
        

# run the following command in terminal at same location :

# Locust -f test-py