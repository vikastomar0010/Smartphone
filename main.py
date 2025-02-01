import pickle
import numpy as np
import pandas as pd
import streamlit as st
st.set_page_config(page_title = "VIZ_DEMO")

# Streamlit UI
st.title(" 📱Smartphone Price Predictor")
st.markdown("""
Welcome to the Smartphone Price Predictor!  
Type the details of a smartphone, and we’ll predict price of smartphone for you.  
---
""")

with open ('df.pkl','rb') as file:
    df = pickle.load(file)
with open ('pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)
st.header("Enter your inputs")

brand_name = st.selectbox('Brand Name',sorted(df['brand_name'].unique().tolist()))
has_5g = st.selectbox('Phone is 5G or NOT',sorted(df['has_5g'].unique().tolist()))
processor_brand = st.selectbox('Processor Brand',sorted(df['processor_brand'].unique().tolist()))
processor_speed = float(st.selectbox('Processor Speed',sorted(df['processor_speed'].unique().tolist())))
Battery = int(st.selectbox('Battery',sorted(df['Battery'].unique().tolist())))
RAM = int(st.selectbox('RAM',sorted(df['RAM'].unique().tolist())))

Storage = int(st.selectbox('Storage',sorted(df['Storage'].unique().tolist())))
screen_size = float(st.selectbox('Screen Size',sorted(df['screen_size'].unique().tolist())))
num_rear_cameras = int(st.selectbox('Numbers Of Rear Camera',sorted(df['num_rear_cameras'].unique().tolist())))
os = st.selectbox('Operating System',sorted(df['os'].unique().tolist()))
primary_camera_rear = float(st.selectbox('Primary Rear Camera',sorted(df['primary_camera_rear'].unique().tolist())))
primary_camera_front = float(st.selectbox('Primary Front Camera',sorted(df['primary_camera_front'].unique().tolist())))


if st.button('Predict'):
    data = [[brand_name, has_5g, processor_brand, processor_speed, Battery, RAM, Storage,
             screen_size, num_rear_cameras,os , primary_camera_rear, primary_camera_front]]

    columns = ['brand_name', 'has_5g', 'processor_brand', 'processor_speed', 'Battery', 'RAM', 'Storage',
             'screen_size', 'num_rear_cameras','os' , 'primary_camera_rear', 'primary_camera_front']

    one_df = pd.DataFrame(data, columns=columns)

    st.dataframe(one_df)

    # Fix Indentation Here
    base_price = int(np.expm1(pipeline.predict(one_df)[0]))
    low = base_price - 2000
    high = base_price + 2000

    st.text("The price of the SmartPhone is between {} and {}".format(low, high))

    st.markdown("---")
    st.markdown("Made with ❤️ by Vikash Tomar")