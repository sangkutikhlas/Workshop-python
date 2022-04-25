# 12. Virtual Environments and Packages
## 12.1. Introduction (Pengantar)
Aplikasi Python akan sering menggunakan package dan modul yang bukan bagian dari daftar pustaka dari python. Aplikasi kadang-kadang membutuhkan versi pustaka tertentu, karena aplikasi mungkin mensyaratkan bug tertentu telah diperbaiki atau aplikasi dapat ditulis menggunakan versi usang dari antarmuka pustaka.

Ini berarti tidak mungkin bagi satu instansi Python untuk memenuhi persyaratan setiap aplikasi. Jika aplikasi A membutuhkan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka persyaratannya bertentangan dan menginstal versi 1.0 atau 2.0 akan membuat satu aplikasi tidak dapat berjalan.

Solusi dari masalah ini adalah membuat virtual environment, sebuah struktur direktori mandiri yang berisi instalasi Python untuk versi tertentu dari Python, serta sejumlah paket tambahan. Aplikasi yang berbeda kemudian dapat menggunakan lingkungan virtual yang berbeda. Untuk menyelesaikan contoh sebelumnya dari persyaratan yang saling bertentangan, aplikasi A dapat memiliki lingkungan virtual sendiri dengan versi 1.0 yang diinstal. Sementara aplikasi B memiliki lingkungan virtual yang lain yakni versi 2.0. Jika aplikasi B membutuhkan pustakan ditingkatkan ke versi 3.0, hal ini tidak akan mempengaruhi lingkungan aplikasi A.

# 12.2. Creating Virtual Environments (Menciptakan Lingkungan Virtual)
Modul yang digunakan untuk membuat dan mengelola lingkungan virtual disebut venv. venv biasanya akan menginstal versi Python terbaru yang kita miliki. Jika kita memiliki beberapa versi Python di sistem, kita dapat memilih versi Python tertentu dengan menjalankan python3 atau versi manapun yang kita inginkan.

Untuk membuat lingkungan virtual, tentukanlah direktori tempat kita ingin menyimpannya, dan jalankan modul venv sebagai script dengan jalur direktori:

```python
python3 -m venv tutorial-env
```

Hal ini akan membuat direktori tutorial-env jika tidak ada, dan juga membuat direktori di dalamnya yang berisi salinan interpreter Python dan berbagai file pendukung.

Lokasi direktori yang umum dipakai untuk lingkungan virtual adalah .venv Nama ini membuat direktori biasanya tersembunyi di shell kita dan berikan nama yang menjelaskan mengapa direktori itu ada. Hal ini juga mencegah bentrok dengan berkas definisi variabel lingkungan .env yang didukung beberapa peralatan.

di Windows, operasikan:

```python
tutorial-env\Scripts\activate.bat
```

pada Unic atau MacOS, operasikan:

```python
source tutorial-env/bin/activate
```

(Skrip ini ditulis untuk bash shell. Jika Anda menggunakan csh atau fish shells, ada pilihan skrip activate.csh dan activate.fish alternatif yang dapat Anda gunakan.)

Mengatifkan lingkungan virtual akan mengubah promt shell kita untuk menunjukan lingkungan virtual apa yang kita gunakan, dan memodifikasi lingkungan sehingga menjalankan python akan membuat kita mendapatkan versi dan instalasi Python tertentu. Sebagai contoh:

```python
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```

## 12.3. Managing Packages with pip (Mengelola Paket dengan pip)
Kita dapat menginstal, mengupgrade, dan menghapus paket menggunakan program yang disebut dengan pip. Secara bawaan pip akan menginstal package dari Python Package Index. Kita dapat menelusuri Python Package Index dengan membuka browser web.

pip memiliki sejumlah sub-perintah "install", "uninstall", "freeze", dls. (Konsultasikan ke panduan Memasang Modul-modul Python untuk dokumentasi lengkap dari pip.)

Kita dapat menginstal versi terbaru dari suatu package dengan menyebutkan nama suatu package.

```python
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

Kita dapat menginstal versi spesifik suatu package dengan memberikan nama package diikuti dengan == dan nomor versi.

```python
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
```

Jika kita menjalankan kembali perintah tersebut, pip akan melihat bahwa versi yang diminta sudah diinstal dan tidak melakukan apa-apa. Kita dapat memberikan nomor versi yang berbeda untuk mendapatkan versi tersebut. Selain itu kita bisa dapat menjalankan pip install --upgrade untuk meningkatkan package ke versi terbaru:

```python
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```

pip uninstall diikuti oleh satu atau beberapa nama paket akan menghapus paket-paket dari lingkungan virtual.

pip show akan menampilkan informasi tentang paket tertentu:

```python
(tutorial-env) $ pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```

pip list akan menampilkan semua paket yang diinstal di lingkungan virtual:

```python
(tutorial-env) $ pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

