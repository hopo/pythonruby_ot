class C
  attr_reader :value
  attr_writer :value
  #attr_accessor :value #reader+wirter 
  def initialize(v)
    @value=v
  end
  def show()
    p @value
  end
end

c1=C.new(10)
p c1.value #attribute read
c1.value=20 #attribute write
p c1.value
