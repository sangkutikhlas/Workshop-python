import shutil
shutil.copyfile('data.db', 'archive.db')
# 'archive.db'
shutil.move('/build/executables', 'installdir')
# 'installdir'