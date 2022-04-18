from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Mengonversi byte menjadi str
        if line.startswith('datetime'):
            print(line.rstrip())         # Hapus baris baru yang tertinggal

# datetime: 2022-01-01T01:36:47.689215+00:00 

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org
Beware the Ides of March.
""")
server.quit()