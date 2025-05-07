import pickle
import gzip
import streamlit as st

#membaca model
with gzip.open('data_compressed.sav', 'rb') as file:
    stroke_model = pickle.load(file)

#judul web
st.title('sistem prediksi stroke')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    gender = st.text_input ('Perempuan/Laki-laki 0/1')

with col1 :
    age = st.text_input ('Berapa Umur Anda')

with col1 :
    hypertension = st.text_input ('apakah anda memiliki riwayat hipertensi Tidak/Ya 0/1')

with col1 :
    heart_disease = st.text_input ('apakah anda memiliki riwayat penyakit jantung Tidak/Ya 0/1')

with col1 :
    ever_married = st.text_input ('apakah anda pernah menikah Tidak/Ya 0/1')

with col2 :
    work_type = st.text_input ('apa tipe pekerjaan anda? pemerintahan/anak-anak/swasta/wiraswasta 0/1/2/3')

with col2 :
    Residence_type = st.text_input ('apa tipe tempat tinggal anda perkotaan/Pedesaan 0/1')

with col2 :
    avg_glucose_level = st.text_input ('berapa kadar glukosa rata-rata anda')

with col2 :
    bmi = st.text_input ('berapa berat badan anda')

with col2 :
    smoking_status = st.text_input ('status merokok dahulu merokok/tidak diketahui/tidak pernah merokok/merokok 0/1/2/3')

#code untuk predeksi
stroke_diagnosis = ''

#tombol prediksi
if st.button('test prediksi stroke') :
    stroke_prediction = stroke_model.predict([[gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status]])

    if (stroke_prediction[0] == 1):
        stroke_diagnosis = 'Anda berpotensi terkena stroke'
    else :
        stroke_diagnosis = 'Anda berkemungkinan tidak terkena stroke'

    st.success(stroke_diagnosis)
    
