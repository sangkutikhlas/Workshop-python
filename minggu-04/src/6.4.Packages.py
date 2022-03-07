#Pengguna paket dapat mengimpor modul individual dari paket
import sound.effects.echo

#Ini memuat submodule sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

#Cara alternatif untuk mengimpor submodule
from sound.effects import echo

#Memuat gema submodul, dan membuatnya tersedia tanpa awalan paketnya
echo.echofilter(input, output, delay=0.7, atten=4)

#Mengimpor fungsi atau variabel yang diinginkan secara langsung
from sound.effects.echo import echofilter

#Ini memuat submodule echo
echofilter(input, output, delay=0.7, atten=4)