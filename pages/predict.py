from PIL import Image
import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components
import pandas as pd
import os
# from matplotlib.pyplot import plt
import sys


def prdict_app():
    st.title("Prdict customer satisfaction")
    st.header("Cluster distribution of users based on experience and engagement")
    image = Image.open('./assets/ClusterDist.png')
    st.image(image, caption="Cluster distribution",
             use_column_width=True)
