import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
model=load_model("Model_Salary.h5")

def process(CandidateData):
    prd=model.predict(CandidateData)
    return prd


