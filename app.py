import streamlit as st
from dotenv import load_dotenv
import pandas as pd 
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import os
load_dotenv()
#get the environment variables
API_KEY = os.getenv("OPENAI_KEY")
llm = OpenAI(API_KEY)
pandas_ai = PandasAI(llm)
st.title("Chat with CSV File")
uploaded_file = st.file_uploader("Upload CSV File", type=['csv'])
if uploaded_file is not None :
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    prompt = st.text_area("Ask me a question about the data")

    if st.button("Generate"):
        if prompt :
            with st.spinner("Generating an answer..."): 
                st.write(pandas_ai.run(df, prompt=prompt))
        else :
            st.warning("Please enter a question")        





