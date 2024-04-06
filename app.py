import streamlit as st
import pickle 
from sklearn.svm import SVC
st.title("my application")
st.write("Welcome")
with open ("svm.pkl", "rb") as f:
    clf=pickle.load(f)
    