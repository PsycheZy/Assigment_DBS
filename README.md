# Bike Sharing Data Analysis Dashboard

## Deskripsi Proyek
Project ini merupakan analisis data pada dataset Bike Sharing untuk mengetahui pola peminjaman sepeda berdasarkan kondisi cuaca, musim, bulan, dan kelompok waktu.

Analisis dilakukan menggunakan Python di notebook, sedangkan dashboard interaktif dibuat menggunakan Streamlit.

## Cara Menjalankan Dashboard
1. Pastikan semua library pada `requirements.txt` sudah terpasang
2. Jalankan perintah berikut di terminal:

## Persiapan Environment
Pastikan Python sudah terpasang di komputer. Disarankan menggunakan Python versi 3.9 atau yang lebih baru
1. Buka Terminal atau Command Prompt
Masuk ke folder utama proyek terlebih dahulu
```
cd "Submission_Muhammad Iqbal Alfarizy"
```
2. Buat Virtual Environment
Windows
```
python -m venv .venv
```
macOS/Linux
```
python3 -m venv .venv
```
3. Aktifkan Virtual Environment
Windows
```
.venv\Scripts\activate
```
macOS/Linux
```
source .venv/bin/activate
```
Jika virtual environment sudah aktif, biasanya nama .venv akan muncul di awal baris terminal

4. Install library yang dibutuhkan
Setelah virtual environment aktif, install seluruh library yang dibutuhkan
```
pip install -r requirements.txt
```
## Run Streamlit App secara Local
Setelah semua dependency berhasil di-install, jalankan dashboard dari folder utama proyek dengan perintah berikut
```
streamlit run Dashboard/Dashboard.py
```
Dashboard akan terbuka di browser lokal. Jika tidak terbuka otomatis, salin URL lokal yang muncul di terminal

## Link Streamlit Cloud
Link dashboard yang sudah dideploy tersedia pada file `url.txt`
