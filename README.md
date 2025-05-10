# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding (Pemahaman Bisnis)

Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000. Selama lebih dari dua dekade, institut ini telah berhasil mencetak banyak lulusan dengan reputasi yang sangat baik di dunia kerja. Keberhasilan ini menunjukkan komitmen Jaya Jaya Institut terhadap kualitas pendidikan dan pengembangan sumber daya manusia. Sebagai lembaga pendidikan, tujuan utama Jaya Jaya Institut adalah menyelenggarakan proses pembelajaran yang efektif dan efisien, serta memastikan keberhasilan mahasiswa dalam menyelesaikan studinya. Reputasi dan keberlanjutan institusi sangat bergantung pada kemampuannya untuk menghasilkan lulusan berkualitas dan mempertahankan tingkat kelulusan yang optimal.

## Permasalahan Bisnis (Business Problems)

Meskipun memiliki rekam jejak yang baik dalam menghasilkan lulusan berkualitas, Jaya Jaya Institut menghadapi tantangan signifikan terkait tingginya angka mahasiswa yang tidak menyelesaikan pendidikannya atau mengalami _dropout_. Permasalahan ini membawa dampak negatif bagi institusi dalam beberapa aspek:

-   **Reputasi Institusi:** Tingkat _dropout_ yang tinggi dapat mempengaruhi persepsi publik dan calon mahasiswa terhadap kualitas dan efektivitas program pendidikan yang ditawarkan oleh Jaya Jaya Institut.
-   **Efisiensi Sumber Daya:** Mahasiswa yang _dropout_ merepresentasikan investasi sumber daya (waktu dosen, fasilitas, biaya operasional) yang tidak menghasilkan output yang diharapkan (lulusan).
-   **Perencanaan Akademik dan Keuangan:** Fluktuasi jumlah mahasiswa aktif akibat _dropout_ dapat menyulitkan perencanaan akademik jangka panjang dan stabilitas keuangan institusi.
-   **Dampak Sosial:** Kegagalan mahasiswa dalam menyelesaikan pendidikan dapat berdampak pada individu mahasiswa tersebut dan kontribusi mereka kepada masyarakat.

Oleh karena itu, Jaya Jaya Institut memiliki kebutuhan mendesak untuk:

1.  **Mengidentifikasi Faktor-faktor Penyebab Dropout:** Memahami akar permasalahan mengapa banyak mahasiswa tidak menyelesaikan pendidikannya.
2.  **Mendeteksi Mahasiswa Berpotensi Dropout Secara Dini:** Mengembangkan mekanisme untuk mengidentifikasi mahasiswa yang menunjukkan tanda-tanda akan _dropout_ secepat mungkin.
3.  **Memberikan Intervensi yang Tepat:** Dengan deteksi dini, institusi dapat memberikan bimbingan atau dukungan khusus kepada mahasiswa yang berisiko untuk mencegah terjadinya _dropout_.
4.  **Meningkatkan Pemahaman Data dan Monitoring Kinerja Mahasiswa:** Membutuhkan alat bantu yang memudahkan pihak manajemen dalam memahami tren data mahasiswa dan memonitor performa akademik secara berkelanjutan.

## Cakupan Proyek (Project Scope)

Untuk membantu Jaya Jaya Institut dalam mengatasi permasalahan tingginya angka _dropout_, proyek ini akan mencakup beberapa hal berikut:

1.  **Analisis Data Mahasiswa:**
    
    -   Melakukan pembersihan data (_data cleaning_) dan pra-pemrosesan (_data preprocessing_) pada dataset "students' performance" yang disediakan.
    -   Melakukan analisis data eksploratif (_Exploratory Data Analysis_ - EDA) untuk mengidentifikasi pola, tren, dan karakteristik mahasiswa yang _dropout_ dibandingkan dengan yang tidak.
    -   Mengidentifikasi fitur-fitur (variabel) kunci dari dataset yang paling berpengaruh terhadap kecenderungan mahasiswa untuk _dropout_.
2.  **Pengembangan Model Prediksi Dropout:**
    
    -   Merancang dan mengembangkan model _machine learning_ yang mampu memprediksi probabilitas seorang mahasiswa untuk _dropout_.
    -   Fokus model adalah pada deteksi dini, idealnya menggunakan data yang tersedia pada semester-semester awal perkuliahan (berdasarkan data semester pertama yang ada di dataset).
    -   Melakukan evaluasi terhadap performa model yang dikembangkan untuk memastikan akurasi dan reliabilitasnya.
3.  **Pembuatan Dashboard Monitoring Kinerja Mahasiswa:**
    
    -   Merancang dan mengembangkan _dashboard_ interaktif yang memvisualisasikan data mahasiswa dan hasil prediksi model.
    -   _Dashboard_ ini bertujuan untuk memberikan kemudahan bagi manajemen Jaya Jaya Institut dalam:
        -   Memahami profil mahasiswa secara keseluruhan.
        -   Memonitor tren performa akademik mahasiswa.
        -   Mengidentifikasi mahasiswa atau kelompok mahasiswa yang berisiko tinggi _dropout_ berdasarkan output model.
        -   Mendukung pengambilan keputusan berbasis data terkait strategi intervensi dan peningkatan kualitas layanan pendidikan.

**Batasan Proyek (Out of Scope):**

-   Proyek ini **tidak** mencakup implementasi langsung program intervensi atau bimbingan khusus bagi mahasiswa yang teridentifikasi berisiko _dropout_. Fokus utama adalah pada penyediaan alat analisis dan sistem deteksi.
-   Proyek ini **tidak** mencakup pengumpulan data baru di luar dataset "students' performance" yang telah disediakan, kecuali jika ada kesepakatan lebih lanjut.
-   Proyek ini **tidak** secara langsung melakukan perubahan kebijakan akademik atau administratif di Jaya Jaya Institut, namun hasil analisis dan model dapat menjadi dasar rekomendasi.
-   Definisi operasional "dropout" akan didasarkan pada informasi yang dapat diekstrak atau diinterpretasikan dari dataset yang ada atau berdasarkan klarifikasi lebih lanjut dari Jaya Jaya Institut mengenai variabel target.

## Persiapan

