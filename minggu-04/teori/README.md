# 6. Modules
Jika Anda keluar dari interpreter Python dan memasukkannya lagi, definisi yang telah Anda buat (fungsi dan variabel) akan hilang. Oleh karena itu, jika Anda ingin menulis program yang lebih panjang, Anda sebaiknya menggunakan editor teks untuk menyiapkan input untuk penerjemah dan menjalankannya dengan file tersebut sebagai input. Ini dikenal sebagai membuat skrip. Saat program Anda semakin panjang, Anda mungkin ingin membaginya menjadi beberapa file untuk perawatan yang lebih mudah. Anda mungkin juga ingin menggunakan fungsi praktis yang telah Anda tulis di beberapa program tanpa menyalin definisinya ke setiap program.

Untuk mendukung ini, Python memiliki cara untuk menempatkan definisi dalam file dan menggunakannya dalam skrip atau dalam instance interpreter yang interaktif. File seperti itu disebut modul; definisi dari sebuah modul dapat diimpor ke modul lain atau ke modul utama (kumpulan variabel yang dapat Anda akses dalam skrip yang dijalankan di tingkat atas dan dalam mode kalkulator).

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__. For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents:

```python
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

Sekarang masukkan interpreter Python dan impor modul ini dengan perintah berikut:

```python
import fibo
```

Ini tidak memasukkan nama fungsi yang didefinisikan dalam fibo secara langsung di tabel simbol saat ini; itu hanya memasukkan nama modul fibo di sana. Menggunakan nama modul Anda dapat mengakses fungsi:

```python
fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

If you intend to use a function often you can assign it to a local name:

```python
fib = fibo.fib
fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

# 6.1. More on Modules
Setiap modul memiliki tabel simbol pribadinya sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. Dengan demikian, pembuat modul dapat menggunakan variabel global dalam modul tanpa mengkhawatirkan bentrokan yang tidak disengaja dengan variabel global pengguna. Di sisi lain, jika Anda tahu apa yang Anda lakukan, Anda dapat menyentuh variabel global modul dengan notasi yang sama yang digunakan untuk merujuk ke fungsinya, modname.itemname.

Modul dapat mengimpor modul lain. Merupakan kebiasaan tetapi tidak diharuskan untuk menempatkan semua pernyataan impor di awal modul (atau skrip, dalam hal ini). Nama modul yang diimpor ditempatkan di tabel simbol global modul pengimpor.

Ada varian dari pernyataan impor yang mengimpor nama dari modul langsung ke tabel simbol modul pengimpor. Sebagai contoh:

```python
from fibo import fib, fib2
fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Bahkan ada varian untuk mengimpor semua nama yang didefinisikan oleh modul:

```python
from fibo import *
fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

ini mengimpor semua nama kecuali yang dimulai dengan garis bawah (_). Dalam kebanyakan kasus, pemrogram Python tidak menggunakan fasilitas ini karena fasilitas ini memperkenalkan serangkaian nama yang tidak diketahui ke dalam juru bahasa, mungkin menyembunyikan beberapa hal yang telah Anda tetapkan.

Jika nama modul diikuti oleh as, maka nama berikut sebagai terikat langsung ke modul yang diimpor.

```python
import fibo as fib
fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Ini secara efektif mengimpor modul dengan cara yang sama seperti mengimpor fibo, dengan satu-satunya perbedaan tersedia sebagai fib.

Itu juga dapat digunakan saat memanfaatkan dari dengan efek serupa:

```python
from fibo import fib as fibonacci
fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

# 6.1.1. Executing modules as scripts
kode dalam modul akan dieksekusi, sama seperti jika Anda mengimpornya, tetapi dengan __name__ disetel ke "__main__". Itu berarti dengan menambahkan kode ini di akhir modul Anda:

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

Anda dapat membuat file dapat digunakan sebagai skrip serta modul yang dapat diimpor, karena kode yang mem-parsing baris perintah hanya berjalan jika modul dijalankan sebagai file "utama":

```python
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

Jika modul diimpor, kode tidak dijalankan:

