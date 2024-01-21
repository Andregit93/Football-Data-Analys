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

def plot_pair_plot(dataframe, selected_club=None, time_range=None):
    # Filter data berdasarkan klub dan rentang waktu
    filtered_data = dataframe.copy()
    if selected_club:
        filtered_data = filtered_data[filtered_data['current_club_name'] == selected_club]
    if time_range:
        filtered_data = filtered_data[(filtered_data['last_season'] >= time_range[0]) & (filtered_data['last_season'] <= time_range[1])]

    # Pair plot untuk melihat korelasi antara beberapa variabel
    pair_plot = sns.pairplot(filtered_data[['age', 'market_value_in_eur', 'assists_2022']], diag_kind=None)
    plt.suptitle('Pair Plot: Umur, Nilai Pasar, dan Jumlah Assist', y=1.02)

    
    st.pyplot(plt.gcf(), clear_figure=True)

def main():
    # Narasi dan deskripsi
    st.title('Analisis Multivariate')
    st.title("Pair Plot: Umur, Nilai Pasar, dan Jumlah Assist")
    st.write("Grafik ini menunjukkan korelasi antara umur, nilai pasar, dan jumlah assist. Gunakan kontrol di bawah untuk memfilter data.")

    # Baca data yang telah diproses
    dataProcessed = pd.read_csv('./output/dataProcessed.csv')

    # Tambahkan kontrol pemilihan klub
    selected_club = st.selectbox('Pilih Klub:', dataProcessed['current_club_name'].unique())

    # Tambahkan kontrol pemilihan rentang waktu
    time_range = st.slider('Pilih Rentang Waktu (Musim):', min_value=int(dataProcessed['last_season'].min()),
                           max_value=int(dataProcessed['last_season'].max()), value=(int(dataProcessed['last_season'].min()), int(dataProcessed['last_season'].max())))

    # Tampilkan pair plot untuk umur, nilai pasar, dan jumlah assist
    plot_pair_plot(dataProcessed, selected_club, time_range)

if __name__ == '__main__':
    main()
