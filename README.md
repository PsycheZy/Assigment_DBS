# Bike Sharing Data Analysis Dashboard

## Deskripsi Proyek
Project ini merupakan analisis data pada dataset Bike Sharing untuk mengetahui pola peminjaman sepeda berdasarkan kondisi cuaca, musim, bulan, dan kelompok waktu.

Analisis dilakukan menggunakan Python di notebook, sedangkan dashboard interaktif dibuat menggunakan Streamlit.

## Pertanyaan Bisnis
1. Bagaimana pengaruh kondisi cuaca terhadap jumlah peminjaman sepeda?
2. Kapan jumlah peminjaman sepeda tertinggi terjadi berdasarkan musim dan bulan?
3. Pada kelompok waktu apa peminjaman sepeda paling tinggi?

## Struktur Folder
- `notebook.ipynb` : notebook analisis data
- `Dashboard.py` : file dashboard Streamlit
- `dashboard_data.csv` : dataset utama untuk dashboard
- `requirements.txt` : daftar library yang dibutuhkan
- `README.md` : dokumentasi project

## Cara Menjalankan Dashboard
1. Pastikan semua library pada `requirements.txt` sudah terpasang.
2. Jalankan perintah berikut di terminal:

```bash
streamlit run Dashboard.py
