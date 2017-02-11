# name1=String.new('harpa')
# name2=String.new('amber')
# puts(name1.reverse())
# puts(name2.reverse())
# puts(name1.upcase())
# puts(name1.size())
# names=Array.new()
# names.push('riceboy')
# names.push('sooki')
# puts(names)
# puts(names.join('--'))

class C
  def initialize(v)
    @value=v
  end
  def show()
    p @value
  end
end
c1=C.new(10)
# p c1.value #do not read(class) at R
# c1.value=20 #do not write(class) at R
c1.show()
