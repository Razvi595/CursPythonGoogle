class Coordinate(object):
    """O coordonata e copusa din x si y"""

    def __init__(self, x, y):
        """ Setam valorile x si y"""
        self.x = x
        self.y = y

    def __str__(self):
        """Returnam self ca si string"""
        return f"<{self.x}, {self.y}>"

    def distance(self, other):
        """Retrurneaza distanta euclidiana dintre doua coordonate"""
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2

        return (x_diff_sq + y_diff_sq)**0.5


a = Coordinate(1, 1)
print(a)
origin = Coordinate(0, 0)
print(origin)
print(origin.distance(a))
print(a.y)
origin.y = -10
print(origin)
