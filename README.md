# TextClassification-streamlit-FastAPI-Docker

## Dataset:
Public dataset downloaded from kaggle.This IMDB dataset having 50K movie reviews for natural language processing or Text analytics.This is a dataset for binary sentiment classification, a set of 25,000 highly polar movie reviews for training and 25,000 for testing.

## Goal:
Predict the number of positive and negative reviews using either classification or deep learning algorithms.

## Model creation steps:  
- data exploration
- data preprocessing
- word embedding 
- Model is built using Keras deep learning algorithms 
- Model with Conv1D layer with BLSTM
- model is saved as .h5 file


## Created a service layer
- Using the saved model file created a function for predicting the movie sentiment
- The function is exposed as an API using FastAPI module
- The Service Layer is dockerized

## Created a UI layer
- A frontend is created using Streamlit module, which call the service layer for the predictions
- The UI layer is also dockerized.

A docker-compose file orchestrates the two services (service layer and UI layer) deployed in two docker containers.

## How to run the application
- Ensure Docker and Docker Compose is installed.
- Clone the repository
- Run the command `docker-compose build`
- Run the command `docker-compose up`
- Access the URL http://localhost:8501 to view the UI.
- Enter a movie review in the text box and click Predict button.
- Some sample movie reviews for testing:
    -  Positive Review : This Was Fun Welcome back Marvel oh how we missed you. Florence Pugh as Yelena is just fantastic
    -  Negative Review : It is a total waste of time. I really dont recommend anyone this movie
