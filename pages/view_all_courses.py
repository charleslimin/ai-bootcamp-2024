#------------------------------ START OF SCRIPT ------------------------------

#```Python
# Set up and run this Streamlit App
import streamlit as st
#Importing the pandas Library 
import pandas as pd

from logics.customer_query_handler import get_course_json

#Reading the JSON File 
#dataFrame = pd.read_json(get_course_json())

df = pd.json_normalize(get_course_json())

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="About Us"
)
# endregion <--------- Streamlit App Configuration --------->

table_data = get_course_json()

st.write(pd.json_normalize(table_data.values()))


#```

#------------------------------ END OF SCRIPT ------------------------------