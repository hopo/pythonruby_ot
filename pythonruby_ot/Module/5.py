import auth

inpt_id=input('ID: ')
if auth.login(inpt_id):
	print('Hello, '+inpt_id)
else:
	print('no user id')