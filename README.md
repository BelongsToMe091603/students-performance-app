# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi baik dalam menghasilkan lulusan berkualitas. Namun, di balik keberhasilan tersebut, terdapat permasalahan serius yaitu tingginya jumlah mahasiswa yang dropout (tidak menyelesaikan studi).

Dropout tidak hanya berdampak pada mahasiswa secara individu, tetapi juga memengaruhi:
- Reputasi institusi
- Tingkat keberhasilan akademik secara keseluruhan
- Efisiensi operasional kampus

Oleh karena itu, diperlukan solusi berbasis data untuk mendeteksi mahasiswa berisiko dropout sejak dini.

### Permasalahan Bisnis

- Tingginya angka mahasiswa dropout setiap tahunnya
- Tidak adanya sistem prediksi untuk identifikasi dini mahasiswa berisiko
- Intervensi (bimbingan, bantuan akademik) masih bersifat reaktif, bukan preventif
- Sulitnya menentukan faktor utama penyebab mahasiswa gagal menyelesaikan studi

### Cakupan Proyek

- Exploratory Data Analysis (EDA)
- Data preprocessing (cleaning, encoding, scaling)
- Feature selection & feature importance analysis
- Training model machine learning (Random Forest / XGBoost)
- Evaluasi model (accuracy, confusion matrix, dll)
- Pembuatan prototype aplikasi menggunakan Streamlit
- Integrasi model ke dalam aplikasi
- Deployment (opsional: Streamlit Cloud)

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

Setup environment:

### 1️ Clone the Repository

```bash
git clone https://github.com/BelongsToMe091603/Students-Performance.git
cd Students-Performance
```

---

### 2️ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---
### 3️ Install Dependencies

Make sure the `requirements.txt` file is available, then run:

```bash
pip install -r requirements.txt
```

---
### 4 Buat File requirements.txt
```bash
pip freeze > requirements.txt
```


## Business Dashboard

Dashboard ini menampilkan ringkasan performa akademik dari total 3.630 mahasiswa. Secara keseluruhan, tingkat kelulusan (Graduate Rate) cukup baik yaitu 60,85%, sementara tingkat dropout berada di angka 39,15% dengan jumlah mahasiswa berisiko (At-Risk Students) sebanyak 1.341 orang. Rata-rata GPA seluruh mahasiswa adalah 3,11, yang menunjukkan performa akademik yang cukup solid secara keseluruhan.

Dari sisi distribusi status mahasiswa, diagram donat menunjukkan bahwa mayoritas mahasiswa berhasil lulus (60,9%) dibandingkan yang dropout (39,1%). Jika dilihat berdasarkan gender, jumlah mahasiswa perempuan lebih banyak daripada laki-laki, namun keduanya sama-sama memiliki proporsi dropout yang cukup signifikan, ditandai dengan bar merah pada grafik batang gender.

Dari sisi status pernikahan, mahasiswa dengan status Single mendominasi jumlah dropout secara absolut dibandingkan kategori lainnya seperti Married, Divorced, atau Facto Union. Hal ini kemungkinan berkaitan dengan usia mahasiswa yang mayoritas masih muda dan belum menikah saat berkuliah.

Pada grafik Dropout by Course, jurusan Management (dua varian) dan Nursing mencatat angka dropout tertinggi, masing-masing di atas 100 mahasiswa. Sebaliknya, jurusan seperti Biofuel Production mencatat dropout paling rendah, kemungkinan karena jumlah mahasiswanya yang memang sedikit.

Terakhir, grafik Total Students by GPA Category menunjukkan bahwa sebagian besar mahasiswa berada di rentang GPA 3–4, yang merupakan kategori tertinggi. Namun terdapat juga kelompok mahasiswa dengan GPA 0–1 dalam jumlah yang cukup besar, yang berpotensi menjadi kelompok paling rentan untuk dropout dan perlu mendapat perhatian lebih dari institusi.


🌐 Akses Dashboard
https://datastudio.google.com/reporting/34be5c92-8176-4101-9d00-3a72be739959

## Menjalankan Sistem Machine Learning (Streamlit)
Go to the application folder (if any), then run it:
```bash
streamlit run app.py
```

Once run, Streamlit will automatically open the browser at:
```bash
http://localhost:8501
```
If it doesn't open automatically, copy the URL into your browser.

🌐 Streamlit (public):
https://studentsperformance-app.streamlit.app/

## Conclusion

Proyek analisis Students Performance di Jaya Jaya Institut berhasil mengidentifikasi faktor-faktor utama yang mempengaruhi kelulusan dan dropout mahasiswa. Dari total 3.630 mahasiswa, tingkat dropout mencapai 39,15% — angka yang cukup tinggi dan memerlukan perhatian serius dari institusi.

Melalui analisis korelasi dan pemodelan machine learning menggunakan Random Forest, ditemukan bahwa lima fitur paling berpengaruh terhadap status mahasiswa adalah jumlah mata kuliah yang lulus di semester 1 dan 2, nilai akademik di kedua semester, serta status pembayaran uang kuliah. Hal ini menunjukkan bahwa performa akademik sejak semester awal dan kondisi finansial mahasiswa merupakan indikator paling kritis dalam menentukan apakah seorang mahasiswa akan lulus atau dropout.

Dashboard bisnis yang dibangun memvisualisasikan pola dropout berdasarkan gender, status pernikahan, jurusan, dan kategori GPA, sehingga pihak institusi dapat dengan mudah memantau dan mengidentifikasi kelompok mahasiswa yang berisiko tinggi. Selain itu, aplikasi prediksi berbasis Streamlit turut dikembangkan untuk membantu institusi mendeteksi potensi dropout secara dini berdasarkan data akademik dan finansial mahasiswa.

Secara keseluruhan, proyek ini memberikan insight berbasis data yang dapat dijadikan dasar pengambilan keputusan bagi Jaya Jaya Institut dalam merancang program intervensi yang lebih tepat sasaran guna menekan angka dropout dan meningkatkan tingkat kelulusan mahasiswa.


### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan guna mengurangi mahasiswa mahasiswa dropout.

- Intervensi Akademik Sejak Dini
Institusi perlu memantau secara ketat performa mahasiswa pada semester 1 dan 2, karena nilai dan jumlah mata kuliah yang lulus di awal perkuliahan terbukti menjadi indikator paling kritis terhadap risiko dropout. Program bimbingan belajar atau tutoring khusus perlu diberikan kepada mahasiswa yang menunjukkan performa rendah sejak semester pertama sebelum kondisinya semakin memburuk.

- Program remedial atau mentoring akademik harus difokuskan pada semester awal
Institusi perlu membentuk membuat program belajar bersama/kelompok supaya mengurangi jumlah angka mahasiswa yang remedial dan tim konselor atau mentor akademik yang secara proaktif mendampingi mahasiswa dengan GPA rendah (kategori 0–1), karena kelompok ini merupakan yang paling rentan mengalami dropout berdasarkan hasil analisis data.

- Memberikan opsi keringanan pembayaran atau beasiswa
Mengingat status pembayaran uang kuliah menjadi salah satu faktor utama dropout, institusi disarankan untuk memperluas akses beasiswa, cicilan uang kuliah, atau program keringanan biaya bagi mahasiswa yang mengalami kesulitan finansial. Identifikasi mahasiswa yang menunggak pembayaran harus dilakukan lebih awal agar bantuan dapat diberikan tepat waktu.