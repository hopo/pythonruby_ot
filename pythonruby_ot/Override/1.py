class C1:
	def m(self):
		return 'Parent'

class C2(C1):
	def m(self):
		return super().m()+'Child'
	pass

o = C2()
print(o.m())
