from dotenv import load_dotenv
import streamlit as st
import docx
import pandas as pd
from langchain.vectorstores import FAISS
from transformers import pipeline

def main():
    load_dotenv()
    st.set_page_config(page_title="Diet")
    st.header("Diet Recipe Ideas  💬")

    # # upload file
    # csv_sp = st.file_uploader("upload file", type={"csv", "txt"})
    # df=pd.DataFrame()
    # if csv_sp is not None:
    #     df = pd.read_csv(csv_sp)
    # st.write(df)
    file1=r"/Users/adithyamadhavan/Documents/Deta/DETA DATASET.xlsx"
    df = pd.read_excel(file1)
    # pdf = st.file_uploader("Upload your excel", type="xlsx")
    # df =pd.read_excel(pdf)

    user_question = st.text_input("Ask for Recipe")
    

    qa_model = pipeline("table-question-answering",model='google/tapas-large-finetuned-wtq')#tokenizer='google-bert/bert-large-uncased-whole-word-masking-finetuned-squad')
    question = user_question
    context = df
    answer=qa_model(table=df,query = question)
    
    st.write(answer['answer'])

if __name__ == '__main__':
    main()