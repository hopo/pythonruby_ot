
def reverse_int(num):
    sl = list(str(num))
    sl.sort(reverse=True)
    return int(''.join(sl))

if __name__ == '__main__':
    ex1 = reverse_int(118372) # 873211
    print(ex1)
