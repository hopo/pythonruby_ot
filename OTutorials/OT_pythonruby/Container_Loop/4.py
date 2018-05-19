inpt_id = input('ID : ')
members = ['harpa', 'amber']
for member in members:
    if member == inpt_id:
        print('Hello world, '+member+'.')
        import sys #R: exit
        sys.exit()
print('no user id.')
