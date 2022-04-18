#menggunakan nama placeholder yang dibentuk oleh $ dengan pengidentifikasi Python yang valid
from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')
# 'Nottinghamfolk send $10 to the ditch fund.'


#Metode pengganti () memunculkan KeyError ketika placeholder tidak disediakan dalam kamus atau argumen kata kunci.
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
t.substitute(d)
Traceback (most recent call last):

KeyError: 'owner'
t.safe_substitute(d)
# 'Return the unladen swallow to $owner.'


#Placeholder seperti tanggal saat ini, nomor urut gambar, atau format file.
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
     delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
# Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
     base, ext = os.path.splitext(filename)
     newname = t.substitute(d=date, n=i, f=ext)
     print('{0} --> {1}'.format(filename, newname))     
"""
img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg"""