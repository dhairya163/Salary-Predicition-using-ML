import streamlit as st
from predict_page import model_dt,model_linear

selection = st.sidebar.selectbox("Regression Model",("Decision Tree Regressor","Linear Regressor"))

if(selection=="Decision Tree Regressor"):
    model_dt()
if(selection=="Linear Regressor"):
    model_linear()