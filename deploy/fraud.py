import streamlit as st
import numpy as np
import string
import pickle
import joblib
import pandas as pd 
st.set_option('deprecation.showfileUploaderEncoding',False) 

model = joblib.load('deploy/my_model_saved.pkl')

# Define the user interface
st.title('Fraud Credit Card Prediction')

TransactionAmt = st.number_input('Transaction Amount')
TransactionDT = st.number_input('Transaction Date and Time (no timestamp)', format='%.0f')
card1 = st.number_input('Card1', format='%.0f')
C14 = st.number_input('C14', format='%.0f')
C13 = st.number_input('C13', format='%.0f')
card2 = st.number_input('Card2', format='%.0f')
C8 = st.number_input('C8', format='%.0f')
addr1 = st.number_input('Addr1',format='%.0f')
v257 = st.number_input('V257', format='%.0f')
C1 = st.number_input('C1', format='%.0f')

# Define the predict function
def predict(TransactionAmt, TransactionDT, card1, C14, C13, card2, C8, addr1, v257, C1):
    X = pd.DataFrame({
        'TransactionAmt': TransactionAmt,
        'TransactionDT': TransactionDT,
        'card1': card1,
        'C14': C14,
        'C13': C13,
        'card2': card2,
        'C8': C8,
        'addr1': addr1,
        'V257': v257,
        'C1': C1
    }, index=[0])
    y_pred = model.predict(X)[0]
    return y_pred

# Add the Predict button
if st.button('Predict'):
    result = predict(TransactionAmt, TransactionDT, card1, C14, C13, card2, C8, addr1, v257, C1)
    if result == 0:
        st.write("The transaction is not fraud.")
    else:
         st.write("The transaction is fraud.")