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

```console
jinju@aiml-linux:~/aiml-workspace/git/TextClassification-streamlit-FastAPI-Docker$ docker-compose build
Building service
Step 1/11 : FROM python:3.8-slim
 ---> 214d62795dbb
Step 2/11 : RUN adduser myuser
 ---> Using cache
 ---> 79242407c587
Step 3/11 : USER myuser
 ---> Using cache
 ---> e481e3a9e9a8
Step 4/11 : RUN pip install --upgrade pip
 ---> Using cache
 ---> 9b4d6c836fce
Step 5/11 : WORKDIR /home/myuser
 ---> Using cache
 ---> 8323397935ec
Step 6/11 : COPY --chown=myuser:myuser ./requirements.txt .
 ---> Using cache
 ---> b318580ddaa6
Step 7/11 : ENV PATH="/home/myuser/.local/bin:${PATH}"
 ---> Using cache
 ---> 7529cde0b636
Step 8/11 : RUN pip install --user -r requirements.txt
 ---> Using cache
 ---> 90c4cc129ec4
Step 9/11 : COPY --chown=myuser:myuser . .
 ---> Using cache
 ---> a6f83887d385
Step 10/11 : EXPOSE 8000
 ---> Using cache
 ---> 61bbf0e97e5c
Step 11/11 : CMD ["python", "main.py"]
 ---> Using cache
 ---> 0dacdcb2a8af
Successfully built 0dacdcb2a8af
Successfully tagged textclassificationstreamlitfastapidocker_service:latest
Building frontendui
Step 1/11 : FROM python:3.8-slim
 ---> 214d62795dbb
Step 2/11 : RUN adduser myuser
 ---> Using cache
 ---> 79242407c587
Step 3/11 : USER myuser
 ---> Using cache
 ---> e481e3a9e9a8
Step 4/11 : RUN pip install --upgrade pip
 ---> Using cache
 ---> 9b4d6c836fce
Step 5/11 : WORKDIR /home/myuser
 ---> Using cache
 ---> 8323397935ec
Step 6/11 : COPY --chown=myuser:myuser ./requirements.txt .
 ---> Using cache
 ---> 099f2f82b607
Step 7/11 : ENV PATH="/home/myuser/.local/bin:${PATH}"
 ---> Using cache
 ---> c7d36cc1bba4
Step 8/11 : RUN pip install --user -r requirements.txt
 ---> Using cache
 ---> 77ff1f858f93
Step 9/11 : COPY --chown=myuser:myuser . .
 ---> Using cache
 ---> 3e800f659494
Step 10/11 : EXPOSE 8501
 ---> Using cache
 ---> 54e1252b5d2d
Step 11/11 : CMD ["streamlit", "run", "app.py"]
 ---> Using cache
 ---> bb778fad2f60
Successfully built bb778fad2f60
Successfully tagged textclassificationstreamlitfastapidocker_frontendui:latest
```
- Run the command `docker-compose up`
- Access the URL http://localhost:8501 to view the UI.
- Enter a movie review in the text box and click Predict button.
- Some sample movie reviews for testing:
    -  Positive Review : This Was Fun Welcome back Marvel oh how we missed you. Florence Pugh as Yelena is just fantastic
    -  Negative Review : It is a total waste of time. I really dont recommend anyone this movie
