import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
sns.set(style="whitegrid")

DATA_PATH = Path(__file__).parent / "dashboard_data.csv"

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH)
    data["dteday"] = pd.to_datetime(data["dteday"])
    return data

dashboard_data = load_data()

st.sidebar.header("Filter Data")

min_date = dashboard_data["dteday"].min().date()
max_date = dashboard_data["dteday"].max().date()

date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

season_options = ["All Seasons", "Spring", "Summer", "Fall", "Winter"]
weather_options = ["All Weathers", "Clear", "Mist/Cloudy", "Light Snow/Rain"]

selected_season = st.sidebar.selectbox("Pilih Musim", season_options)
selected_weather = st.sidebar.selectbox("Pilih Kondisi Cuaca", weather_options)

filtered_data = dashboard_data[
    (dashboard_data["dteday"].dt.date >= start_date) &
    (dashboard_data["dteday"].dt.date <= end_date)
]

if selected_season != "All Seasons":
    filtered_data = filtered_data[filtered_data["season"] == selected_season]

if selected_weather != "All Weathers":
    filtered_data = filtered_data[filtered_data["weathersit"] == selected_weather]

st.title("Dashboard Analisis Bike Sharing")
st.write(
    "Dashboard ini menampilkan analisis peminjaman sepeda berdasarkan "
    "cuaca, musim, bulan, kelompok waktu, dan rentang tanggal."
)

if filtered_data.empty:
    st.warning("Data tidak tersedia untuk kombinasi filter yang dipilih.")
    st.stop()

total_rentals = int(filtered_data["cnt"].sum())
avg_rentals = round(filtered_data["cnt"].mean(), 2)
max_rentals = int(filtered_data["cnt"].max())

col1, col2, col3 = st.columns(3)
col1.metric("Total Peminjaman", f"{total_rentals:,}")
col2.metric("Rata-rata Harian", f"{avg_rentals:,.2f}")
col3.metric("Peminjaman Maksimum", f"{max_rentals:,}")

st.caption(
    f"Data ditampilkan untuk periode {start_date} sampai {end_date}. "
    "Gunakan filter di sidebar untuk membandingkan kondisi tertentu."
)

season_order = ["Spring", "Summer", "Fall", "Winter"]
weather_order = ["Clear", "Mist/Cloudy", "Light Snow/Rain"]
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Rata-rata Peminjaman Berdasarkan Kondisi Cuaca")
    weather_rentals = (
        filtered_data.groupby("weathersit")["cnt"]
        .mean()
        .reindex(weather_order)
        .dropna()
    )

    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    sns.barplot(x=weather_rentals.index, y=weather_rentals.values, ax=ax)
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Rata-rata Peminjaman")
    ax.tick_params(axis="x", rotation=15)
    st.pyplot(fig, use_container_width=False)

with col_b:
    st.subheader("Rata-rata Peminjaman Berdasarkan Musim")
    season_rentals = (
        filtered_data.groupby("season")["cnt"]
        .mean()
        .reindex(season_order)
        .dropna()
    )

    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    sns.barplot(x=season_rentals.index, y=season_rentals.values, ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Peminjaman")
    st.pyplot(fig, use_container_width=False)

st.subheader("Tren Rata-rata Peminjaman Berdasarkan Bulan")
monthly_rentals = (
    filtered_data.groupby("month_name")["cnt"]
    .mean()
    .reindex(month_order)
    .dropna()
)

fig, ax = plt.subplots(figsize=(7, 3.5))
sns.lineplot(x=monthly_rentals.index, y=monthly_rentals.values, marker="o", ax=ax)
ax.set_xlabel("Bulan")
ax.set_ylabel("Rata-rata Peminjaman")
st.pyplot(fig, use_container_width=False)

st.subheader("Rata-rata Peminjaman Berdasarkan Kelompok Waktu")
time_group_rentals = filtered_data[
    [
        "avg_cnt_dini_hari",
        "avg_cnt_pagi",
        "avg_cnt_siang",
        "avg_cnt_sore",
        "avg_cnt_malam"
    ]
].mean()

time_labels = ["Dini Hari", "Pagi", "Siang", "Sore", "Malam"]

fig, ax = plt.subplots(figsize=(6, 3.5))
sns.barplot(x=time_labels, y=time_group_rentals.values, ax=ax)
ax.set_xlabel("Kelompok Waktu")
ax.set_ylabel("Rata-rata Peminjaman")
st.pyplot(fig, use_container_width=False)

st.subheader("Insight Utama")
st.markdown(
    """
    - Rata-rata peminjaman cenderung lebih tinggi pada kondisi cuaca cerah dibandingkan saat berkabut atau hujan ringan
    - Permintaan tertinggi terlihat pada musim Fall/Summer dan bulan-bulan pertengahan hingga akhir tahun, terutama pada bulan September dan Oktober
    - Kelompok waktu sore memiliki rata-rata peminjaman tertinggi, sehingga periode ini perlu mendapat perhatian dalam pengelolaan ketersediaan sepeda
    """
)

with st.expander("Lihat Data yang Sudah Difilter"):
    st.dataframe(filtered_data)
