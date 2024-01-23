# Import modul-modul yang diperlukan
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Atasi pengaturan opsi Pandas
pd.set_option('mode.use_inf_as_na', True)

# Function untuk melakukan Visualisasi distribusi umur pemain dan menampilkan plot menggunakan Streamlit
def plot_age_distribution(dataframe):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=dataframe, x='age', bins=20, kde=True)
    plt.title('Distribusi Umur Pemain')
    plt.xlabel('Umur')
    plt.ylabel('Frekuensi')
    
    st.pyplot(plt.gcf(), clear_figure=True)

# Function untuk memfilter data yang ditampilkan berdasarkan liga dan posisi pemain
def filter_data_by_league_and_position(dataframe, selected_league, selected_position):
    # Salin data agar tidak merubah data asli
    filtered_data = dataframe.copy()

    # Filter data berdasarkan liga yang dipilih, jika ada
    if selected_league:
        filtered_data = filtered_data[filtered_data['name_competition'] == selected_league]

    # Filter data berdasarkan posisi yang dipilih, jika ada
    if selected_position:
        filtered_data = filtered_data[filtered_data['position'] == selected_position]

    return filtered_data

# Function untuk tampilan streamlit dan pengaturan kontrol
def main():
    # Judul halaman Streamlit
    st.title('Analisis Univariate')
    st.markdown('Distribusi Umur Pemain')
    st.write("Distribusi umur pemain diukur dalam tahun, Histogram menunjukkan frekuensi umur pemain. Gunakan kontrol di bawah untuk memfilter data.")

    # Load data yang telah diproses
    dataProcessed = pd.read_csv('./output/dataProcessed.csv')

    # Tambahkan kontrol pemilihan liga dan posisi menggunakan Streamlit
    selected_league = st.selectbox('Pilih Liga:', dataProcessed['name_competition'].unique())
    selected_position = st.selectbox('Pilih Posisi Pemain:', dataProcessed['position'].unique())

    # Filter data berdasarkan kontrol yang dipilih
    filtered_data = filter_data_by_league_and_position(dataProcessed, selected_league, selected_position)

    # Tampilkan histogram distribusi umur pemain untuk data yang difilter
    plot_age_distribution(filtered_data)

if __name__ == '__main__':
    main()
