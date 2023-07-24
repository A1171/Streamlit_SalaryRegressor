#import streamlit as st
#import numpy as np
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
from keras import regularizers


def CreteModel():
    L2_1=0.0
    model_simple = Sequential()
    #model_simple.add(BatchNormalization(input_dim=x_train_01.shape[1]))
    model_simple.add(Dense(256, activation='relu',input_dim=(39)))
    model_simple.add(Dense(256, activation='relu',kernel_regularizer=regularizers.l2(L2_1)))
    model_simple.add(Dense(128, activation='relu',kernel_regularizer=regularizers.l2(L2_1)))
    model_simple.add(Dense(1, activation='linear'))
    model_simple.compile(optimizer=Adam(learning_rate=1e-5), loss='mse', metrics=['mae'])
    return model_simple

model=CreteModel()
model.load_weights("Model_Salary_weights.h5")

def process(CandidateData):
    prd=model.predict(CandidateData)
    return prd

