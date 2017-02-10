def login(_id):
	members=['harpa','amber','riceboy']
	for member in members:
		if member==_id:
			return True
	return False