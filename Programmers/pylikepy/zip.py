# https://docs.python.org/3/library/functions.html?highlight=built%20function#zip

#========
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = [[],[],[]]

for i in range(3):
    for j in range(3):
        new_list[i].append( mylist[j][i] )


# zip()
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))


#==========
mylist = [ 1,2,3 ]
new_list = [ 40, 50, 60 ]
for i in zip(mylist, new_list):
    print (i)

#ex1)
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for i, j, k in zip(list1, list2, list3):
   print( i + j + k )

#ex2)
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds))

