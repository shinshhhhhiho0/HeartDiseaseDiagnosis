import streamlit as st

def get_user_input():
  blood_pressure = st.number_input("what is your blood pressure?")
  heart_rate = st.number_input("what is your maximum heart rate?")
  age = st.number_input("what is your age?")
  input_features = [[blood_pressure, heart_rate]] # put your features in here!
  return input_features
