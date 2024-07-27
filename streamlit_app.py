import streamlit as st
import pandas as pd
import base64
import io
from PIL import Image
from streamlit_option_menu import option_menu

EXAMPLE_NO = 1

def streamlit_menu(example=1):
    if example == 1:
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu", 
                options=["Informasi Umum", "Materi dan Rumus", "Kalkulator", "Upaya Pengendalian Pencemaran Udara"], 
                icons=["house", "clipboard", "calculator", "search"],
                menu_icon="cast",
                default_index=0,
            )
        return selected
    
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

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


selected = streamlit_menu(example=EXAMPLE_NO)

css = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("bg.jpg");
    background-size: 180%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
}
</style>
"""

# Apply the CSS to the Streamlit app
st.markdown(css, unsafe_allow_html=True)

html_title = """
<h1 style="text-align: center;">KALKULATOR KADAR DEBU PM 10</h1>
"""
st.markdown(html_title, unsafe_allow_html=True)
st.divider()

if selected == "Informasi Umum":
    
    image_paths = ['foto-ariyani.jpg', 'foto-febri.jpg' , 'foto-nauval.jpg' , 'foto-sabila.jpg' ]
    image_base64_list = [image_to_base64(path) for path in image_paths]
    st.header(':sparkles: **Selamat Datang** di :blue[Aplikasi Kalkulator Kadar Debu PM 10] :sparkles:', divider='blue') 
    st.write("Aplikasi Kalkulator Kadar Debu PM10 hadir untuk membantu analis dalam memproses data pengukuran alat HVAS seperti penentuan volume udara yang di sampling, volume udara yang disampling dalam keadaan standar, dan kadar debu yang hasilnya akan dibandingkan dengan standar baku mutu udara ambien.")

    html = f"""
    <h5 style="text-align:center; margin-top:40px;">Anggota Kelompok 7</h5>
    <table style="width:100%; border-collapse: collapse; margin-bottom:50px;">
    <thead>
        <tr>
            <th style="border: 1px solid black; padding: 8px; text-align:center;">Ariyani Leila Syari’fa </th>
            <th style="border: 1px solid black; padding: 8px; text-align:center;">Febrizianty Nur Fajriani </th>
            <th style="border: 1px solid black; padding: 8px; text-align:center;">Muhammad Naufal Farras Wijatmoko </th>
            <th style="border: 1px solid black; padding: 8px; text-align:center;">Sabila Nur Inayah</th>
        </tr>
        <tr>
            <td style="border: 1px solid black; padding: 8px; text-align:center;">2330487</td>
            <td style="border: 1px solid black; padding: 8px; text-align:center;">2330503</td>
            <td style="border: 1px solid black; padding: 8px; text-align:center;">2330514</td>
            <td style="border: 1px solid black; padding: 8px; text-align:center;">2330527</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; padding: 8px; text-align:center;">
                <img src="data:image/jpeg;base64,{image_base64_list[0]}" alt="Image 1" style="width:100px; height:200px;">
            </td>
            <td style="border: 1px solid black; padding: 8px; text-align:center;">
                <img src="data:image/jpeg;base64,{image_base64_list[1]}" alt="Image 2" style="width:100px; height:200px;">
            </td>
            <td style="border: 1px solid black; padding: 8px; text-align:center;">
                <img src="data:image/jpeg;base64,{image_base64_list[2]}" alt="Image 3" style="width:100px; height:200px;">
            </td>
            <td style="border: 1px solid black; padding: 8px; text-align:center;">
                <img src="data:image/jpeg;base64,{image_base64_list[3]}" alt="Image 4" style="width:100px; height:200px;">
            </td>
        </tr>
    </thead>
    <tbody>
    </tbody>
    </table>
    """
    st.markdown(html, unsafe_allow_html=True)

    st.subheader(':rocket: Cara Penggunaan Aplikasi', divider='grey')
    instructions = """
        1. **Pilih Tab "Kalkulator"**
        2. Isi form Volume Udara dengan menginput data **laju alir awal, laju alir akhir, dan lama pengukuran**
        3. **Klik Hitung**, dan akan memunculkan hasil volume udara yang disampling
        4. Isi form Volume udara dalam kondisi standar dengan menginput **tekanan udara dalam satuan mmHg dan suhu dalam satuan Kelvin**
        5. **Klik Hitung**, dan akan memunculkan hasil volume udara dalam kondisi standar
        6. Isi form Hitung kadar debu dengan menginput **bobot awal dan bobot akhir dalam gram**
        7. **Klik Hitung**
        8. Hasil perhitungan akan menunjukkan hasil kadar debu beserta keterangan **apakah kadar tersebut memenuhi standar baku mutu atau tidak** menurut Peraturan Pemerintah Republik Indonesia Nomor 41 Tahun 1999 Tentang Pengendalian Pencemaran Udara
        """
    st.markdown(instructions)

    st.divider()
    st.markdown('Jika terjadi masalah pada web aplikasi, anda dapat menghubungi kami ke  \n:envelope: innovativecalculator@gmail.com')
    
if selected == "Materi dan Rumus":
    st.subheader(":dizzy: Pengantar", divider='rainbow')
    st.write("Pencemaran udara adalah kondisi di mana udara di suatu wilayah menjadi terkontaminasi oleh berbagai zat kimia, partikel padat, atau mikroorganisme yang dapat membahayakan kesehatan manusia, hewan, tumbuhan, dan lingkungan secara keseluruhan. Salah satu parameter pencemar udara yakni PM 10.")
    st.write("Particulate Matter (PM) adalah polutan berupa partikulat tersuspensi. PM10 adalah partikel polutan udara dengan diameter 10 mikrometer atau kurang. Partikel ini cukup kecil untuk terhirup ke dalam saluran pernapasan dan dapat menyebabkan masalah kesehatan, termasuk penyakit pernapasan dan kardiovaskular. PM10 dapat berasal dari berbagai sumber, seperti debu jalan, pembakaran bahan bakar fosil, dan aktivitas industri.")
    st.write("High Volume Air Sampler (PM 10) adalah alat yang digunakan untuk mengumpulkan partikel udara dalam jumlah besar selama periode waktu tertentu. Alat ini biasanya digunakan dalam pemantauan kualitas udara untuk mengukur konsentrasi Total Suspended Particles (TSP) atau Particulate Matter (PM) seperti PM10 dan PM2.5")
    image = Image.open('alat-hvas.jpg')
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image(image, caption='Gambar Alat HVAS', width=300)
        

    st.subheader(':bulb: Rumus', divider='blue')
    rumus = Image.open('rumus.PNG')
    ket = Image.open('keterangan.PNG')
    st.image(rumus, width=500)
    st.image(ket, width=500)
if selected == "Kalkulator":

    # Form untuk menghitung volume udara
    with st.form(key="vol-udara"):
        st.subheader(':fog: Form :gray[Volume Udara]', divider='blue') 
        laju_alir_awal = st.number_input(":droplet: Input Laju Alir Awal (L/menit)", placeholder=0.0)
        laju_alir_akhir = st.number_input(":droplet: Laju Alir Akhir (L/menit)", placeholder=0.0)
        lama_pengukuran = st.number_input(":stopwatch: Input Lama Pengukuran (menit)", placeholder=0.0)

        enabled_btn = st.form_submit_button("Hitung")


        if enabled_btn:
            if laju_alir_awal == 0.0 and laju_alir_akhir == 0.0 and lama_pengukuran == 0.0:
                st.error("Harap isi inputan dengan angka yang valid") 
            else: 
                st.divider()
                volume_udara_meter_kubik = hitung_volume_udara(laju_alir_awal, laju_alir_akhir, lama_pengukuran)
                st.write(f":star: **Volume udara yang disampling adalah *{volume_udara_meter_kubik:} m³***")
                st.session_state.volume_udara_meter_kubik = volume_udara_meter_kubik

    with st.form(key="vol-udara-standar"):
        st.subheader('Form :orange[Volume udara dalam kondisi standar]', divider='orange')
        volume_udara_sampling = st.number_input(":fog: Input Volume Udara yang Disampling (m³)", value=st.session_state.get('volume_udara_meter_kubik', 0.0), format="%.2f")
        tekanan_udara = st.number_input(":dash: Input Tekanan Udara (mmHg)", value=0.0, format="%.2f")
        suhu = st.number_input(":thermometer: Input Suhu (K)", value=0.0, format="%.2f")
        
        submit_button_standar = st.form_submit_button(label=':green[Hitung]')

        if submit_button_standar:
            if volume_udara_sampling == 0.0 or tekanan_udara == 0.0 or suhu == 0.0:
                st.error("Harap isi inputan dengan angka yang valid")
            else:
                st.divider()
                volume_udara_standar = hitung_volume_standar(volume_udara_sampling, tekanan_udara, suhu)
                st.write(f":star: **Volume udara dalam kondisi standar adalah *{volume_udara_standar:.2f} Nm³***")
                st.session_state.volume_udara_standar = volume_udara_standar
    
    with st.form(key="kadar-debu"):
        st.subheader('Form :blue[Hitung kadar debu]', divider='violet')
        bobot_awal = st.number_input("Input Bobot Awal (gram)", value=0.0, format="%.2f")
        bobot_akhir = st.number_input("Input Bobot Akhir (gram)", value=0.0, format="%.2f")
        
        submit_button_debu =  st.form_submit_button(label=':green[Hitung]')

        if submit_button_debu:
            if bobot_awal == 0.0 and bobot_akhir == 0.0:
                st.error("Harap isi inputan dengan angka yang valid")
            else:
                st.divider()
                kadar_debu = hitung_kadar_debu(bobot_awal, bobot_akhir, st.session_state.volume_udara_standar)
                kadar_debu_real=kadar_debu*1000
                st.write(f":star:**Kadar debu adalah *{kadar_debu:} mg/Nm³***")
                st.session_state.kadar_debu_real = kadar_debu_real
        
    
            if st.session_state.kadar_debu_real < 0:
                st.subheader(f"Total kadar debu pm 10 adalah {st.session_state.kadar_debu_real} µg/Nm3 **Tidak Memenuhi** Standar Baku Mutu Berdasarkan Peraturan Pemerintah Republik Indonesia Nomor 41 Tahun 1999 Tentang Pengendalian Pencemaran Udara")
            elif 0 < kadar_debu_real <= 150:
                st.subheader(f"Total kadar debu pm 10 adalah {st.session_state.kadar_debu_real} µg/Nm3 **Memenuhi** Standar Baku Mutu Berdasarkan Peraturan Pemerintah Republik Indonesia Nomor 41 Tahun 1999 Tentang Pengendalian Pencemaran Udara")
            elif kadar_debu_real== 0.00:
                st.subheader("")
            else:
                st.subheader(f"Total kadar debu pm 10 adalah {st.session_state.kadar_debu_real} µg/Nm3 **Tidak Memenuhi** Standar Baku Mutu Berdasarkan Peraturan Pemerintah Republik Indonesia Nomor 41 Tahun 1999 Tentang Pengendalian Pencemaran Udara")
                    
if selected == "Upaya Pengendalian Pencemaran Udara":
    # st.title("Upaya Pengendalian Pencemaran Udara")
    st.header(":pushpin: Upaya Pengendalian Pencemaran Udara", divider='rainbow')
    st.subheader("**Perketat Emisi Industri**")
    st.write("Industri-industri yang menghasilkan emisi pencemar udara harus diatur untuk mematuhi standar emisi yang telah ditetapkan oleh pemerintah. Ini bisa mencakup penggunaan teknologi kontrol polusi, seperti peralatan pembersih udara dan sistem penangkapan emisi.")
    st.subheader("**Tersedianya Transportasi Ramah Lingkungan**")
    st.write("Mengurangi emisi dari kendaraan bermotor adalah langkah penting. Ini dapat dicapai melalui promosi transportasi umum, mobil listrik, dan teknologi bahan bakar alternatif.")
    st.subheader("**Penghijauan**")
    st.write("Tanaman dapat membantu mengurangi pencemaran udara dengan menyerap karbondioksida dan memproduksi oksigen. Penanaman pohon dan tumbuhan di kawasan perkotaan dapat membantu memperbaiki kualitas udara.")
    st.subheader("**Monitoring Kualitas Udara**")
    st.write("Pemantauan teratur terhadap kualitas udara diperlukan untuk mengetahui tingkat pencemaran udara dan dampaknya terhadap lingkungan dan kesehatan manusia. Data ini dapat digunakan sebagai dasar untuk mengambil keputusan pengendalian pencemaran.")
    st.write("Monitoring kualitas udara bagi industri perlu dilakukan kajian-kajian yang detail terhadap penyebab hingga melakukan analisa dampak dari seluruhnya. Oleh karena itu, industri perlu melakukan monitoring dengan menggandeng Institusi Laboratorium Lingkungan.")