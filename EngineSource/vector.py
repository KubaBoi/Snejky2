import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getPosition(self):
        return (self.x, self.y, self.z)

    def selfLength(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def distance(self, vector):
        return math.sqrt(pow(self.x - vector.x, 2) + 
                        pow(self.y - vector.y, 2) + 
                        pow(self.z - vector.z, 2))

    #bod - pricte k bodu vektor 
    def addVector(self, vector):
        return Vector(self.x + vector.x,
                    self.y + vector.y,
                    self.z + vector.z)

    #obrati vektor
    def reverseVector(self):
        return Vector(self.x * -1,
                      self.y * -1,
                      self.z * -1)

    #nastavi delku vektoru
    def setVectorLeng(self, m):
        norm = self.norm()
        return Vector(norm.x * m,
                      norm.y * m,
                      norm.z * m)
    #vynasobi vektor
    def multipleVector(self, m):
        return Vector(self.x * m,
                      self.y * m,
                      self.z * m)

    #vector - vrati normalizovany vektor
    def norm(self):
        if (self.selfLength() != 0):
            return Vector(self.x / self.selfLength(),
                          self.y / self.selfLength(),
                          self.z / self.selfLength())
        else: return Vector(0, 0, 0)

    #bod - vytvori novy vektor k bodu
    #self je zacatek vektoru
    def newVector(self, point):
        return Vector(point.x - self.x,
                      point.y - self.y,
                      point.z - self.z)

    #vektor - zjisti jestli jsou vektory rovnobezne(muzou byt i opacne)
    def parallelVector(self, vector):
        if (abs(self.norm().x) == abs(vector.norm().x) and
            abs(self.norm().y) == abs(vector.norm().y) and
            abs(self.norm().z) == abs(vector.norm().z)):
            return True
        return False

    #vektor - vrati skalarni soucin vektoru
    def scalar(self, vector):
        return (self.x * vector.x +
                self.y * vector.y +
                self.z * vector.z)

    def angle(self, vector):
        if (self.selfLength() * vector.selfLength() == 0):
            return 0
        try:
            return (math.acos(self.scalar(vector) /
                          (self.selfLength() * vector.selfLength())))
        except: return 0

    def equals(self, vector):
        d = 10000
        return (int(self.x*d) == int(vector.x*d) and
                int(self.y*d) == int(vector.y*d) and
                int(self.z*d) == int(vector.z*d))  