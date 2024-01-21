# Load libraries needed
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Selamat Datang di Aplikasi Analisis eksploratif dan visualisasi data",
    page_icon="🙌",
    layout="wide"
)

# Add content to your Streamlit app
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;; border-bottom: 2px solid white;'>Selamat Datang di Aplikasi Analisis Eksploratif dan Visualisasi Data</h1>",
    unsafe_allow_html=True
)

# Display the waving GIF
st.markdown("<div style='display: flex; justify-content: center;'>"
            "<img src='https://www.animatedimages.org/data/media/707/animated-welcome-image-0048.gif' width='auto' height='auto'>"
            "</div>", unsafe_allow_html=True)

# Add CSS for animation and styling
st.write("""
    <style>
        body {
            background-color: #008000;  /* Kode warna hijau gelap */
            color: #ffffff;  /* Warna teks untuk kontras dengan latar belakang */
        }
        @keyframes slide-in {
            0%{
                transform: translateX(-100%);
            }
            100% {
                transform: translateX(0);
            }
        }

        .slide-in-animation {
            animation: slide-in 1.5s ease-in-out;
        }

        .custom-container {
            padding: 20px;
            background-color: #006400;  /* Kode warna hijau gelap untuk container */
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .sidebar-header {
            font-size: 18px;
            font-weight: bold;
            color: #2e2e2e;
        }

        .subheader-content {
            font-size: 16px;
            color: #2e2e2e;
        }

        .feature-list {
            margin-top: 10px;
            list-style-type: none;
            padding-left: 20px;
        }

        .feature-list li {
            margin-bottom: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Text with animation
st.markdown("<div style='text-align: center; font-size: 20px;' class='slide-in-animation'>"
            "Aplikasi ini dirancang sedemikian rupa melakukan analisis eksploratif dan visualisasi data berdasarkan dataset sepak bola dari Transfermarkt"
            "</div>", unsafe_allow_html=True)

# Add a sidebar to select pages
st.sidebar.header("Navigasi")

# Create a Streamlit container for the subheader
with st.sidebar.container():
    st.sidebar.markdown("Pilih halaman di atas.")

# Define the subheader content
subheader_content = """
<div class="slide-in-animation custom-container">
    <h3 style='text-align: center;'font-size: 30px;'> Hal yang Dapat Anda Lakukan Di Aplikasi Ini:</h3>
    <ul class="feature-list" style='font-size: 18px;'>
        <li>Menjalankan Analisis Univariatet</li>
        <li>Menjalankan Analisis Bivariate</li>
        <li>Menjalankan Analisis Multivariate</li>
        <li>Melihat Waktu dan Trend Analysis</li>
    </ul>
</div>
"""

# Apply CSS animation using HTML/CSS
st.markdown(subheader_content, unsafe_allow_html=True)
