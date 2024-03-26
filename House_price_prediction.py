import streamlit as st
import pandas as pd
import numpy as np
import sklearn

import pickle

df= pd.read_csv('cleaned_data.csv')
model = pickle.load(open('RidgeModel.pkl', 'rb'))

st.title(":house_with_garden: Bangalore House Price Prediction")
st.text("Kindly Select your preference")

df=df['location'].unique()
location_options = list(range(len(df)))
loc = st.selectbox("Location", location_options, format_func=lambda x:df[x])

sqft = st.number_input('size/area of the House',value=None,placeholder='Type a number')

bhk_display = ("select number of bedroom",1,2,3,4,5,6)
bhk_options = list(range(len(bhk_display)))
bhk = st.selectbox("Number of Bedrooms", bhk_options, format_func=lambda x: bhk_display[x])

bath_display = ("select number of bathroom",1,2,3,4,5,6)
bath_options = list(range(len(bath_display)))
bath = st.selectbox("Number of bathroom", bath_options, format_func=lambda x: bath_display[x])


if st.button("Submit"):
    if loc is None :
        st.write("Please select a location")
    elif bhk is None:
        st.write("Please select BHK number")
    elif bath is None:
        st.write("Please select Bathroom count")
    elif sqft<1000 or sqft is None:
        st.write("Please Enter feasible Square Feet")
    else:
        input=pd.DataFrame([[df[loc],sqft,bhk,bath]],columns=['location','total_sqft','bhk','bath'])

        predict=model.predict(input)[0]*1000000
        st.write(predict)

        predict=np.round(predict,2)
        if predict is None:
            st.error('sorry! something wrong :disappointed:')
        else:
            st.write(":point_right: Predicted Price: ₹",predict)
