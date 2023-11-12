class Rectangle:

    def __init__(self, a, b):
         self.a = a
         self.b = b

    def P(self):
        return f'P: {2 * (self.a + self.b)}'

    def S(self):
         return f'S: {self.a * self.b}'



rec = Rectangle(1, 5)
print(rec.P())
print(rec.S())