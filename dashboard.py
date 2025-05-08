import streamlit as st

# Judul aplikasi
st.title('🧠 Sistem Prediksi Stroke')

# Membuat tampilan awal dengan informasi tentang stroke
st.write('## Apa Itu Stroke?')
st.write(
    'Stroke terjadi ketika suplai darah ke bagian otak terganggu atau berkurang, menghambat oksigen dan nutrisi yang diperlukan oleh otak. '
    'Hal ini dapat menyebabkan kematian sel otak dalam waktu singkat dan berdampak serius pada kesehatan.'
)

st.write('## Bahaya Stroke')
st.write('- **Gangguan motorik** seperti kesulitan berjalan atau menggunakan tangan.')
st.write('- **Gangguan bicara** yang membuat sulit berbicara atau memahami orang lain.')
st.write('- **Kehilangan memori** yang dapat menyebabkan masalah kognitif.')
st.write('- **Kelumpuhan** pada bagian tubuh tertentu.')
st.write('- **Risiko komplikasi kesehatan lain**, termasuk penyakit jantung.')

st.write('## Diagnosis Stroke')
st.write(
    'Sekarang kita bisa melakukan diagnosis stroke dengan cepat klik tombol di bawah untuk memulai.'
)

if st.button('🔍 Mulai Diagnosis'):
    st.switch_page('pages/sistem_stroke.py')

