# 00
class Coord00(object):
    def __init__(self, x, y):
        self.x, self.y = x, y


point = Coord00(1, 2)
print(f'({point.x}, {point.y})')

# 또는


def print_coord(coord00):
    print('({}, {})'.format(coord00.x, coord00.y))


print_coord(point)


# 01


class Coord(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f'({self.x}, {self.y})'


point = Coord(1, 2)

print('01:', point)
