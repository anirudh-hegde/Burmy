import pandas as pd
import streamlit as st
#uploade the file
uploaded_file = st.file_uploader("Choose a JSon file: ", type="json")
if uploaded_file is not None:
    res=pd.read_json(uploaded_file)
    
    #converts json file to csv file
    Csv_file=res.to_csv(index=False).encode()

#download the csv file to your system
    st.download_button(
        label="Download the csv file",
        data='csv_file',
        file_name='converted_file.csv',
        mime='csv',
    )
