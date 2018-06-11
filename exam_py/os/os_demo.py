import os

ex1 = os.path.isdir("/Users/hp/.gdrive/list.txt") # dir
ex2 = os.path.exists("/Users/hp/.gdrive/list.txt") # dir or file

print(ex1)
print(ex2)
