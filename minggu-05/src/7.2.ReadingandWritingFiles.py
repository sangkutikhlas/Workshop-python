f = open('workfile', 'w')


# Using with is also much shorter than writing equivalent try-finally blocks:
with open('workfile') as f:
     read_data = f.read()

# We can check that the file has been automatically closed.
f.closed
# True