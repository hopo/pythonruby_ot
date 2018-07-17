import os

home = os.environ['HOME']
ex1 = os.path.isdir(f'{home}/.python') # dir
ex2 = os.path.exists(f'{home}/.python/list.txt') # dir or file

print(ex1)
print(ex2)