```pyton
import fibo
```
Ini sering digunakan baik untuk menyediakan antarmuka pengguna yang nyaman ke modul, atau untuk tujuan pengujian (menjalankan modul saat skrip mengeksekusi rangkaian pengujian).

# 6.1.2. The Module Search Path
Saat modul bernama spam diimpor, penerjemah pertama-tama mencari modul bawaan dengan nama itu. Jika tidak ditemukan, maka akan mencari file bernama spam.py dalam daftar direktori yang diberikan oleh variabel sys.path. sys.path diinisialisasi dari lokasi ini:

* Direktori yang berisi skrip input (atau direktori saat ini ketika tidak ada file yang ditentukan).
* PYTHONPATH (daftar nama direktori, dengan sintaks yang sama dengan variabel shell PATH).
* Default yang bergantung pada penginstalan (menurut konvensi termasuk direktori paket situs, ditangani oleh modul situs).

Setelah inisialisasi, program Python dapat memodifikasi sys.path. Direktori yang berisi skrip yang sedang dijalankan ditempatkan di awal jalur pencarian, di depan jalur pustaka standar. Ini berarti bahwa skrip di direktori itu akan dimuat alih-alih modul dengan nama yang sama di direktori perpustakaan. Ini adalah kesalahan kecuali penggantian dimaksudkan. Lihat bagian Modul Standar untuk informasi lebih lanjut.

# 6.1.3. “Compiled” Python files
Untuk mempercepat pemuatan modul, Python menyimpan versi kompilasi dari setiap modul di direktori __pycache__ di bawah nama module.version.pyc, di mana versi mengkodekan format file yang dikompilasi; biasanya berisi nomor versi Python. Misalnya, di CPython rilis 3.3 versi kompilasi dari spam.py akan di-cache sebagai __pycache__/spam.cpython-33.pyc. Konvensi penamaan ini memungkinkan modul yang dikompilasi dari rilis yang berbeda dan versi Python yang berbeda untuk hidup berdampingan.

Python memeriksa tanggal modifikasi sumber terhadap versi yang dikompilasi untuk melihat apakah itu kedaluwarsa dan perlu dikompilasi ulang. Ini adalah proses yang sepenuhnya otomatis. Juga, modul yang dikompilasi adalah platform-independen, sehingga perpustakaan yang sama dapat dibagi di antara sistem dengan arsitektur yang berbeda.

Python tidak memeriksa cache dalam dua keadaan. Pertama, selalu mengkompilasi ulang dan tidak menyimpan hasil untuk modul yang dimuat langsung dari baris perintah. Kedua, tidak memeriksa cache jika tidak ada modul sumber. Untuk mendukung distribusi non-sumber (hanya dikompilasi), modul yang dikompilasi harus berada di direktori sumber, dan tidak boleh ada modul sumber.

# 6.2. Standard Modules
Beberapa modul dibangun ke dalam juru bahasa; ini menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti panggilan sistem. Kumpulan modul tersebut adalah opsi konfigurasi yang juga bergantung pada platform yang mendasarinya. Misalnya, modul winreg hanya tersedia di sistem Windows. Satu modul tertentu patut mendapat perhatian: sys, yang dibangun ke dalam setiap juru bahasa Python. Variabel sys.ps1 dan sys.ps2 mendefinisikan string yang digunakan sebagai prompt primer dan sekunder:

```python
import sys
sys.ps1
'>>> '
sys.ps2
'... '
sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

Variabel sys.path adalah daftar string yang menentukan jalur pencarian interpreter untuk modul. Ini diinisialisasi ke jalur default yang diambil dari variabel lingkungan PYTHONPATH, atau dari default bawaan jika PYTHONPATH tidak disetel. Anda dapat memodifikasinya menggunakan operasi daftar standar:

```python
import sys
sys.path.append('/ufs/guido/lib/python')
```

# 6.3. The dir() Function
Fungsi bawaan dir() digunakan untuk mengetahui nama yang didefinisikan oleh modul. Ini mengembalikan daftar string yang diurutkan:

```python
import fibo, sys
dir(fibo)
['__name__', 'fib', 'fib2']
dir(sys)  
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
```

Tanpa argumen, dir() mencantumkan nama yang telah Anda tetapkan saat ini:

```python
a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

