# 8. Error dan Exception
di Python, ada dua jenis error yaitu syntax error dan exceptions.

# 8.1. Syntax Error (Kesalahan pada Syntax)
Syntax Error adalah suatu keadaan saat kode python mengalami kesalahan penulisan. Python interpreter dapat mendeteksi kesalahan ini saat kode dieksekusi. Hal ini juga dikenal sebagai kesalahan penguraian parsing, mungkin merupakan jenis keluhan paling umum yang kita dapatkan ketika kita masih belajar Python:

```python
while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

Pengurai parser mengulangi baris yang menyinggung dan menampilkan arrow yang menunjuk pada tikik paling awal di baris di mana kesalahan terdeteksi. Kesalahan disebabkan oleh (atau setidaknya terdeteksi pada) token preceding. Dalam contoh, kesalahan terdeteksi pada fungsi print(), karena titik dua (:) yang hilang sebelum itu. Nama file dan nomor baris dicetak sehingga kita tahu ke mana harus mencari masukan yang berasal dari script.

# 8.2. Pengecualian (Exceptions)
Exception adalah suatu keadaan saat penulisan syntax sudah benar, namun kesalahan terjadi karena syntax tidak bisa dijalankan, melainkan karena adanya kesalahan matematika, kesalahan nama function, library, dan lainnya. Bahkan jika pernyataan atau ungkapan secara sintaksis benar, itu dapat menyebabkan kesalahan ketika suatu usaha dilakukan untuk mengeksekusinya. Namun, sebagian besar pengecualian tidak ditangani oleh program, dan menghasilka pesan kesalahan seperti contoh berikut:

```python
10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
'2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Dalam program tersebut, pada baris terakhir dari pesan kesalahan menunjukkan apa yang terjadi. Pengecualian ada berbagai jenis yang berbeda, dan tipe dicetak sebagai bagian dari pesan. Contohnya dalam program yakni ZeroDivisionError, NameError dan TypeError. String yang dicetak sebagai jenis pengecualian adalah nama pengecualian bawaan yang terjadi. Hal ini berlaku untuk semua jenis pengecualian bawaan, tetapi tidak harus sama untuk pengecualian yang dibuat pengguna. Nama pengecualian standar adalah pengindentifikasi bawaan (bukan kata kunci yang dipesan reserved keyword).

Kemudian mari kita bedah tentang contoh pengecualian dalam program di atas

* ZeroDivisonError adalah exception yang terjadi saat eksekusi program menghasilkan perhitungan matematika pembagian dengan angka nol.
* NameError adalah exception yang terjadi saat kode mengeksekusi terhadap local name atau global name yang tidak terdefinisi. Misalnya saat menjumlahkan variabel yang tidak didefinisikan, memanggil function yang tidak ada, dan lain-lain.
* TypeError adalah exception yang terjadi saat dilakukan eksekusi terhadap suatu operasi atau fungsi dengan tipe objek yang tidak sesuai.

Bagian pesan kesalahan sebelumnya menunjukkan konteks di mana pengecualian terjadi, dalam bentuk pelacakan balik tumpukan. Secara umum, ini berisi baris sumber daftar traceback stack; namun, itu tidak akan menampilkan baris yang dibaca dari input standar.

# 8.3. Menangani Pengecualian (Handling Exceptions)
Merupakan suatu mekanisme penanganan flow normal program karena terjadi exception dengan melanjutkan flow ke code block lainnya. Dimungkinkan untuk menuliskan program yang menangani pengecualian yang dipilih. Lihatlah contoh berikut, yang meminta masukan dari pengguna sampai integer yang valid telah dimasukkan, tetapi memungkinkan pengguna untuk menghentikan program (dengan menggunakan ctrl+C atau apapun yang didukung sistem operasi)

Perhatikan bahwa gangguan yang dibuat pengguna ditandai dengan munculnya pengecualian KeyboardInterrupt.

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
     except ValueError:
         print("Oops!  That was no valid number.  Try again...")
```

Pertanyaan try berfungsi sebagai berikut:

* Pertama, try clause (pernyataan-pernyataan) di antara kata kunci try dan except dieksekusi.
* Jika tidak ada pengecualian yang terjadi, except clause dilewati dan mengeksekusi pernyatan keyword try kemudian selesai.
* Jika pengecualian terjadi selama eksekusi try clause, sisa klausa akan dilewati. Kemudian, jika tipenya cocok dengan pengecualian yang dinamai kata kunci except, klausa except dijalankan, dan kemudian eksekusi dilanjutkan setelah blok continues atau except.
* Jika terjadi pengecualian yang tidak cocok dengan pengecualian yang disebutkan dalam except clause, hal itu akan diteruskan ke pernyataan percobaan luar; jika tidak ada penanganan yang ditemukan, hal tersebut adalah pengecualian yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.

Pernyataan try mungkin memiliki lebih dari satu except clause, untuk menentukan penanganan untuk pengecualian yang berbeda. Paling banyak satu handler akan dieksekusi. Handler hanya menangani pengecualian yang terjadi di klausa try yang sesuai, bukan di handler lain dari pernyataan try yang sama. Klausa pengecualian dapat menyebutkan beberapa pengecualian sebagai tuple dalam kurung, misalnya:

```python
except (RuntimeError, TypeError, NameError):
     pass
