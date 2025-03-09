# 🚴‍♂️ Dashboard Analisis Penggunaan Sepeda

## 📌 Deskripsi Proyek
Proyek ini merupakan dashboard interaktif yang dikembangkan dengan Streamlit untuk mengeksplorasi penggunaan sepeda berdasarkan berbagai faktor, termasuk kondisi cuaca, perbedaan antara hari kerja dan akhir pekan, serta variasi musiman. Dataset yang digunakan adalah **Bike Sharing Dataset**, yang menyajikan informasi peminjaman sepeda berdasarkan hari dan jam.

## 📊 Pertanyaan Bisnis
1. **Bagaimana pengaruh kondisi cuaca terhadap jumlah pengguna sepeda?**
   - Analisis ini bertujuan untuk memahami seberapa besar dampak cuaca terhadap keputusan orang untuk menggunakan sepeda.

2. **Apa perbedaan pola penggunaan sepeda antara hari kerja dan akhir pekan?**
   - Dengan membandingkan data peminjaman pada hari kerja dan akhir pekan, kita dapat mengidentifikasi tren penggunaan yang berbeda.

3. **Bagaimana variasi musiman mempengaruhi penggunaan sepeda?**
   - Analisis ini akan membantu dalam memahami bagaimana musim yang berbeda mempengaruhi jumlah pengguna sepeda.

## 📊 Fitur Utama
- **Filter Waktu**: Pengguna dapat memilih rentang tanggal, bulan, tahun, dan jam untuk menganalisis data yang lebih spesifik.
- **Visualisasi Interaktif**: Menampilkan grafik yang menunjukkan pengaruh cuaca, musim, dan jenis hari terhadap penggunaan sepeda.

## 📁 Struktur Proyek
- `dashboard/`: Berisi file `dashboard.py` yang digunakan untuk membuat dashboard analisis.
- `data/`: Folder yang berisi file data mentah dalam format CSV.
- `notebook.ipynb`: File Jupyter Notebook untuk analisis data.
- `README.md`: Dokumen ini.

## 📦 Instalasi
1. Clone repository ini ke mesin lokal Anda:
   ```bash
   git clone https://github.com/Fadelhamkaa/Proyek-Analisis-Data.git
   
   ```
2. Masuk ke direktori proyek:
   ```bash
   cd PROYEK-ANALISIS-DATA
   ```
3. Instal paket yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Penggunaan
1. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run dashboard/dashboard.py
   ```
2. Akses aplikasi di browser Anda di `https://bike-usage-data.streamlit.app/`.

## 📂 Struktur Direktori
```
├── dashboard/		
│   ├── dashboard.py
│   ├── main_data.csv
├── data/	
│   ├── day.csv
│   ├── hour.csv
├── notebook.py		
├── requirements.txt	
├── README.md
├── url.txt		
```

## 📊 Insight Utama
1. **Pengaruh Cuaca**: Penggunaan sepeda cenderung meningkat pada hari-hari cerah, sementara kondisi cuaca buruk seperti hujan atau salju mengurangi jumlah peminjaman.
2. **Hari Kerja vs. Akhir Pekan**: Terdapat perbedaan signifikan dalam pola penggunaan sepeda antara hari kerja dan akhir pekan, dengan lebih banyak peminjaman terjadi pada hari kerja.
3. **Variasi Musiman**: Musim panas menunjukkan tingkat peminjaman yang lebih tinggi dibandingkan dengan musim dingin, menunjukkan bahwa cuaca yang lebih hangat mendorong lebih banyak orang untuk bersepeda.

## 📊 Sumber Data
Proyek ini menggunakan **Bike Sharing Dataset** yang dapat diakses dari [Kaggle]([https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)).

---

## 🤝 Kontribusi
Kontribusi sangat dihargai! Silakan fork repository ini dan buat pull request untuk perbaikan atau fitur baru.
