import pickle
import gzip
import streamlit as st

#membaca model
with gzip.open('data_compressed.sav', 'rb') as file:
    stroke_model = pickle.load(file)

#judul web
st.title('sistem prediksi stroke')

import streamlit as st

# Membagi kolom untuk input pengguna
col1, col2 = st.columns(2)

with col1:
    gender = 0 if st.radio('Jenis Kelamin?', ['Perempuan', 'Laki-laki']) == 'Perempuan' else 1
    age = st.number_input('Berapa umur Anda?', min_value=0, max_value=120)
    hypertension = 1 if st.radio('Punya Riwayat Hipertensi?', ['Ya', 'Tidak']) == 'Ya' else 0
    heart_disease = 1 if st.radio('Punya Riwayat Jantung?', ['Ya', 'Tidak']) == 'Ya' else 0
    ever_married = 1 if st.radio('Apakah Anda Pernah Menikah?', ['Ya', 'Tidak']) == 'Ya' else 0

with col2:
    work_type = st.radio('Pilih tipe pekerjaan:', ['Pemerintahan', 'Anak-anak', 'Swasta', 'Wiraswasta'])
    Residence_type =  1 if st.radio('apa tipe tempat tinggal', ['Perkotaan', 'Pedesaan']) == 'Perkotaan' else 0
    avg_glucose_level = st.number_input('Berapa kadar glukosa rata-rata Anda?', min_value=0.0, format="%.2f")
    bmi = st.number_input('Berapa berat badan Anda?', min_value=0.0, format="%.2f")
    smoking_status = st.radio('Pilih status merokok:', ['Dahulu merokok', 'Tidak diketahui', 'Tidak pernah merokok', 'Merokok'])

# Konversi ke nilai numerik menggunakan ternary operator
work_type = (
    0 if work_type == 'Pemerintahan' else 
    1 if work_type == 'Anak-anak' else 
    2 if work_type == 'Swasta' else 
    3  # "Wiraswasta"
)
# Konversi ke nilai numerik menggunakan ternary operator
smoking_status = (
    0 if smoking_status == 'Dahulu merokok' else 
    1 if smoking_status == 'Tidak diketahui' else 
    2 if smoking_status == 'Tidak pernah merokok' else 
    3  # "Merokok"
)

# Tampilkan data yang dimasukkan pengguna
st.write('### Data yang Anda Masukkan:')
st.write(f"- **Jenis Kelamin:** {gender}")
st.write(f"- **Usia:** {age}")
st.write(f"- **Hipertensi:** {hypertension}")
st.write(f"- **Penyakit Jantung:** {heart_disease}")
st.write(f"- **Status Pernikahan:** {ever_married}")
st.write(f"- **Tipe pekerjaan:** {work_type}")
st.write(f"- **Tempat Tinggal:** {Residence_type}")
st.write(f"- **Kadar Glukosa:** {avg_glucose_level}")
st.write(f"- **BMI:** {bmi}")
st.write(f"- **Status merokok Anda:** {smoking_status}")

#code untuk predeksi
stroke_diagnosis = ''

# Tombol prediksi
if st.button('Test Prediksi Stroke'):
    stroke_prediction = stroke_model.predict([[gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status]])

    if stroke_prediction[0] == 1:
        stroke_diagnosis = 'Anda berpotensi terkena stroke'
        st.success(stroke_diagnosis)

        # Menampilkan saran pencegahan
        st.write('## Saran Pencegahan Stroke:')
        st.write('- **Jaga Tekanan Darah**: Pastikan tekanan darah tetap dalam batas normal.')
        st.write('- **Kurangi Konsumsi Garam**: Hindari makanan dengan kadar garam tinggi.')
        st.write('- **Rutin Berolahraga**: Aktivitas fisik dapat meningkatkan kesehatan jantung dan pembuluh darah.')
        st.write('- **Berhenti Merokok**: Jika merokok, segera hentikan untuk mengurangi risiko stroke.')
        st.write('- **Pola Makan Sehat**: Konsumsi lebih banyak sayur, buah, dan makanan kaya serat.')
        st.write('- **Hindari Stres Berlebihan**: Kelola stres dengan meditasi, olahraga, atau kegiatan menyenangkan.')
        st.write('- **berkonsultasi dengan dokter spesialis**: jika di perlukan kamu bisa berkonsultasi dengan dokter spesialis.')

    else:
        stroke_diagnosis = 'Anda berkemungkinan tidak terkena stroke'
        st.success(stroke_diagnosis)

    