```

Kelas dalam except clause kompatibel dengan pengecualian jika itu adalah kelas yang sama atau kelas dasar daripada hal itu (tetapi tidak sebaliknya, except clause yang mencantumkan kelas turunan tidak kompatibel dengan kelas dasar). Misalnya, kode berikut akan mencetak B, C, D dalam urutan itu:

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

Perhatikan bahwa jika except clause dibalik (dengan kecuali B terlebih dahulu), itu akan mencetak B, B, B. Kemudian pencocokan pertama except clause dipicu.

Semua pengecualian mewarisi dari BaseException, sehingga dapat digunakan untuk berfungsi sebagai wildcard. Gunakan ini dengan sangat hati-hati, karena mudah untuk menutupi kesalahan pemrograman yang sebenarnya dengan cara ini! Itu juga dapat digunakan untuk mencetak pesan kesalahan dan kemudian menaikkan kembali pengecualian (memungkinkan penelepon untuk menangani pengecualian juga):

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

Sebagai alternatif, klausa pengecualian terakhir dapat menghilangkan nama pengecualian, namun nilai pengecualian kemudian harus diambil dari sys.exc_info()[1].

Pernyataan try ... except memiliki klausa else opsional, yang atau jika ada, harus mengikuti semua except clause. Berguna untuk kode yang harus dijalankan jika klausa try tidak memunculkan eksepsi. Sebagai contoh:

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

Penggunaan klausa else lebih baik daripada menambahkan kode tambahan ke klausa try karena menghindari secara tidak sengaja menangkap pengecualian yang tidak dimunculkan oleh kode yang dilindungi oleh pernyataan try ... :keyword: !except.

Ketika pengecualian terjadi, itu mungkin memiliki nilai terkait, juga dikenal sebagai argument pengecualian. Kehadiran dan jenis argumen tergantung pada jenis pengecualian.

Klausa except dapat menentukan variabel setelah nama pengecualian. Variabel terikat ke instance pengecualian dengan argumen yang disimpan di instance.args. Untuk kenyamanan, instance pengecualian mendefinisikan __str__() sehingga argumen dapat dicetak secara langsung tanpa harus merujuk ke .args. Seseorang juga dapat membuat instance pengecualian terlebih dahulu sebelum menaikkannya dan menambahkan atribut apa pun ke dalamnya seperti yang diinginkan.

```python
 try:
    raise Exception('spam', 'eggs')
 except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                          # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)

<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

Jika pengecualian memiliki argumen, mereka dicetak sebagai bagian terakhir (detail) dari pesan untuk pengecualian yang tidak ditangani. Pengendali pengecualian tidak hanya menangani pengecualian jika terjadi segera di klausa try, tetapi juga jika terjadi di dalam fungsi yang dipanggil (bahkan secara tidak langsung) dalam klausa try. Sebagai contoh:

```python
def this_fails():
     x = 1/0

 try:
     this_fails()
 except ZeroDivisionError as err:
     print('Handling run-time error:', err)

Handling run-time error: division by zero
```

# 8.4. Memunculkan Pengecualian (Raising Exceptions)
Pernyataan raise memungkinkan programmer untuk memaksa pengecualian yang ditentukan terjadi. Sebagai contoh:

```python
raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

Satu-satunya argumen untuk raise menunjukkan pengecualian dimunculkan. Hal ini harus berupa intance pengecualian atau kelas pengecualian (kelas yang berasal dari dari Exception). Jika kelas pengecualian dikirimkan, itu akan secara implisit diinstansiasi dengan memanggil pembangunnya constructor tanpa argumen:

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

Jika kita perlu menentukan apakah pengecualian muncul tetapi tidak bermaksud menanganinya, bentuk yang lebih sederhana dari pernyataan else memungkinkan kita untuk memunculkan kembali pengecualian:

```python
try:
     raise NameError('HiThere')
 except NameError:
     print('An exception flew by!')
     raise

An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

# 8.5. Exception Chaining
raise statement memungkinkan opsional yang memungkinkan pengecualian berantai. Sebagai contoh:

```python
# exc must be exception instance or None.
raise RuntimeError from exc
```

