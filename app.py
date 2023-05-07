import uvicorn
from fastapi import FastAPI, Request
# from chno import chno
import numpy as np
import pickle
from fastapi.responses import JSONResponse
# create the app object
app = FastAPI()
pickle_in = open("regressor.pkl", "rb")
regressor = pickle.load(pickle_in)


# index page route, opens automatically at http://127:0:0:1:8000
@app.get("/")
def index():
    return {'message': 'practicle methane production analysis through machine learning'}


# Expose the prediction functionality, make a prediction from the passed JSON data
#  and return predicted TMP is returned with the confidence
@app.post('/predict')
async def predict(coming: Request):
    # convert the data into type dictionary
    try:
        data = await coming.json()
        print(data)
        C = data['carbon']
        H = data['hydrogen']
        N = data["nitrogen"]
        O = data["oxygen"]
        Ash = data["ash"]
        X_test = np.array([C, H, N, O, Ash]).reshape(1,-1)
        prediction = regressor.predict(X_test)
        print(prediction)
        if prediction[0]:
            return{
                'prediction': prediction[0]
            }
    except Exception:
        return JSONResponse(
            status_code=500,
            content={"prediction": "Oops! issue in machine learning execution, try again later"}

        )
            
        
    
    
    

# Run the API on unicorn
# will run on http://127:0:0:1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)