# pandas
pandas adalah alat analisis dan manipulasi data open source yang cepat, kuat, fleksibel, dan mudah digunakan, dibangun di atas bahasa pemrograman Python.

## install pandas
### Instruksi instalasi

Langkah selanjutnya memberikan cara termudah dan direkomendasikan untuk menyiapkan lingkungan Anda untuk menggunakan panda. Pilihan instalasi lainnya dapat ditemukan di halaman instalasi lanjutan.

1. Unduh Anaconda untuk sistem operasi Anda dan versi Python terbaru, jalankan penginstal, dan ikuti langkah-langkahnya. Tolong dicatat:
* Tidak diperlukan (dan tidak disarankan) untuk menginstal Anaconda sebagai root atau administrator.
* Ketika ditanya apakah Anda ingin menginisialisasi Anaconda3, jawab ya.
* Mulai ulang terminal setelah menyelesaikan instalasi.

Petunjuk rinci tentang cara menginstal Anaconda dapat ditemukan di dokumentasi Anaconda.

2. Di prompt Anaconda (atau terminal di Linux atau MacOS), mulai JupyterLab.

3. Di JupyterLab, buat buku catatan (Python 3) baru.

4. Di sel pertama Notebook.

### Installing with Anaconda

Memasang panda dan tumpukan NumPy dan SciPy lainnya bisa sedikit sulit bagi pengguna yang tidak berpengalaman.

Cara paling sederhana untuk menginstal tidak hanya panda, tetapi Python dan paket paling populer yang membentuk tumpukan SciPy ( IPython , NumPy , Matplotlib , ...) adalah dengan Anaconda , distribusi Python lintas platform (Linux, macOS, Windows) untuk data analitik dan komputasi ilmiah.

Setelah menjalankan penginstal, pengguna akan memiliki akses ke panda dan tumpukan SciPy lainnya tanpa perlu menginstal apa pun, dan tanpa perlu menunggu perangkat lunak apa pun dikompilasi.

Keuntungan lain menginstal Anaconda adalah Anda tidak memerlukan hak admin untuk menginstalnya. Anaconda dapat menginstal di direktori home pengguna, yang membuatnya sepele untuk menghapus Anaconda jika Anda memutuskan (hapus saja folder itu).

pandas adalah bagian dari distribusi Anaconda dan dapat diinstal dengan Anaconda atau Miniconda:

conda install pandas

atau pandas dapat diinstal melalui pip dari PyPI.

pip install pandas

## Package overview
pandas adalah paket Python yang menyediakan struktur data yang cepat, fleksibel, dan ekspresif yang dirancang untuk membuat bekerja dengan data "relasional" atau "berlabel" menjadi mudah dan intuitif. Ini bertujuan untuk menjadi blok bangunan tingkat tinggi yang mendasar untuk melakukan analisis data dunia nyata yang praktis dengan Python. Selain itu, ia memiliki tujuan yang lebih luas untuk menjadi alat analisis/manipulasi data open source yang paling kuat dan fleksibel yang tersedia dalam bahasa apa pun. Ini sudah berjalan dengan baik menuju tujuan ini.

panda sangat cocok untuk berbagai jenis data:

* Data tabular dengan kolom yang diketik secara heterogen, seperti dalam tabel SQL atau spreadsheet Excel
* Data deret waktu berurutan dan tidak berurutan (belum tentu frekuensi tetap).
* Data matriks arbitrer (diketik secara homogen atau heterogen) dengan label baris dan kolom
* Bentuk lain dari kumpulan data observasional/statistik. Data tidak perlu diberi label sama sekali untuk ditempatkan ke dalam struktur data pandas

Dua struktur data utama panda, Series (1-dimensi) dan DataFrame (2-dimensi), menangani sebagian besar kasus penggunaan tipikal di bidang keuangan, statistik, ilmu sosial, dan banyak bidang teknik. Untuk pengguna R, DataFrame berikan semua yang disediakan R data.frame dan banyak lagi. pandas dibangun di atas NumPy dan dimaksudkan untuk berintegrasi dengan baik dalam lingkungan komputasi ilmiah dengan banyak perpustakaan pihak ke-3 lainnya.

