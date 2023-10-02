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

C14 = st.number_input('C14', format='%.0f')
C13 = st.number_input('C13', format='%.0f')
C4 = st.number_input('C4', format='%.0f')
V294= st.number_input('V294', format='%.0f')
C8 = st.number_input('C8', format='%.0f')
TransactionAmt = st.number_input('Transaction Amount')
card6 = st.number_input('card6', format='%.0f')
V317 = st.number_input('V317', format='%.0f')
V280 = st.number_input('V280', format='%.0f')
V97 = st.number_input('V97',format='%.0f')


# Define the predict function


def predict(C14, C13, C4, V294, C8, TransactionAmt, card6, V317, V280, V97):

    X = pd.DataFrame({
        'C14': C14,
        'C13': C13,
        'C4': C4,
        'V294': V294,
        'C8': C8,
        'TransactionAmt': TransactionAmt,
        'card6': card6,
        'V317': V317,
        'V280': V280,
        'V97': V97
    }, index=[0])
    y_pred = model.predict(X)[0]
    return y_pred

# Add the Predict button
if st.button('Predict'):
    result = predict(C14, C13, C4, V294, C8, TransactionAmt, card6, V317, V280, V97)
    if result == 0:
        st.write("The transaction is not fraud.")
    else:
         st.write("The transaction is fraud.")