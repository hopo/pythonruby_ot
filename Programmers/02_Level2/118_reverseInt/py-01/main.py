
def reverse_int(num):
    l = list()
    for s in str(num):
       l.append(s) 
    l.sort(reverse=True)
    return int(''.join(l))

if __name__ == '__main__':
    ex1 = reverse_int(118372) # 873211
    print(ex1)
