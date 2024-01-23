# Import modul-modul yang diperlukan
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Atasi pengaturan opsi Pandas
pd.set_option('mode.use_inf_as_na', True)

# Function untuk membuat scatter plot untuk membandingkan dua variabel di sumbu x dan sumbu y
def plot_scatter_plot(dataframe, x_variable, y_variable):

    # Scatter plot untuk membandingkan dua variabel
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=dataframe, x=x_variable, y=y_variable)
    plt.title(f'Scatter Plot: {y_variable} vs {x_variable}')
    plt.xlabel(x_variable)
    plt.ylabel(y_variable)

    # Narasi dan deskripsi menggunakan Streamlit
    st.markdown(f"### Scatter Plot: {y_variable} vs {x_variable}")
    st.write(f"Grafik ini membandingkan {y_variable} dengan {x_variable}. Gunakan kontrol di atas untuk memfilter data.")
    st.pyplot(plt.gcf(), clear_figure=True)

# Function untuk tampilan streamlit dan pengaturan kontrol
def main():
    
    st.title('Analisis Bivariate')

    # Load data yang telah diproses
    dataProcessed = pd.read_csv('./output/dataProcessed.csv')

    # Kontrol pemilihan variabel x dan y menggunakan Streamlit
    x_variable = st.selectbox('Pilih Variabel untuk Sumbu X:', dataProcessed.columns)
    y_variable = st.selectbox('Pilih Variabel untuk Sumbu Y:', dataProcessed.columns)

    # Tampilkan scatter plot untuk variabel yang dipilih
    plot_scatter_plot(dataProcessed, x_variable, y_variable)

if __name__ == '__main__':
    main()
