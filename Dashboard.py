import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
sns.set(style="whitegrid")

dashboard_data = pd.read_csv("dashboard_data.csv")
dashboard_data["dteday"] = pd.to_datetime(dashboard_data["dteday"])

st.sidebar.header("Filter Data")

season_options = ["Spring", "Summer", "Fall", "Winter"]
weather_options = ["Clear", "Mist/Cloudy", "Light Snow/Rain"]
month_options = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

selected_seasons = st.sidebar.multiselect(
    "Pilih Musim",
    options=season_options,
    default=season_options
)

selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca",
    options=weather_options,
    default=weather_options
)

selected_months = st.sidebar.multiselect(
    "Pilih Bulan",
    options=month_options,
    default=month_options
)

filtered_data = dashboard_data[
    (dashboard_data["season"].isin(selected_seasons)) &
    (dashboard_data["weathersit"].isin(selected_weather)) &
    (dashboard_data["month_name"].isin(selected_months))
]

st.title("Dashboard Analisis Bike Sharing")
st.write(
    "Dashboard ini menampilkan analisis peminjaman sepeda berdasarkan "
    "cuaca, musim, bulan, dan kelompok waktu."
)

if filtered_data.empty:
    st.warning("Data tidak tersedia untuk kombinasi filter yang dipilih.")
    st.stop()

total_rentals = int(filtered_data["cnt"].sum())
avg_rentals = round(filtered_data["cnt"].mean(), 2)
max_rentals = int(filtered_data["cnt"].max())

col1, col2, col3 = st.columns(3)
col1.metric("Total Peminjaman", total_rentals)
col2.metric("Rata-rata Harian", avg_rentals)
col3.metric("Peminjaman Maksimum", max_rentals)

st.subheader("Rata-rata Peminjaman Berdasarkan Kondisi Cuaca")

weather_rentals = (
    filtered_data.groupby("weathersit")["cnt"]
    .mean()
    .reindex(weather_options)
    .dropna()
)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=weather_rentals.index, y=weather_rentals.values, ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Jumlah Peminjaman")
plt.xticks(rotation=15)
st.pyplot(fig)

st.subheader("Rata-rata Peminjaman Berdasarkan Musim")

season_rentals = (
    filtered_data.groupby("season")["cnt"]
    .mean()
    .reindex(season_options)
    .dropna()
)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=season_rentals.index, y=season_rentals.values, ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Jumlah Peminjaman")
st.pyplot(fig)

st.subheader("Tren Rata-rata Peminjaman Berdasarkan Bulan")

monthly_rentals = (
    filtered_data.groupby("month_name")["cnt"]
    .mean()
    .reindex(month_options)
)

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=monthly_rentals.index, y=monthly_rentals.values, marker="o", ax=ax)
ax.set_xlabel("Bulan")
ax.set_ylabel("Rata-rata Jumlah Peminjaman")
st.pyplot(fig)

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

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=time_labels, y=time_group_rentals.values, ax=ax)
ax.set_xlabel("Kelompok Waktu")
ax.set_ylabel("Rata-rata Jumlah Peminjaman")
st.pyplot(fig)

with st.expander("Lihat Data"):
    st.dataframe(filtered_data.head())