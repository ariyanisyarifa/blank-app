# import streamlit as st

# # Judul aplikasi
# st.title("Perhitungan Total Partikulat Suspended")

# # Side bar: Input data
# st.sidebar.header("Input Data")
# laju_alir_awal = st.sidebar.number_input("Laju Alir Awal (L/menit)", value=0.0, format="%.2f")
# laju_alir_akhir = st.sidebar.number_input("Laju Alir Akhir (L/menit)", value=0.0, format="%.2f")
# lama_pengukuran = st.sidebar.number_input("Lama Pengukuran (menit)", value=0.0, format="%.2f")

# # Hitung volume udara
# volume_udara_liter = ((laju_alir_awal + laju_alir_akhir) / 2) * lama_pengukuran
# volume_udara_meter_kubik = volume_udara_liter / 1000  # Konversi liter ke meter kubik

# # Tampilkan hasil
# st.header("Hasil")
# st.write(f"Volume udara yang disampling adalah *{volume_udara_meter_kubik:.2f} m³*")

# import streamlit as st
# #Side bar 2: Input data
# st.sidebar.header("Input Data")
# volume_udara_sampling = st.sidebar.number_input("Volume Udara yang Disampling (m³)", value=0.0, format="%.2f")
# tekanan_udara = st.sidebar.number_input("Tekanan Udara (mmHg)", value=0.0, format="%.2f")
# suhu = st.sidebar.number_input("Suhu (K)", value=0.0, format="%.2f")

# # Hitung volume udara dalam kondisi standar
# volume_udara_standar = volume_udara_sampling * ((tekanan_udara / suhu) * (298 / 760))
# 22
# # Tampilkan hasil
# st.header("Hasil")559
# st.write(f"Volume udara dalam kondisi standar adalah *{volume_udara_standar:.2f} Nm³*")

# # Side bar 3: Input data 
# st.sidebar.header("Input Data")
# bobot_awal = st.sidebar.number_input("Bobot Awal (gram)", value=0.0, format="%.2f")
# bobot_akhir = st.sidebar.number_input("Bobot Akhir (gram)", value=0.0, format="%.2f")

# # Hitung kadar debu
# kadar_debu = ((bobot_awal - bobot_akhir) * 1000) / volume_udara_standar  # Konversi gram ke miligram

# # Tampilkan hasil
# st.header("Hasil")
# st.write(f"Kadar debu adalah *{kadar_debu:.2f} mg/Nm³*")
import streamlit as st

# Fungsi untuk menghitung volume udara
def hitung_volume_udara(laju_alir_awal, laju_alir_akhir, lama_pengukuran):
    volume_udara_liter = ((laju_alir_awal + laju_alir_akhir) / 2) * lama_pengukuran
    volume_udara_meter_kubik = volume_udara_liter / 1000
    return round(volume_udara_meter_kubik, 2)

# Fungsi untuk menghitung volume standar
def hitung_volume_standar(volume_udara_sampling, tekanan_udara, suhu):
    if suhu == 0.0:
        return 0
    volume_udara_standar = volume_udara_sampling * ((tekanan_udara / suhu) * (298 / 760))
    return round(volume_udara_standar, 2)

# Fungsi untuk menghitung kadar debu
def hitung_kadar_debu(bobot_awal, bobot_akhir, volume_udara_standar):
    if bobot_awal == 0.00 and bobot_akhir == 0.00:
        return 0
    kadar_debu = ((bobot_awal - bobot_akhir) * 1000) / volume_udara_standar
    return round(kadar_debu, 2)

