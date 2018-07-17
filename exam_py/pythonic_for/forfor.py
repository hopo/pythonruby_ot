
ls = [(n, m) for n in range(2, 10) for m in range(1, 10)]

for n, m in ls:
    print("{} x {} = {}".format(n, m, n*m))
