import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import streamlit as st

with open('feature_extraction.pkl','rb') as file:
    feature_extraction  = pickle.load(file)
    
with open('model.pkl','rb') as file:
    model  = pickle.load(file)
    
## streamlit app 
st.title('Spam Ham Mail Prediction')

## user input
Message = st.text_input("Enter the mail text here: ")

mail_data = feature_extraction.transform([Message]) 

## Prediction 
if st.button("Predict"):
    prediction = model.predict(mail_data)

    if (prediction[0]==1):
        st.write('Ham Mail')
    else:
        st.write('Spam mail')