dir() tidak mencantumkan nama fungsi dan variabel bawaan. Jika Anda ingin daftarnya, mereka didefinisikan dalam modul standar bawaan:

```python
import builtins
dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```

# 6.4. Packages
Paket adalah cara menyusun namespace modul Python dengan menggunakan "nama modul bertitik". Misalnya, nama modul AB menunjuk submodule bernama B dalam paket bernama A. Sama seperti penggunaan modul menyelamatkan penulis modul yang berbeda dari harus khawatir tentang nama variabel global masing-masing, penggunaan nama modul bertitik menyelamatkan penulis paket multi-modul seperti NumPy atau Bantal karena harus khawatir tentang nama modul masing-masing.

Misalkan Anda ingin merancang kumpulan modul ("paket") untuk penanganan file suara dan data suara yang seragam. Ada banyak format file suara yang berbeda (biasanya dikenali dari ekstensinya, misalnya: .wav, .aiff, .au), jadi Anda mungkin perlu membuat dan memelihara koleksi modul yang terus bertambah untuk konversi antara berbagai format file. Ada juga banyak operasi berbeda yang mungkin ingin Anda lakukan pada data suara (seperti mencampur, menambahkan gema, menerapkan fungsi equalizer, membuat efek stereo buatan), jadi selain itu Anda akan menulis aliran modul yang tidak pernah berakhir untuk dilakukan operasi ini. Berikut adalah kemungkinan struktur untuk paket Anda (dinyatakan dalam sistem file hierarkis)

```python
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

Saat mengimpor paket, Python mencari melalui direktori di sys.path mencari subdirektori paket.

File __init__.py diperlukan untuk membuat Python memperlakukan direktori yang berisi file sebagai paket. Ini mencegah direktori dengan nama umum, seperti string, secara tidak sengaja menyembunyikan modul valid yang muncul kemudian di jalur pencarian modul. Dalam kasus yang paling sederhana, __init__.py hanya dapat berupa file kosong, tetapi juga dapat mengeksekusi kode inisialisasi untuk paket atau mengatur variabel __all__, yang akan dijelaskan nanti.

Pengguna paket dapat mengimpor modul individual dari paket, misalnya:
```python
import sound.effects.echo
```

Ini memuat submodule sound.effects.echo. Itu harus dirujuk dengan nama lengkapnya.
```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

Cara alternatif untuk mengimpor submodule adalah:
```python
from sound.effects import echo
```

Ini juga memuat gema submodul, dan membuatnya tersedia tanpa awalan paketnya, sehingga dapat digunakan sebagai berikut:
```python
echo.echofilter(input, output, delay=0.7, atten=4)
```

Namun variasi lain adalah mengimpor fungsi atau variabel yang diinginkan secara langsung:
```python
from sound.effects.echo import echofilter
```

Sekali lagi, ini memuat submodule echo, tetapi ini membuat fungsinya echofilter() langsung tersedia:
```python
echofilter(input, output, delay=0.7, atten=4)
```

Perhatikan bahwa saat menggunakan item impor paket, item dapat berupa submodul (atau subpaket) paket, atau nama lain yang ditentukan dalam paket, seperti fungsi, kelas, atau variabel. Pernyataan impor pertama-tama menguji apakah item tersebut didefinisikan dalam paket; jika tidak, ia menganggapnya sebagai modul dan mencoba memuatnya. Jika gagal menemukannya, pengecualian ImportError dimunculkan.

Sebaliknya, saat menggunakan sintaks seperti import item.subitem.subsubitem, setiap item kecuali yang terakhir harus berupa paket; item terakhir dapat berupa modul atau paket tetapi tidak dapat berupa kelas atau fungsi atau variabel yang ditentukan dalam item sebelumnya.

