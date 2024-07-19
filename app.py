import streamlit as st
from joblib import load

# Imports the functions we coded above
from header import *
from userinput import *
from response import *
from predictor import *

# Load our DecisionTree model into our web app
model = load("model.joblib")
st.write ("Model uploaded!") # You may remove this in your finalized web app!

create_header()
input_features = get_user_input()
prediction = make_prediction(model, input_features)
get_app_response(prediction)

