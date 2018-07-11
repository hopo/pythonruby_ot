
# 00
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    raw = line.split()
    print(raw)

f.close()


# 01
with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))
