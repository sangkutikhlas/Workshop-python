# Buat lingkungan baru bernama "ular" yang berisi Python 3.9:
# conda create --name snakes python=3.9

# Aktifkan lingkungan baru:
# conda activate snakes

# Verifikasi bahwa lingkungan ular telah ditambahkan dan aktif:
# conda info --envs
# Output:
"""
# conda environments:
#
base                     /home/username/anaconda3
snakes                *  /home/username/anaconda3/envs/snakes
snowflakes               /home/username/anaconda3/envs/snowflakes
"""

# Verifikasi versi Python mana yang ada di lingkungan Anda saat ini:
# python --version

# Nonaktifkan lingkungan ular dan kembali ke lingkungan dasar:
# conda activate