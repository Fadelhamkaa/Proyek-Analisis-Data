import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman
st.set_page_config(page_title="Dashboard Bike Sharing", page_icon="🚴", layout="wide")

# Membaca data
all_df = pd.read_csv("dashboard/main_data.csv")
all_df["dteday"] = pd.to_datetime(all_df["dteday"])

# Sidebar Header
st.sidebar.title("🚴 Bike Sharing Analytics")
st.sidebar.write("Analisis penggunaan sepeda berdasarkan waktu, cuaca, dan pola pengguna.")

# Sidebar - Filter
st.sidebar.subheader("📅 Filter Waktu")
min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()
date_range = st.sidebar.date_input("Rentang Tanggal:", [min_date, max_date], min_value=min_date, max_value=max_date)

# Pilih bulan
month_mapping = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "Mei", 6: "Jun",
                 7: "Jul", 8: "Agu", 9: "Sep", 10: "Okt", 11: "Nov", 12: "Des"}
month_list = ["Semua"] + [month_mapping[m] for m in sorted(all_df["mnth"].unique())]
selected_month = st.sidebar.selectbox("Pilih Bulan:", month_list, index=0)

# Pilih tahun
year_mapping = {0: "2011", 1: "2012"}
year_list = ["Semua"] + [year_mapping[y] for y in sorted(all_df["yr"].unique())]
selected_year = st.sidebar.selectbox("Pilih Tahun:", year_list, index=0)

# Pilih jam
selected_hour = st.sidebar.slider("Pilih Jam:", min_value=0, max_value=23, value=(0, 23))

# Filter Data
filtered_df = all_df[
    (all_df["dteday"] >= pd.to_datetime(date_range[0])) & 
    (all_df["dteday"] <= pd.to_datetime(date_range[1])) & 
    (all_df["hr"] >= selected_hour[0]) & (all_df["hr"] <= selected_hour[1])
]

if selected_month != "Semua":
    month_num = [k for k, v in month_mapping.items() if v == selected_month][0]
    filtered_df = filtered_df[filtered_df["mnth"] == month_num]

if selected_year != "Semua":
    year_num = [k for k, v in year_mapping.items() if v == selected_year][0]
    filtered_df = filtered_df[filtered_df["yr"] == year_num]

# Dashboard - Header
st.title("🚲 Dashboard Analisis Bike Sharing")
st.markdown("📊 **Analisis pola penggunaan sepeda berdasarkan cuaca, musim, hari kerja, dan jam operasional.**")

# 1. Pengaruh Cuaca terhadap Penggunaan Sepeda
st.subheader("🌦 Pengaruh Cuaca terhadap Penggunaan Sepeda")

# Menghitung rata-rata pengguna sepeda berdasarkan kondisi cuaca
weather_data = filtered_df.groupby("weathersit")["cnt"].mean().reset_index()

# Membuat bar chart dengan warna yang sesuai
fig_weather = px.bar(
    weather_data,
    x="weathersit",
    y="cnt",
    labels={"weathersit": "Kondisi Cuaca"},
    color="cnt",
    color_continuous_scale=["#95a3c3", "#f54d28", "#72b6a1"]  # Warna yang mirip dengan gambar kedua
)

# Mengupdate label sumbu x
fig_weather.update_xaxes(tickmode="array", tickvals=[1, 2, 3], ticktext=["Cerah", "Berawan", "Hujan Ringan"])

# Menampilkan chart
st.plotly_chart(fig_weather, use_container_width=True)

# 2. Pola Penggunaan Berdasarkan Jam
st.subheader("📊 Pola Penggunaan Sepeda Berdasarkan Jam")
workingday_hour_data = filtered_df.groupby(["hr", "workingday"])["cnt"].mean().reset_index()
fig_line = px.line(
    workingday_hour_data, x="hr", y="cnt", color="workingday",
    labels={"hr": "Jam", "cnt": "Jumlah Pengguna"},
    color_discrete_map={0: "red", 1: "blue"}
)
st.plotly_chart(fig_line, use_container_width=True)