# Fungsi Utama
def main():
    # Judul Projek
    st.title('Perhitungan :green[Total Partikulat Suspended]')
    st.markdown('Aplikasi ini digunakan untuk membantu analisis dalam mencari **volume udara yang disampling**, **volume udara yang disampling dalam keadaan standar**, dan **kadar debu pada udara ambien menggunakan alat HVAS PM10**.')

    # Form untuk menghitung volume udara
    st.subheader(':fog: Form :gray[Volume Udara]', divider='green') 
    laju_alir_awal = st.number_input(":droplet: Input Laju Alir Awal (L/menit)", placeholder=0.0)
    laju_alir_akhir = st.number_input(":droplet: Laju Alir Akhir (L/menit)", placeholder=0.0)
    lama_pengukuran = st.number_input(":stopwatch: Input Lama Pengukuran (menit)", placeholder=0.0)

    if st.button(':green[Hitung]'):
        if laju_alir_awal == 0.0 and laju_alir_akhir == 0.0 and lama_pengukuran == 0.0:
            st.error("Harap isi inputan dengan angka yang valid")  
    volume_udara_meter_kubik = hitung_volume_udara(laju_alir_awal, laju_alir_akhir, lama_pengukuran)
    st.write(f":star: **Volume udara yang disampling adalah *{volume_udara_meter_kubik:} m³***")

    # Form Untuk menghitung volume udara standar
    st.subheader('Form :orange[Volume udara dalam kondisi standar]', divider='orange')
    volume_udara_sampling = st.number_input(":fog: Input Volume Udara yang Disampling (m³)", value=volume_udara_meter_kubik, format="%.2f")
    tekanan_udara = st.number_input(":dash: Input Tekanan Udara (mmHg)", value=0.0, format="%.2f")
    suhu = st.number_input(":thermometer: Input Suhu (K)", value=0.0, format="%.2f")
    submit_button_standar = st.button(':green[Hitung]', key='submit-button-standar')

    if submit_button_standar:
        if volume_udara_sampling == 0.0 and tekanan_udara == 0.0 and suhu == 0.0:
            st.error("Harap isi inputan dengan angka yang valid")
    volume_udara_standar = hitung_volume_standar(volume_udara_sampling, tekanan_udara, suhu)
    st.write(f":star: **Volume udara dalam kondisi standar adalah *{volume_udara_standar:} Nm³***")

    st.subheader('Form :blue[Hitung kadar debu]', divider='blue')
    bobot_awal = st.number_input("Input Bobot Awal (gram)", value=0.0, format="%.2f")
    bobot_akhir = st.number_input("Input Bobot Akhir (gram)", value=0.0, format="%.2f")
    submit_button_debu =  st.button(':green[Hitung]', key='submit_button_debu')

    if submit_button_debu:
        if bobot_awal == 0.0 and bobot_akhir == 0.0:
            st.error("Harap isi inputan dengan angka yang valid")
    kadar_debu = hitung_kadar_debu(bobot_awal, bobot_akhir, volume_udara_standar)
    kadar_debu_real=kadar_debu*1000
    st.write(f"**Kadar debu adalah *{kadar_debu:} mg/Nm³***")
    if kadar_debu_real < 0:
        st.subheader("Tidak Memenuhi Baku Mutu")
    elif 0 < kadar_debu_real <= 150:
        st.subheader ("Memenuhi Baku Mutu")
    elif kadar_debu_real== 0.00:
        st.subheader("")
    else:
        st.subheader("Kadar Debu Tidak Valid")

if __name__ == '__main__': 
    main()

# import streamlit as st

# # Fungsi untuk menghitung volume udara
# def hitung_volume_udara(laju_alir_awal, laju_alir_akhir, lama_pengukuran):
#     volume_udara_liter = ((laju_alir_awal + laju_alir_akhir) / 2) * lama_pengukuran
#     volume_udara_meter_kubik = volume_udara_liter / 1000
#     return volume_udara_meter_kubik

# # Fungsi untuk menghitung volume standar
# def hitung_volume_standar(volume_udara_sampling, tekanan_udara, suhu):
#     volume_udara_standar = volume_udara_sampling * ((tekanan_udara / suhu) * (298 / 760))
#     return volume_udara_standar

# # Fungsi untuk menghitung kadar debu
# def hitung_kadar_debu(bobot_awal, bobot_akhir, volume_udara_standar):
#     kadar_debu = ((bobot_awal - bobot_akhir) * 1000) / volume_udara_standar
#     return kadar_debu

# # Fungsi Utama
# def main():
#     # Menyimpan status form menggunakan session_state
#     if 'step' not in st.session_state:
#         st.session_state.step = 1

#     # Judul Projek
#     st.title('Perhitungan :green[Total Partikulat Suspended]')
#     st.markdown('Aplikasi ini digunakan untuk membantu analisis dalam mencari **volume udara yang disampling**, **volume udara yang disampling dalam keadaan standar**, dan **kadar debu pada udara ambien menggunakan alat HVAS PM10**.')
#     st.divider()
    
