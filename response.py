import streamlit as st

def get_app_response(prediction):
  if prediction == 120: # CHANGE THIS!
    st.write("You might have a heart disease.")
  # ADD MORE IF / ELIF STATEMENTS HERE
  else:
    st.write("The model predicts that you have nothing.")
