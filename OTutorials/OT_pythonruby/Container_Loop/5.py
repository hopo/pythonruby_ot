inpt_id = input('ID: ')

def login(_id):
	members = ['harpa','amber','riceboy']
	for member in members:
		if member == _id:
			return True
	return False

if login(inpt_id):
	print('Hello, '+inpt_id+'.')
else:
	print('no user id.')

print('* app5 term *')
