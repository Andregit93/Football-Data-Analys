import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Import modules
import numpy as np
import os
from scipy.stats import zscore
from sklearn.preprocessing import StandardScaler

# Atasi pengaturan opsi Pandas
pd.set_option('mode.use_inf_as_na', True)

players = pd.read_csv("./output/dataProcessed.csv")

def plot_age_distribution(dataframe):
    # Visualisasi distribusi umur pemain
    plt.figure(figsize=(10, 6))
    sns.histplot(data=dataframe, x='age', bins=20, kde=True)
    plt.title('Distribusi Umur Pemain')
    plt.xlabel('Umur')
    plt.ylabel('Frekuensi')

    
    st.pyplot(plt.gcf(), clear_figure=True)

def filter_data_by_league_and_position(dataframe, selected_league, selected_position):
    # Filter data berdasarkan liga dan posisi yang dipilih
    filtered_data = dataframe.copy()

    if selected_league:
        filtered_data = filtered_data[filtered_data['name_competition'] == selected_league]

    if selected_position:
        filtered_data = filtered_data[filtered_data['position'] == selected_position]

    return filtered_data

def main():
    st.title('Analisis Univariate')
    st.markdown('Distribusi Umur Pemain')
    st.write("Distribusi umur pemain diukur dalam tahun, Histogram menunjukkan frekuensi umur pemain. Gunakan kontrol di bawah untuk memfilter data.")

    # Baca data yang telah diproses
    dataProcessed = pd.read_csv('./output/dataProcessed.csv')

    # Tambahkan kontrol pemilihan liga dan posisi
    selected_league = st.selectbox('Pilih Liga:', dataProcessed['name_competition'].unique())
    selected_position = st.selectbox('Pilih Posisi Pemain:', dataProcessed['position'].unique())

    # Filter data berdasarkan kontrol yang dipilih
    filtered_data = filter_data_by_league_and_position(dataProcessed, selected_league, selected_position)

    # Tampilkan histogram distribusi umur pemain untuk data yang difilter
    plot_age_distribution(filtered_data)

if __name__ == '__main__':
    main()