Ini bisa berguna saat kita mengubah pengecualian. Sebagai contoh:

```python
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

Rantai pengecualian terjadi secara otomatis ketika pengecualian dimunculkan di dalam sebuah except atau finally bagian. Ini dapat dinonaktifkan dengan menggunakan from None idiom:

```python
try:
    open('database.sqlite')
 except OSError:
    raise RuntimeError from None

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

# 8.6. Pengecualian yang Ditentukan Pengguna (User-defined Exceptions)
Program dapat memberi nama Exception mereka sendiri dengan membuat kelas Exception baru. Exception biasanya berasal dari kelas Exception, baik secara langsung atau tidak langsung.

Exception classes dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penanganan untuk Exception. Sebagian besar Exception didefinisikan dengan nama yang diakhiri dengan Error, mirip dengan penamaan Exception standar.

Banyak modul standar yang menentukan Exception mereka sendiri, untuk melaporkan kesalahan yang mungkin terjadi pada fungsi yang mereka tetapkan.

# 8.7. Mendefinisikan Tindakan Pembersihan (Defining Clean-up Actions)
Pernyataan try memiliki klausa opsional lain yang dimaksudkan untuk menentukan tindakan pembersihan yang harus dijalankan dalam semua keadaan. Sebagai contoh:

```python
try:
     raise KeyboardInterrupt
finally:
     print('Goodbye, world!')

Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```

Jika ada klausa finally, klausa untuk finally akan dijalankan sebagai tugas terakhir sebelum pernyataan try selesai. Klausa finally, dapat berjalan baik atau tidak apabila peryataan try menghasilkan suatu pengecualian atau Exception. Poin-poin berikut membahas kasus yang lebih kompleks saat Exception terjadi:

* Jika Exception terjadi selama eksekusi klausa untuk :keyword: !try, maka pengecualian tersebut dapat ditangani oleh klausa except. Jika pengecualian tidak ditangani oleh klausa :keyword: !except, maka pengecualian dimunculkan kembali setelah klausa finally dieksekusi.* Pengecualian dapat terjadi selama pelaksanaan klausa except atau else. Sekali lagi, pengecualian akan muncul kembali setelah klausa finally telah dieksekusi.
* Jika klausa last mengeksekusi pernyataan break, continue, atau return, exception tidak dimunculkan kembali.
* Jika pernyataan klausa untuk try mencapai klausa break, continue atau :keyword: return maka, pernyataan untuk klausa finally akan dieksekusi sebelum break, continue atau return dieksekusi.
* Jika klausa untuk :keyword:!finally telah menyertakan pernyataan return, nilai yang dikembalikan akan menjadi salah satu dari pernyataan untuk finally dan dari klausa return, bukan nilai dari try pernayataan untuk return.

Sebagai Contoh:

```python
def bool_return():
     try:
         return True
     finally:
         return False

bool_return()
False
```

Kemudian Contoh yang lebih rumit:

```python
def divide(x, y):
     try:
         result = x / y
     except ZeroDivisionError:
         print("division by zero!")
     else:
         print("result is", result)
     finally:
         print("executing finally clause")

>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

Seperti yang kita lihat, klausa finally dieksekusi dalam peristiwa apa pun. TypeError yang ditimbulkan dengan membagi dua string tidak ditangani oleh klausa except dan karenanya kembali muncul setelah klausa finally telah dieksekusi. Dalam aplikasi dunia nyata, klausa finally berguna untuk melepaskan sumber daya eksternal (seperti berkas atau koneksi jaringan), terlepas dari apakah penggunaan sumber daya tersebut berhasil.

# 8.8. Tindakan Pembersihan yang Sudah Ditentukan (Predefined Clean-up Actions)
Beberapa objek mendefinisikan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Sebagai contoh berikut yang mencoba membuka berkas dan mencetak ke layar:

```python
for line in open("myfile.txt"):
    print(line, end="")
```

dalam kode di atas terdapat masalah. Masalah dengan kode tersebut ialah membiarkan berkas terbuka untuk jumlah waktu yang tidak ditentukan setelah bagian kode tersebut selesai dieksekusi. Hal tersebut bukan merupakan masalah dalam script sederhana, tetapi bisa menjadi masalah untuk aplikasi yang lebih kompleks. Pernyataan with memungkinkan objek seperti berkas digunakan dengan cara yang memastikan mereka selalu dibersihkan secepatnya dan dengan benar. Seperti pada contoh:

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

Setelah pernyataan dieksekusi, file f selalu ditutup, bahkan jika ada masalah saat pemrosesan baris-baris, kemudian objek seperti berkas-berkas akan memberikan tindakan pembersihan yang telah ditentukan dan akan menunjukan ini dalam dokumentasi.