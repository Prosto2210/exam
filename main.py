from io import StringIO
from scipy.stats import mannwhitneyu
from scipy import stats
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.set_option("deprecation.showPyplotGlobalUse", False)
uploaded_file = st.file_uploader(
    "Выберите файл", accept_multiple_files=False, type=("csv")
)
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    index = string_data.split("\n")[0].split(",")
    option1 = st.selectbox("Выберите первую колонку с данными.", (index))
    st.write("Вы выбрали:", option1)
    option2 = st.selectbox("Выберите вторую колонку с данными.", (index))
    st.write("Вы выбрали:", option2)
    var1 = df.loc[:, option1][0]
    var2 = df.loc[:, option2][0]
    if ((type(var1) is np.int64) or (type(var1) is np.float64)) and (
        (type(var2) is np.int64) or (type(var2) is np.float64)
    ):
        coll_1 = df[[option1]].dropna().to_numpy().flatten()
        coll_2 = df[[option2]].dropna().to_numpy().flatten()
        data_plotter = [coll_1, coll_2]
        plt.violinplot(data_plotter)
        plt.show()
        st.pyplot()
        tests = ["A/B тестирование", "Тест Манна-Уитни U-test", "t-тест"]
        option3 = st.selectbox("Выберите алгоритм теста гипотез.", (tests))
        if option3 == tests[0]:
            result_ab_test = df[option2].sum() - df[option1].sum()
            st.write("Результат A/B тестирования: ", result_ab_test)
        if option3 == tests[1]:
            result_mannwhitneyu = mannwhitneyu(
                df[option1].dropna(), df[option2].dropna()
            )
            st.write(result_mannwhitneyu)
        if option3 == tests[2]:
            result_t_test = stats.ttest_ind(
                df[option1].dropna(), df[option2].dropna(), equal_var=False
            )
            st.write(f"P-Значение: {result_t_test.pvalue / 2:.4f}")

    else:
        st.write("Ошибка! Выберите столбцы с целочисленными или дробными переменными.")
