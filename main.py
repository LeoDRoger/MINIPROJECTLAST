import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pickle
# from mlxtend.frequent_patterns import apriori, association_rules



def load_data_raw():
    data = pd.read_csv('https://raw.githubusercontent.com/LeoDRoger/DATASET_PEMAINBOLA/main/Data.csv')
    return data

def main():

    def load_data(url):
        return pd.read_csv(url)

    # data = load_data(url)
    # Mendapatkan parameter dari URL
    params = st.experimental_get_query_params()
    page = params.get("page", "home")

    # Membuat navigasi
    st.sidebar.title("Navigasi")
    pages = {
        "Home": "home",
        "EDA": "EDA",
        "Modeling Assosiate": "Modeling Assosiate"
    }
    selection = st.sidebar.radio("Pergi ke", list(pages.keys()))

    # Navigasi berdasarkan pilihan
    if selection == "Home":
        page = "home"
    elif selection == "EDA":
        page = "EDA"
    elif selection == "Modeling Assosiate":
        page = "Modeling Assosiate"

    # Konten berdasarkan halaman
    if page == "home":
        st.title('Analisis Data Tim Sepak Bola - Halaman Home')

        st.title('Analisis Data Tim Sepak Bola')

        st.header('Tujuan Bisnis')
        st.markdown("""
        - Meningkatkan peluang tim untuk memenangkan pertandingan dan liga.
        - Mengidentifikasi pemain yang berkinerja baik dan membutuhkan pengembangan.
        - Mengoptimalkan strategi dan taktik tim.
        - Meningkatkan pendapatan dan basis penggemar.
        """)

        st.header('Assess Situation')
        st.subheader('Persaingan')
        st.write('Bagaimana performa tim dibandingkan dengan tim lain di liga?')
        st.subheader('Kekuatan dan Kelemahan')
        st.write('Apa saja aspek yang perlu ditingkatkan oleh tim?')
        st.subheader('Peluang')
        st.write('Apa saja peluang yang dapat dimanfaatkan tim untuk meningkatkan performanya?')
        st.subheader('Ancaman')
        st.write('Apa saja hambatan yang dapat menghambat performa tim?')

        st.header('Data Mining Goals')
        st.markdown("""
        - Mengidentifikasi pola dan tren dalam data pertandingan dan pemain.
        - Memprediksi hasil pertandingan dan performa pemain.
        - Mengembangkan model untuk membantu tim dalam membuat keputusan strategis.
        """)

        st.header('Project Plan')
        st.markdown("""
        - Rencana Pertama: Pemahaman bisnisnya seperti menetapkan tujuan dan memahami kebutuhan stakeholders.
        - Mengidentifikasi pertanyaan bisnis yang dapat dijawab dengan data mining.
        """)

    elif page == "EDA":
        st.title('Exploratory Data Analysis (EDA) Pemain Bola')

    # Load data
        url = "https://raw.githubusercontent.com/LeoDRoger/DATASET_PEMAINBOLA/main/Data%20Cleaned.csv"
        data = load_data_raw()

        # Menampilkan informasi dataset
        st.subheader('Informasi Dataset')
        st.write(data.info())

        # Menampilkan statistik deskriptif
        st.subheader('Statistik Deskriptif')
        st.write(data.describe())

        # Visualisasi data
        st.subheader('Visualisasi Data')

        # Histogram usia pemain
        # st.subheader('Histogram Usia Pemain')
        # plt.figure(figsize=(10, 6))
        # sns.histplot(data['Age'], kde=True)
        # plt.xlabel('Usia')
        # plt.ylabel('Frekuensi')
        # st.pyplot()

        # Box plot gaji pemain
        # st.subheader('Box Plot Gaji Pemain')
        # plt.figure(figsize=(10, 6))
        # sns.boxplot(y=data['Wage'])
        # plt.ylabel('Gaji')
        # st.pyplot()
        numeric_cols = data.select_dtypes(include=['float64', 'int64'])
        # Korelasi antar fitur
        st.subheader('Korelasi Antar Fitur')
        plt.figure(figsize=(10, 6))
        sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=2)
        st.pyplot(plt)

    elif page == "Modeling Assosiate":
        st.title('MODELING')
        st.write('Welcome to the MODELING.')

        st.title('Data Pemain Bola')
        st.write('Berikut adalah beberapa baris pertama dari dataset pemain bola: ')
        st.write(load_data_raw().head())

        # Statistik deskriptif
        st.write('Statistik Deskriptif:')
        st.write(load_data_raw().describe())

        # Input nilai fitur untuk prediksi
        st.title('MODELING')
        st.write('Welcome to the MODELING.')

        Name = st.text_input('Name')
        Age = st.text_input('Age')
        Nationality = st.text_input('Nationality')
        Overall = st.text_input('Overall')

    # Model prediksi
    if st.button('Predict'):
        # Cek apakah semua nilai input telah diisi
        if Name and Age and Nationality and Overall:
            # Contoh model prediksi
            # Misalnya, kita membuat model prediksi sederhana dengan syarat tertentu
            if int(Age) > 25 and int(Overall) > 80:
                prediction_result = "High Potential"
            else:
                prediction_result = "Low Potential"

            # Tampilkan hasil prediksi
            st.write(f'Predicted: {prediction_result}')
        else:
            st.error("Please fill in all input values before predicting.")


if __name__ == "__main__":
    main()