# 🚴‍♂️ Dashboard Analisis Peminjaman Sepeda  

## 📖 Deskripsi Proyek  
Proyek ini menghadirkan **dashboard interaktif** berbasis **Streamlit** yang dirancang untuk mengeksplorasi pola peminjaman sepeda berdasarkan berbagai faktor, seperti kondisi cuaca, perbedaan antara hari kerja dan akhir pekan, serta perubahan musiman. Data yang digunakan berasal dari **Bike Sharing Dataset**, yang mencatat informasi peminjaman sepeda secara harian dan per jam.  

## 🔎 Pertanyaan yang Dianalisis  
1. **Bagaimana cuaca memengaruhi jumlah peminjaman sepeda?**  
   - Menganalisis dampak kondisi cuaca terhadap keputusan pengguna dalam menggunakan sepeda.  

2. **Apakah terdapat perbedaan pola penggunaan sepeda antara hari kerja dan akhir pekan?**  
   - Membandingkan data peminjaman di hari kerja dan akhir pekan untuk melihat tren yang muncul.  

3. **Bagaimana perubahan musim berpengaruh terhadap jumlah pengguna sepeda?**  
   - Mengevaluasi variasi peminjaman sepeda pada musim yang berbeda.  

## ⚡ Fitur Utama  
- **Filter Fleksibel**: Memungkinkan pengguna untuk menyaring data berdasarkan tanggal, bulan, tahun, dan jam.  
- **Visualisasi Dinamis**: Grafik interaktif untuk memahami tren peminjaman sepeda berdasarkan faktor cuaca, musim, dan jenis hari.  

## 📂 Struktur Proyek  
- `dashboard/` → Berisi skrip utama (`dashboard.py`) untuk membangun dashboard.  
- `data/` → Folder penyimpanan dataset dalam format CSV.  
- `notebook.ipynb` → Notebook Jupyter untuk eksplorasi dan analisis data.  
- `README.md` → Dokumentasi proyek ini.  

## ⚙️ Cara Instalasi  
1. Clone repository ini ke perangkat Anda:  
   ```bash
   git clone https://github.com/Fadelhamkaa/Proyek-Analisis-Data.git
   ```  
2. Masuk ke direktori proyek:  
   ```bash
   cd PROYEK-ANALISIS-DATA
   ```  
3. Instal dependensi yang dibutuhkan:  
   ```bash
   pip install -r requirements.txt
   ```  

## 🚀 Menjalankan Dashboard  
1. Jalankan aplikasi Streamlit dengan perintah berikut:  
   ```bash
   streamlit run dashboard/dashboard.py
   ```  
2. Buka browser dan akses aplikasi melalui: `https://bike-usage-data.streamlit.app/`.  

## 📁 Struktur Direktori  
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

## 🔬 Wawasan Utama  
1. **Dampak Cuaca** 🌦️: Penggunaan sepeda meningkat saat cuaca cerah, tetapi menurun saat hujan atau bersalju.  
2. **Hari Kerja vs. Akhir Pekan** 📅: Lebih banyak sepeda digunakan pada hari kerja dibandingkan akhir pekan, menunjukkan tren pemakaian untuk keperluan sehari-hari.  
3. **Pengaruh Musim** ❄️☀️: Pemakaian sepeda cenderung meningkat di musim panas dibandingkan musim dingin, menunjukkan peran suhu dalam keputusan pengguna.  

## 📊 Sumber Data  
Dataset ini diperoleh dari [Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset).  

## 💡 Kontribusi  
Masukan dan saran sangat diapresiasi! Jika ingin menambahkan fitur baru atau memperbaiki kode, silakan **fork** repository ini dan kirim **pull request**.  
