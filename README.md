# Tweets Classification
## DANGER TWEETS DETECTION :thinking:
### INTRODUCTION :speech_balloon:

Twitter has become an important communication channel in the terms of emergency. With the help of smartphones people announce an emergency they’re observing in real-time. Therefore, more agencies are interested in monitoring Twitter. It’s not always clear whether the tweets are actually announcing a disaster or not. In this project we build a machine learning model that predicts which tweets are danger and which one’s aren’t.  

List of things we tackled in this project:  
> presentation :white_check_mark:  
airflow (prediction job and ingestion job) :white_check_mark:  
great expectations (implemented in the Ingestion DAG) :white_check_mark:  
predictions job (uses the API to predict) :white_check_mark:  
github branches (each one has their own branch) :white_check_mark:  
documentation :white_check_mark:  
model as a service :white_check_mark:  
user interface (filling a form + uploading a file) :white_check_mark:  
predcitons saved in db :white_check_mark:  
ingestion job (gets a file checks its content then move it to the prediction_folder to be used by the prediction job) :white_check_mark:  
allerting system :white_check_mark:  
monitoring dashboard :white_check_mark: 

## General Notes:  
* We host our postgres Database on AWS RDS.  
* We used AWS CloudWatch to monitor the Database performance (on of the grafana dashboards is related to that).  
* We packaged the whole Backend to have more flexibility in imporing services + classes (like the databse class + Tweets class + our model). 
* to run the project kindly run the following first. 
```
pip install -r requirements.txt
```
then run the below to download our Backend Package:   
```
pip install -i https://test.pypi.org/simple/ back-package-dsp2. 
```


## Frontend. 
we used Streamlit to create a form to be filled by users, in addition to the option of uploading a file to make several predictions.  
we also have a History page to see all the Tweets in our Database.  
to run the Sreamlit server use go to this directory `src/FrontEnd/` the run the following:  
```
streamlit run Streamlit.py
```

## Backend. 
we used Flask to build our APIs and to have the model as a service, we have three APIs that we will explain in details, but now in order to run flask server you need to set the FLASK_APP variable using:  
```
export FLASK_APP='src/Backend_APIs/app.py'. 
```
then you run the server using:  
```
flask run
```
the three APIs we have are:
#### * SubmitFile API:  
it takes a csv file called **data_file** and it sends it to the model then the model predicts the whether the the user who tweeted is in danger or not. after that, it sends this data to the database to be stored **Bulk Storing**.
you can reach this API on the route `/SubmitFile`.  

#### * Submit API:  
it handles the form part, which takes the user input and sends it to the backend as `JSON`, we send this object to the model, it predicts it, then we store the data with its prediction in the database.  
you can reach this API on the route `/Submit`.  
in case you would like to use **postman** or other API testing tools,you can use this following `JSON` object:  
```json
{
    "YourEmail": "ali.massoud136@gmail.com",
    "EmeEmail": "ali.massoud136@gmail.com",
    "Location": "Paris",
    "text": "HELPPPP, I am in DANGER!"
}
```

### * getAllTweets API:
we use this API to get all the tweets we have in the databse, we created this mainly to retrieve this data for the history page we have in the frontend.  
you can reach this API on the route `/getAllTweets`.  

### MODEL IMPLEMENTATION
1. Data setup(load the data, train and test split)
2. Main feature preprocessing(text normalization and vectorization)
3. Model training and saving the model in the `model.joblib` file
4. Model evaluation(accurancy, precision, recall and F-score)

### CODE EXTRACTION IN PYTHON MODULES
1. For text normalization and vectorization - `preprocess.py`
2. For model building and training - `train.py`
3. For making a prediction - `inference.py`


