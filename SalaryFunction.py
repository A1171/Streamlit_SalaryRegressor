#import streamlit as st
#import numpy as np
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
from keras import regularizers
import keras
import pickle
import numpy as np
from scipy.sparse import csr_matrix
"""
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
"""
def CreateModel():
  L2_1=0.0
  inputs1 = keras.Input(shape=(39))
  inputs2 = keras.Input(shape=(2000))
  x1 = keras.layers.Dense(512, activation='relu')(inputs1)
  x1 = keras.layers.Dense(512, activation='relu')(x1)
  x2 = keras.layers.Dense(512, activation='relu')(inputs2)
  x2 = keras.layers.Dense(256, activation='relu')(x2)
  x = keras.layers.Concatenate()([x1,inputs2])
  x = keras.layers.Dense(128, activation='relu',kernel_regularizer=regularizers.l2(L2_1))(x)
  x = keras.layers.Dense(1, activation='linear',kernel_regularizer=regularizers.l2(L2_1))(x)
  model=keras.Model(inputs=[inputs1,inputs2], outputs=x)
  model.compile(optimizer=Adam(learning_rate=1e-5), loss='mse', metrics=['mae'])
  return model
def ScaleBackSalary(Y,Std):
  Y1=np.power(2.719,Y*Std*2)
  return Y1
model=CreateModel()
model.load_weights("Model_Salary_weights.h5")
with open('vectorizer.pkl','rb') as f:
  y_std,tfidf_job_type=pickle.load(f)
  
def process(CandidateData,JobDescription):
    TFIDF_result=tfidf_job_type.transform([JobDescription])
    TFIDF_result=csr_matrix(TFIDF_result)
    TFIDF_result.sort_indices()
    #print(CandidateData.shape)
    #print(TFIDF_result.shape)
    #model.summary()
    prd=model.predict([CandidateData,TFIDF_result])
    prd=ScaleBackSalary(prd[0],y_std)
    return prd

