require_relative ('amber')
module Harpa
	module_function()
	def a()
		return 'a'
	end
end

def a()
	return 'B'
end

puts(a())
puts(Harpa.a())
puts(Amb.y())