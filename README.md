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

Dashboard Students Performance memberikan gambaran menyeluruh mengenai kondisi akademik mahasiswa serta tingkat risiko dropout di institusi. Dari total 4.424 mahasiswa, sekitar 49,93% berhasil lulus, sementara 32,12% mengalami dropout, yang menunjukkan bahwa hampir sepertiga mahasiswa tidak menyelesaikan studinya. Selain itu, terdapat 1.621 mahasiswa yang teridentifikasi sebagai at-risk students, sehingga menjadi fokus utama untuk dilakukan intervensi lebih lanjut. Meskipun rata-rata GPA berada di angka 3,15 yang tergolong baik, tingginya angka dropout mengindikasikan bahwa faktor penyebab tidak hanya berasal dari performa akademik, tetapi juga kemungkinan dipengaruhi oleh faktor lain seperti kondisi finansial atau sosial.

Distribusi status mahasiswa memperlihatkan bahwa proporsi dropout cukup signifikan dibandingkan mahasiswa yang masih terdaftar. Berdasarkan gender, baik mahasiswa laki-laki maupun perempuan menunjukkan pola dropout yang relatif seimbang, sehingga gender bukan menjadi faktor utama. Sementara itu, dari sisi status pernikahan, mayoritas dropout berasal dari mahasiswa dengan status single, yang sejalan dengan dominasi populasi mahasiswa secara umum. Analisis lebih lanjut pada tingkat program studi menunjukkan bahwa beberapa jurusan seperti Management, Nursing, dan Journalism memiliki angka dropout yang lebih tinggi dibandingkan jurusan lainnya, sehingga perlu perhatian khusus dari institusi.

Di sisi lain, distribusi GPA menunjukkan bahwa sebagian besar mahasiswa berada pada kategori nilai tinggi (3–4), yang memperkuat indikasi bahwa dropout tidak selalu terjadi pada mahasiswa dengan performa akademik rendah. Hal ini menegaskan pentingnya pendekatan yang lebih komprehensif dalam menangani permasalahan dropout.

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

Kesimpulan dari proyek Students Performance di Jaya Jaya Institut menunjukkan bahwa permasalahan tingginya angka dropout merupakan isu yang signifikan dan memerlukan penanganan berbasis data. Dari hasil analisis dan visualisasi dashboard, diketahui bahwa sekitar sepertiga mahasiswa tidak berhasil menyelesaikan studinya, meskipun secara umum rata-rata performa akademik tergolong baik. Hal ini menegaskan bahwa faktor penyebab dropout tidak hanya dipengaruhi oleh nilai akademik, tetapi juga melibatkan aspek lain seperti kondisi finansial, beban studi, serta karakteristik individu mahasiswa.

Melalui proses analisis data dan pemodelan machine learning, proyek ini berhasil mengidentifikasi pola serta faktor-faktor yang berkontribusi terhadap risiko dropout, seperti jumlah mata kuliah yang tidak lulus, performa di semester awal, dan kemungkinan kendala ekonomi. Selain itu, ditemukan bahwa beberapa program studi memiliki tingkat dropout yang lebih tinggi dibandingkan yang lain, sehingga membutuhkan perhatian khusus. Model yang dibangun juga mampu mengklasifikasikan mahasiswa ke dalam kategori dropout, enrolled, dan graduate, sehingga dapat digunakan sebagai dasar dalam pengambilan keputusan.

Secara keseluruhan, proyek ini memberikan nilai tambah bagi institusi dengan menyediakan sistem prediksi dini (early warning system) untuk mengidentifikasi mahasiswa yang berisiko dropout. Dengan adanya sistem ini, pihak kampus dapat melakukan intervensi secara lebih cepat dan tepat sasaran, seperti memberikan bimbingan akademik, dukungan finansial, atau pendampingan khusus. Implementasi solusi ini diharapkan dapat menurunkan angka dropout, meningkatkan tingkat kelulusan, serta mendukung pengambilan keputusan yang lebih efektif dan berbasis data di Jaya Jaya Institut.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan guna mengurangi mahasiswa mahasiswa dropout.

- Mahasiswa dengan nilai rendah atau banyak mata kuliah tidak lulus perlu diberikan bimbingan khusus
- Program remedial atau mentoring akademik harus difokuskan pada semester awal
- Mengidentifikasi mahasiswa dengan tunggakan lebih awal
- Memberikan opsi keringanan pembayaran atau beasiswa
- Lakukan evaluasi pada jurusan dengan tingkat dropout tinggi
- Tinjau ulang kurikulum dan beban akademik
- Sesuaikan metode pembelajaran dengan kebutuhan mahasiswa