#     # Form untuk menghitung volume udara
#     if st.session_state.step == 1:
#         st.subheader(':fog: Form :gray[Volume Udara]', divider='green') 
#         laju_alir_awal = st.number_input(":droplet: Input Laju Alir Awal (L/menit)", key='laju_alir_awal', value=0.0)
#         laju_alir_akhir = st.number_input(":droplet: Laju Alir Akhir (L/menit)", key='laju_alir_akhir', value=0.0)
#         lama_pengukuran = st.number_input(":stopwatch: Input Lama Pengukuran (menit)", key='lama_pengukuran', value=0.0)

#         if st.button(':green[Hitung]'):
#             if laju_alir_awal == 0.0 and laju_alir_akhir == 0.0 and lama_pengukuran == 0.0:
#                 st.error("Harap isi inputan dengan angka yang valid")
#             else:
#                 volume_udara_meter_kubik = hitung_volume_udara(laju_alir_awal, laju_alir_akhir, lama_pengukuran)
#                 st.write(f":star: **Volume udara yang disampling adalah *{volume_udara_meter_kubik:.2f} m³***")
#                 st.session_state.volume_udara_meter_kubik = volume_udara_meter_kubik  # Store in session_state
#                 st.session_state.step = 2

#     # Form Untuk menghitung volume udara standar
#     if st.session_state.step == 2:
#         # Check if volume_udara_meter_kubik is stored in session_state
#         if 'volume_udara_meter_kubik' not in st.session_state:
#             st.error("Volume udara yang disampling belum dihitung. Silakan kembali ke langkah sebelumnya untuk menghitungnya.")
#         else:
#             st.subheader('Form :orange[Volume udara dalam kondisi standar]', divider='orange')
#             volume_udara_sampling = st.number_input(":fog: Input Volume Udara yang Disampling (m³)", key='volume_udara_sampling', value=st.session_state.volume_udara_meter_kubik, format="%.2f")
#             tekanan_udara = st.number_input(":dash: Input Tekanan Udara (mmHg)", key='tekanan_udara', value=0.0, format="%.2f")
#             suhu = st.number_input(":thermometer: Input Suhu (K)", key='suhu', value=0.0, format="%.2f")

#             if st.button(':green[Hitung]', key='button-standar'):
#                 if volume_udara_sampling == 0.0 and tekanan_udara == 0.0 and suhu == 0.0:
#                     st.error("Harap isi inputan dengan angka yang valid")
#                 else:
#                     volume_udara_standar = hitung_volume_standar(volume_udara_sampling, tekanan_udara, suhu)
#                     st.session_state.volume_udara_standar = volume_udara_standar  # Store in session_state
#                     st.write(f":star: **Volume udara dalam kondisi standar adalah *{volume_udara_standar:.2f} Nm³***")
#                     st.session_state.step = 3

#     # Form untuk menghitung kadar debu
#     if st.session_state.step == 3:
#         st.subheader('Form :blue[Hitung Kadar Debu]', divider='blue')
#         bobot_awal = st.number_input("Input Bobot Awal (gram)", key='bobot_awal', value=0.0, format="%.2f")
#         bobot_akhir = st.number_input("Input Bobot Akhir (gram)", key='bobot_akhir', value=0.0, format="%.2f")

#         if st.button(':green[Hitung]', key='button-debu'):
#             if bobot_awal == 0.0 and bobot_akhir == 0.0:
#                 st.error("Harap isi inputan dengan angka yang valid")
#             else:
#                 volume_udara_standar = st.session_state.volume_udara_standar
#                 kadar_debu = hitung_kadar_debu(bobot_awal, bobot_akhir, volume_udara_standar)
#                 st.write(f"**Kadar debu adalah *{kadar_debu:.2f} mg/Nm³***")
#                 st.divider()
#                 if kadar_debu > 150:
#                   st.subheader("Partikulat Tidak Memenuhi Baku Mutu")
#                 else:
#                    st.subheader("Partikulat Memenuhi Baku Mutu")

#     # Tombol reset
#     if st.button('Reset'):
#         st.session_state.clear()
#         st.session_state.step = 1
    
# if __name__ == '__main__':
#     main()