pip freeze akan menghasilkan daftar yang sama dari paket yang diinstal, tetapi keluarannya menggunakan format yang diharapkan oleh pip install. Sebuah konvensi yang umum digunakan adalah meletakkan daftar ini dalam file requirements.txt:

```python
(tutorial-env) $ pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```

requirements.txt kemudian dapat dikirimkan atau commit ke sistem kontrol versi dan dikirim sebagai bagian dari aplikasi. Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan install -r:

```python
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```

# Conda
Package, Dependency, and environment management untuk bahasa apapun seperti Python, R, Ruby, Lua, Scala, Java, Javascript, C/C++, dan FORTRAN

Conda adalah sistem manajemen package sumber terbuka dan sistem manajemen lingkungan yang berjalan di Windows, MacOS, dan Linux. Conda dengan cepat menginstal, menjalankan, dan memperbarui package dan dependensinya.

Conda dengan mudah membuat, menyimpan, memuat, dan beralih antar lingkungan di komputer lokal kita. Hal ini dibuat untuk program Python tetapi dapat mengemas dan mendistribusikan perangkat lunak untuk bahasa apapun.

Conda sebagai package manager membantu kita dalam menemukan dan menginstal package. jika memerlukan package yang memerlukan versi Python yang berbeda, kita tidak perlu beralih ke pengelola lingkungan lain karena konda juga merupakan pengelola lingkungan.

Hanya dengan beberapa perintah, kita dapat mengatur lingkungan yang benar-benar terpisah untuk menjalankan versi Python yang berbeda, sambil terus menjalankan versi Python kita yang biasa di lingkungan normal kita.

Dalam konfigurasi default, conda dapat menginstal dan mengelola lebih dari 7.500 package yang dibuat, ditinjau, dan dikelola oleh Anaconda. Conda juga dapat dikombinasikan dengan sistem integrasi berkelanjutan seperti Travis CI dan AppVeyor untuk menyediakan pengujian kode kita yang sering kita buat dan secara otomatis.

Package conda dan environment manager disertakan dalam semua versi Anaconda, Miniconda, dan Anaconda Repository. Conda juga disertakan dalam Anaconda Enterprise, yang menyediakan package perusahaan di tempat dan manajemen lingkungan untuk Python, R, Nodejs, Java, dan aplikasi stack lainnya.

# Concepts
## Conda Command

Perintah conda adalah antarmuka utama untuk mengelola instalasi berbagai package. Dapat berupa:

* Kueri dan mencari indeks package Anaconda dan instalasi Anaconda saat ini.
* Buat lingkungan conda baru.
* Install dan perbarui package ke lingkungan conda yang ada.
Catatan:

Kita dapat menyingkat banyak opsi yang sering digunakan yang didahului oleh 2 tanda hubung (--) menjadi hanya 1 tanda hubung dan huruf pertama dari opsi tersebut. jadi --name dan -n adalah sama, dan --envs dan -e juga sama

## Conda Package

Package conda adalah file terball terkompresi (.tar.bz2) atau file .conda yang berisi:

* perpustakaan tingkat sistem.
* Python atau modul lainnya.
* Program yang dapat dieksekusi dan komponen lainnya
* Metadata di bawah info/direktori.
* Kumpulan file yang diinstal langsung menjadi install awalan.
* Conda melacak ketergantungan antara package dan platform. Format package conda identik di seluruh platform dan sistem operasi.

Merupakan file saja, termasuk tautan simbolik yang merupakan bagian dari package conda. Direktori dapat dibuat dan dihapus sesuai kebutuhan. Namun, kita tidak dapat membuat direktori kosong dari arsip tar secara langsung.

# Format file .conda

Format file .conda diperkenalkan di conda 4.7 sebagai alternatif tarball yang lebih ringkas, dan dengan demikian lebih cepat.

Format file .conda terdiri dari wadah format ZIP luar yang tidak terkompresi, dengan 2 file .tar terkompresi dalam.

Untuk dukungan format kompresi internal awal format .conda, kami memilih Zstandard (zstd). Sebenarnya format kompresi yang digunakan tidak masalah, selama format tersebut didukung oleh libarchive. Format kompresi dapat berubah di masa mendatang karena algoritme kompresi yang lebih maju sedang dikembangkan dan tidak diperlukan perubahan pada format .conda. Hanya libarchive yang diperbarui yang diperlukan untuk menambahkan format kompresi baru ke file .conda.

File terkompresi ini bisa jauh lebih kecil daripada yang setara dengan bzip2. Selain itu, mereka melakukan dekompresi lebih cepat. .conda adalah format file yang lebih disukai untuk digunakan jika tersedia, meskipun kami terus menyediakan file .tar.bz2 secara bersamaan.

