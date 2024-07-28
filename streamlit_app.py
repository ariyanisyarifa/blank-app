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
    kadar_debu = ((bobot_akhir - bobot_awal) * 1000) / volume_udara_standar
    return round(kadar_debu, 2)

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def load_css():
    st.markdown(
        """
        <style>
        .justified-text {
            text-align: justify;
        }
        .header-divider-rainbow {
            border-bottom: 3px solid transparent;
            background-image: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
            background-repeat: no-repeat;
            background-size: 100% 2px;
            background-position: 0 100%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Load custom CSS
load_css()

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
    
    image_paths = ['foto-ariyani.jpeg', 'foto-febri.jpeg' , 'foto-nauval.jpeg' , 'foto-sabila.jpeg' ]
    image_base64_list = [image_to_base64(path) for path in image_paths]
    st.header(':sparkles: **Selamat Datang** di :green[Aplikasi Kalkulator Kadar Debu PM 10] :sparkles:', divider='green') 
    st.markdown("<p class='justified-text'>Aplikasi Kalkulator Kadar Debu PM10 hadir untuk membantu analis dalam memproses data pengukuran alat HVAS seperti penentuan volume udara yang di sampling, volume udara yang disampling dalam keadaan standar, dan kadar debu yang hasilnya akan dibandingkan dengan standar baku mutu udara ambien.</p>", unsafe_allow_html=True)
    
    st.subheader(':seven: Anggota Kelompok 7', divider='blue')

    html = f"""
        <div style="display: flex; flex-direction: column; margin-bottom:50px;">
            <div style="display: flex; align-items: center; margin-bottom:20px;">
                <div style="width:70px; height:70px; border-radius:50%; overflow:hidden; margin-right:20px;">
                    <img src="data:image/jpeg;base64,{image_base64_list[0]}" alt="Image 1" style="width:100%; height:100%; object-fit:cover;">
                </div>
                <div style="text-align:left;">
                    <div style="font-weight:bold;">Ariyani Leila Syari’fa</div>
                    <div>2330487</div>
                </div>
            </div>
            <div style="display: flex; align-items: center; margin-bottom:20px;">
                <div style="width:70px; height:70px; border-radius:50%; overflow:hidden; margin-right:20px;">
                    <img src="data:image/jpeg;base64,{image_base64_list[1]}" alt="Image 2" style="width:100%; height:100%; object-fit:cover;">
                </div>
                <div style="text-align:left;">
                    <div style="font-weight:bold;">Febrizianty Nur Fajriani</div>
                    <div>2330503</div>
                </div>
            </div>
            <div style="display: flex; align-items: center; margin-bottom:20px;">
                <div style="width:70px; height:70px; border-radius:50%; overflow:hidden; margin-right:20px;">
                    <img src="data:image/jpeg;base64,{image_base64_list[2]}" alt="Image 3" style="width:100%; height:100%; object-fit:cover;">
                </div>
                <div style="text-align:left;">
                    <div style="font-weight:bold;">Muhammad Naufal Farras Wijatmoko</div>
                    <div>2330514</div>
                </div>
            </div>
            <div style="display: flex; align-items: center; margin-bottom:20px;">
                <div style="width:70px; height:70px; border-radius:50%; overflow:hidden; margin-right:20px;">
                    <img src="data:image/jpeg;base64,{image_base64_list[3]}" alt="Image 4" style="width:100%; height:100%; object-fit:cover;">
                </div>
                <div style="text-align:left;">
                    <div style="font-weight:bold;">Sabila Nur Inayah</div>
                    <div>2330527</div>
                </div>
            </div>
        </div>
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
    
    st.markdown("<p class='justified-text'>Pencemaran udara adalah kondisi di mana udara di suatu wilayah menjadi terkontaminasi oleh berbagai zat kimia, partikel padat, atau mikroorganisme yang dapat membahayakan kesehatan manusia, hewan, tumbuhan, dan lingkungan secara keseluruhan. Salah satu parameter pencemar udara yakni PM 10.</p>", unsafe_allow_html=True)
    
    st.markdown("<p class='justified-text'>Particulate Matter (PM) adalah polutan berupa partikulat tersuspensi. PM10 adalah partikel polutan udara dengan diameter 10 mikrometer atau kurang. Partikel ini cukup kecil untuk terhirup ke dalam saluran pernapasan dan dapat menyebabkan masalah kesehatan, termasuk penyakit pernapasan dan kardiovaskular. PM10 dapat berasal dari berbagai sumber, seperti debu jalan, pembakaran bahan bakar fosil, dan aktivitas industri.</p>", unsafe_allow_html=True)
    
    st.markdown("<p class='justified-text'>High Volume Air Sampler (PM 10) adalah alat yang digunakan untuk mengumpulkan partikel udara dalam jumlah besar selama periode waktu tertentu. Alat ini biasanya digunakan dalam pemantauan kualitas udara untuk mengukur konsentrasi Total Suspended Particles (TSP) atau Particulate Matter (PM) seperti PM10 dan PM2.5</p>", unsafe_allow_html=True)
    
    
    st.markdown("<p class='justified-text'>Standar baku mutu yang diperbolehkan untuk parameter PM10 sebesar 150μg/Nm³ berdasarkan Peraturan Pemerintah Republik Indonesia Nomor 41 Tahun 1999 Tentang Pengendalian Pencemaran Udara</p>", unsafe_allow_html=True)
    
    image = Image.open('alat-hvas.png')
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image(image, caption='Gambar Alat HVAS', width=300)
    
    
    st.subheader('Cara Uji Partikel dengan Ukuran ≤ 10 μm (PM10) Menggunakan Peralatan High Volume Air Sampler (HVAS) dengan Metode Gravimetri Berdasarkan SNI 7119.15:2016', divider='violet')
    alat = """
    <h5 style="margin-top:20px;">Alat yang digunakan</h5>

    <ol style="list-style-type: lower-alpha;">
        <li>Peralatan HVAS yang dilengkapi dengan inlet selektif PM 10;</li>
        <li>Timbangan analitik dengan ketelitian 0,1 mg;</li>
        <li>Barometer;</li>
        <li>Manometer yang mampu mengukur hingga 4 kPa (40 cm H2O) atau pencatat laju alir yang mampu membaca laju alir dengan ketelitian minimum 0,1 m³/menit;</li>
        <li>Pencatat waktu yang mampu membaca selama 24 jam;</li>
        <li>Termometer;</li>
        <li>Desikator; dan</li>
        <li>Pinset.</li>
    </ol>

    <p><strong>CATATAN</strong> Penimbangan dilakukan pada ruangan dengan temperatur 15°C sampai dengan 35°C dan kelembaban relatif &lt; 50%.</p>
    """

    st.markdown(alat, unsafe_allow_html=True)

    bahan = """
    ##### Bahan yang digunakan

    a) Filter serat kaca (fiber glass)  
    b) Filter serat kuarsa  
    c) Filter politetrafluoroetilena (PTFE) yang dilapisi serat kaca (fiber glass) dan  
    d) Filter membran PTFE
    """
    st.markdown(bahan)

    st.subheader(':clipboard: Cara Kerja', divider='grey')
    st.markdown("""
    <div style="text-align: justify;">
        <h5>Persiapan filter</h5>
        <ol>
            <li>Beri identitas pada filter</li>
            <li>Simpan filter pada ruangan yang sudah dikondisikan dengan temperatur 15°C sampai dengan 35°C dan kelembaban relatif &lt; 50% serta biarkan selama 24 jam</li>
            <li>Timbang lembaran filter dengan timbangan analitik (W₁) <br> <b>CATATAN:</b> Bila digunakan desikator, maka penimbangan filter dilakukan hingga didapatkan berat konstan, yaitu selisih penimbangan terakhir dan sebelumnya 4% atau 0,5 mg</li>
            <li>Simpan filter ke dalam wadah dengan lembaran antara (glassine) kemudian bungkus dengan plastik selama transportasi ke lapangan</li>
        </ol>
        <h5>Pengambilan contoh uji</h5>
        <ol>
            <li>Tempatkan alat uji di posisi dan lokasi pengukuran menurut metoda penentuan lokasi titik ambien sesuai SNI 19-7119.6</li>
            <li>Tempatkan filter pada filter holder</li>
            <li>Pasang inlet selektif PM10</li>
            <li>Lakukan pengambilan contoh uji selama 24 jam ± 1 jam dengan menyambungkan pencatat waktu ke motor untuk mendeteksi kehilangan waktu karena gangguan listrik kemudian hidupkan alat uji dan pantau laju alir udara setiap jam. Catat waktu, tanggal, temperatur, tekanan barometer, serta laju alir, pastikan laju alir udara berada pada rentang 1,1 m³/menit sampai dengan 1,7 m³/menit<br> <b>CATATAN 1:</b> Bila filter sudah penuh dengan partikel, ditandai dengan turunnya laju alir &lt; 1,1 m³/menit, ganti filter dan pengambilan contoh uji segera dilanjutkan<br> <b>CATATAN 2:</b> Aerosol cair, seperti minyak dan partikel sisa pembakaran yang tertinggal di filter dapat menyebabkan filter yang digunakan menjadi basah dan rusak serta filtrasi tidak terjadi dengan baik. Jika hal tersebut terjadi, segera ganti filter, filter lama tetap diperlakukan sebagai contoh uji<br> <b>CATATAN 3:</b> Kemungkinan terjadinya kegagalan voltase atau padamnya listrik pada saat pengambilan akan menyebabkan kesalahan, maka pencatatan laju alir dilakukan secara berkala</li>
            <li>Pindahkan filter secara hati-hati, jaga agar tidak ada partikel yang terlepas, lipat filter dengan posisi contoh uji berada di bagian dalam lipatan. Simpan filter tersebut ke dalam wadah penyimpan filter dan beri identitas<br> <b>CATATAN:</b> Benda selain partikel seperti serangga yang tertangkap dalam filter akan menambah berat. Pisahkan dengan menggunakan pinset.</li>
        </ol>
        <h5>Penimbangan contoh uji</h5>
        <ol>
            <li>Simpan filter pada ruangan yang sudah dikondisikan dengan temperatur 15°C sampai dengan 35°C dan kelembaban relatif &lt; 50% serta biarkan selama 24 jam</li>
            <li>Timbang filter dan catat massanya (W2)<br> <b>CATATAN:</b> Bila digunakan desikator, maka penimbangan filter dilakukan hingga didapatkan berat konstan, yaitu selisih penimbangan terakhir dan sebelumnya 4% atau 0,5 mg</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    st.subheader(':bulb: Rumus', divider='green')
    st.latex(r'''
    \text{Volume udara yang disampling} = \text{rata-rata laju alir} \left(\frac{l}{\text{menit}}\right) \times \text{lama pengukuran (menit)}
    ''')
    
    st.latex(r'''
        V_{\text{standar}} = \text{Volume} \times \frac{ \rho_a}{T_a} \times \frac{298 \text{ K}}{760 \text{ mmHg}}
    ''')
    st.latex(r'''
        \text{Kadar debu} = \frac{\text{selisih bobot (gram)}}{\text{volume standar} \text{ (Nm}^3)}
    ''')

    st.markdown("**Keterangan**")

    st.markdown(r'''
    - Rata-rata laju alir adalah $\frac{\text{Laju alir awal} \left(\frac{L}{\text{menit}}\right) + \text{Laju alir akhir}\left(\frac{L}{\text{menit}}\right)}{2}$.
    - $\rho_a$ adalah tekanan udara aktual dalam satuan mmHg
    - $T_a$ adalah suhu aktual dalam satuan Kelvin
    - 298 K adalah suhu dalam keadaan standar
    - 760 mmHg adalah tekanan dalam keadaan standar
    - Selisih bobot adalah $\frac{\text{Bobot Akhir (gram)} - \text{Bobot Awal (gram)}}{\text{Volume Standar}}$
    ''')
    
if selected == "Kalkulator":

    # Form untuk menghitung volume udara
    with st.form(key="vol-udara"):
        st.subheader(':fog: Form :gray[Volume Udara]', divider='green') 
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
        st.subheader('Form :green[Hitung kadar debu]', divider='violet')
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
    st.header(":pushpin: Upaya Pengendalian Pencemaran Udara", divider='rainbow')
    st.markdown("<h3><b>Perketat Emisi Industri</b></h3>", unsafe_allow_html=True)
    st.markdown("<p class='justified-text'>Industri-industri yang menghasilkan emisi pencemar udara harus diatur untuk mematuhi standar emisi yang telah ditetapkan oleh pemerintah. Ini bisa mencakup penggunaan teknologi kontrol polusi, seperti peralatan pembersih udara dan sistem penangkapan emisi.</p>", unsafe_allow_html=True)
    
    st.markdown("<h3><b>Tersedianya Transportasi Ramah Lingkungan</b></h3>", unsafe_allow_html=True)
    st.markdown("<p class='justified-text'>Mengurangi emisi dari kendaraan bermotor adalah langkah penting. Ini dapat dicapai melalui promosi transportasi umum, mobil listrik, dan teknologi bahan bakar alternatif.</p>", unsafe_allow_html=True)
    
    st.markdown("<h3><b>Penghijauan</b></h3>", unsafe_allow_html=True)
    st.markdown("<p class='justified-text'>Tanaman dapat membantu mengurangi pencemaran udara dengan menyerap karbondioksida dan memproduksi oksigen. Penanaman pohon dan tumbuhan di kawasan perkotaan dapat membantu memperbaiki kualitas udara.</p>", unsafe_allow_html=True)
    
    st.markdown("<h3><b>Monitoring Kualitas Udara</b></h3>", unsafe_allow_html=True)
    st.markdown("<p class='justified-text'>Pemantauan teratur terhadap kualitas udara diperlukan untuk mengetahui tingkat pencemaran udara dan dampaknya terhadap lingkungan dan kesehatan manusia. Data ini dapat digunakan sebagai dasar untuk mengambil keputusan pengendalian pencemaran.</p>", unsafe_allow_html=True)
    st.markdown("<p class='justified-text'>Monitoring kualitas udara bagi industri perlu dilakukan kajian-kajian yang detail terhadap penyebab hingga melakukan analisa dampak dari seluruhnya. Oleh karena itu, industri perlu melakukan monitoring dengan menggandeng Institusi Laboratorium Lingkungan.</p>", unsafe_allow_html=True)