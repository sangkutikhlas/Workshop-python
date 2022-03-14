for line in f:
     print(line, end='')

#This is the first line of the file.
#Second line of the file


# returning the number of characters written.
f.write('This is a test\n')
#15


# bytes object (in binary mode) – before writing them:
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)
#18