## Cara menggunakan Package
* kita dapat mencari package
```python
conda search scipy
```

* kita dapat mnginstal sebuah package
```python
conda install scipy
```

* Kida dapat membuat package setelah kita menginstal conda-build
```python
conda build my_fun_package
```

## Structure Package
.
├── bin
│   └── pyflakes
├── info
│   ├── LICENSE.txt
│   ├── files
│   ├── index.json
│   ├── paths.json
│   └── recipe
└── lib
    └── python3.5

* bin berisi binari yang relevan untuk paket tersebut.
* lib berisi file perpustakaan yang relevan (mis. file .py).
* info berisi metadata paket.

## Meta Package

Ketika paket conda digunakan untuk metadata saja dan tidak berisi file apa pun, itu disebut sebagai metapackage. Metapackage mungkin berisi dependensi ke beberapa inti, perpustakaan tingkat rendah dan dapat berisi tautan ke file perangkat lunak yang diunduh secara otomatis saat dijalankan. Metapackages digunakan untuk menangkap metadata dan membuat spesifikasi paket yang rumit menjadi lebih sederhana.

```python
Paket meta Anaconda
```

Metapackage Anaconda digunakan dalam pembuatan installer Anaconda Distribution sehingga mereka memiliki satu set paket yang terkait dengannya. Setiap rilis penginstal memiliki nomor versi, yang sesuai dengan kumpulan paket tertentu pada versi tertentu. Kumpulan paket pada versi tertentu dienkapsulasi dalam metapackage Anaconda.

Metapackage Anaconda berisi beberapa inti, perpustakaan tingkat rendah, termasuk kompresi, enkripsi, aljabar linier, dan beberapa perpustakaan GUI.

```python
Paket meta mutex
```

Metapackage mutex adalah paket yang sangat sederhana yang memiliki nama. Itu tidak perlu memiliki dependensi atau membangun langkah. Metapackage mutex sering kali merupakan "output" dalam resep yang membangun beberapa varian dari paket lain. Metapackages Mutex berfungsi sebagai alat untuk membantu mencapai eksklusivitas timbal balik di antara paket-paket dengan nama yang berbeda.

```python
Paket Noarch
```

Paket Noarch adalah paket yang tidak spesifik arsitektur dan oleh karena itu hanya perlu dibangun sekali. Paket Noarch bersifat generik atau Python. Paket generik Noarch memungkinkan pengguna untuk mendistribusikan dokumen, kumpulan data, dan kode sumber dalam paket conda. Paket Noarch Python dijelaskan di bawah ini.

Mendeklarasikan paket-paket ini seperti noarch di build bagian meta.yaml pengurangan sumber daya CI bersama. Oleh karena itu, semua paket yang memenuhi syarat untuk menjadi paket noarch harus dinyatakan demikian.

```python
Python Noarch
```

Arahan di bagian build membuat paket-paket Python murni yang hanya perlu dibangun sekali .noarch: python

Paket Noarch Python mengurangi biaya pembuatan beberapa paket Python murni yang berbeda pada arsitektur dan versi Python yang berbeda dengan memilah platform dan perbedaan spesifik versi Python pada waktu penginstalan.

Untuk memenuhi syarat sebagai paket Python noarch, semua kriteria berikut harus dipenuhi:

* Tidak ada skrip pasca-tautan, pra-tautan, atau pra-pembatalan tautan.
* Tidak ada skrip build khusus OS.
* Tidak ada persyaratan khusus versi Python.
* Tidak ada lompatan kecuali untuk versi Python. Jika resepnya hanya py3, hapus pernyataan lewati dan tambahkan batasan versi pada Python di bagian host dan jalankan.
* 2to3 tidak digunakan.
* Argumen skrip di setup.py tidak digunakan.
* Jika console_scripttitik masuk ada di setup.py, mereka terdaftar di meta.yaml.
* Tidak mengaktifkan skrip.
* Bukan ketergantungan conda.

## Getting started with conda
Conda adalah pengelola paket dan pengelola lingkungan andal yang Anda gunakan dengan perintah baris perintah di Anaconda Prompt untuk Windows, atau di jendela terminal untuk macOS atau Linux.

Di Windows, semua perintah di bawah ini diketik ke jendela Anaconda Prompt.

## MacOS

* Buka Launchpad, lalu klik ikon terminal.
Di macOS, semua perintah di bawah ini diketik ke jendela terminal.

## Linux

* Buka jendela terminal.
Di Linux, semua perintah di bawah ini diketik ke jendela terminal.

## Mengelola Conda
Verifikasi bahwa conda diinstall dan berjalan di sistem kita dengan mengetik:

```python
conda --version
```

Conda menampilkan nomor version yang telah kita install. Kita tidak perlu menavigasi ke direktori Anaconda.

