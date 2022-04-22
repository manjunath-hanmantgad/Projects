# creating fastapi app here

from fastapi import FastAPI
app = FastAPI()

# add @app.post to run the app using web server and route requests at endpoint mentioned in python file 
# endpoint can be api/version/name
# endpoint = api/v1/sentiment 
# this api accepts http requests 

class Sentiment(Enum):
    POSITIVE =1
    NEGATIVE = 0

@app.post("api/v1/sentiment", response_model=Review)

# predict method retrieves the text field from the input and performs the preprocessing and vectorization steps.
# It uses the model we trained earlier to predict the sentiment of the product review. 
# The returned sentiment is specified as an Enum class to restrict the possible return values for the API

# Depends keyword in the function definition. This allows us to load dependencies or other resources that are required before the function is called.

def load_model():
    try:
        print('Calling Depends Function')
        global prediction_model, vectorizer
        prediction_model = pickle.load(
            open('models/sentiment_classification.pickle', 'rb'))
        vectorizer = pickle.load(open('models/tfidf_vectorizer.pickle', 'rb'))
        print('Models have been loaded')
    except Exception as e:
        raise ValueError('No model here')


def predict(review: Review, model = Depends(load_model())):
    text_clean = preprocessing.clean(review.text)
    text_tfidf = vectorizer.transform([text_clean])
    sentiment = prediction_model.predict(text_tfidf)
    review.sentiment = Sentiment(sentiment.item()).name
    return review


# The class is as specified next and contains the text of the review, a mandatory field along with reviewerID, productID, and sentiment

# schema_extra as an example to act as a guide to developers who want to use the API:


class Review(BaseModel):
    text: str
    reviewerID: Optional[str] = None
    asin: Optional[str] = None
    sentiment: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "text": "This was a great purchase, saved me much time!",
                "reviewerID": "A1VU337W6PKAR3",
                "productID": "B00K0TIC56"
            }
        }