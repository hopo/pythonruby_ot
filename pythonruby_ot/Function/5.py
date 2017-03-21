# def floop():
# 	inpt_str=input('str: ')
# 	inum=input('num: ')
# 	print(inpt_str*int(inum))

# inum=input('num: ')
# numbers=list(range(1,int(inum)+1))
# for number in numbers:
# 	print(str(number)+'. hello')
# print('* app term *')

# def app5():
# 	inum=input('num: ')
# 	numbers=list(range(1,int(inum)+1))
# 	for number in numbers:
# 		print(str(number)+'. hello')
# 	print('* app term *')

def app5():
	istr = input('str: ')
	inum = input('num: ')
	numbers = list(range(1, int(inum)+1))
	for number in numbers:
		print(str(number)+'. '+istr)
	print('* app term *')

app5()