Contoh: conda 4.7.12

Catatan: Jika kita mendapatkan pesan kesalahan, pastikan kita menutup dan membuka kembali jendela terminal setelah menginstal, atau lakukan sekarang. Kemudian verifikasi bahwa kita masuk ke akun pengguna yang sama yang kita gunakan untuk menginstal Anaconda atau Miniconda.

Perbarui conda ke versi saat ini. Ketik berikut ini:
```python
conda update conda
```

Conda membadingkan versi dan kemudian menampilkan apa yang tersedia untuk diinstall.

Jika versi conda yang lebih baru tersedia, ketik y untuk memperbarui:

```python
Proceed ([y]/n)? y
```

# Mengelola Lingkungan
Conda memungkinkan kita membuat lingkungan terpisah yang berisi file, paket, dan dependensinya yang tidak akan berinteraksi dengan lingkungan lain.

Saat kita mulai menggunakan conda, kita sudah memiliki lingkungan default bernama base. Kita tidak ingin memasukkan program ke dalam lingkungan dasar kita. Buat lingkungan terpisah untuk menjaga program kita tetap terisolasi satu sama lain.

1. Buat lingkungan baru dan install package di dalamnya
Kita akan memberi nama lingkungan snowflakes dan menginstal package BioPython. Di Anaconda Promt atau di jendela terminal kita, ketikkan yang berikut ini:

```python
conda create --name snowflakes biopython
```

Conda memeriksa untuk melihat package tambahan ("dependensi") apa yang dib utuhkan BioPython, dan menanyakan apakah kita ingin melanjutkan:
```python
Proceed ([y]/n)? y
```

Ketik y dan tekan Enter untuk melanjutkan.

2. Untuk menggunakan, atau mengaktifkan lingkungan baru, ketik berikut ini:
* Windows: conda activate snowflakes
* macOS dan Linux: conda activate snowflakes

Catatan: conda activate hanya berfungsi pada conda 4.6 dan versi terbaru

3. untuk melihat dafatar semua lingkungan kita, ketik:

```python
conda info -e
```

Daftar lingkungan muncul, mirip dengan berikut ini:

```python
conda environments:

    base           /home/username/Anaconda3
    snowflakes   * /home/username/Anaconda3/envs/snowflakes
Catatan: Lingkungan atau Environment yang aktif dengan tanda bintang (*).
```

4. Ubah lingkungan saat ini kembali ke default (basis): conda activate

# Mengelola Python
Saat kita membuat lingkungan baru, conda menginstal versi Python yang sama dengan yang kita gunakan saat mengunduh dan menginstal Anaconda. Jika kita ingin menggunakan versi Python yang berbeda, misalnya Python 3.5, cukup buat lingkungan baru dan tentukan versi Python yang kita inginkan.

1. Buat lingkungan baru bernama snakes yang berisi Python 3.9:

```python
conda create --name snakes python=3.9
```

Ketika conda bertanya kita ingin melanjutkan, ketik y dan tekan Enter.

2. Aktifkan lingkungan baru:
* Windows:
```python
conda activate snakes
```

* macOS dan Linux:

```python
conda activate snakes
```

3. Varifikasi bahwa lingkungan snakes telah ditambahkan dan aktif:

```python
conda info --envs
```

Conda menampilkan daftar semua lingkungan dengan tanda bintang (*) setelah nama lingkungan aktif:

```python
# conda environments:
#
base                     /home/username/anaconda3
snakes                *  /home/username/anaconda3/envs/snakes
snowflakes               /home/username/anaconda3/envs/snowflakes
```

Lingkungan aktif juga ditampilkan di depan prompt kita di () atau [] seperti berikut:

```python
(snakes) $
```

4. Verifikasi versi Python mana yang ada di lingkungan kita saat ini:

```python
python --version
```

5. Nonaktifkan lingkungan snakes dan kembali ke lingkungan dasar: conda activate

# Mengelola Package
Di bagian ini, kita memeriksa package yang telah kita install, memeriksa mana yang tersedia dan mencari package tertentu dan menginstalnya.

1. Untuk menemukan paket yang telah Kita instal, aktifkan terlebih dahulu lingkungan yang ingin Kita cari. Lihat di atas untuk perintah untuk mengaktifkan lingkungan ular Kita .

2. Periksa untuk melihat apakah paket yang belum Kita instal bernama "beautifulsoup4" tersedia dari repositori Anaconda (harus terhubung ke Internet):

```python
conda search beautifulsoup4
```

Conda meampilkan daftar semua package dengan nama itu di repostory Anaconda.

3. Install package ini ke lingkungan saat ini:

```python
conda install beautifulsoup4
```

4. Periksa untuk melihat apakah program yang baru diinstall ada di lingkungan ini:

```python
conda list
```