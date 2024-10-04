import math

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def print(self, title = "(x, y)"):
        print("{} ({}, {})".format(title, self.x, self.y))

    def mag(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

    def sub(self, vec):
        self.x -= vec.x
        self.y -= vec.y

    def mult(self, scaler):
        self.x *= scaler
        self.y *= scaler

    def div(self, scaler):
        self.x /= scaler
        self.y /= scaler

    def negate(self):
        self.x = -self.x
        self.y = -self.y

    def normalize(self):
        mag = self.mag()
        if mag != 0:
            self.div(mag)

    def t_add(self, vec):
        x = self.x + vec.x
        y = self.y + vec.y
        return Vector(x, y)

    def t_sub(self, vec):
        x = self.x - vec.x
        y = self.y - vec.y
        return Vector(x, y)

    def t_mult(self, scaler):
        x = self.x * scaler
        y = self.y * scaler
        return Vector(x, y)

    def t_div(self, scaler):
        x = self.x / scaler
        y = self.y / scaler
        return Vector(x, y)

    def t_negate(self):
        x = -self.x
        y = -self.y
        return Vector(x, y)

    def t_normalize(self):
        mag = self.mag()
        if mag != 0:
            x = self.x / mag
            y = self.y / mag
            return Vector(x, y)
        else:
            return Vector(0, 0)

    def dot(self, vec):
        return self.x * vec.x + self.y * vec.y

    def string(self):
        return f"({self.x}, {self.y})"
