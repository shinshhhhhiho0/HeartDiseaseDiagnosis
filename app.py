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

def make_prediction(model, input_features):
  return model.predict(input_features)

import streamlit as st

def get_user_input():
  blood_pressure = st.number_input("what is your blood pressure?")
  heart_rate = st.number_input("what is your maximum heart rate?")
  age = st.number_input("what is your age?")
  input_features = [[blood_pressure, heart_rate]] # put your features in here!
  return input_features

  if prediction < 150: # CHANGE THIS!
    st.write("You might have a heart disease.")
  # ADD MORE IF / ELIF STATEMENTS HERE
  else:
    st.write("The model predicts that you have nothing.")


features = ['blood_pressure', 'heart_rate']
input_data = patient_data[features]
output_data = patient_data['disease'] # FILL ME IN

tree_model = DecisionTreeClassifier(max_depth=5)
input_data = patient_data[['heart_rate','blood_pressure']]
output_data = patient_data[['disease']]


tree_model.fit(input_data, output_data)
predictions = tree_model.predict(input_data)
show_predictions(predictions)

visualize_tree(tree_model, input_data)
