from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


LOADED_MODEL = load_model('movie_sent.h5')

app = FastAPI(title="Moview Review Service", description="API to predict sentiment of movie review")


class Data(BaseModel):
    text:str


@app.post("/predict")
def predict(data:Data):

    message = data.text
    print(message)	
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
        x_1 = tokenizer.texts_to_sequences([message])
        x_1 = pad_sequences(x_1, maxlen=500)
        predictions = LOADED_MODEL.predict(x_1)[0][0]
        print(type(predictions))
    return float(predictions)

 

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