Berikut adalah beberapa hal yang dilakukan panda dengan baik:

* Penanganan data yang hilang dengan mudah (direpresentasikan sebagai NaN) dalam data floating point maupun non-floating point.
* Perubahan ukuran: kolom dapat dimasukkan dan dihapus dari DataFrame dan objek dimensi yang lebih tinggi.
* Penyelarasan data otomatis dan eksplisit : objek dapat secara eksplisit disejajarkan dengan sekumpulan label, atau pengguna dapat mengabaikan label dan membiarkan Series, DataFrame, dll. secara otomatis menyelaraskan data untuk Anda dalam perhitungan.
* Grup yang kuat dan fleksibel berdasarkan fungsionalitas untuk melakukan operasi split-apply-combine pada kumpulan data, baik untuk menggabungkan dan mengubah data.
* Permudah untuk mengonversi data yang tidak rata dan diindeks secara berbeda dalam struktur data Python dan NumPy lainnya menjadi objek DataFrame.
* Pengirisan berbasis label yang cerdas , pengindeksan mewah , dan subset dari kumpulan data besar.
* Menggabungkan dan menggabungkan kumpulan data secara intuitif.
* Membentuk kembali dan memutar set data secara fleksibel.
* Pelabelan hierarkis sumbu (mungkin memiliki beberapa label per centang).
* Alat IO yang kuat untuk memuat data dari file datar (CSV dan dibatasi), file Excel, database, dan menyimpan / memuat data dari format HDF5 ultrafast.
* Fungsionalitas khusus deret waktu : pembuatan rentang tanggal dan konversi frekuensi, statistik jendela bergerak, pergeseran tanggal, dan kelambatan.

Banyak dari prinsip-prinsip ini di sini untuk mengatasi kekurangan yang sering dialami menggunakan bahasa lain / lingkungan penelitian ilmiah. Untuk ilmuwan data, bekerja dengan data biasanya dibagi menjadi beberapa tahap: munging dan membersihkan data, menganalisis / memodelkannya, kemudian mengatur hasil analisis ke dalam bentuk yang cocok untuk plotting atau tampilan tabel. pandas adalah alat yang ideal untuk semua tugas ini.

Beberapa catatan lainnya

* panda cepat. Banyak bit algoritmik tingkat rendah telah diubah secara ekstensif dalam kode Cython . Namun, seperti hal lain, generalisasi biasanya mengorbankan kinerja. Jadi, jika Anda berfokus pada satu fitur untuk aplikasi Anda, Anda mungkin dapat membuat alat khusus yang lebih cepat.
* pandas adalah ketergantungan statsmodels , menjadikannya bagian penting dari ekosistem komputasi statistik di Python.
* panda telah digunakan secara luas dalam produksi dalam aplikasi keuangan.

## Perintah yang ada pada pandas :

* Fungsi shape() digunakan untuk melihat berapa banyak baris dan kolom pada dataframe

* Informasi statistik untuk setiap kolom seperti nilai minimum, nilai maksimum, standar deviasi, rata-rata dan sebagainya, dapat ditampilkan dengan mengikuti perintah berikut df.describe(include='all')

* Untuk mendapatkan informasi kolom, datatype dan informasi struktur lainnya menggunakan perintah df.info()

* Untuk melihat jumlah data pada setiap kolom menggunakan perintah count() df.count()

* Fungsi sample() pada Pandas dapat digunakan jika kita ingin menampilkan data secara acak. df.sample(5)

* Jika ingin menampilkan seluruh data yang ada pada dataframe. df

* Penggunaan fungsi tail() sama seperti fungsi head() yang membedakannya hanya outputnya saja, fungsi tail() hanya untuk melihat data terakhir dari dataframe df.tail()