# 6.4.1. Importing * From a Package
Sekarang apa yang terjadi ketika pengguna menulis dari sound.effects import *? Idealnya, orang akan berharap bahwa ini entah bagaimana keluar ke sistem file, menemukan submodul mana yang ada dalam paket, dan mengimpor semuanya. Ini bisa memakan waktu lama dan mengimpor sub-modul mungkin memiliki efek samping yang tidak diinginkan yang seharusnya hanya terjadi ketika sub-modul diimpor secara eksplisit.

Satu-satunya solusi adalah bagi pembuat paket untuk memberikan indeks eksplisit dari paket tersebut. Pernyataan impor menggunakan konvensi berikut: jika kode __init__.py paket mendefinisikan daftar bernama __all__, itu dianggap sebagai daftar nama modul yang harus diimpor ketika dari paket impor * ditemukan. Terserah pembuat paket untuk tetap memperbarui daftar ini ketika versi baru dari paket dirilis. Pembuat paket juga dapat memutuskan untuk tidak mendukungnya, jika mereka tidak melihat gunanya mengimpor * dari paket mereka. Misalnya, file sound/effects/__init__.py dapat berisi kode berikut:

```python
__all__ = ["echo", "surround", "reverse"]
```

Ini berarti bahwa from sound.effects import * akan mengimpor tiga submodul yang bernama dari paket suara.

Jika __all__ tidak ditentukan, pernyataan dari sound.effects import * tidak mengimpor semua submodul dari paket sound.effects ke dalam namespace saat ini; itu hanya memastikan bahwa paket sound.effects telah diimpor (mungkin menjalankan kode inisialisasi apa pun di __init__.py) dan kemudian mengimpor nama apa pun yang ditentukan dalam paket. Ini termasuk nama yang ditentukan (dan submodul yang dimuat secara eksplisit) oleh __init__.py. Ini juga mencakup submodul apa pun dari paket yang dimuat secara eksplisit oleh pernyataan impor sebelumnya. Pertimbangkan kode ini:

```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```
Dalam contoh ini, modul echo dan surround diimpor ke namespace saat ini karena mereka didefinisikan dalam paket sound.effects saat pernyataan from...import dijalankan. (Ini juga berfungsi ketika __all__ didefinisikan.)

Meskipun modul tertentu dirancang untuk mengekspor hanya nama yang mengikuti pola tertentu saat Anda menggunakan import *, itu masih dianggap sebagai praktik buruk dalam kode produksi.

Ingat, tidak ada yang salah dengan menggunakan from package import specific_submodule! Sebenarnya, ini adalah notasi yang disarankan kecuali modul pengimpor perlu menggunakan submodul dengan nama yang sama dari paket yang berbeda.

# 6.4.2. Intra-package References
Saat paket disusun menjadi subpaket (seperti paket suara dalam contoh), Anda dapat menggunakan impor absolut untuk merujuk ke submodul paket saudara. Misalnya, jika modul sound.filters. vocoder perlu menggunakan modul gema di sound.effects paket, dapat menggunakan from sound.effects import echo.

Anda juga dapat menulis impor relatif, dengan bentuk nama impor modul dari pernyataan impor. Impor ini menggunakan titik awal untuk menunjukkan paket saat ini dan induk yang terlibat dalam impor relatif. Dari modul surround misalnya, Anda dapat menggunakan:

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

Perhatikan bahwa impor relatif didasarkan pada nama modul saat ini. Karena nama modul utama selalu "__main__", modul yang dimaksudkan untuk digunakan sebagai modul utama aplikasi Python harus selalu menggunakan impor absolut.

# 6.4.3. Packages in Multiple Directories
Paket mendukung satu atribut khusus lagi, __path__. Ini diinisialisasi menjadi daftar yang berisi nama direktori yang menyimpan __init__.py paket sebelum kode dalam file itu dieksekusi. Variabel ini dapat dimodifikasi; hal itu akan memengaruhi pencarian modul dan subpaket di masa mendatang yang terdapat dalam paket.

Meskipun fitur ini tidak sering diperlukan, fitur ini dapat digunakan untuk memperluas kumpulan modul yang ditemukan dalam sebuah paket.