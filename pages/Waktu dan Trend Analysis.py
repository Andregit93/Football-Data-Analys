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

def plot_time_series_chart(dataframe, selected_league=None, time_range=None):
    # Filter data berdasarkan liga dan rentang waktu
    filtered_data = dataframe.copy()
    if selected_league:
        filtered_data = filtered_data[filtered_data['name_competition'] == selected_league]
    if time_range:
        filtered_data = filtered_data[(filtered_data['last_season'] >= time_range[0]) & (filtered_data['last_season'] <= time_range[1])]

    # Time series chart untuk melihat tren transfer pemain dari tahun ke tahun
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=filtered_data, x='last_season', y='market_value_in_eur', estimator='mean', ci=None)
    plt.title('Time Series Chart: Tren Nilai Pasar Pemain per Musim')
    plt.xlabel('Musim Transfer')
    plt.ylabel('Rata-rata Nilai Pasar (EUR)')

    st.pyplot(plt.gcf(), clear_figure=True)

def main():
    # Narasi dan deskripsi
    st.title('Waktu dan Trend Analysis')
    st.markdown("### Time Series Chart: Tren Nilai Pasar Pemain per Musim")
    st.write("Grafik ini menunjukkan tren nilai pasar pemain dari tahun ke tahun. Gunakan kontrol di bawah untuk memfilter data.")

    # Baca data yang telah diproses
    dataProcessed = pd.read_csv('./output/dataProcessed.csv')

    # Tambahkan kontrol pemilihan liga
    selected_league = st.selectbox('Pilih Liga:', dataProcessed['name_competition'].unique())

    # Tambahkan kontrol pemilihan rentang waktu
    time_range = st.slider('Pilih Rentang Waktu (Musim):', min_value=int(dataProcessed['last_season'].min()),
                           max_value=int(dataProcessed['last_season'].max()), value=(int(dataProcessed['last_season'].min()), int(dataProcessed['last_season'].max())))

    # Tampilkan time series chart untuk tren nilai pasar pemain
    plot_time_series_chart(dataProcessed, selected_league, time_range)

if __name__ == '__main__':
    main()
