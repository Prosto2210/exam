from io import StringIO
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader(
    "Выберите файл", accept_multiple_files=False, type=("csv")
)
if uploaded_file:
    df = pd.read_csv(uploaded_file, sep=";")
    st.write(df)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    index = string_data.split("\n")[0].split(";")
    option1 = st.selectbox("Выберите первую колонку с данными.", (index))
    st.write("Вы выбрали:", option1)
    option2 = st.selectbox("Выберите вторую колонку с данными.", (index))
    st.write("Вы выбрали:", option2)
