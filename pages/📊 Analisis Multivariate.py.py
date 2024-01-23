# Import modul-modul yang diperlukan
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Atasi pengaturan opsi Pandas
pd.set_option('mode.use_inf_as_na', True)

# Function untuk melakukan Visualisasi dan menampilkan pairplot menggunakan Streamlit
def plot_pair_plot(dataframe, selected_club=None, time_range=None):
    # Salin data agar tidak merubah data asli
    filtered_data = dataframe.copy()
    
    # Filter data berdasarkan klub jika ada
    if selected_club:
        filtered_data = filtered_data[filtered_data['current_club_name'] == selected_club]
    
    # Filter data berdasarkan rentang waktu jika ada
    if time_range:
        filtered_data = filtered_data[(filtered_data['last_season'] >= time_range[0]) & (filtered_data['last_season'] <= time_range[1])]

    # Pair plot untuk melihat korelasi antara beberapa variabel
    pair_plot = sns.pairplot(filtered_data[['age', 'market_value_in_eur', 'assists_2022']], diag_kind=None)
    plt.suptitle('Pair Plot: Umur, Nilai Pasar, dan Jumlah Assist', y=1.02)
    
    # Tampilkan plot menggunakan Streamlit
    st.pyplot(plt.gcf(), clear_figure=True)

# Function untuk memfilter data yang ditampilkan berdasarkan korelasi antara umur, nilai pasar, dan jumlah assist
def main():
    # Judul halaman Streamlit dan narasi
    st.title('Analisis Multivariate')
    st.title("Pair Plot: Umur, Nilai Pasar, dan Jumlah Assist")
    st.write("Grafik ini menunjukkan korelasi antara umur, nilai pasar, dan jumlah assist. Gunakan kontrol di bawah untuk memfilter data.")

    # Load data yang telah diproses
    dataProcessed = pd.read_csv('./output/dataProcessed.csv')

    # Tambahkan kontrol pemilihan klub menggunakan Streamlit
    selected_club = st.selectbox('Pilih Klub:', dataProcessed['current_club_name'].unique())

    # Tambahkan kontrol pemilihan rentang waktu menggunakan Streamlit
    time_range = st.slider('Pilih Rentang Waktu (Musim):', min_value=int(dataProcessed['last_season'].min()),
                           max_value=int(dataProcessed['last_season'].max()), value=(int(dataProcessed['last_season'].min()), int(dataProcessed['last_season'].max())))

    # Tampilkan pair plot untuk umur, nilai pasar, dan jumlah assist
    plot_pair_plot(dataProcessed, selected_club, time_range)

if __name__ == '__main__':
    main()
