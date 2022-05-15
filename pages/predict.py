from PIL import Image
import streamlit as st
import plotly.express as px
import pickle
import streamlit.components.v1 as components
import pandas as pd
import os
# from matplotlib.pyplot import plt
import sys


def load_model():
    pickle_in = open('./models/satisfaction_model.pkl', 'rb')
    satisfaction_model = pickle.load(pickle_in)
    return satisfaction_model


def prdict_app():
    st.title("Prdict customer satisfaction")

    eng_score = st.slider("Engineering score", 0, 10)
    exp_score = st.slider("Experience score", 0, 10)

    if st.button("Predict"):
        model = load_model()
        result = model.predict([[eng_score, exp_score]])

        st.success(f"The customer satisfaction is {result[0][0]}")
