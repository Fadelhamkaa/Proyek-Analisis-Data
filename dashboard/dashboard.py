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

# Rentang tanggal
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

# Ringkasan Data
col1, col2, col3 = st.columns(3)
col1.metric("📌 Total Pengguna", filtered_df["cnt"].sum())
col2.metric("📌 Rata-rata Pengguna per Hari", round(filtered_df["cnt"].mean(), 2))
col3.metric("📌 Rata-rata Waktu Sewa (Jam)", f"{selected_hour[0]} - {selected_hour[1]}")

# 1. Pengaruh Kondisi Cuaca terhadap Penggunaan Sepeda
st.subheader("🌦 Pengaruh Cuaca terhadap Penggunaan Sepeda")
weather_labels = {1: "Cerah", 2: "Berawan", 3: "Hujan/Salju"}
weather_data = filtered_df.groupby("weathersit")["cnt"].mean().reset_index()
fig_weather = px.bar(
    weather_data, x="weathersit", y="cnt", text_auto=True, color="cnt",
    labels={"weathersit": "Kondisi Cuaca", "cnt": "Jumlah Pengguna"},
    color_continuous_scale="sunsetdark"
)
fig_weather.update_xaxes(tickmode="array", tickvals=[1, 2, 3], ticktext=list(weather_labels.values()))
st.plotly_chart(fig_weather, use_container_width=True)

# 2. Pengaruh Musim terhadap Penggunaan Sepeda
st.subheader("🌤 Pengaruh Musim terhadap Penggunaan Sepeda")
season_labels = {1: "Semi", 2: "Panas", 3: "Gugur", 4: "Dingin"}
season_data = filtered_df.groupby("season")["cnt"].mean().reset_index()
fig_season = px.line(
    season_data, x="season", y="cnt", markers=True, text=season_data["cnt"],
    labels={"season": "Musim", "cnt": "Jumlah Pengguna"},
    color_discrete_sequence=["#FF5733"]
)
fig_season.update_xaxes(tickmode="array", tickvals=[1, 2, 3, 4], ticktext=list(season_labels.values()))
st.plotly_chart(fig_season, use_container_width=True)

# 3. Pola Penggunaan Sepeda Berdasarkan Hari Kerja vs. Akhir Pekan
st.subheader("📆 Pola Penggunaan Sepeda Berdasarkan Hari")
workingday_labels = {0: "Akhir Pekan", 1: "Hari Kerja"}
workingday_data = filtered_df.groupby("workingday")["cnt"].mean().reset_index()
fig_workingday = px.pie(
    workingday_data, names="workingday", values="cnt",
    labels={"workingday": "Kategori Hari", "cnt": "Jumlah Pengguna"},
    color_discrete_sequence=["#3498db", "#e74c3c"]
)
fig_workingday.update_traces(textinfo="percent+label", hole=0.4)
st.plotly_chart(fig_workingday, use_container_width=True)

# 4. Pola Penggunaan Sepeda Berdasarkan Jam
st.subheader("📊 Pola Penggunaan Sepeda Berdasarkan Jam")
workingday_hour_data = filtered_df.groupby(["hr", "workingday"])["cnt"].mean().reset_index()
fig_line = px.area(
    workingday_hour_data, x="hr", y="cnt", color="workingday",
    labels={"hr": "Jam", "cnt": "Jumlah Pengguna", "workingday": "Kategori Hari"},
    color_discrete_map={0: "#e74c3c", 1: "#3498db"}
)
fig_line.for_each_trace(lambda t: t.update(name=workingday_labels[int(t.name)]))
st.plotly_chart(fig_line, use_container_width=True)

# 5. Perbedaan Respons Pengguna Terdaftar vs Kasual terhadap Cuaca
st.subheader("🔍 Perbedaan Respons Pengguna Terdaftar vs Kasual terhadap Cuaca")
df_melt = filtered_df.melt(id_vars=["workingday", "weathersit"], value_vars=["casual", "registered"],
                           var_name="user_type", value_name="count")
group_data = df_melt.groupby(["workingday", "weathersit", "user_type"])["count"].mean().reset_index()
fig_diff = px.bar(
    group_data, x="weathersit", y="count", color="user_type", barmode="group",
    facet_col="workingday", labels={"weathersit": "Cuaca", "count": "Pengguna"},
    color_discrete_map={"casual": "orange", "registered": "green"}
)
fig_diff.update_xaxes(tickmode="array", tickvals=[1, 2, 3], ticktext=list(weather_labels.values()))
st.plotly_chart(fig_diff, use_container_width=True)
