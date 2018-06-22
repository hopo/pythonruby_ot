
# ============
list1 = ['1', '100', '33']
list2 = []
for i in list1:
    list2.append(int(i))

# ============
list1 = ['1', '100', '33']
list2 = list(map(int, list1))

