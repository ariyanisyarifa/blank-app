import streamlit as st

# Judul aplikasi
st.title("Perhitungan Total Partikulat Suspended")

# Side bar: Input data
st.sidebar.header("Input Data")
laju_alir_awal = st.sidebar.number_input("Laju Alir Awal (L/menit)", value=0.0, format="%.2f")
laju_alir_akhir = st.sidebar.number_input("Laju Alir Akhir (L/menit)", value=0.0, format="%.2f")
lama_pengukuran = st.sidebar.number_input("Lama Pengukuran (menit)", value=0.0, format="%.2f")

# Hitung volume udara
volume_udara_liter = ((laju_alir_awal + laju_alir_akhir) / 2) * lama_pengukuran
volume_udara_meter_kubik = volume_udara_liter / 1000  # Konversi liter ke meter kubik

# Tampilkan hasil
st.header("Hasil")
st.write(f"Volume udara yang disampling adalah *{volume_udara_meter_kubik:.2f} m³*")

import streamlit as st
#Side bar 2: Input data
st.sidebar.header("Input Data")
volume_udara_sampling = st.sidebar.number_input("Volume Udara yang Disampling (m³)", value=0.0, format="%.2f")
tekanan_udara = st.sidebar.number_input("Tekanan Udara (mmHg)", value=0.0, format="%.2f")
suhu = st.sidebar.number_input("Suhu (K)", value=0.0, format="%.2f")

# Hitung volume udara dalam kondisi standar
volume_udara_standar = volume_udara_sampling * ((tekanan_udara / suhu) * (298 / 760))

# Tampilkan hasil
st.header("Hasil")
st.write(f"Volume udara dalam kondisi standar adalah *{volume_udara_standar:.2f} Nm³*")

# Side bar 3: Input data 
st.sidebar.header("Input Data")
bobot_awal = st.sidebar.number_input("Bobot Awal (gram)", value=0.0, format="%.2f")
bobot_akhir = st.sidebar.number_input("Bobot Akhir (gram)", value=0.0, format="%.2f")

# Hitung kadar debu
kadar_debu = ((bobot_awal - bobot_akhir) * 1000) / volume_udara_standar  # Konversi gram ke miligram

# Tampilkan hasil
st.header("Hasil")
st.write(f"Kadar debu adalah *{kadar_debu:.2f} mg/Nm³*")